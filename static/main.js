

var map = L.map('map').setView([28.2096, 83.9856], 7);



var osm = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',{
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3']
});

var googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',{
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3']
});

var googleHybrid = L.tileLayer('http://{s}.google.com/vt/lyrs=s,h&x={x}&y={y}&z={z}',{
    maxZoom: 20,
    subdomains:['mt0','mt1','mt2','mt3']
});


// var marker = L.marker([28.2096, 83.9856]).addTo(map)
//     .bindPopup(' I am at Pokhara')
//     .openPopup();

var baseMap = {
    'osm':osm,
    'googleStreets':googleStreets,
    'googleSat':googleSat,
    'googleHybrid':googleHybrid


};
L.control.layers(baseMap).addTo(map);

//adding search bar
L.Control.geocoder().addTo(map);

//adding geojason file

// L.geoJSON(nepalData).addTo(map);