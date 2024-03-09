import telebot
import time

# Replace with your Telegram bot token
BOT_TOKEN = '6957887433:AAHXjE-2p5RM6h98ZKauhpaMjQlevYdDTVU'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name

    # Create keyboard with buttons
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    qr_button = telebot.types.KeyboardButton("QR Code Generator")
    url_button = telebot.types.KeyboardButton("URL Shortener")
    updates_button = telebot.types.KeyboardButton("Updates Channel")
    keyboard.add(qr_button, url_button)
    keyboard.add(updates_button)

    welcome_message = f"Hello  {first_name},\n\n**Jesse Network Services**\n\nHow may I assist you today?"
    bot.send_message(chat_id, welcome_message, parse_mode='Markdown', reply_markup=keyboard)

@bot.message_handler(commands=['qrcode'])
def qrcode_handler(message):
    # Add your logic for handling QR code generation (e.g., library integration)
    bot.send_message(message.chat.id, "QR Code generation functionality coming soon!")

@bot.message_handler(commands=['linkshort'])
def linkshort_handler(message):
    # Add your logic for handling URL shortening (e.g., library integration)
    bot.send_message(message.chat.id, "URL shortening functionality coming soon!")

@bot.message_handler(func=lambda message: True)  # Handle updates button click
def updates_handler(message):
    chat_id = message.chat.id

    for i in range(3):
        bot.send_chat_action(chat_id, 'typing')  # Simulate typing animation
        time.sleep(1)

    bot.send_message(chat_id, "Please join our Updates Channel for news and announcements:\nhttps://t.me/web_jesse_network")

if __name__ == '__main__':
    bot.polling()
