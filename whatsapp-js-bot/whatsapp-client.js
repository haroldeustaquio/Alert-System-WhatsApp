const fs = require('fs');
const qrcode = require('qrcode-terminal');
const { Client, LocalAuth } = require('whatsapp-web.js');
const sendMessage = require('./sendMessage');
const sendFile = require('./sendFile');
const keepAlive = require('./keepAlive');

const client = new Client({
    authStrategy: new LocalAuth()
});

const number = '51XXXXXXXXX@c.us'; // Hacer prueba con num, luego pasar a grupo


const message = '';
const filePath = './prueba.txt'; // Cambiar ubicación del archivo
const fileName = ''; // Nombre del archivo

client.on('qr', (qr) => {
    qrcode.generate(qr, { small: true });
    console.log('Scan the QR code to log in.');
});

client.on('ready', () => {
    console.log('Client is ready!');

    keepAlive(client);

    setInterval(() => {
        sendMessage(client, number, message);
        sendFile(client, number, filePath, fileName); 
    }, 60000); // Cambiar duración del intervalo
});

// Inicializar el cliente
client.initialize();
