import * as THREE from "three";
import { OrbitControls } from "./vendor/OrbitControls.js";

const BOARD_W = 9;
const BOARD_D = 16;

function feltTexture() {
  const w = 720, h = 1280;
  const c = document.createElement("canvas");
  c.width = w; c.height = h;
  const g = c.getContext("2d");
  g.fillStyle = "#6a7a3e";
  g.fillRect(0, 0, w, h);
  for (let i = 0; i < 18000; i++) {
    const x = Math.random() * w, y = Math.random() * h;
    const n = 0.55 + Math.random() * 0.45;
    g.fillStyle = `rgba(${70 + n * 50},${90 + n * 55},${30 + n * 25},${0.18 + Math.random() * 0.25})`;
    g.fillRect(x, y, 1 + Math.random() * 2, 1 + Math.random() * 2);
  }
  // dirt path
  g.strokeStyle = "#8a6b45";
  g.lineWidth = 18;
  g.lineCap = "round";
  g.beginPath();
  g.moveTo(w * 0.62, 90);
  g.bezierCurveTo(w * 0.7, h * 0.28, w * 0.58, h * 0.48, w * 0.68, h * 0.72);
  g.lineTo(w * 0.7, h * 0.95);
  g.stroke();
  // river — flat painted channel on the board, not a 3D sculpture
  g.lineWidth = 78;
  g.strokeStyle = "#3a6a7a";
  g.beginPath();
  g.moveTo(w * 0.52, -10);
  g.bezierCurveTo(w * 0.62, h * 0.18, w * 0.38, h * 0.38, w * 0.5, h * 0.52);
  g.bezierCurveTo(w * 0.64, h * 0.68, w * 0.22, h * 0.82, w * 0.18, h + 20);
  g.stroke();
  g.lineWidth = 58;
  g.strokeStyle = "#4f8ea0";
  g.stroke();
  g.lineWidth = 22;
  g.strokeStyle = "rgba(200,230,235,0.35)";
  g.stroke();
  // hex grout
  const hexAcross = 6.4 / 1.35;
  const hexW = w / hexAcross;
  const size = hexW / Math.sqrt(3);
  const vert = size * 1.5;
  g.strokeStyle = "rgba(42,32,20,0.55)";
  g.lineWidth = 1.2;
  let row = 0;
  for (let y = -size * 0.15; y < h + size; y += vert, row++) {
    const ox = row % 2 ? hexW * 0.5 : 0;
    for (let x = ox; x < w + hexW; x += hexW) {
      g.beginPath();
      for (let i = 0; i <= 6; i++) {
        const a = ((60 * i - 30) * Math.PI) / 180;
        const px = x + size * Math.cos(a);
        const py = y + size * Math.sin(a);
        if (i === 0) g.moveTo(px, py); else g.lineTo(px, py);
      }
      g.stroke();
    }
  }
  g.fillStyle = "#2a1c10";
  g.font = "700 42px Georgia, serif";
  g.textAlign = "center";
  g.fillText("LYTHMERE", w / 2, 64);
  g.font = "700 22px Georgia, serif";
  g.fillStyle = "#3a2818";
  g.fillText("INN", w * 0.24, h * 0.30);
  g.fillText("MARKET", w * 0.20, h * 0.545);
  g.fillText("CLUB", w * 0.80, h * 0.44);
  const tex = new THREE.CanvasTexture(c);
  tex.colorSpace = THREE.SRGBColorSpace;
  tex.anisotropy = 8;
  return tex;
}

function mat(color, extra = {}) {
  return new THREE.MeshStandardMaterial({
    color, roughness: 0.78, metalness: 0.04, ...extra,
  });
}

function box(group, w, h, d, color, x, y, z, rotY = 0) {
  const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), mat(color));
  m.position.set(x, y, z);
  m.rotation.y = rotY;
  m.castShadow = true;
  m.receiveShadow = true;
  group.add(m);
  return m;
}

function gableRoof(group, w, d, h, color, y, zOff = 0) {
  const shape = new THREE.Shape();
  shape.moveTo(-w / 2, 0);
  shape.lineTo(w / 2, 0);
  shape.lineTo(0, h);
  shape.closePath();
  const geo = new THREE.ExtrudeGeometry(shape, { depth: d, bevelEnabled: false });
  geo.rotateX(-Math.PI / 2);
  geo.translate(0, 0, -d / 2);
  const m = new THREE.Mesh(geo, mat(color));
  m.position.set(0, y, zOff);
  m.castShadow = true;
  group.add(m);
  return m;
}

function chimney(group, x, y, z) {
  box(group, 0.16, 0.42, 0.16, 0x6a5344, x, y, z);
  box(group, 0.18, 0.05, 0.18, 0x4a3a32, x, y + 0.22, z);
}

function windowPane(group, x, y, z, w = 0.12, h = 0.14) {
  box(group, w, h, 0.02, 0x1a2430, x, y, z);
}

