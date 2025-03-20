from dotenv import load_dotenv
import discord
import os
from app.mistral_ai.mistralai import mistral_response  

# Load environment variables
load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(message.content)  

        # Ignore bot messages
        if message.author == self.user:
            return
        
        command, user_message = None, None
        for text in ['/ai', '/bot', '/mistral']:
            if message.content.startswith(text):
                command = text
                user_message = message.content[len(text):].strip()  # Strip leading spaces

                print(f"Command: {command}, User Message: {user_message}")
                break  # Stop checking after the first match
        
        if command:
            bot_response = mistral_response(prompt=user_message)  # Ensure this function works
            await message.channel.send(f"Answer: {bot_response}")

# Set up bot with message content intent
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

# Run the bot
client.run(discord_token)
