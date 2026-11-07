import os
import telebot
import google.generativeai as genai

TELEGRAM_TOKEN = "8996493982:AAHLFIM790ZxZHuRFwHuKQDTBq25KkMtufM"
API_KEY = "AQ.Ab8RN6JAoGzTAakG_5A0BslqKdfTSg5t4Zz5eiBJ42-YMe_77g"

# Настраиваем официальный SDK Google для работы с OAuth-ключом
genai.configure(api_key=API_KEY)

# Используем официальную стабильную модель
model = genai.GenerativeModel("gemini-1.5-flash")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text or ""
    if text:
        try:
            prompt = f"Ты — Патрик, харизматичный, ироничный друг. Отвечай с юмором и коротко. Сообщение: {text}"
            response = model.generate_content(prompt)
            
            if response and response.text:
                bot.reply_to(message, response.text)
            else:
                bot.reply_to(message, "Патрик призадумался...")
        except Exception as e:
            bot.reply_to(message, f"Ошибка ИИ: {e}")

if __name__ == "__main__":
    print("Патрик запущен через официальный SDK...")
    bot.infinity_polling()
    
    
    
    
    
    


    
    
 
  
