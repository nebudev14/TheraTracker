import React from 'react';
import { GoogleMap, withScriptjs, withGoogleMap } from 'react-google-maps';

function Map() {
    return(
        <GoogleMap defaultZoom={10} defaultCenter={{lat: 27.2046, lng:-77.4977}} />
    );
}

export default Map;
