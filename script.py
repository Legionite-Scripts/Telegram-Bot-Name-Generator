import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from faker import Faker
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get the bot token from .env
token = os.getenv("BOT_TOKEN")

# Create Faker Instance
fake = Faker()

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define the command handler function
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hi! Use /name to get a random name and surname.\nUse /address to generate Random Address."
    )


async def random_name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    random_name = fake.name()  # Generate a random name using Faker
    await update.message.reply_text(random_name)


async def random_address(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    random_address = fake.address()  # Generate a random Address using Faker
    await update.message.reply_text(random_address)


def main() -> None:
    # Application Created and passed to Bot's Token
    application = ApplicationBuilder().token(token).build()

    # Command Handlers Registered
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("name", random_name))
    application.add_handler(CommandHandler("address", random_address))

    # Start Bot
    application.run_polling()


if __name__ == "__main__":
    main()
