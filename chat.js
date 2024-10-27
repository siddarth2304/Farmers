function toggleChat() {
    const chatbox = document.getElementById('chatbox');
    chatbox.style.display = chatbox.style.display === 'none' ? 'flex' : 'none';
}

document.getElementById('sendMessage').addEventListener('click', function() {
    const userInput = document.getElementById('userInput').value;
    const messagesDiv = document.getElementById('messages');

    messagesDiv.innerHTML += `<p>User: ${userInput}</p>`;

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        messagesDiv.innerHTML += `<p>Bot: ${data.response}</p>`;
        document.getElementById('userInput').value = ''; // Clear input
    });
});

document.getElementById('helpButton').addEventListener('click', function() {
    const helpMessage = "You can ask me about the weather or type 'help' for available commands.";
    const messagesDiv = document.getElementById('messages');
    messagesDiv.innerHTML += `<p>Bot: ${helpMessage}</p>`;
});
