import React from 'react';
import { GoogleMap } from 'react-google-maps';

function Map() {
    return(
        <GoogleMap defaultZoom={10} defaultCenter={{lat: 40.2046, lng:-77.4977}} />
    );
}

export default Map;
