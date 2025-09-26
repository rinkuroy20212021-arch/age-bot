from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import datetime

# ⚠ Naya token yaha dalen
TOKEN = "8460909850:AAEDcQHT4VsaFzs-Y6wi-RfJ8o1upuhoX1w"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hi! Send me your birthdate in format DD-MM-YYYY and I’ll calculate your age."
    )

# Age calculator
async def calculate_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        birth_date = datetime.strptime(update.message.text, "%d-%m-%Y")
        today = datetime.today()
        age = today.year - birth_date.year - (
            (today.month, today.day) < (birth_date.month, birth_date.day)
        )
        await update.message.reply_text(f"🎉 Your age is: {age} years.")
    except ValueError:
        await update.message.reply_text("⚠ Please use format DD-MM-YYYY (example: 25-09-2000).")

def main():
    print("Bot is starting...")  # Debug print
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT, calculate_age))  # Simple filter

    print("Polling started...")  # Debug print
    app.run_polling()

if __name__ == "__main__":
    main()