function tree(x, z, scale = 1) {
  const g = new THREE.Group();
  const trunk = new THREE.Mesh(new THREE.CylinderGeometry(0.05 * scale, 0.07 * scale, 0.28 * scale, 6), mat(0x5a3a22));
  trunk.position.y = 0.14 * scale;
  trunk.castShadow = true;
  const leaves = new THREE.Mesh(new THREE.ConeGeometry(0.28 * scale, 0.7 * scale, 7), mat(0x3d5a28));
  leaves.position.y = 0.55 * scale;
  leaves.castShadow = true;
  g.add(trunk, leaves);
  g.position.set(x, 0, z);
  return g;
}

function makeInn() {
  const g = new THREE.Group();
  box(g, 1.15, 0.72, 0.85, 0x8a5a32, 0, 0.36, 0);
  box(g, 0.7, 0.55, 0.55, 0x7a4e2c, 0.45, 0.28, 0.12);
  gableRoof(g, 1.28, 0.95, 0.48, 0x4a4038, 0.72);
  gableRoof(g, 0.82, 0.62, 0.38, 0x4a4038, 0.55, 0.12);
  chimney(g, -0.15, 1.12, -0.1);
  box(g, 0.22, 0.32, 0.04, 0x3a2416, 0, 0.22, 0.44);
  windowPane(g, -0.32, 0.48, 0.44);
  windowPane(g, 0.32, 0.48, 0.44);
  windowPane(g, -0.32, 0.22, 0.44);
  windowPane(g, 0.32, 0.22, 0.44);
  box(g, 0.38, 0.08, 0.16, 0x3a2a1c, 0, 0.08, 0.5);
  // fence
  for (let i = -2; i <= 2; i++) {
    box(g, 0.04, 0.16, 0.04, 0x5a3e28, i * 0.22, 0.08, 0.62);
  }
  box(g, 0.95, 0.03, 0.03, 0x5a3e28, 0, 0.14, 0.62);
  g.userData.label = "Inn";
  return g;
}

function makeMarket() {
  const g = new THREE.Group();
  box(g, 0.95, 0.55, 0.7, 0x7a4a28, 0, 0.28, 0);
  gableRoof(g, 1.08, 0.78, 0.4, 0x5a4a40, 0.55);
  chimney(g, 0.2, 0.92, -0.05);
  // striped awning
  const awn = box(g, 0.7, 0.04, 0.42, 0xc46a32, 0, 0.42, 0.42);
  awn.rotation.x = -0.35;
  box(g, 0.04, 0.36, 0.04, 0x5a3a22, -0.3, 0.18, 0.52);
  box(g, 0.04, 0.36, 0.04, 0x5a3a22, 0.3, 0.18, 0.52);
  box(g, 0.55, 0.22, 0.4, 0x6a4224, 0, 0.12, 0.38);
  windowPane(g, -0.22, 0.32, 0.36);
  g.userData.label = "Market";
  return g;
}

function makeClub() {
  const g = new THREE.Group();
  box(g, 1.05, 0.58, 0.78, 0x6e4a30, 0, 0.29, 0);
  gableRoof(g, 1.18, 0.88, 0.42, 0x6a5a48, 0.58);
  chimney(g, 0.28, 0.95, 0.05);
  box(g, 0.85, 0.22, 0.28, 0x5a3c26, 0, 0.12, 0.48);
  box(g, 0.04, 0.22, 0.04, 0x4a3220, -0.38, 0.2, 0.58);
  box(g, 0.04, 0.22, 0.04, 0x4a3220, 0.38, 0.2, 0.58);
  box(g, 0.82, 0.03, 0.03, 0x4a3220, 0, 0.3, 0.58);
  windowPane(g, -0.28, 0.38, 0.4);
  windowPane(g, 0.28, 0.38, 0.4);
  box(g, 0.18, 0.28, 0.04, 0x3a2418, 0, 0.18, 0.4);
  g.userData.label = "Club";
  return g;
}

function makeRiverside() {
  const g = new THREE.Group();
  box(g, 0.85, 0.42, 0.55, 0x6a4528, -0.15, 0.21, 0);
  gableRoof(g, 0.95, 0.62, 0.32, 0x4a443c, 0.42, 0);
  chimney(g, -0.28, 0.72, -0.05);
  // sign
  box(g, 0.55, 0.18, 0.03, 0xc8b48a, 0.22, 0.48, 0.12);
  // dock
  box(g, 0.7, 0.06, 0.85, 0x6a4a30, 0.15, 0.06, 0.55);
  for (let i = 0; i < 4; i++) {
    box(g, 0.05, 0.18, 0.05, 0x4a3220, -0.1 + i * 0.16, 0.02, 0.88);
  }
  // boat
  const hull = new THREE.Mesh(new THREE.SphereGeometry(0.22, 8, 6), mat(0x5a3a22));
  hull.scale.set(1.8, 0.45, 0.7);
  hull.position.set(0.22, 0.08, 0.95);
  hull.castShadow = true;
  g.add(hull);
  box(g, 0.03, 0.32, 0.03, 0x3a2a1c, 0.22, 0.28, 0.95);
  g.userData.label = "Riverside";
  return g;
}

