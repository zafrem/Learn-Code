# pip install python-telegram-bot

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# token
token="Your Token"


async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context):
    _help_str = '''This is test bot.'''
    await update.message.reply_text(_help_str)


async def echo(update, context):
    await update.message.reply_text(update.message.text)


def main():
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(token).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    #application.add_handler(CommandHandler("order", order_function))

    # on non command i.e message - echo
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()