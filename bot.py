from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import random

# Global variable for the bot token
TELEGRAM_TOKEN = "YOUR_TELEGRAM_TOKEN"

# List of names to draw from
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# Dictionary to track users who have already drawn
drawn_users = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Starts the conversation and provides instructions."""
    await update.message.reply_text("Hello! Type /draw to draw a name from the urn.")

async def draw_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the drawing of names."""
    user_id = update.message.from_user.id

    # Check if the user has already drawn a name
    if user_id in drawn_users:
        await update.message.reply_text("You have already drawn a name and cannot draw another!")
        return

    # Check if there are still names available
    if not names:
        await update.message.reply_text("There are no more names in the urn!")
        return

    # Randomly select a name from the list
    chosen_name = random.choice(names)
    names.remove(chosen_name)
    drawn_users[user_id] = chosen_name  # Record that the user has drawn a name

    await update.message.reply_text(f"You have drawn the name: {chosen_name}")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles unknown commands."""
    await update.message.reply_text("Unknown command. Use /draw to draw a name.")

def main():
    """Main function to start the bot."""
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("draw", draw_name))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
