import ChatMessage from "./ChatMessage";

function ChatBox({ messages }) {
  return (
    <div className="chat-container">
      {messages.map((msg, index) => (
        <ChatMessage
          key={index}
          sender={msg.sender}
          text={msg.text}
        />
      ))}
    </div>
  );
}

export default ChatBox;