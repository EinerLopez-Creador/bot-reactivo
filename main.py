
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes



# Tu token de Telegram
TOKEN = '7450212431:AAH-PHefwoO-i6Mf5m8_-pe9_tMDx6XfblA'



# Definir los comandos y mensajes
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    keyboard = [
        [InlineKeyboardButton("Menú", callback_data='menu')],
        [InlineKeyboardButton("Video Introductorio", url="https://www.youtube.com/watch?v=By9axsanjKI")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(f'Hola {user.first_name}, Bienvenido a @MentorMegaBot! ¿Cómo puedo ayudarte hoy?', reply_markup=reply_markup)

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Tutoriales", callback_data='tutoriales'),
         InlineKeyboardButton("Canales", callback_data='canales')],
        [InlineKeyboardButton("Info", callback_data='info'),
         InlineKeyboardButton("Soporte", callback_data='support')],
        [InlineKeyboardButton("Landing Page", url="https://einer-lopez-maker-global-megamaker.my.canva.site/"),
         InlineKeyboardButton("Inicia con Mega Maker", url="https://app.megamaker.org/mmp?referrer=0xA2493c2b6bB7C4aA48AB368442DEb4cfcE305B54")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.edit_text('Menú para explorar opciones:', reply_markup=reply_markup)

async def tutoriales(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Introducción a Mega Maker", url="https://www.youtube.com/watch?v=wj0DjKelJ-A&list=PL1n2hn2CAZz8h-aRwzZDclzRAmRxVUHua&index=7%27"),
         InlineKeyboardButton("Crear cuenta en Meta Mask", url="https://www.youtube.com/watch?v=dID5Pwx1Srw&list=PL1n2hn2CAZz8h-aRwzZDclzRAmRxVUHua&index=2%27")],
        [InlineKeyboardButton("Comprar USDT y convertir a Matic", url="https://www.youtube.com/watch?v=hqeGUBkIz3A&list=PL1n2hn2CAZz8h-aRwzZDclzRAmRxVUHua&index=3%27"),
         InlineKeyboardButton("Conseguir MakerX y Maker Flip", url="https://www.youtube.com/watch?v=qqBrCyNPvGk&list=PL1n2hn2CAZz8h-aRwzZDclzRAmRxVUHua&index=4%27")],
        [InlineKeyboardButton("Participar en Mega Maker", url="https://www.youtube.com/watch?v=dez5FN4jcxA&list=PL1n2hn2CAZz8h-aRwzZDclzRAmRxVUHua&index=7%27"),
         InlineKeyboardButton("Minting de tu NFT", url="https://www.youtube.com/watch?v=UCjEkQsZ9sQ&list=PL1n2hn2CAZz8h-aRwzZDclzRAmRxVUHua&index=6%27")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.edit_text('Elige un tutorial:', reply_markup=reply_markup)

async def canales(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Discord", url="https://discord.gg/Ft9cWBhP"),
         InlineKeyboardButton("Foro Discord", url="https://discord.gg/megamaker")],
        [InlineKeyboardButton("Telegram Canal Oficial", url="https://t.me/MegaMakerComunidad"),
         InlineKeyboardButton("WhatsApp Canal Oficial", url="https://whatsapp.com/channel/0029Va9mIv09hXEznnVOHZ05")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.edit_text('Síguenos en nuestros canales informativos:', reply_markup=reply_markup)

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("White Paper", url="https://megamaker.tigercyberhouse.com/")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.edit_text('Conoce más sobre Mega Maker:', reply_markup=reply_markup)

async def support(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Contactar por WhatsApp", url="https://wa.me/message/XDVEL5HAGGALL1")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.edit_text('Para soporte con un humano, contacta a un mentor:', reply_markup=reply_markup)


def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(menu, pattern='menu'))
    application.add_handler(CallbackQueryHandler(tutoriales, pattern='tutoriales'))
    application.add_handler(CallbackQueryHandler(canales, pattern='canales'))
    application.add_handler(CallbackQueryHandler(info, pattern='info'))
    application.add_handler(CallbackQueryHandler(support, pattern='support'))

    application.run_polling()

if __name__ == '__main__': main( )