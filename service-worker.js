const CACHE_NAME = 'card-road-pwa-v37-binder-patch';
const CORE_ASSETS = [
  './index.html',
  './manifest.webmanifest',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './assets/locations/market.webp',
  './assets/locations/riverside.webp',
  './assets/locations/inn.webp',
  './assets/locations/card_club.webp',
  './assets/npcs/tomas.webp',
  './assets/npcs/nessa_standee_final_v14.png'
,
  './assets/npcs/bram_standee_v15.png',
  './assets/npcs/elira_standee_v17.png',
  './assets/ui/date_time_frame.png',
  './assets/ui/location_title_frame.png',
  './assets/ui/noticeboard_frame.png',
  './assets/ui/presence_message_frame.png',
  './assets/ui/match_club_table.png',
  './assets/ui/card_gilt_frame.png',
  './assets/ui/deck_binder_cover.png',
  './assets/ui/deck_binder_page.png',
  './assets/ui/deck_binder_tab.png',
  './assets/ui/deck_binder_tab_on.png',
  './assets/ui/deck_binder_well.png',
  './assets/ui/deck_binder_ring.svg'];

self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    // Explicit reload avoids reusing the browser HTTP cache during a deploy update.
    await Promise.all(CORE_ASSETS.map(async url => {
      const response = await fetch(url, { cache: 'reload' });
      if (response.ok) await cache.put(url, response);
    }));
  })());
  self.skipWaiting();
});

self.addEventListener('activate', event => {
  event.waitUntil((async () => {
    const keys = await caches.keys();
    await Promise.all(keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k)));
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;

  // App/page: network first so each Netlify deploy is seen immediately.
  if (event.request.mode === 'navigate') {
    event.respondWith(
      fetch(event.request, { cache: 'no-store' })
        .then(async response => {
          if (response.ok) {
            const cache = await caches.open(CACHE_NAME);
            cache.put('./index.html', response.clone());
          }
          return response;
        })
        .catch(() => caches.match('./index.html'))
    );
    return;
  }

  // Static art: serve cached instantly; the new SW install refreshes these on every deploy.
  event.respondWith(
    caches.match(event.request).then(cached =>
      cached || fetch(event.request).then(async response => {
        if (response.ok) {
          const cache = await caches.open(CACHE_NAME);
          cache.put(event.request, response.clone());
        }
        return response;
      })
    )
  );
});
