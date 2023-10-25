# библиотеки,загружаемые извне

from telebot import types
import telebot
TOKEN = 'Введите свой токен'


bot = telebot.Telebot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # клавиатура
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("⚽ Мой репозиторий")
    item2 = types.KeyboardButton("🎃 Написать в личку")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Привет от слона, {0.first_name}!".format(
        message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

# назначаем действия для клавиатуры


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '⚽ Мой репозиторий':
            bot.send_message(message.chat.id, 'https: // github.com/alesh89/')
        elif message.text == "🎃 Написать в личку":
            bot.send_message(message.chat.id, 'https: // t.me/vitos89/')
        else:
            bot.send_message(message.chat.id, "Не знаю,что ответить")


bot.polling(none_stop=True)
