from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler

from bot_commands import *
import emoji

app = ApplicationBuilder().token("TOKEN").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("play", play_command))
print(emoji.emojize(f'Привет :thumbs_up:'))
app.run_polling()
print("Server start")

app.run_polling()









# import matplotlib.pyplot as plt
# import numpy as np

# list = [1, 5, 7, 3, 6, 4]
# plt.plot(list)

# plt.show()





# import emoji

# print(emoji.emojize(':pulgar_hacia_arriba:', language='es'))




exit()
from progress.bar import Bar
import time

with Bar('Processing', max=20) as bar:
    for i in range(20):
        time.sleep(0.1)
        bar.next()



exit()
from isOdd import isOdd


print(isOdd(1))
print(isOdd(5))