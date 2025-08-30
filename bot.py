import telebot
from telebot import * 
from base import TOKEN, password, teacher_id, archive, is_student, new_student, save, rating, students_marks_list, changing_mark, my_rating
from markups import markup1, markup2, techpodderjka

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.chat.id
    if str(user_id) == str(teacher_id):
        markup = markup1()
        bot.send_message(chat_id=user_id, text='Здравствуйте! Используйте меню для управления ботом.', reply_markup=markup)
    elif is_student(user_id) != None:
        markup = markup2()
        bot.send_message(chat_id=user_id, text='Здравствуйте! Используйте меню для управления ботом.', reply_markup=markup)
    else:
        bot.send_message(chat_id=user_id, text='Здравствуйте! Чтобы авторизироваться, как ученик, введите код. Узнать код вы можете у учителя.')
        bot.register_next_step_handler(message, get_password)
def get_password(message):
    user_id = message.chat.id
    text = message.text
    if text != password:
        bot.send_message(chat_id=user_id, text='Вы ввели неверный код. Узнайте код у учителя и попробуйте еще раз, используя команду /start')
    else:
        bot.send_message(chat_id=user_id, text='Отлично! Для авторизации введите свое имя и фамилию. Пожалуйста, отправьте свои данные именно в этом порядке. Разделите имя и фамилию одним пробелом.')
        bot.register_next_step_handler(message, get_new_name)
def get_new_name(message):
    user_id = message.chat.id
    name = message.text
    new_student(user_id, name)
    markup = markup2()
    bot.send_message(chat_id=user_id, text='Вы успешно прошли регистрацию! Используйте меню для управления ботом.', reply_markup=markup)
    saved = save()
    bot.send_message(chat_id=archive, text=saved)



@bot.message_handler(func=lambda message: message.text == 'Список учеников')
def studentsrating(message):
    chat_id = message.chat.id 
    teachers_rating = rating()
    if not teachers_rating == 'Ваш список учеников и их средний балл:\n':
        bot.send_message(chat_id=chat_id, text=teachers_rating)
    else:
        bot.send_message(chat_id=chat_id, text='Список учеников пуст.')


@bot.message_handler(func=lambda message: message.text == 'Успеваемость ученика')
def onerating(message):
    chat_id = message.chat.id
    bot.send_message(chat_id=chat_id, text='Введите имя и фамилию ученика.\n\nПожалуйста, для корректной работы бота отправьте данные именно в этом порядке. Разделите имя и фамилию одним пробелом.')
    bot.register_next_step_handler(message, choose_student)

def choose_student(message):
    chat_id = message.chat.id
    name = message.text
    text = students_marks_list(name)
    if text != 'Ученик не найден.':
        bot.send_message(chat_id=chat_id, text=text)
        bot.send_message(chat_id=chat_id, text='Чтобы изменить или добавить оценку введите ее существующее или новое название.\n\nЕсли вы не хотите менять или добавлять оценки, отправьте "-".')
        bot.register_next_step_handler(message, lambda msg: change_mark(msg, name)) 

def change_mark(message, name):  
    chat_id = message.chat.id
    text = message.text
    if text == '-':
        bot.send_message(chat_id=chat_id, text='Вы покинули меню изменения оценок.')
    else:
        bot.send_message(chat_id=chat_id, text='Введите новую оценку')
        bot.register_next_step_handler(message, lambda msg: change_marks_value(msg, name, text))  

def change_marks_value(message, name, text):  
    chat_id = message.chat.id
    mark = message.text
    changing_mark(name, text, mark)
    new_list = students_marks_list(name)
    bot.send_message(chat_id=chat_id, text='Успешно обновлено!\n\n'+new_list)
    saved = save()
    bot.send_message(chat_id=archive, text=saved)

@bot.message_handler(func=lambda message: message.text == 'Техподдержка') #запрос техподдержки, одинаковый для ученика и учителя
def need_support(message):
    markup = techpodderjka()
    chat_id = message.chat.id  
    message_id = message.message_id  
    bot.send_message(chat_id=chat_id, text='Перейдите по ссылке, чтобы связаться с техподдержкой.', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Мои оценки') 
def myrating(message):
    chat_id = message.chat.id   
    rating = my_rating(chat_id)
    bot.send_message(chat_id=chat_id, text=rating)
    

    



bot.polling()