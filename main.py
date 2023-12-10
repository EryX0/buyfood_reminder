import os
import datetime
from dotenv import load_dotenv # pip install python-dotenv
from telegram.ext import Application, CallbackContext

load_dotenv()
env_vars = os.environ

async def sendMsg(context: CallbackContext):
    chat_id = env_vars['CHAT_ID']
    # Get the current date and time
    now = datetime.datetime.now()
    two_days_ahead = now + datetime.timedelta(days=2)
    weekday = two_days_ahead.weekday()
    persian_weekdays = {0: 'دوشنبه', 1: 'سه‌ شنبه', 2: 'چهارشنبه', 3: 'پنج‌ شنبه', 4: 'جمعه', 5: 'شنبه', 6: 'یک‌شنبه'}
    persian_weekday = persian_weekdays[weekday]
    text = "❗🍴 یادآوری خرید غذای " + persian_weekday + " 🍴❗\n"
    # Send the message
    await context.bot.send_message(chat_id=chat_id, text=text)
    print("Notified Users")

    
def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("env_vars['BOT_TOKEN']").build()
    application.job_queue.run_once(sendMsg, 15)
    application.run_polling(drop_pending_updates=True)
if __name__ == "__main__":
    main()
