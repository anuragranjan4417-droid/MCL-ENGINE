from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = "8662012390:AAHRsdwQQrpRQbMw17aL4dLC01B6PqAuF4Q"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚔️ Solo Match", callback_data="solo")],
        [InlineKeyboardButton("👥 Team Match", callback_data="team")],
        [InlineKeyboardButton("🏆 Tournament", callback_data="tournament")],
        [InlineKeyboardButton("📊 Profile", callback_data="profile")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🏏 Welcome to MCL Cricket Engine!\n\nChoose an option:",
        reply_markup=reply_markup,
    )

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("✅ MCL Cricket Engine Started...")
app.run_polling()
