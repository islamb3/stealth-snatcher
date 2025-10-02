# bot.py
# بوت بسيط: يرد على /start برسالة ترحيب
# مبدئياً هذا الملف قد يحتوي على TOKEN مكان REPLACE_TOKEN
# و ADMIN_ID مكان REPLACE_ADMIN_ID حتى يتم استبداله أو تهيئته من سكربت التشغيل.

TOKEN = "REPLACE_TOKEN"
ADMIN_ID = "REPLACE_ADMIN_ID"  # اختياري: لو تحتاج تستخدمه لاحقاً

try:
    import telebot
except Exception as e:
    # لو لم تثبت المكتبة سيتم طباعة الخطأ
    print("مطلوب تثبيت المكتبة pyTelegramBotAPI (telebot). استخدم: pip install pyTelegramBotAPI")
    raise

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start(message):
    # رسالة بسيطة عند الضغط على /start
    bot.send_message(message.chat.id, "ههههه 😈 انا هكر ورح اهكرك لاترسل ستارت هههه")

if __name__ == "__main__":
    print("Bot is starting... (press Ctrl+C to stop)")
    try:
        bot.polling(non_stop=True)
    except Exception as e:
        print("Bot stopped with error:", e)