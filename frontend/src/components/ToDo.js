import React from 'react'

const ToDoItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.project}</td>
            <td>{todo.description}</td>
            <td>{todo.created_by}</td>
            <td>{todo.users}</td>
            <td>{todo.created}</td>
            <td>{todo.updated}</td>
            <td>{todo.is_active}</td>
            <td>{todo.deadline}</td>
        </tr>
    )
}

const ToDoList = ({todos}) =>  {
    return (
        <table>
        <th>Проект</th>
        <th>Описание</th>
        <th>Поставлено от</th>
        <th>Участники</th>
        <th>Создано</th>
        <th>Обновлено</th>
        <th>Активно</th>
        <th>Срок задачи</th>
        {todos.map((todo) => <ToDoItem todo={todo} />)}
        </table>
    )
}

export default ToDoList