import React from 'react'

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.name}</td>
            <td>{project.creator}</td>
            <td>{project.repository_url}</td>
            <td>{project.created}</td>
            <td>{project.updated}</td>
            <td>{project.is_active}</td>
        </tr>
    )
}

const ProjectList = ({projects}) =>  {
    return (
        <table>
        <th>Название</th>
        <th>Создатель</th>
        <th>Ссылка</th>
        <th>Создано</th>
        <th>Обновлено</th>
        <th>Активно</th>
        {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList