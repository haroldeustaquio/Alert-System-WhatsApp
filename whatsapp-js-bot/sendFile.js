// sendFile.js
const { MessageMedia } = require('whatsapp-web.js');
const fs = require('fs');

const sendFile = (client, number, filePath, fileName) => {
    try {
        if (!fs.existsSync(filePath)) {
            throw new Error('File not found: ' + filePath);
        }

        // Crea el objeto de media desde el archivo
        const media = MessageMedia.fromFilePath(filePath);

        client.sendMessage(number, media, { caption: fileName })
            .then(response => {
                console.log('File sent successfully:', response);
            })
            .catch(err => {
                console.error('Error sending file:', err);
            });
    } catch (error) {
        console.error('Error sending file:', error);
    }
};

module.exports = sendFile;
