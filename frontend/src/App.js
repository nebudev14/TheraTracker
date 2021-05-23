import React from 'react';
import Map from './components/Map';
import { withScriptjs, withGoogleMap } from 'react-google-maps'

const WrappedMap = withScriptjs(withGoogleMap(Map));

function App() {
  return (
    <div style={{width: '98vw', height: '98vh'}}>
      <WrappedMap googleMapURL={`https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=geometry,drawing,places&key=${process.env.REACT_APP_GOOGLE_KEY}`}
      loadingElement={<div style={{ height: "100%" }} />}
      containerElement={<div style={{ height: "100%" }} />}
      mapElement={<div style={{ height: "100%" }} />}
      />
    </div>
  );
}

export default App;
