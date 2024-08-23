import './App.css';
import React, {useState, useEffect} from 'react';

function App() {

  const [clientId, setClientId] = useState(
    Math.floor(new Date().getTime()/1000));
  const [usernameInput, setUsernameInput] = useState(false);
  const [username, setUsername] = useState("");
  // const [isOnline, setIsOnline] = useState(false);
  const [websckt, setWbsckt] = useState()
  const [message, setMessage] = useState([]);
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const url = "ws://localhost:8080/ws/" + clientId;
    const ws = new WebSocket(url);

    ws.onopen = (event) => {
      // const temp_message = [clientId, username, username + " joined the chat.", true]
      // ws.send(JSON.stringify(temp_message))
    }

    ws.onmessage = (e)=>{
      const temp_message = JSON.parse(e.data);
      console.log(e);
      setMessages((messages) => [...messages, temp_message]);
    }

    setWbsckt(ws);

    return () => ws.close();
  }, []);

  const sendMessage = () => {
    console.log(username);
    const temp_message = [clientId, username, message, false, true]
    websckt.send(JSON.stringify(temp_message));
    setMessage([]);
  };

  const joinChat = () => {
    let temp = message;
    const flag = temp.trim().length;
    if(flag){
      setUsername(temp.trim());
      const temp_message = [clientId, temp.trim(), " " + temp.trim() + " joined the chat.", true, true]
      websckt.send(JSON.stringify(temp_message));
      setMessage([]);
      setUsernameInput(true);
    }
  };

  async function fetchData(client_id) {
    try {
      const response = await fetch('http://localhost:8080/check/' + client_id);
      const data = await response.json();
      console.log("Result:", data.result);
      return data.result;
    } catch (error) {
      console.error("Error fetching data:", error);
      return false;
    }
  }

  // useEffect(() => {
  //   let temp_messages = [], temp_message = [];
  //   for(let i = 0; i < messages.length; i++){
  //     if(!fetchData(messages[i].client_id))
  //     console.log("object print: ", messages[i]);
  //     temp_message = messages[i];
  //     if(!fetchData(temp_message.client_id)){
  //       temp_message.status = false;
  //     }
  //     temp_messages = [...temp_messages, temp_message];
  //   }
  //   setMessages(temp_messages);
  // });

  if(usernameInput){
    return (
      <div className="container">
        <h1>You joined as "{username}"</h1>
        <div className="chat-container">
          <div className="chat">
            {messages.map((value, index) => {
              if (value.client_id === clientId ){
                if(value.welcome === false){
                  return (
                    <div key={index} className="my-message-container">
                      <div className="my-message">
                        <p className="client">You</p>
                        <p className="message">{value.message}</p>
                      </div>
                    </div>
                    );
                }else{
                  return (
                    <div key={index} className="my-message-container">
                      <div className="my-message">
                        <p className="message">You joined the chat.</p>
                      </div>
                    </div>
                    );
                }
              }else{
                let status ="offline";
                if(fetchData(value.client_id)){
                  status = "online"
                }
                
                // console.log("api call: ", data);
                if(value.welcome === false){
                  let connection = (<></>);
                  if(value.status){
                    connection = (<p className='client'>{/* <span className={status}></span>   */} {value.username}</p>);
                  }
                  return (
                  <div key={index} className="another-message-container">
                    <div className="another-message">
                      {connection}
                      <p className="message">{value.message}</p>
                    </div>
                  </div>
                  );
                }else{
                  return (
                    <div key={index} className="another-message-container">
                      <div className="another-message">
                        <p className="message">{value.username} joined the chat.</p>
                      </div>
                    </div>
                    );
                }
              }
            })}
          </div>
          <div className="input-chat-container">
            <input 
            className="input-chat" 
            type="text" 
            placeholder="Chat message..." 
            onChange={(e)=> setMessage(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && sendMessage()} 
            value={message}></input>
            <button className="submit-chat" onClick={sendMessage}>Send</button>
          </div>
        </div>
      </div>
    );
  }else{
    return (
      <div className="container">
        <h1>Welcome to chat server....</h1>
        <div className="chat-container">
          <div className="join-chat-container">
            <input 
            className="join-chat" 
            type="text" 
            placeholder="Enter your name to start chat..." 
            onChange={(e)=> setMessage(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && joinChat()} 
            value={message}></input>
            <button className="submit-name" onClick={joinChat}>Join</button>
          </div>
        </div>
      </div>
    )
  }
}

export default App;
