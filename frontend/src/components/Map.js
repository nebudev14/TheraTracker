import React from 'react';
import { GoogleMap, LoadScript } from 'react-google-maps';
import axios from 'axios';

const containerStyle = {
    width: "400px",
    height: "400px",
  };

export default function Map() {
    const [currentLoc, setCurrentLoc] = React.useState({
        lat: 42.331429,
        lng: -83.045753
    })

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
          setCurrentLoc({
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          });
        });
      }
      
  return (
      <GoogleMap
        mapContainerStyle={containerStyle}
        center={{ lat: currentLoc.lat, lng: currentLoc.lng }}
        zoom={10}
      >
        {/* Child components, such as markers, info windows, etc. */}
        <></>
      </GoogleMap>
  );
}


