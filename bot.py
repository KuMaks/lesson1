from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import content

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    dp = mybot.dispatcher

    logging.info('Бот запущен')

    # список команд боту
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("git", about_git))
    
    # ответ бота на сообщения от пользователя
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    # ... что-то связано с запросами бота (необходимо позже дописать)
    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    """функция приветствия на команду /start""" 
    text = "Вызвана команда /start"
    print(text)
    update.message.reply_text(text)

def about_git(bot, update):
    """функция ответа на команду /git"""
    for key, value in content.git_answer:
        update.message.reply_text(value + " - " + key)
    
def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text + " ... сорян," + " но я пока не понимаю что это значит...")


main()