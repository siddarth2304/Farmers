// Initialize chatbot
function initializeChatbot() {
    const botConnection = new BotChat.DirectLine({
        secret: 'YOUR_DIRECT_LINE_SECRET' // Replace with your Direct Line secret
    });

    BotChat.App({
        botConnection: botConnection,
        user: { id: 'USER_ID', name: 'User' },
        bot: { id: 'BOT_ID', name: 'Farming Bot' },
        resize: 'detect'
    }, document.getElementById("bot"));
}

// Call functions to initialize
initializeChatbot();
