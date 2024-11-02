from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random
import json

# Global variable for the bot token - replace with your actual token
TELEGRAM_TOKEN = "YOUR_TELEGRAM_TOKEN"

# Load participants from a separate JSON file
def load_participants(filename='participants.json'):
    with open(filename, 'r') as file:
        return json.load(file)

# Load restrictions from a separate JSON file
def load_restrictions(filename='restrictions.json'):
    with open(filename, 'r') as file:
        return json.load(file)

# Priority order for drawing names
draw_order = [
    "marialicia", "rosalinda", "francesca", "simone", 
    "marica", "coccia", "giulia", "redon", 
    "flavio", "pasquale", "francesco_pio", "roby03", "antonio"
]

# Load participants and restrictions
participants = load_participants()
restrictions = load_restrictions()

# Remaining names to draw
remaining_names = list(participants.keys())

# Tracking who has drawn and who they picked
drawn_users = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Starts the bot and provides instructions."""
    await update.message.reply_text("Benvenuti al Secret Santa! Scrivi /pesca per estrarre un nome.")

async def draw_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles the drawing of names."""
    user_id = update.message.from_user.id
    user_name = participants.get(str(user_id), "Unknown")

    print(f"User {user_name} (ID: {user_id}) is attempting to draw a name.")

    # Check if user has already drawn a name
    if user_id in drawn_users:
        await update.message.reply_text("Hai già estratto un nome e non puoi estrarne un altro!")
        return

    # Check if all names are drawn
    if not remaining_names:
        await update.message.reply_text("Non ci sono più nomi nell'urna!")
        return

    # Check if it's the user's turn based on the draw order
    if draw_order[0] != user_name.lower():
        next_person = participants[draw_order[0]]
        await update.message.reply_text(f"Non è ancora il tuo turno. Aspetta che {next_person} faccia la sua estrazione.")
        return

    # Filter the remaining names excluding prohibited names for the current user
    allowed_names = [
        uid for uid in remaining_names 
        if uid != user_name and user_name not in restrictions.get(user_name.lower(), [])
    ]

    # Check if there are any valid names to draw
    if not allowed_names:
        await update.message.reply_text("Nessun nome disponibile per te! Contatta l'amministratore.")
        return

    # Randomly select a valid name
    chosen_id = random.choice(allowed_names)
    drawn_users[user_id] = chosen_id  # Record the drawn name
    remaining_names.remove(chosen_id)  # Remove chosen name from pool
    draw_order.pop(0)  # Move to the next person in the draw order

    await update.message.reply_text(f"Hai estratto: {participants[chosen_id]}")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles unknown commands."""
    await update.message.reply_text("Comando sconosciuto. Usa /pesca per estrarre un nome.")

def main():
    """Main function to start the bot."""
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pesca", draw_name))

    print("Bot avviato...")
    app.run_polling()

if __name__ == "__main__":
    main()
