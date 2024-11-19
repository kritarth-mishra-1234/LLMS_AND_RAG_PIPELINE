import os
import telebot
import openai
from openai import OpenAI

OPEN_AI_API=os.environ.get('OPEN_AI_API')
# openai.api_key=OPEN_AI_API
client=OpenAI(api_key=OPEN_AI_API)
BOT_TOKEN=os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start','hello'])
def send_welcome(message):
    bot.reply_to(message, " hey this is kritarths ai powered chatbot? Ask whatever you wish to ask !")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    user_input = message.text

    try:
        # OpenAI API call for response generation
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            model="gpt-4o",
        )
        # Extracting and sending the reply from OpenAI
        bot_reply = response.choices[0].message.content.strip()
        bot.reply_to(message, bot_reply)

    except Exception as e:
        bot.reply_to(message, f"An unexpected error occurred: {str(e)}")

# Start the bot
bot.infinity_polling()