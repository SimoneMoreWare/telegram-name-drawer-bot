Telegram Name Drawer Bot
========================

A simple Telegram bot that allows users to draw a name randomly from a predefined list. Each user can draw only once, simulating a lottery or drawing from an urn.

Features
--------

*   Users can start a conversation and draw a name.
*   Each user can only draw once.
*   Provides feedback if there are no more names left to draw.

Requirements
------------

*   Python 3.6 or higher
*   An active Telegram account
*   A Telegram bot token (obtained from [BotFather](https://core.telegram.org/bots#botfather))

Installation
------------

1.  Clone the repository:
    
        git clone https://github.com/your-username/telegram-name-drawer-bot.git
        cd telegram-name-drawer-bot
    
2.  Install the required packages:
    
        pip install -r requirements.txt
    
3.  Obtain your bot token from [BotFather](https://core.telegram.org/bots#botfather) and replace `YOUR_TELEGRAM_TOKEN` in the `bot.py` file with your actual bot token.

Usage
-----

1.  Run the bot:
    
        python bot.py
    
2.  Open Telegram and search for your bot using its username.
3.  Start a conversation with your bot by sending the command `/start`.
4.  To draw a name, send the command `/draw`.

Global Variables
----------------

*   `TELEGRAM_TOKEN`: The token provided by BotFather. Replace the placeholder with your actual token.
*   `names`: A list of names from which the bot can randomly draw. Modify this list to change the available names.
*   `drawn_users`: A dictionary that tracks users who have already drawn a name. This ensures each user can draw only once.

Contributing
------------

Feel free to contribute by opening issues or submitting pull requests. Your feedback and contributions are welcome!

License
-------

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
