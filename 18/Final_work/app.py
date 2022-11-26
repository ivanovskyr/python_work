import telebot
from config import keys, TOKEN
from extensions import APIException, CryptoConverter
bot = telebot.TeleBot(TOKEN)

# @bot.message_handler() # Создадим обработчик для проверки работы бота
# def echo_test(message: telebot.types.Message):
#     bot.send_message(message.chat.id, 'Hello')

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем фотмате: \
    <имя валюты> \
    <в какую валюту перевести> \
    <количество переводимой валюты> \nДля вывода списка доступных валют введите /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise APIException("Неверное количество параметров. Для информации введите /help")
        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} равна {total_base*float(amount)}'
        bot.send_message(message.chat.id, text)

bot.polling()