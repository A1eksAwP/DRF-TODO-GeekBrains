import React from 'react'


class ProjectsForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'name': '',
            'repository_url': ''
        }
    }

    handleSubmit(event) {
        this.props.createProject(this.state.name, this.state.repository_url)
        event.preventDefault()
    }

    handleChange(event) {
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    render() {
        return (
        <form onSubmit={(event) => this.handleSubmit(event)}>
            <input type="text" name="name" placeholder="Название проекта" value={this.state.name} onChange={(event) => this.handleChange(event)} />
            <input type="text" name="repository_url" placeholder="URL на GitHub" value={this.state.repository_url} onChange={(event) => this.handleChange(event)} />
            <input type="submit" value="Create" />
        </form>
        )
    }
}

export default ProjectsForm;