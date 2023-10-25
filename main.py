from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN: Final = '6693963040:AAFgN6tI71ujSFeoPbiqlpX-5F-lMIIOgvU'

BOT_USERNAME: Final = '@Leonian_bot'


#change1

# Commands


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('سلام نسرین بانو من در خدمتم...')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('برای راهنمایی بیشتر به امیر زنگ بزنید')

async def nasrin_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('نسرین بانو امر امر شماست، درخدمتگزاری حاضرم')

# Responses

def handel_response(text: str) -> str:
    if 'hi' in text:
        return 'سلام بر نسرین بانو'
    
async def handel_message(update: Update, contex: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    response: str = handel_response(text)
    await update.message.reply_text(response)


if __name__ == '__main__':
    print('starting bot...')
    app = Application.builder().token(TOKEN).build()


    # Command
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('nasrin', nasrin_command))


    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)


