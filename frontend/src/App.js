import React from 'react';
import './App.css';
import axios from 'axios'
import UserList from './components/Users.js'

class App extends React.Component {

  constructor(props) {
    super(props)
    this.state = {
      'users': []
    }
  }
  
  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/users')
      .then(response => {
        const users = response.data
          this.setState(
          {
            'users': users
          }
        )
      }).catch(error => console.log(error))
  }

  render () {
    return (
      <div>
        <p>Menu</p>
        <p>Content</p>
        <UserList users={this.state.users} />
        <p>Footer</p>
      </div>
    )
  }


}

export default App;
