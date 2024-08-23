import React, {useState, useEffect} from 'react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Button, Modal, Form, Input} from 'antd';
import Home_Page from './home_page';
import About_Page from './about_page';
import Contact_Page from './contact_page';
import {BrowserRouter as Router, Routes, Route, Navigate,} from "react-router-dom";


function App(props) {
    const PopUpForm = ({form, form_name}) => {
        if(form_name === "Login"){
            return (
            <Form form={form} layout="vertical" name="form_in_modal" initialValues={{ modifier: 'public', }}>
                <Form.Item name="username" label="User Name" rules={[{ required: true, message: 'Please enter username!', }, ]}>
                <Input />
                </Form.Item>
                <Form.Item name="password" label="Password" rules={[{required: true, message: 'Please enter password!',},]}>
                <Input type="password" />
                </Form.Item>
            </Form>
            );
        }else{
        return (
            <Form form={form} layout="vertical" name="form_in_modal" initialValues={{ modifier: 'public', }}>
            <Form.Item name="firstname" label="First Name" rules={[{ required: true, message: 'Please enter First Name!', }, ]}>
                <Input type="text"/>
            </Form.Item>
            <Form.Item name="lastname" label="Last Name" rules={[{ required: true, message: 'Please enter Last Name!', }, ]}>
                <Input type="text"/>
            </Form.Item>
            <Form.Item name="username" label="User Name" rules={[{ required: true, message: 'Please enter username!', }, ]}>
                <Input />
            </Form.Item>
            <Form.Item name="password" label="Password" rules={[{required: true, message: 'Please enter password!',},]}>
                <Input type="password" />
            </Form.Item>
            <Form.Item name="confirm password" label="Confirm Password" rules={[{required: true, message: 'Please confirm your password!',},]}>
                <Input type="password" />
            </Form.Item>
            </Form>
        );
        }
    };


    const CollectionCreateForm = ({ visible, onCreate, onCancel, button_name }) => {
      const [form] = Form.useForm();
      const [usersData, setUsersData] =  useState([]);

      let users_data = JSON.parse(localStorage.getItem("users") || "[]");
      // console.log(users_data);
      useEffect(() => {
          if(users_data){
              setUsersData(users_data);
          }
      }, [visible]);

      return (
          <Modal visible={visible} title={button_name} okText={button_name} cancelText="Cancel" onCancel={onCancel} onOk={() => {
              form.validateFields().then((values) => {
                  form.resetFields();
                  onCreate(values);
                  if(button_name === "Login"){
                      const temp = usersData.find((usersData) => { return values['username'] === usersData["username"]});
                      if(temp != undefined){
                      if(temp['username']===values['username'] && temp['password']===values['password']){
                          alert(`Welcome: ${values['username']}`);
                      }else{
                          alert('Invalid username or password.');
                      }
                      }else{
                      alert("No such user exists. Please register.");
                      }
                  }else{
                      const temp = usersData.find((usersData) => { return values['username'] === usersData.username});
                      if(temp !== undefined){
                      alert("Username already exists.");
                      }else if(values['password'] !== values['confirm password']){
                      alert("Password didn't matched.");
                      }else{
                      var temp_usersData = usersData;
                      temp_usersData.push(values);
                      setUsersData(temp_usersData);
                      localStorage.setItem('users', JSON.stringify(usersData));
                      alert("Registration Complete. You can login now.");
                      }
                  }
                  }).catch((info) => {
                  console.log('Validate Failed:', info);
                  });
              }}>
              <PopUpForm form={form} form_name={button_name}/>
          </Modal>
          );
    };

    const CollectionsPage = ({button_name}) => {
        const [visible, setVisible] = useState(false);
        const onCreate = (values) => {
            // console.log('Received values of form: ', values);
            setVisible(false);
        };
        return (
            <div>
            <Button class="btn btn-outline-success m-4" type="primary" onClick={() => { setVisible(true); }}> {button_name} </Button>
            <CollectionCreateForm visible={visible} onCreate={onCreate} onCancel={() => { setVisible(false); }} button_name={button_name}/>
            </div>
        );
    };

    return (
        <>
          <nav class="navbar bg-white navbar-expand-lg">
            <div class="container">
              <a class="navbar-brand" href="#">Navbar</a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/">Home</a>
                  </li>

                  <li class="nav-item">
                    <a class="nav-link" aria-current="page" href="/about">About</a>
                  </li>

                  <li class="nav-item">
                    <a class="nav-link" aria-current="page" href="/contactus">Contact Us</a>
                  </li>
                </ul>
                {/* <button class="btn btn-outline-success mx-4">Login</button> */}
                <div class="mx-2">
                  <CollectionsPage button_name={"Login"} />
                </div>
                <div class="mx-2">
                  <CollectionsPage button_name={"Register"} />
                </div>
                {/* <button class="btn btn-outline-success mx-4" type="submit">Register</button> */}
              </div>
            </div>
          </nav>
          <Router>
              <Routes>
                  <Route
                      exact
                      path="/"
                      element={<Home_Page />}
                  />
                  <Route
                      path="/about"
                      element={<About_Page />}
                  />
                  <Route
                      path="/contactus"
                      element={<Contact_Page />}
                  />
                  <Route
                      path="*"
                      element={<Navigate to="/" />}
                  />
              </Routes>
            </Router>
        </>
    );
}
export default App;