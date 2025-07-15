# Desktop Data Entry Bot

> **⚠️ IMPORTANT NOTE**: This script has been tested successfully on **macOS only**. It has not been tested on Windows or Linux systems.

## Overview

The Desktop Data Entry Bot is an automated solution that fetches blog posts from the JSONPlaceholder API and creates formatted text files using desktop applications (TextEdit on macOS, Notepad on Windows). The bot processes 10 blog posts and saves them as individual `.txt` files in a `tjm-project` directory on your desktop.


## Prerequisites

- Python 3.7 or higher
- Internet connection (for API access)
- macOS, Windows, or Linux operating system
- TextEdit (macOS), Notepad (Windows), or compatible text editor (Linux)

## Setup Instructions

### 1. Create Virtual Environment

```bash
# Navigate to your project directory
cd /path/to/Automated_Data_Entry

# Create virtual environment
python3 -m venv automated_env

# Activate virtual environment
# On macOS/Linux:
source automated_env/bin/activate
# On Windows:
automated_env\Scripts\activate
```

### 2. Install Dependencies

```bash
# Install required packages
pip install pyautogui requests
```

**Required Dependencies:**
- `pyautogui`: For desktop automation and keyboard/mouse control
- `requests`: For API calls to fetch blog posts
- We didn't install BotCity as it's not required for the project


## Usage

### Running the Bot

1. **Activate your virtual environment** (if not already active):
   ```bash
   source automated_env/bin/activate  # macOS/Linux
   # or
   automated_env\Scripts\activate     # Windows
   ```

2. **Run the desktop bot**:
   ```bash
   python desktop_bot.py
   ```

3. **Follow the on-screen instructions**:
   - The bot will detect your operating system
   - A 3-second countdown will give you time to prepare
   - Move your mouse to the top-left corner of the screen to stop the bot at any time

### What to Expect

#### During Execution:
1. **System Detection**: Bot identifies your OS and prepares appropriate text editor
2. **API Fetching**: Retrieves 10 blog posts from JSONPlaceholder
3. **File Processing**: For each post:
   - Launches text editor (TextEdit/Notepad)
   - Types formatted blog content
   - Opens save dialog
   - Saves file to `~/Desktop/tjm-project/`
   - Closes text editor
4. **Progress Updates**: Real-time status for each post
5. **Completion Summary**: Shows success/failure counts and file locations

#### Expected Output:
```
🤖 Desktop Automation Bot Starting...
⚠️  IMPORTANT: Move your mouse to the top-left corner to stop the bot at any time
🍎 macOS detected - Using TextEdit
💡 Note: TextEdit will be set to plain text mode automatically
💾 Save dialog will be opened with Cmd+S using .hold() method
⚡ Ultra-fast typing mode enabled
⏰ Starting in 3 seconds...
3...
2...
1...
🚀 Starting Desktop Automation Bot...
============================================================
🍎 Using TextEdit on macOS
💡 Will use Cmd+S with .hold() method for save dialog
⚡ Ultra-fast typing enabled
🌐 Fetching posts from JSONPlaceholder API...
📋 Retrieved 10 posts
============================================================

[1/10] Processing post 1...
📝 Processing Post 1: sunt aut facere repellat provident occaecati...
📁 Project directory exists: /Users/username/Desktop/tjm-project
⌨️  Typing content for post 1...
💾 Saving as post 1.txt...
💾 Saving to: /Users/username/Desktop/tjm-project/post 1.txt
✅ Successfully saved post 1.txt

[... continues for all 10 posts ...]

============================================================
🎉 AUTOMATION COMPLETE
✅ Successful: 10 posts
❌ Failed: 0 posts
📁 Files saved to: /Users/username/Desktop/tjm-project

📄 Created files:
  - post 1.txt
  - post 2.txt
  - post 3.txt
  - post 4.txt
  - post 5.txt
  - post 6.txt
  - post 7.txt
  - post 8.txt
  - post 9.txt
  - post 10.txt
```


## Platform-Specific Behavior

### macOS (Tested ✅)

### Windows (Not Tested ⚠️)

### Linux (Not Tested ⚠️)

## Safety Features

### Emergency Stop
- **Move your mouse to the top-left corner** of the screen to immediately stop the bot
- This is PyAutoGUI's built-in failsafe mechanism

### Keyboard Interrupt
- Press `Ctrl+C` in the terminal to stop the bot
- The bot will gracefully exit and close any open applications

