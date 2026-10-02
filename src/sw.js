// FoodsUp service worker — makes the app work offline.
//
// Strategy: serve from cache first (instant + offline), and refresh the cache
// in the background whenever there is a connection. A new version therefore
// shows up the next time the app is opened. Bump CACHE when the list of
// files below changes.
const CACHE = 'foodsup-v1';
const ASSETS = [
  './',
  './index.html',
  './manifest.webmanifest',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
  './icons/apple-touch-icon.png',
  './icons/favicon-32.png',
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE)
      .then(cache => cache.addAll(ASSETS.map(url => new Request(url, { cache: 'reload' }))))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;

  event.respondWith(
    caches.open(CACHE).then(async cache => {
      // Navigations (opening the app, with or without ?query) all map to index.html
      const isNav = req.mode === 'navigate';
      const key = isNav ? './index.html' : req;
      const cached = await cache.match(key, { ignoreSearch: isNav });
      // A navigate-mode Request can't be cloned with options, so build a fresh one
      const network = fetch(isNav ? new Request('./index.html', { cache: 'no-cache' }) : new Request(req, { cache: 'no-cache' }))
        .then(res => {
          if (res.ok) cache.put(key, res.clone());
          return res;
        })
        .catch(() => null);

      if (cached) {
        event.waitUntil(network);
        return cached;
      }
      return (await network) || new Response('Offline', { status: 503, statusText: 'Offline' });
    })
  );
});
