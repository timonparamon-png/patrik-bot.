import os
import telebot
from groq import Groq

TELEGRAM_TOKEN = "8996493982:AAGhSYjJvPIYFtCjo34b1VOQGrr9WbTgHIs"
GROQ_API_KEY = "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"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = (
    "Ты — Патрик, харизматичный участник дружеского чата. "
    "Ты относишься к чату с теплой иронией и харизмой. "
    "Умеешь поддерживать любой разговор коротко и естественно."
)

def generate_reply(user_message):
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            temperature=0.75,
            max_tokens=300
        )
        return completion.choices[0].message.content
    except Exception:
        return None

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        text = message.text or ""
        if text:
            response = generate_reply(text)
            if response:
                bot.reply_to(message, response)
    except Exception:
        pass

if __name__ == "__main__":
    print("Патрик запущен...")
    bot.infinity_polling()
    
  
