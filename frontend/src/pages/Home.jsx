import Header from "../components/Header";
import UploadBox from "../components/UploadBox";
import ChatBox from "../components/ChatBox";
import MessageInput from "../components/MessageInput";
import { useState } from "react";

import "../styles/Home.css";
import "../styles/Chat.css";
import "../styles/Upload.css";

function Home() {

  const [messages, setMessages] = useState([
    {
      sender: "ai",
      text: "Hello! Upload a document and ask me anything.",
    },
  ]);

  return (
    <div className="container">

      <Header />

      <UploadBox />

      <ChatBox messages={messages} />

      <MessageInput
        messages={messages}
        setMessages={setMessages}
      />

    </div>
  );
}

export default Home;