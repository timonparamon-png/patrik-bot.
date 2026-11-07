import os
import telebot
import google.generativeai as genai

TELEGRAM_TOKEN = "8996493982:AAHLFIM790ZxZHuRFwHuKQDTBq25KkMtufM"
GEMINI_API_KEY = "AQ.Ab8RN6JFe6EyCdlSJWlvA1Pjm8jYs45oRwR0tr85yI1WNgGN1w"

# Инициализируем официальный клиент Google Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Настраиваем параметры генерации
generation_config = {
    "temperature": 0.9,
    "max_output_tokens": 300,
}

# Используем стабильную модель через официальный SDK
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

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
                bot.reply_to(message, "Патрик призадумался и остался без слов...")
        except Exception as e:
            bot.reply_to(message, f"Ошибка ИИ: {e}")

if __name__ == "__main__":
    print("Патрик запущен с официальным SDK Gemini...")
    bot.infinity_polling()
    
    
    
    


    
    
 
  
