
from email.mime import application
from telegram.ext import *
from weather import hi_command, help_command,get_command


# if name == "main":
app = application.builder().token("5759772520:AAEVHcs8e7Jd4lA-pjZ8GoZRcZR382rCnWs").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("get", get_command))
app.run_polling()