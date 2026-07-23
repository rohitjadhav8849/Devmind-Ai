import { useState } from "react";
import api from "../services/api";

function MessageInput({ messages, setMessages }) {
  const [question, setQuestion] = useState("");

  const sendMessage = async () => {
    if (!question.trim()) return;

    // Add user message
    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text: question,
      },
    ]);

    try {
      const res = await api.post("/chat", {
        question,
      });

      // Add AI reply
      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text: res.data.answer,
        },
      ]);
    } catch (err) {
      console.error(err);

      setMessages((prev) => [
        ...prev,
        {
          sender: "ai",
          text: "Something went wrong.",
        },
      ]);
    }

    setQuestion("");
  };

  return (
    <div className="message-input">
  
      <input
        type="text"
        value={question}
        placeholder="Ask anything about your document..."
        onChange={(e) => setQuestion(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === "Enter") {
            sendMessage();
          }
        }}
      />
  
      <button onClick={sendMessage}>
        Send
      </button>
  
    </div>
  );
}

export default MessageInput;