function makeBridge() {
  const g = new THREE.Group();
  box(g, 0.42, 0.06, 1.35, 0x7a5a38, 0, 0.1, 0);
  for (let i = -4; i <= 4; i++) {
    box(g, 0.4, 0.03, 0.08, 0x6a4a2c, 0, 0.14, i * 0.14);
  }
  box(g, 0.04, 0.16, 0.04, 0x5a3a22, -0.18, 0.12, -0.6);
  box(g, 0.04, 0.16, 0.04, 0x5a3a22, 0.18, 0.12, -0.6);
  box(g, 0.04, 0.16, 0.04, 0x5a3a22, -0.18, 0.12, 0.6);
  box(g, 0.04, 0.16, 0.04, 0x5a3a22, 0.18, 0.12, 0.6);
  return g;
}

export function mountBoard(host) {
  const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: false });
  renderer.setPixelRatio(Math.min(2, window.devicePixelRatio || 1));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.setClearColor(0x2a241e, 1);
  host.innerHTML = "";
  host.appendChild(renderer.domElement);

  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0x2a241e);

  const aspect0 = 9 / 16;
  const halfH = BOARD_D * 0.51;
  const camera = new THREE.OrthographicCamera(
    -halfH * aspect0, halfH * aspect0, halfH, -halfH, 0.1, 80
  );
  const mapPos = new THREE.Vector3(0, 26, 6.5);
  const tiltPos = new THREE.Vector3(0, 11, 18);
  camera.position.copy(mapPos);
  camera.lookAt(0, 0, 0);

  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enablePan = false;
  controls.minDistance = 8;
  controls.maxDistance = 40;
  controls.minPolarAngle = 0.15;
  controls.maxPolarAngle = 1.2;
  controls.target.set(0, 0, 0);
  controls.enableDamping = true;
  controls.dampingFactor = 0.08;

  scene.add(new THREE.AmbientLight(0xfff0d8, 0.55));
  const sun = new THREE.DirectionalLight(0xffe2b0, 1.35);
  sun.position.set(-6, 12, 4);
  sun.castShadow = true;
  sun.shadow.mapSize.set(1024, 1024);
  sun.shadow.camera.left = -8;
  sun.shadow.camera.right = 8;
  sun.shadow.camera.top = 10;
  sun.shadow.camera.bottom = -10;
  scene.add(sun);
  scene.add(new THREE.HemisphereLight(0xc8d8f0, 0x5a4a30, 0.35));

  // Flat slab
  const slab = new THREE.Mesh(
    new THREE.BoxGeometry(BOARD_W + 0.08, 0.32, BOARD_D + 0.08),
    mat(0x4a3424)
  );
  slab.position.y = -0.17;
  slab.castShadow = true;
  scene.add(slab);

  const board = new THREE.Mesh(
    new THREE.PlaneGeometry(BOARD_W, BOARD_D),
    new THREE.MeshStandardMaterial({
      map: feltTexture(),
      roughness: 0.95,
      metalness: 0,
    })
  );
  board.rotation.x = -Math.PI / 2;
  board.receiveShadow = true;
  scene.add(board);

  function place(model, x, z, rot = 0, s = 1) {
    model.position.set(x, 0, z);
    model.rotation.y = rot;
    model.scale.setScalar(s);
    scene.add(model);
  }

  place(makeInn(), -2.35, -4.15, 0.18, 1.15);
  place(makeMarket(), -2.45, -0.55, 0.12, 1.08);
  place(makeClub(), 2.45, -1.35, -0.35, 1.05);
  place(makeRiverside(), -2.15, 3.35, 0.05, 1.12);
  place(makeBridge(), 0.15, 1.05, 0.15, 1);

  [
    [-3.2, -6.2, 0.85], [3.1, -5.8, 1.1], [3.4, -3.4, 0.9],
    [2.9, 2.2, 1.05], [3.2, 5.4, 1.2], [-3.3, 6.1, 0.95],
    [-3.4, 1.4, 0.75], [1.6, -6.6, 0.7],
  ].forEach(([x, z, s]) => scene.add(tree(x, z, s)));

  function resize() {
    const { clientWidth: w, clientHeight: h } = host;
    if (!w || !h) return;
    renderer.setSize(w, h, false);
    const aspect = w / h;
    const hh = BOARD_D * 0.51;
    camera.left = -hh * aspect;
    camera.right = hh * aspect;
    camera.top = hh;
    camera.bottom = -hh;
    camera.updateProjectionMatrix();
  }
  const ro = new ResizeObserver(resize);
  ro.observe(host);
  resize();

  let mode = "map";
  function setView(next) {
    mode = next;
    const p = next === "tilt" ? tiltPos : mapPos;
    camera.position.copy(p);
    controls.target.set(0, 0, 0);
    camera.lookAt(0, 0, 0);
    controls.update();
  }

  let raf = 0;
  function tick() {
    raf = requestAnimationFrame(tick);
    controls.update();
    renderer.render(scene, camera);
  }
  tick();

  return {
    setView,
    getMode: () => mode,
    renderer,
    dispose() {
      cancelAnimationFrame(raf);
      ro.disconnect();
      controls.dispose();
      renderer.dispose();
    },
  };
}
