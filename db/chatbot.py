import openai
import sqlite3
from datetime import datetime
from utils import JSON
from nextcord.ext import commands

conversations = {}
openai.api_key = JSON.Read("json/config.json")["OpenAIKey"]

# Create the table conversations if it doesn't exist


def create_table():
    conn = sqlite3.connect("./db/conversations.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS conversations
                 (user_id text, question text, response text)''')
    conn.commit()
    conn.close()

# Store a conversation in the database


def store_conversation(user_id, question, response):
    conn = sqlite3.connect("./db/conversations.db")
    c = conn.cursor()
    c.execute("INSERT INTO conversations VALUES (?, ?, ?)",
              (user_id, question, response))
    conn.commit()
    conn.close()

# Get a conversation from the database for a specific user


def get_conversation(user_id):
    conn = sqlite3.connect("./db/conversations.db")
    c = conn.cursor()
    c.execute(
        "SELECT question, response FROM conversations WHERE user_id=?", (user_id,))
    conversation = c.fetchall()
    conn.close()
    return conversation


class Chatbot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f"\u001b[32m[{datetime.now().strftime('%H:%M:%S')}] COG] » CHATBOT loaded successfully!\u001b[0m")
        create_table()

        # on startup, delete all conversations from the database
        conn = sqlite3.connect("./db/conversations.db")
        c = conn.cursor()
        c.execute("DELETE FROM conversations")
        conn.commit()
        conn.close()

    # Event that is triggered when a message is sent in a channel
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.channel.id == JSON.Read("json/config.json")["YourChannelID"]:
            user_id = str(message.author.id)

            # Obtains the conversation of the current user and if the user is the bot itself it does not do anything
            if user_id in conversations:
                conversation = conversations[user_id]
            else:
                conversation = []

            # Adds the current message to the conversation of the user
            conversation.append(message.content)

            # OpenAI API
            response = openai.Completion.create(
                engine="text-davinci-003", prompt="\n".join(conversation), max_tokens=1024, n=1, stop=None, temperature=0.7
            ).choices[0].text.strip()

            # Adds the OpenAI response to the conversation of the user
            conversation.append(response)
            store_conversation(user_id, message.content, response)
            conversations[user_id] = conversation

            # if the response is too long to be sent then send a message saying that the response is too long
            if len(response) > 2000:
                await message.reply("The response is too long to be sent.")
            # if cannot send an empty message (error 50006) then send a message saying that the response is null
            elif response == "":
                await message.reply("The OpenAI response is null.")
            # if the conversation is too long to be sent then send a message saying that the conversation is too long and delete the user's conversation from the database
            elif len("\n".join(conversation)) > 4000:
                await message.reply("``The conversation is too long to be sent, deleting user history...``")
                conn = sqlite3.connect("./db/conversations.db")
                c = conn.cursor()
                c.execute(
                    "DELETE FROM conversations WHERE user_id=?", (user_id,))
                conn.commit()
                conn.close()
                del conversations[user_id]
            else:
                await message.reply(response)
        await self.client.process_commands(message)


def setup(client):
    client.add_cog(Chatbot(client))
