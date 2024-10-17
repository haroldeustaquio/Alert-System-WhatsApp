// keepAlive.js
module.exports = (client) => {
    setInterval(() => {
        console.log('Keeping session alive...');
    }, 300000); // Cada 5 minutos
};
