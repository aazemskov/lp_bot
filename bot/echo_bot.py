import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from cred import TOKEN

logging.basicConfig(filename='bot.log', level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def greet_user(update, context):
    print('Вызван /start')
    return update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    return update.message.reply_text(text)


def main():
    mybot = Updater(TOKEN, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info(f' >> Бот стартовал')

    mybot.start_polling()
    mybot.idle()


if __name__ == '__main__':
    main()
