from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8788093564:AAE0-Vuc2GunWbBquE5AWPQ3QzLeWz2DTbM"
ADMIN_ID = 8454986179

def save_user(user_id):
    with open("users.txt", "a+") as f:
        f.seek(0)
        users = f.read().splitlines()
        if str(user_id) not in users:
            f.write(str(user_id) + "\n")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    save_user(update.effective_user.id)
    await update.message.reply_text("Bot is working ✅")
 async def myid(update, context):
    await update.message.reply_text(f"Your ID is: {update.message.from_user.id}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("myid", myid))
app.add_handler(CommandHandler("admin", admin))

print("Bot Started...")
app.run_polling()"
ADMIN_ID = 8454986179


def save_user(user_id):
    with open("users.txt", "a+") as f:
        f.seek(0)
        users = f.read().splitlines()

        if str(user_id) not in users:
            f.write(str(user_id) + "\n")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    save_user(update.effective_user.id)
    await update.message.reply_text("✅ Bot is working")


async def myid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"Your ID is: {update.message.from_user.id}"
    )


async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
 if update.message.from_user.id == ADMIN_ID:
        await update.message.reply_text("👑 Admin Panel")
    else:
        await update.message.reply_text("❌ You are not admin")


async def course(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 Courses:\n\n"
        "1. Video Editing - ₹99\n"
        "2. Instagram Growth - ₹99\n"
        "3. AI Tools - ₹99\n"
        "4. Coding PW Skills Combo - ₹99"
 )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("myid", myid))
app.add_handler(CommandHandler("admin", admin))
app.add_handler(CommandHandler("course", course))

print("Bot Started...")
app.run_polling()
