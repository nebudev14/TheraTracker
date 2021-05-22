import React from 'react';
import Map from './components/Map';
import { withScriptjs, withGoogleMap } from 'react-google-maps'

const WrappedMap = withScriptjs(withGoogleMap(Map));

function App() {
  return (
    <div className="App">
      <WrappedMap googleMapURL={``}/>
    </div>
  );
}

export default App;
