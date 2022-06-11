import React from 'react';
import './App.css';
import axios from 'axios'
import UserList from './components/Users.js'
import ProjectList from './components/Projects.js'
import ToDoList from './components/ToDo.js'
import LoginForm from './components/LoginForm.js'
import ProjectsForm from './components/ProjectsForm.js'
import ToDoForm from './components/ToDoForm.js'
import {BrowserRouter, Route, Routes, Link, useLocation} from 'react-router-dom'


const NotFound = () => {
  let location = useLocation()

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
            'todos': '',
            'token': ''
        }
    }

    obtainAuthToken(login, password) {

        axios
            .post('http://127.0.0.1:8000/api-auth-token/', {"username": login, "password": password})
            .then(response => {
                let token = response.data.token
                console.log(token)
                localStorage.setItem('token', token)
                this.setState({
                    'token': token
                }, this.getData)
            })
            .catch(error => console.log(error))
    }

    componentDidMount() {

        let token = localStorage.getItem('token')
        this.setState({
            'token': token
        }, this.getData)
    }

    logOut() {
        localStorage.setItem('token', '')
        this.setState({
            'token': ''
        }, this.getData)
    }

    isAuth() {
        return !!this.state.token
    }

    getHeaders() {
        if (this.isAuth()) {
            return {
                'Authorization': 'Token ' + this.state.token
            }
        }
        return {}
    }

    getData() {
        let headers = this.getHeaders()

        axios
            .get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                let users = response.data
                this.setState({
                    'users': users
                })
            })
            .catch(error => {
                this.setState({
                    'users': []
                })
                console.log(error)
            })

        axios
            .get('http://127.0.0.1:8000/api/projects/', {headers})
            .then(response => {
                let projects = response.data
                this.setState({
                    'projects': projects
                })
            })
            .catch(error => {
                this.setState({
                    'projects': []
                })
                console.log(error)
            })

        axios
            .get('http://127.0.0.1:8000/api/todo/', {headers})
            .then(response => {
                let todo = response.data
                this.setState({
                    'todos': todo
                })
            })
            .catch(error => {
                this.setState({
                    'todos': []
                })
                console.log(error)
            })

    }

    createProject(name, repository_url) {
        let headers = this.getHeaders()

        axios
            .post('http://127.0.0.1:8000/api/projects/', {'name': name, 'repository_url': repository_url}, {headers})
            .then(response => {
                this.getData()
            })
            .catch(error => {
                console.log(error)
            })

    }

    createToDo(description, project, users, deadline) {
        let headers = this.getHeaders()

        axios
            .post('http://127.0.0.1:8000/api/todo/', {'description': description, 'project': project, 'users': users, 'deadline': deadline}, {headers})
            .then(response => {
                this.getData()
            })
            .catch(error => {
                console.log(error)
            })

    }

    deleteProject(id) {
        let headers = this.getHeaders()

        axios
            .delete(`http://127.0.0.1:8000/api/projects/${id}`, {headers})
            .then(response => {
                this.setState({
                    'projects': this.state.projects.filter((project) => project.id !== id)
                })
            })
            .catch(error => {
                console.log(error)
            })
    }

    deleteToDo(id) {
        let headers = this.getHeaders()

        axios
            .delete(`http://127.0.0.1:8000/api/todo/${id}`, {headers})
            .then(response => {
                this.setState({
                    'todos': this.state.projects.filter((todo) => todo.id !== id)
                })
            })
            .catch(error => {
                console.log(error)
            })
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <li><Link to='/users'>Пользователи</Link></li>
                        <li><Link to='/projects'>Проекты</Link></li>
                        <li><Link to='/projects/create'>Создать проект</Link></li>
                        <li><Link to='/todos'>Задачи</Link></li>
                        <li><Link to='/todos/create'>Поставить новую задачу</Link></li>
                        <li>
                        { this.isAuth() ? <button onClick={()=>this.logOut()}>Logout</button> : <Link to='/login'>Login</Link> }
                        </li>
                    </nav>

                    <Routes>
                        <Route exact path='/' element = {<UserList users={this.state.users} />} />
                        <Route exact path='/users' element = {<UserList users={this.state.users} />} />
                        <Route exact path='/projects' element = {<ProjectList projects={this.state.projects} deleteProject={(id) => this.deleteProject(id)}/>} />
                        <Route exact path='/projects/create' element = {<ProjectsForm projects={this.state.projects} createProject={(name, repository_url) => this.createProject(name, repository_url)} />} />
                        <Route exact path='/todos' element = {<ToDoList todos={this.state.todos} deleteToDo={(id) => this.deleteToDo(id)}/>} />
                        <Route exact path='/todos/create' element = {<ToDoForm todos={this.state.todos} projects={this.state.projects} users={this.state.users} createToDo={(description, project, users, deadline) => this.createToDo(description, project, users, deadline)} />} />
                        <Route exact path='/login' element = {<LoginForm obtainAuthToken={(login, password) => this.obtainAuthToken(login, password)}/>} />
                        <Route path='*' element = {<NotFound />} />
                    </Routes>
                </BrowserRouter>
            </div>
        )
    }
  }

  export default App;