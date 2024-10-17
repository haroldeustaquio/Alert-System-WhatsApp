// sendMessage.js
module.exports = async (client, number, message) => {
    try {
        await client.sendMessage(number, message);
        console.log('Message sent successfully');
    } catch (error) {
        console.error('Error sending message:', error);
    }
};
