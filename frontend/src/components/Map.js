import React from 'react';
import { GoogleMap, Marker, InfoWindow } from 'react-google-maps';
import axios from 'axios';


const containerStyle = {
    width: "400px",
    height: "400px",
  };

export default class Map extends React.Component {

    constructor(props) {
      super(props);

      this.setTherapist = this.setTherapist.bind(this);
      this.setPsychiatrist = this.setPsychiatrist.bind(this);
      this.setCurrentDoctor = this.setCurrentDoctor.bind(this);

      this.state = {
        lat: 42.331429,
        lng: -83.045753,
        therapistList: [],
        psychiatristList: [],
        currentDoctor: null
      }
    }

    componentDidMount() {

      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
          this.setState({
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          });
          axios.get('http://127.0.0.1:5000/therapist/' + this.state.lat.toString() + '/' + this.state.lng.toString())
          .then(response => {
            this.setTherapist(response['data']);
          });
    
          axios.get('http://127.0.0.1:5000/psychiatrist/' + this.state.lat.toString() + '/' + this.state.lng.toString())
          .then(response => {
            this.setPsychiatrist(response['data']);
          });
        });
      }
    }

    setTherapist(content) {
      this.setState({
        therapistList: content
      });
    }

    setPsychiatrist(content) {
      this.setState({
        psychiatristList: content
      });
    }

    setCurrentDoctor(content) {
      this.setState({
        currentDoctor: content
      });
    }

  render() {   
    return (
        <GoogleMap
          mapContainerStyle={containerStyle}
          center={{ lat: this.state.lat, lng: this.state.lng }}
          zoom={10}
        > 
        {
        this.state.therapistList.map(therapist => (
          <Marker 
              key={therapist.id}
              position={{lat: therapist.coords[0], lng: therapist.coords[1]}}
              onClick={() => {
                this.setCurrentDoctor(therapist);
                console.log(this.state.currentDoctor)
              }}
          />
        )) 
        }
        {
          this.state.psychiatristList.map(psychiatrist => (
            <Marker 
                key={psychiatrist.id}
                position={{lat: psychiatrist.coords[0], lng: psychiatrist.coords[1]}}
                onClick={() => {
                  this.setCurrentDoctor(psychiatrist);
                  console.log(this.state.currentDoctor)
                }}
            />
          )) 
        }
        {
          this.state.currentDoctor && (
            <InfoWindow
            position={{lat: this.state.currentDoctor.coords[0], lng: this.state.currentDoctor.coords[1]}}
            onCloseClick={() => {
              this.setCurrentDoctor(null)
            }}
            >
            <div>
              <p>{this.state.currentDoctor.name}</p>
              <p>{this.state.currentDoctor.address}</p>
              <p>Rating: {this.state.currentDoctor.rating}</p>
              <p>Number of Ratings: {this.state.currentDoctor.numRatings}</p>
            </div>
            </InfoWindow>
          )
        }
        </GoogleMap>
    );
  }
}


