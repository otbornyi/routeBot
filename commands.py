import telebot
import webbrowser
import tgKey
bot = telebot.TeleBot(tgKey.priv())
def botCommands():
    @bot.message_handler(commands = ['about'])
    def about(message):
        bot.send_message(message.chat.id, ' Мы крупная федеральная сеть доставки вкуснейших суши и роллов"Koldun-Boldun"\n Мы занимаемся этим делом с 2015 года и готовы предложить вам продукцию из свежайших ингридиентов\n У нас вы можете заказать как через данного бота так и по телефону +7 999 999 99 99 ' )

    @bot.message_handler(commands = ["start"])
    def main(message):
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}, жмакай понравившуюся кнопку")

    @bot.message_handler()
    def info(message):
        if message.text.lower() == 'привет' :
            bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}")
        elif message.text.lower() == 'id':
            bot.reply_to(message, f'ID : {message.from_user.id}')
        elif message.text.lower() == 'что ты умеешь?':
            bot.send_message(message.chat.id, "Для полного ознакомления введи команду /help")

    bot.polling(non_stop=True)