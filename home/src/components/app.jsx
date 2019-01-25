import React, { Component } from 'react';
import { Route, Switch, Redirect } from 'react-router-dom';

import Home from './home';
import SignUp from './signup';
import Login from './login';

class App extends Component {
  render() {
    return (
      <React.Fragment>
        <div className="row header">
          <h1>DeRegNet REST API</h1>
        </div>
        <div>
          <Switch>
            <Route path="/signup" exact component={SignUp} />
            <Route path="/login" exact component={Login} />
            <Route path="/home" exact component={Home} />
            <Redirect from="/" to="/home" />
            <Redirect to="/home" />
          </Switch>
        </div>
      </React.Fragment>
    );
  }
}

export default App;
