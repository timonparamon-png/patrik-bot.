import os
import telebot
from groq import Groq

 "TELEGRAM_TOKEN = "8996493982:AAHLFIM790ZxZHuRFwHuKQDTBq25KkMtufM"
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
            model="llama-3-8b-8192",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            temperature=0.75,
            max_tokens=300
        )
        print("Ответ от Groq целиком:", completion)
        
        if completion.choices and completion.choices[0].message:
            return completion.choices[0].message.content
        return "Пустой массив ответов"
    except Exception as e:
        print(f"Ошибка внутри generate_reply: {e}")
        return f"Ошибка ИИ: {e}"

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        print(f"Получено: {message.text}")
        text = message.text or ""
        if text:
            response = generate_reply(text)
            if response:
                bot.reply_to(message, response)
            else:
                bot.reply_to(message, "Хм, пустой ответ от ИИ...")
    except Exception as e:
        print(f"Ошибка: {e}")
        bot.reply_to(message, f"Ошибка: {e}")

if __name__ == "__main__":
    print("Патрик запущен...")
    bot.infinity_polling()
 
