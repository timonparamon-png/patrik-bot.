import os
import telebot
from groq import Groq

TELEGRAM_TOKEN = "8996493982:AAHLFIM790ZxZHuRFwHuKQDTBq25KkMtufM"
GROQ_API_KEY = "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"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = Groq(api_key=GROQ_API_KEY)

SYSTEM_PROMPT = (
    "Ты — Патрик, харизматичный, ироничный и умный участник чата. "
    "Ты умеешь поддержать разговор с юмором, отвечаешь емко и по делу."
)

def generate_reply(user_message):
    try:
        # Используем актуальную легкую модель
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            temperature=0.75,
            max_tokens=300
        )
        if completion.choices and completion.choices[0].message:
            return completion.choices[0].message.content
        return "Хм, пустота в голове..."
    except Exception as e:
        return f"Ошибка ИИ: {e}"

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        text = message.text or ""
        if text:
            # Отправляем сообщение нейросети
            response = generate_reply(text)
            bot.reply_to(message, response)
    except Exception as e:
        bot.reply_to(message, f"Ошибка: {e}")

if __name__ == "__main__":
    print("Патрик с мозгами запущен...")
    bot.infinity_polling()
    
    
 
 
