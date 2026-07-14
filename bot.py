from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_TOKEN = "8662012390:AAHRsdwQQrpRQbMw17aL4dLC01B6PqAuF4Q"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⚔️ Solo Match", callback_data="solo")],
        [InlineKeyboardButton("👥 Team Match", callback_data="team")],
        [InlineKeyboardButton("🏆 Tournament", callback_data="tournament")],
        [InlineKeyboardButton("👤 Profile", callback_data="profile")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🏏 **Welcome to MCL Cricket Engine**\n\n"
        "Choose an option below:",
        parse_mode="Markdown",
        reply_markup=reply_markup,
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "solo":
        await query.edit_message_text(
            "⚔️ Solo Match\n\nComing in the next step..."
        )

    elif query.data == "team":
        await query.edit_message_text(
            "👥 Team Match\n\nComing in the next step..."
        )

    elif query.data == "tournament":
        await query.edit_message_text(
            "🏆 Tournament System\n\nComing Soon..."
        )

    elif query.data == "profile":
        user = query.from_user
        await query.edit_message_text(
            f"👤 Profile\n\n"
            f"Name: {user.first_name}\n"
            f"User ID: {user.id}"
        )


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

print("✅ MCL Cricket Engine Started Successfully...")
app.run_polling()
