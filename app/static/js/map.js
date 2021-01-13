
// var cities = L.layerGroup();

// L.marker([39.61, -105.02]).bindPopup('This is Littleton, CO.').addTo(cities),
// L.marker([39.74, -104.99]).bindPopup('This is Denver, CO.').addTo(cities),
// L.marker([39.73, -104.8]).bindPopup('This is Aurora, CO.').addTo(cities),
// L.marker([39.77, -105.23]).bindPopup('This is Golden, CO.').addTo(cities);


var OpenStreetMap_HOT = L.tileLayer('https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
	maxZoom: 19,
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Tiles style by <a href="https://www.hotosm.org/" target="_blank">Humanitarian OpenStreetMap Team</a> hosted by <a href="https://openstreetmap.fr/" target="_blank">OpenStreetMap France</a>'
});

var OpenStreetMap_Mapnik = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	maxZoom: 19,
	attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

var map = L.map('map', {
	center: [-21.532898, -64.732580],
	zoom: 15,
	// scrollWheelZoom: false,
	// layers: [streets, cities]
	layers: [OpenStreetMap_HOT, ]
});

var baseLayers = {
	"OpenStreetMap HOT": OpenStreetMap_HOT,
	"OpenStreetMap_Mapnik": OpenStreetMap_Mapnik
};

var overlays = {
	// "Cities": cities
};

L.control.layers(baseLayers, overlays).addTo(map);
