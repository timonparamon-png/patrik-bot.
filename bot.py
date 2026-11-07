import os
import telebot

TELEGRAM_TOKEN = "8996493982:AAHLFIM790ZxZHuRFwHuKQDTBq25KkMtufM"
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    try:
        print(f"Получено: {message.text}")
        # Бот отвечает заготовленной харизматичной фразой Патрика
        bot.reply_to(message, "Йоу! Я Патрик. На связи, бро!")
    except Exception as e:
        print(f"Ошибка: {e}")
        bot.reply_to(message, f"Ошибка: {e}")

if __name__ == "__main__":
    print("Патрик запущен...")
    bot.infinity_polling()
    
 
 
