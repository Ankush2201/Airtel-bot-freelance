import pandas as pd
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Load your Excel file
EXCEL = r"C:\Users\lenov\Ankushpandey\rakesh_bot\CAF_TRACE_5_OCT.xlsx"  # Update with your actual file path
df = pd.read_excel(EXCEL)

# Function to handle the /start command
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Welcome! Send me a value to search.")

# Function to handle user input
async def search(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text.strip()

    # Search for the user input in the specified columns 'FAT' and 'DSL_DESCRIPTION'
    results = df[df['FAT'].str.contains(user_input, case=False, na=False) | 
                 df['DSL_DESCRIPTION'].str.contains(user_input, case=False, na=False)]

    if not results.empty:
        # Convert results to a list of dictionaries
        results_dict = results.to_dict(orient='records')

        # Limit output to two messages
        message_count = 0
        for entry in results_dict:
            # Format each entry as a string
            response = "\n".join(f"{key}: {value}" for key, value in entry.items())

            await update.message.reply_text(response)
            message_count += 1
            
            # Stop sending messages after two
            if message_count >= 4:
                break
    else:
        await update.message.reply_text("No matching entries found.")

def main() -> None:
    # Replace 'YOUR_TOKEN' with your bot's token
    print("Bot started")
    application = Application.builder().token("7826602538:AAHshlFKWWOZoEWx-CHOZkAYb6XWGL2J6cc").build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
