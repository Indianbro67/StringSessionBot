from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="pyrogram")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/adult_updates")],
    ]

    START = """
Hey {}

Welcome to {}

To Save To Timer Photos And Timer Video\nGenerating Session

By @Black_Devil_Admin
    """

    HELP = """
✨ **Available Commands** ✨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
**About This Bot** 

Telegram Bot to generate Pyrogram and Telethon string session by @StarkBots

Source Code : [Click Here](https://github.com/StarkBotsIndustries/StringSessionBot)

Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)

Developer : @StarkAgent
    """
