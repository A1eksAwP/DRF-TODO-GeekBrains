import React from 'react'


class ToDoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'description': '',
            'project': [], 
            'users': [], 
            'deadline': ''
        }
    }

    handleSubmit(event) {
        this.props.createToDo(this.state.description, this.state.project, this.state.users, this.state.deadline)
        event.preventDefault()
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    handleUserChange(event) {
        if (!event.target.selectedOptions) {
            return
        }

        let users = event.target.selectedOptions.item(0).value

        this.setState({
            'users': users
        })
    }

    handleProjectChange(event) {

        let project = event.target.value

        this.setState({
            'project': project
        })
    }

    render() {
        return (
        <form onSubmit={(event) => this.handleSubmit(event)}>
            <input type="text" name="description" placeholder="Описание задачи" value={this.state.description} onChange={(event) => this.handleChange(event)} />
            <input list="control" value={this.props.projects.find(p=>this.state.project==p.id)?.name} onChange={(event) => this.handleProjectChange(event)}/>
            <datalist id="control" >
                {this.props.projects.map((project) => <option value={project.id}>{project.name}</option>)}
            </datalist>
            <select onChange={(event) => this.handleUserChange(event)}>
                {this.props.users.map((user) => <option value={user.id}>{user.username}</option>)}
            </select>
            <input type="text" name="deadline" placeholder="Крайний срок выполнения" value={this.state.deadline} onChange={(event) => this.handleChange(event)} />
            <input type="submit" value="Create" />
        </form>
        )
    }
}

export default ToDoForm;