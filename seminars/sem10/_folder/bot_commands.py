from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
import play

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{datetime.datetime.now().time()}')
  
async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text
    items = mess.split()
    a = int(items[1])
    b = int(items[2])
    await update.message.reply_text(a+b)

async def play_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mess = update.message.text.split()
    
    await update.message.reply_text(play.showMatrix())
    await update.message.reply_text(int(mess[1]))
    await update.message.reply_text(play.player(int(mess[1])))