import os
import random
import telebot
from groq import Groq

TELEGRAM_TOKEN = "ВАШ_TELEGRAM_TOKEN"
GROQ_API_KEY = "ВАШ_GROQ_API_KEY"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = (
    "Ты — Патрик, харизматичный участник дружеского чата на 20 человек. "
    "Ты относишься к чату с теплой иронией, дружеской иронией и харизмой. "
    "Умеешь поддерживать любой разговор — от повседневных тем, жизненных историй и юмора до обсуждения любых интересов компании. "
    "Пиши естественно, коротко, без искусственной вежливости и без шаблонов 'Чем я могу помочь?'. "
    "Разговаривай на равных, как старый приятель."
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
def handle_group_messages(message):
    try:
        username = message.from_user.username or ""
        text = message.text or ""

        is_bot_tagged = "@" in text.lower() or "патрик" in text.lower()
        is_reply = message.reply_to_message and message.reply_to_message.from_user.id == bot.get_me().id

        random_interject = random.random() < 0.05

        if is_bot_tagged or is_reply or random_interject:
            response = generate_reply(text)
            if response:
                bot.reply_to(message, response)
    except Exception:
        pass

if __name__ == "__main__":
    print("Патрик запущен...")
    bot.infinity_polling()
  
