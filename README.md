

# Telegram Bot for Excel Data Search

### Freelance Project: Telegram Bot to Search Excel Data Using Python and Pandas

---

## Overview

This Telegram bot was created as part of a freelance project aimed at automating the process of searching for specific data points in an Excel file. The bot accepts user input, searches predefined columns in the Excel sheet, and responds with matching results. The solution leverages the `python-telegram-bot` library for communication, `pandas` for data handling, and `requests` to fetch files from Google Drive.

---

## Features

- **Data Handling**: Loads an Excel file and allows users to search specific columns ('FAT' and 'DSL_DESCRIPTION').
- **Google Drive Integration**: The bot can download the Excel file directly from a Google Drive link.
- **Asynchronous Processing**: Uses async functions to handle user inputs and bot responses.
- **Customizable**: Can be easily adapted to work with any Excel file and search any columns.
  
---

## Skills Demonstrated

### 1. **Python Development**:
   - Developed an interactive Telegram bot using Python and the `python-telegram-bot` library.
   - Implemented async functions for efficient and responsive interaction between the bot and users.

### 2. **Data Processing**:
   - Utilized `pandas` to load and search data from an Excel file, allowing for flexible data manipulation.
   - Integrated file handling techniques to download and read an Excel file directly from Google Drive.

### 3. **Asynchronous Programming**:
   - Implemented asynchronous functions to manage multiple user requests simultaneously, ensuring the bot remains responsive during searches.

### 4. **API Integration**:
   - Connected the bot to Telegram’s API for communication.
   - Utilized the Google Drive API to fetch files dynamically for data processing.

---

## Project Files

- **`bot.py`**: The main Python file containing the bot’s functionality.
- **`requirements.txt`**: Contains the necessary Python libraries required to run the project.

---

## Prerequisites

- **Python 3.7+**
- **Telegram Bot Token**: You need to create a Telegram bot and get your token from [BotFather](https://core.telegram.org/bots#botfather).
- **Google Drive Excel File**: Ensure your Google Drive Excel file is publicly accessible or shared with a direct download link.

---

## Installation and Setup

### 1. Clone the repository:

```bash
git clone https://github.com/Ankush2201/Airtel-bot-freelance.git
cd Airtel-bot-freelance
```

### 2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3. Modify the Bot Token:

Open the `bot.py` file and replace the placeholder token with your actual Telegram bot token.

```python
application = Application.builder().token("YOUR_BOT_TOKEN").build()
```

### 4. Update the Google Drive link:

Update the Google Drive link in the `bot.py` file where the Excel file is downloaded:

```python
url = "https://drive.google.com/uc?export=download&id=YourFileID"
```

### 5. Run the bot:

```bash
python bot.py
```

---

## How to Use the Bot

1. Start the bot by typing `/start` in your Telegram chat.
2. Enter any search term, and the bot will search through the `FAT` and `DSL_DESCRIPTION` columns of the provided Excel file.
3. The bot will return the top matching results in the chat window.

---

## Tech Stack

- **Languages**: Python
- **Libraries**: 
  - `pandas` for data handling
  - `python-telegram-bot` for Telegram API integration
  - `requests` for file downloading
  - `openpyxl` for Excel file processing
- **Deployment**: The bot can be deployed on platforms such as Railway, Heroku, or any other cloud environment supporting Python.

---

## Challenges Faced

1. **Handling Large Excel Files**: Optimized data loading and search mechanisms to ensure quick responses even with large datasets.
2. **Google Drive Integration**: Managed file fetching directly from Google Drive and handling permissions to make the file accessible.
3. **Asynchronous Programming**: Ensured the bot handles multiple requests simultaneously without downtime, using async functions.

---

## Future Improvements

1. **Add More File Types**: Extend support for other data file types such as CSV, Google Sheets, etc.
2. **Enhanced Search**: Implement fuzzy search and advanced filters to improve search accuracy.
3. **User Authentication**: Add features for authenticating users to limit bot access to authorized personnel.

---

## Contact

**Ankush Pandey**  
Freelance Python Developer  
Feel free to contact me via email or through my GitHub profile for further inquiries or project collaborations.

