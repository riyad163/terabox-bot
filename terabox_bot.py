import os
import telebot

# ======== CONFIGURATION ========
BOT_TOKEN = "8131017134:AAHJFSlhTd9_ZK1x7kaK4jB-wbp9RPPYEwg"
TERABOX_EMAIL = "samirjrsa88@gmail.com"
TERABOX_PASSWORD = "Samir28agust#"
# ===============================

bot = telebot.TeleBot(BOT_TOKEN)

def upload_to_terabox(file_path):
    # Replace this mock with real upload logic later
    return f"https://terabox.fake.link/{os.path.basename(file_path)}"

@bot.message_handler(content_types=['video', 'document'])
def handle_file(message):
    file_id = message.video.file_id if message.content_type == 'video' else message.document.file_id
    file_info = bot.get_file(file_id)
    file_data = bot.download_file(file_info.file_path)

    file_name = os.path.basename(file_info.file_path)
    with open(file_name, 'wb') as f:
        f.write(file_data)

    bot.send_message(message.chat.id, "📤 Uploading to Terabox...")
    link = upload_to_terabox(file_name)
    bot.send_message(message.chat.id, f"✅ Uploaded!\n🔗 {link}")

    os.remove(file_name)

bot.polling()
