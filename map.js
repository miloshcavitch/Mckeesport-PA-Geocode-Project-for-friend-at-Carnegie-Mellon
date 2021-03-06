function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 14,
    center: {lat: 40.340103, lng: -79.840227}, //center(ish) of Mckeesport, PA
  });

  var townCoords = [
    {lat: 40.364188, lng: -79.836728},
    {lat: 40.362360, lng: -79.837239},
    {lat: 40.357168, lng: -79.843567},
    {lat: 40.356429, lng: -79.847292},
    {lat: 40.355496, lng: -79.870794},
    {lat: 40.353960, lng: -79.877378},
    {lat: 40.345248, lng: -79.885875},
    {lat: 40.343439, lng: -79.881767},
    {lat: 40.341552, lng: -79.881256},
    {lat: 40.343692, lng: -79.878501},
    {lat: 40.343828, lng: -79.878143},
    {lat: 40.344684, lng: -79.877250},
    {lat: 40.346356, lng: -79.875056},
    {lat: 40.346998, lng: -79.874316},
    {lat: 40.347351, lng: -79.873758},
    {lat: 40.347559, lng: -79.873242},
    {lat: 40.347674, lng: -79.872514},
    {lat: 40.347674, lng: -79.871755},
    {lat: 40.348345, lng: -79.870784},
    {lat: 40.348461, lng: -79.869540},
    {lat: 40.346079, lng: -79.868751},
    {lat: 40.341615, lng: -79.866050},
    {lat: 40.336619, lng: -79.858251},
    {lat: 40.332432, lng: -79.853669},
    {lat: 40.328291, lng: -79.846325},
    {lat: 40.325954, lng: -79.843958},
    {lat: 40.319754, lng: -79.840863},
    {lat: 40.320564, lng: -79.838890},
    {lat: 40.320864, lng: -79.838617},
    {lat: 40.320934, lng: -79.838162},
    {lat: 40.321479, lng: -79.837090},
    {lat: 40.324261, lng: -79.832752},
    {lat: 40.320564, lng: -79.831145},
    {lat: 40.320467, lng: -79.829512},
    {lat: 40.320759, lng: -79.828338},
    {lat: 40.320136, lng: -79.827036},
    {lat: 40.322159, lng: -79.824230},
    {lat: 40.322646, lng: -79.823872},
    {lat: 40.322938, lng: -79.823260},
    {lat: 40.322335, lng: -79.822035},
    {lat: 40.318774, lng: -79.820785},
    {lat: 40.317938, lng: -79.820376},
    {lat: 40.319341, lng: -79.816719},
    {lat: 40.319867, lng: -79.816821},
    {lat: 40.321754, lng: -79.817637},
    {lat: 40.324244, lng: -79.816362},
    {lat: 40.326462, lng: -79.815953},
    {lat: 40.328466, lng: -79.817127},
    {lat: 40.327551, lng: -79.818173},
    {lat: 40.332551, lng: -79.820725},
    {lat: 40.337841, lng: -79.820470},
    {lat: 40.337958, lng: -79.818735},
    {lat: 40.343054, lng: -79.818760},
    {lat: 40.343754, lng: -79.821440},
    {lat: 40.344552, lng: -79.821542},
    {lat: 40.344552, lng: -79.826262},
    {lat: 40.344727, lng: -79.828465},
    {lat: 40.347734, lng: -79.830567},
    {lat: 40.348312, lng: -79.830203},
    {lat: 40.350833, lng: -79.829656},
    {lat: 40.351226, lng: -79.829292},
    {lat: 40.351457, lng: -79.828898},
    {lat: 40.351619, lng: -79.827654},
    {lat: 40.351573, lng: -79.826652},
    {lat: 40.351966, lng: -79.826045},
    {lat: 40.352521, lng: -79.825347},
    {lat: 40.354001, lng: -79.824103},
    {lat: 40.355458, lng: -79.826561},
    {lat: 40.356545, lng: -79.828625},
    {lat: 40.357239, lng: -79.831325},
    {lat: 40.357031, lng: -79.832266},
    {lat: 40.358117, lng: -79.831598},
    {lat: 40.359435, lng: -79.830385},
    {lat: 40.360407, lng: -79.828867},
    {lat: 40.360684, lng: -79.828746},
    {lat: 40.361031, lng: -79.828928},
    {lat: 40.361355, lng: -79.829231},
    {lat: 40.361424, lng: -79.829656},
    {lat: 40.361655, lng: -79.829656},
    {lat: 40.361725, lng: -79.830142},
    {lat: 40.362071, lng: -79.830172},
    {lat: 40.362834, lng: -79.830445},
    {lat: 40.362834, lng: -79.831781},
    {lat: 40.361956, lng: -79.831750},
    {lat: 40.362465, lng: -79.832054},
    {lat: 40.362349, lng: -79.832478},
    {lat: 40.361956, lng: -79.833267},
    {lat: 40.361447, lng: -79.833328},
    {lat: 40.361285, lng: -79.834239},
    {lat: 40.362626, lng: -79.834936},
  ];

  // Construct the polygon.
  var boundary = new google.maps.Polygon({
    paths: townCoords,
    strokeColor: '#0000FF',
    strokeOpacity: 0.8,
    strokeWeight: 2,
    fillColor: '#3300FF',
    fillOpacity: 0.35
  });
  boundary.setMap(map);
}

//https://docs.google.com/spreadsheets/d/17GDVuLTowyjtUW9j7yG9eBvQ9YQ_W5M_yuVXvL_vMDQ/pubhtml
//^^above is published
