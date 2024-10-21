# WhatsApp Automation Bot

## Introduction
This repository contains two projects focused on automating the process of sending messages and file attachments through WhatsApp. Both projects use WhatsApp Web for the message delivery mechanism but leverage different tools and approaches for automation. These solutions can be used to send timely alerts based on various triggers, ensuring fast and efficient communication directly through WhatsApp.

---

## Project 1: WhatsApp-Selenium-Bot

### Overview
The **WhatsApp-Selenium-Bot** project automates sending alerts through WhatsApp using the Selenium framework. This project is designed to handle real-time data extraction, processing, and report generation. Based on certain conditions, such as temperature or humidity thresholds, it triggers alerts that are sent via WhatsApp, ensuring prompt notifications. The alerts can include both text messages and file attachments, such as detailed reports in Excel format.

### Folder Structure
- **Messages Folder**: Contains scripts responsible for sending alerts as text messages without attachments.
- **Messages and Files Folder**: Includes the core functionality to handle both text messages and file attachments. 

Scripts here:
  - Connect to databases, extract and clean data.
  - Generate and format Excel reports.
  - Send notifications and files through WhatsApp Web.

### Key Features
- **Automated Alerts**: Automatically detects specific conditions and sends corresponding WhatsApp alerts.
- **File Attachments**: The bot generates reports, such as Excel files, and sends them alongside alert messages.
- **Data Processing**: Integrates data extraction, cleaning, and processing before generating and sending alerts.

### Limitations
- **WhatsApp Web Session**: An active WhatsApp Web session is required for the automation to function. If the session is interrupted, alerts will not be sent.
- **Server Dependence**: Continuous server uptime is essential. Any server failure can result in missed alerts.

---

## Project 2: WhatsApp-js-Bot

### Overview
The **WhatsApp-js-Bot** project uses the `whatsapp-web.js` API to automate sending messages and files through WhatsApp. The bot initiates a session by scanning a QR code and remains active to send periodic messages and file attachments to designated WhatsApp numbers or groups. This project is highly customizable, allowing users to modify the target recipients, messages, and files to fit various use cases.

### Key Features
- **QR Code Login**: The bot uses WhatsApp Web by scanning a QR code to authenticate and log in.
- **Send Messages and Files**: It can send both text messages and files to a target WhatsApp number or group.
- **Session Keep Alive**: Includes functionality to keep the WhatsApp session active, avoiding the need for constant re-authentication.
  
### File Structure
- **whatsapp-client.js**: Initializes the WhatsApp client, handles QR code generation, and manages sending text messages and files.
- **sendMessage.js**: Defines the function that sends a text message to a specified WhatsApp number.
- **sendFile.js**: Exports the function to send file attachments to a specified number or group.
- **keepAlive.js**: Ensures the session stays active by periodically sending logs to prevent disconnection.