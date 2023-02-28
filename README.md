# OpenAI Discord Chatbot

This is a simple chatbot for Discord that uses the OpenAI API to generate responses to user queries. The bot can be trained on various language models and can be customized with different parameters.

Features:
- Interactive messaging: The bot engages in a conversation with users, responding to their questions and providing contextually relevant information.
- Data persistence: The bot remembers previous conversations and can retrieve them later.
- Command-based interface: Users interact with the bot through commands, which can be customized and extended.
- Easy deployment: The bot can be run on any server that supports Python and Nextcord.

Dependencies:
- Python 3.7 or higher
- Nextcord 2.0 or higher
- OpenAI API key (get one for free at https://beta.openai.com/signup/)
- SQLite3 (built-in with Python)

Usage:
1. Clone this repository and install the dependencies.
2. Set the following environment variables:
    - DISCORD_TOKEN: the Discord bot token (get one at https://discord.com/developers/applications/)
    - OPENAI_API_KEY: the OpenAI API key (get one at https://beta.openai.com/signup/)
4. Edit your config.json file with api keys...
3. Run the bot with `python main.py`.

Contributing:
Feel free to contribute to this project by submitting bug reports, feature requests, or code improvements. Pull requests are welcome!

License:
This project is licensed under the MIT License. See LICENSE.md for more details.
