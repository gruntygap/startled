self.addEventListener("install", (installEvent) => {
	installEvent.waitUntil(
		caches.open('yeet').then((cache) => {
			console.log('opened cache');
			return cache.addAll(['/', '/static/js/index.js']);
		})
	);
});

