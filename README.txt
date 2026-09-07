CARD ROAD — PWA v22

Playable files are in this folder. DESIGN_BIBLE.md is canon.
Do not publish "Old GPT files" (gitignored).

How to test an update
1. Work in this folder (open index.html, or a local server).
2. Hard refresh: Ctrl+Shift+R, or a private window. The PWA caches old UI.
3. Check Market, Journal, Time, and that a refresh keeps your save.
4. Deploy only when that session is worth sharing.

How to auto-deploy to Netlify
1. Create a GitHub repository (private is fine). Empty, no README.
2. In Git Bash, from this folder:

   git add .
   git commit -m "Initial Card Road web core."
   git branch -M main
   git remote add origin https://github.com/YOUR_USER/YOUR_REPO.git
   git push -u origin main

3. Netlify: Add new site → Import from Git → that repo.
   Publish directory: .   (dot, the folder root)
   After that, every git push updates the site.

If the live site looks old: wait for the deploy to finish, then hard-refresh or clear the site's service worker.
