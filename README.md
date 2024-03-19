# Telegram HTML Correction Bot

This Python script creates a Telegram bot that corrects HTML files based on user input. The bot engages users to provide a grade (ranging from 0 to 150) and then adjusts specific sections of an HTML file accordingly. The corrected HTML file is then sent back to the user via Telegram.

## Features:
- **User Interaction:** Users communicate with the bot by providing a grade input.
- **HTML Correction:** The bot modifies designated sections of an HTML file, including start time, finish time, time difference, and grade values.
- **Randomization:** It generates random time and date values for modification.
- **Ukrainian Date Formatting:** Dates are formatted according to Ukrainian standards.
- **Percentage Calculation:** The bot computes and updates grade values based on user input.
- **Error Handling:** It handles incorrect input formats and guides users towards valid input.

## Installation:
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Jitters007/HTMLEditor.git

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Obtain a Bot Token:**
   Get a bot token from BotFather on Telegram and replace the TOKEN variable in the script with your token.
   
5. **Change admins telegram id:**
   On line 136 change "YOUR_TELEGRAM_ID_HERE" to your telegram id

## Usage: 
1. **Run the Python Script:**
   ```bash
   python bot.py
2. **Initiate a Conversation with the Bot on Telegram: Follow the instructions to input a grade.**
3. **Receive the Corrected HTML File from the Bot.**

## Example:
Below is a simplified example of the bot's operation:

1. **User inputs a grade of 120.**
2. **The bot generates a random date and time, calculates grade values, and adjusts the HTML file accordingly.**
3. **The corrected HTML file is sent back to the user.**

## License:
This project is licensed under the MIT License.
