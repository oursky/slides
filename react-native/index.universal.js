'use strict';

var React = require('react-native');
var {
  AppRegistry,
  StyleSheet,
  Text,
  View,
} = React;
// 1 OMIT
var ChatRoom = React.createClass({

  getInitialState: function() {
    return {
      email: 'rick.mak@gmail.com',
      password: '123456',
      responseText: 'Click to load the remote data'
    };
  },
// 2 OMIT
  remote: function() {
    fetch('https://keybase.io/rickmak/key.asc')
      .then((response) => response.text())
      .then((responseText) => {
        this.setState({
          responseText
        })
        console.log(responseText);
      }.bind(this))
      .catch((error) => {
        console.warn(error);
      });
  },
// 3 OMIT
  jsourd: function() {
    var jsourd = require('jsourd');
    jsourd.endPoint = 'http://192.168.1.89/';
    jsourd.configApiKey('secretOURD');
    var email = this.state.email;
    var password = this.state.password;
    jsourd.login(email, password).then(function() {
      console.log('login ok');
      console.log(jsourd.currentAccessToken);
      this.setState({
        responseText: jsourd.currentAccessToken
      })
    }.bind(this), function(error) {
      console.log('login failed');
      console.log(error);
      this.setState({
        responseText: error
      });
    }.bind(this));
  },
// 4 OMIT
  render: function() {
    return (
      <View style={styles.container}>
        <Text style={styles.welcome}>
          Welcome to JS Rule Nine Realms!
        </Text>
        <Text style={styles.remote} onPress={this.remote}>
          {this.state.responseText}
        </Text>
      </View>
    );
  }
});

var styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 10,
  },
  remote: {
    fontSize: 9,
    height: 100,
    textAlign: 'center',
    color: '#333333',
    marginTop: 5,
    overflow: 'hidden',
  },
});
// 5 OMIT
AppRegistry.registerComponent('ChatRoom', () => ChatRoom);
