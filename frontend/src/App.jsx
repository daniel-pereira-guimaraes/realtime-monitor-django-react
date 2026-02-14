import { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8000/ws/monitor/");

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      setMessage(data.message);
    };

    return () => socket.close();
  }, []);

  return (
    <div>
      <h1>Monitor</h1>
      <p key={message} className="received">{message}</p>
    </div>
  );
}

export default App;