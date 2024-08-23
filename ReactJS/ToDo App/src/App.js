import React from "react";
import { useState, useEffect } from 'react';
import "./App.css";


function taskStatus(task) {
  if (task["isDone"]) {
    return (<div>Completed</div>);
  } else if (task["inProcess"]) {
    return (<div>in Process</div>);
  } else {
    return (<div>not Started</div>);
  }
}

function App(props) {
  const [taskStatusScreen, setTaskStatusScreen] = useState(0);
  const [allTodos, setAllTodos] = useState([]);
  const [newTask, setNewTask] = useState("");
  const sampleData = [
    { "task": "this is task 1", "isDone": true, "inProcess": false },
    { "task": "this is task 2", "isDone": false, "inProcess": true },
    { "task": "this is task 3", "isDone": false, "inProcess": false }
  ];

  const storeUpdateTodo = (allTodos) => {
    // console.log(typeof allTodos);
    // console.log("data : ", allTodos);
    localStorage.setItem('data', JSON.stringify(allTodos));
    setAllTodos(allTodos);
  };

  const handleSubmit = (event) => {
    newTask = newTask.trim();
    if(newTask){
      let newTaskItem = { "task": newTask, "isDone": false, "inProcess": false };
      let updatedTodoArray = [...allTodos];
      updatedTodoArray.splice(0, 0, newTaskItem);
      storeUpdateTodo(updatedTodoArray);
    }
    setNewTask("");
  };

  const handleEditTodo = (index) => {
    let updatedTask = prompt("Updated Task", allTodos[index]["task"]);
    updatedTask = updatedTask.trim();
    while (updatedTask.length === 0) {
      alert("Please enter valid task");
      updatedTask = prompt("Updated Task", allTodos[index]["task"]);
    }
    allTodos[index]["task"] = updatedTask;
    storeUpdateTodo(allTodos);
    window.location.reload();
  };

  const handleCompleteTodo = (index) => {
    let previousTask = allTodos[index];
    let updatedTodo = [...allTodos];
    if (previousTask["isDone"]) {
      previousTask["isDone"] = false;
      previousTask["inProcess"] = false;
    } else if (previousTask["inProcess"]) {
      previousTask["isDone"] = true;
      previousTask["inProcess"] = false;
    } else {
      previousTask["isDone"] = false;
      previousTask["inProcess"] = true;
    }
    updatedTodo[index] = previousTask;
    storeUpdateTodo(updatedTodo);
  };

  const handleDeleteTodo = (index, allTodo, doneTodos) => {
    let reducedTodo = [...allTodos];
    if (allTodo) {
      reducedTodo = [];
    } else if (doneTodos) {
      while (index < reducedTodo.length) {
        if (reducedTodo[index]["isDone"]) {
          reducedTodo.splice(index, 1);
        } else {
          index += 1;
        }
      }
    } else {
      reducedTodo.splice(index, 1);
    }
    storeUpdateTodo(reducedTodo);
  };

  useEffect(() => {
    let savedTodos = JSON.parse(localStorage.getItem('data'));
    if (savedTodos) {
      setAllTodos(savedTodos);
    } else {
      setAllTodos(sampleData);
    }
  }, []);

  const displayTodos = () => {
    let todoList = allTodos;
    if (taskStatusScreen === 1) {
      todoList = todoList.filter((item) => item["inProcess"] === true);
    } else if (taskStatusScreen === 2) {
      todoList = todoList.filter((item) => item["isDone"] === true);
    }
    return (
      <>
        {todoList && todoList.map((item, index) =>
          <div className="todo-list-item" key={index}>
            <div style={{
              textDecoration: item["isDone"] ? 'line-through' : 'none',
              color: item["inProcess"] ? 'orange' : item["isDone"] ? 'red': 'black'
            }} onClick={() => handleCompleteTodo(allTodos.indexOf(todoList[index]))} className="task-name">{item["task"]}</div>
            <div className="task-status">{taskStatus(item)}</div>
            <button className="task-delete" onClick={() => handleDeleteTodo(allTodos.indexOf(todoList[index]), false, false)}>delete</button>
            <button className="task-edit" onClick={() => handleEditTodo(allTodos.indexOf(todoList[index]))}>edit</button>
          </div>

        )}
      </>
    );
  };

  return (
    <div className="todo-container">
      <div className='todo-input'>
        <h1>Todo Input</h1>
        <div className="todo-input-box">
          <input type="text" placeholder="New Todo" value={newTask} onChange={(e) => setNewTask(e.target.value)} style={{fontSize:20}} />
        </div>
        <div className="todo-submit-button">
          <button style={{
            backgroundColor: newTask ? 'rgb(22, 184, 233)' : 'rgb(180, 180, 180)',
            color: newTask ? 'white' : 'rgb(100, 100, 100)',
            border: newTask ? '1px solid rgb(22, 184, 233)' : '1px solid rgb(180, 180, 180)'
          }} type='button' className='todo-button' onClick={() => handleSubmit()}><h2>Add Task</h2></button>
        </div>
      </div>
      <div className="todo-list-container">
        <h1>TodoList</h1>
        <div className="button-area">
          <button type='button' className={`isCompleteScreen ${taskStatusScreen === 0 && 'active-button'}`} onClick={() => setTaskStatusScreen(0)} ><h2>All</h2></button>
          <button type='button' className={`isCompleteScreen ${taskStatusScreen === 1 && 'active-button'}`} onClick={() => setTaskStatusScreen(1)} ><h2>In Process</h2></button>
          <button type='button' className={`isCompleteScreen ${taskStatusScreen === 2 && 'active-button'}`} onClick={() => setTaskStatusScreen(2)} ><h2>Completed</h2></button>
        </div>
        <div className="todo-list">
          {displayTodos()}
        </div>
        <div className="delete-button-area">
          <button type='button' className='delete-button' onClick={() => handleDeleteTodo(0, false, true)}><h2>Delete done tasks</h2></button>
          <button type='button' className='delete-button' onClick={() => handleDeleteTodo(0, true, false)}><h2>Delete all tasks</h2></button>
        </div>
      </div>
    </div>
  );
}
export default App;
