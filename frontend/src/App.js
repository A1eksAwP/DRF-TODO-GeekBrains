import React from 'react';
import './App.css';
import axios from 'axios'
import UserList from './components/Users.js'
import ProjectList from './components/Projects.js'
import ToDoList from './components/ToDo.js'
import {BrowserRouter, Route, Routes, Link, useLocation} from 'react-router-dom'


const NotFound = () => {
  var location = useLocation()

  return (
      <div>
          Page "{location.pathname}" not found
      </div>
  )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
        }
    }

    componentDidMount() {
        axios
            .get('http://127.0.0.1:8000/api/users/')
            .then(response => {
                let users = response.data
                this.setState({
                    'users': users
                })
            })
            .catch(error => console.log(error))
        axios
            .get('http://127.0.0.1:8000/api/projects/')
            .then(response => {
                let projects = response.data
                this.setState({
                    'projects': projects
                })
            })
            .catch(error => console.log(error))
        axios
            .get('http://127.0.0.1:8000/api/todo/')
            .then(response => {
                let todo = response.data
                this.setState({
                    'todos': todo
                })
            })
            .catch(error => console.log(error))
    }
// http://localhost:3000/#/projects
// http://localhost:3000/projects
    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <li><Link to='/users'>Пользователи</Link></li>
                        <li><Link to='/projects'>Проекты</Link></li>
                        <li><Link to='/todos'>Задачи</Link></li>
                    </nav>

                    <Routes>
                        <Route exact path='/' element = {<UserList users={this.state.users} />} />
                        <Route exact path='/users' element = {<UserList users={this.state.users} />} />
                        <Route exact path='/projects' element = {<ProjectList projects={this.state.projects} />} />
                        <Route exact path='/todos' element = {<ToDoList todos={this.state.todos} />} />
                        <Route path='*' element = {<NotFound />} />
                    </Routes>
                </BrowserRouter>
            </div>
        )
    }
  }

  export default App;