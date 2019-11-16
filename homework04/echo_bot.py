import telebot


access_token = '981879027:AAH9zDV_BUrvhyZ3V6Txq7XMqHUlGsHRlbQ'
telebot.apihelper.proxy = {'https': 'https://188.170.233.105:3128'}

# Создание бота с указанным токеном доступа
bot = telebot.TeleBot(access_token)


# Бот будет отвечать только на текстовые сообщения
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling()
