from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7085020077:AAFaj_B4ZbUaVLZ6omMFSpb3Yggdeb4-Ytw"
ADMIN_ID = 8454986179

def save_user(user_id):
    with open("users.txt", "a+") as f:
        f.seek(0)
        users = f.read().splitlines()
        if str(user_id) not in users:
            f.write(str(user_id) + "\n")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    save_user(update.effective_user.id)
    await update.message.reply_text("Bot is running!")

async def myid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Your Telegram ID: {update.effective_user.id}")

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_ID:
        try:
            with open("users.txt", "r") as f:
                count = len(f.read().splitlines())
            await update.message.reply_text(f"Total registered users: {count}")
        except FileNotFoundError:
            await update.message.reply_text("No users registered yet.")
    else:
        await update.message.reply_text("Unauthorized.")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("myid", myid))
    app.add_handler(CommandHandler("admin", admin))
    print("Bot Started...")
    app.run_polling()

if __name__ == "__main__":
    main()
