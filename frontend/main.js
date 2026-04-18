const ws = new WebSocket("ws://localhost:8000/ws/chat");

const chatBox = document.getElementById("chatBox");

function addMessage(text, className) {
    const msg = document.createElement("div");
    msg.className = "message " + className;
    msg.innerText = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMessage() {
    const input = document.getElementById("messageInput");
    const text = input.value;

    if (!text) return;

    addMessage(text, "user");
    ws.send(text);

    input.value = "";
}

ws.onmessage = function (event) {
    addMessage(event.data, "bot");
};

// Enter key support
document.getElementById("messageInput").addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});