from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests

Token: Final = 'Your Token'

BOT_USERNAME: Final = 'Your Bot Username'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام، به ربات قیمت طلا و دلار خوش اومدین")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("این ربات به منظور اعلام قیمت دلار و طلا ساخته شده")


#Responses

def handle_response(text: str):

    processed: str = text
    
    if "قیمت طلا" in processed:
        price = get_gold_price()
        if price:
            return f"{price}: تومان"
    elif "قیمت دلار" in processed:
        price = get_dollar_price()
        if price:
            return f"{price}: تومان"
    else:
        return "لطفا قیمت دلار یا قیمت طلا را تایپ کنید"

def get_gold_price():
        return "لطفا عیار طلای مورد نظر را انتخاب کنید"
def get_dollar_price():
    return "قیمت دلار"
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not isinstance(update.message.text, str):
        return  # پیام متن نیست، کاری نکن

    text = update.message.text
    response = handle_response(text)

    if response:  # فقط اگر پاسخی هست ارسال کن
        await update.message.reply_text(response)



def main():
    print("Bot is running...")

    app = Application.builder().token(Token).build()

    # commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # normal text
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()



