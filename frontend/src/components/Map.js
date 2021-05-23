import React from 'react';
import { GoogleMap, LoadScript } from 'react-google-maps';
import axios from 'axios';
import { render } from 'react-dom';

const containerStyle = {
    width: "400px",
    height: "400px",
  };

export default class Map extends React.Component {

    constructor(props) {
      super(props);

      this.state = {
        lat: 42.331429,
        lng: -83.045753,
        therapistList: [],
        psychiatristList: []
      }

    }

    componentDidMount() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
          this.setState({
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          });
        });
      }

      axios.get('http://127.0.0.1:5000/therapist/' + this.state.lat.toString() + '/' + this.state.lng.toString())
      .then(response => {
        this.setState({
          therapistList: response
        });
      });

      axios.get('http://127.0.0.1:5000/psychiatrist/' + this.state.lat.toString() + '/' + this.state.lng.toString())
      .then(response => {
        this.setState({
          psychiatristList: response
        });
      });

    }

  render() {   
    return (
        <GoogleMap
          mapContainerStyle={containerStyle}
          center={{ lat: this.state.lat, lng: this.state.lng }}
          zoom={10}
        >
          {/* Child components, such as markers, info windows, etc. */}
          <></>
        </GoogleMap>
    );
  }
}


