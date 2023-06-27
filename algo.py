import telebot

bot = telebot.TeleBot('5605087419:AAHmJ1TZWJntYdlEm0A7IHrIU61M-mdmnbs');  
@bot.message_handler(content_types=['text']) 
def get_text_messages(message): 
 
 
 
    if message.text == "Привет": 
        bot.send_message(message.from_user.id, "Привет давай найдем тебе друга в Standoff 2") 
    elif message.text == "Хочу тимейта у которого классные скины": 
          bot.send_message(message.from_user.id, "Могу тебе посоветовать игрока по имени  Асмир его ID:1432534346") 
    elif message.text == " дай совет новичку в Standoff 2 ": 
          bot.send_message(message.from_user.id, "Если ты только начал играть в Standoff 2  то посмотри ютубера Велю или же VLADMIX ") 
    elif message.text == "дай айди человека который играет с читами": 
          bot.send_message(message.from_user.id, "Есть игрок его зовут Владимир ID:657864754") 
    elif message.text == "что делать если тебя забанили просто так?": 
          bot.send_message(message.from_user.id, "Просто напиши на адрес standoff2@axlebolt.com.") 
    elif message.text == "ты какой то душный,давай поговорим?": 
          bot.send_message(message.from_user.id, "Да конечно!") 
    elif message.text == "как у тебя дела?": 
          bot.send_message(message.from_user.id, "У меня дела отлично!") 
    elif message.text == "мне не понравился бот": 
          bot.send_message(message.from_user.id, "Если вам что то не понравилось то напишите @Sinysenbgr") 
    elif message.text == "какие песни тебе нравятся?": 
          bot.send_message(message.from_user.id, "как виртуальный помощник я не могу испытывать чувств и предпочтений как люди.Однако я знаком с многими жанрами музыки и могу помочь вам найти сведение о любых песнях или музыкальных испольнителях. ") 
    elif message.text == "как тебе погода?": 
          bot.send_message(message.from_user.id, "как исскуственному интеллекту погода мне не имеет значения я не могу ее чувствовать или оценивать.") 
    elif message.text == "Какие заведение есть в Бишкек?": 
          bot.send_message(message.from_user.id, " Могу предложить Азия Молл, Цум,Гум,Площадь Ала - Тоо") 
    elif message.text == "/help": 
            bot.send_message(message.from_user.id, "Напиши привет") 

    else: 
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)