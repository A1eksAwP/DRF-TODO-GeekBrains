import React from 'react'

const ToDoItem = ({todo, deleteToDo, users}) => {
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
            <td><button onClick={()=>deleteToDo(todo.id)} >Delete</button></td>
        </tr>
    )
}

const ToDoList = ({todos, deleteToDo, users}) =>  {
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
        {todos.map((todo) => <ToDoItem todo={todo} users={users} deleteToDo={deleteToDo}/>)}
        </table>
    )
}

export default ToDoList