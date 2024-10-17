# WhatsApp SeleniumBot

## Overview
This project automates the process of sending alerts and reports through WhatsApp. It integrates data extraction, cleaning, and the creation of notifications based on predefined conditions. Alerts include both messages and file attachments, ensuring timely updates directly to WhatsApp.

## Objective
The main goal of the project is to automate the detection of specific conditions (e.g., temperature and humidity thresholds) and send corresponding alerts via WhatsApp, complete with detailed reports in Excel format.

## Folder Structure

1. **Messages Folder**  
   Contains scripts that handle the automation of sending alerts as messages through WhatsApp, without file attachments.

2. **Messages and Files Folder**  
   Contains two key scripts that manage both sending messages and file attachments:
   - ``functions.py``: 
     - Connects to the database and retrieves data.
     - Cleans and processes the data.
     - Sends alert messages for temperature and humidity via WhatsApp.
     - Generates and formats an Excel report.
     - Automates sending the report as an attachment through WhatsApp.
   - ``wsp.py``: 
     - Manages the scheduling and execution of the alerting process.
     - Calls the functions from `functions.py` to process data and trigger alerts.
     - Ensures timely delivery of alerts and reports based on set schedules.


## Limitations

- **WhatsApp Web Session**: The script requires an active WhatsApp Web session, meaning the browser window with WhatsApp must remain open for the automation to function properly. If the session is interrupted, the alerts will not be sent.
- **Server Reliability**: The script depends on the server running continuously. Any issues with the server, such as a crash or network outage, will cause the script to stop and potentially miss sending critical alerts.