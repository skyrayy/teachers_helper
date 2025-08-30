#переменные
TOKEN = 'токен бота' 
prog_link = 't.me/имя_пользователя_техподдержки' #ссылка на чат техподдержки
teacher_id = 'ID учителя' 
password = 'Код подтверждения'
archive = 'ID фрхив-чата' #чат, куда бот отправляет списки. в случае сброса бота, можно использовать архив для восстановления данных.

student_id_name = {}
student_id_works = {}

def is_student(id): #проверка на наличие ученика в списке
    name = student_id_name.get(id)
    if name != None:
        return name
    else: return None

def new_student(id, name):
    student_id_name[id] = name
    student_id_works[id] = {}

def save():
    saved = f"students_id_name = {str(student_id_name)}\nstudents = {str(student_id_works)}"
    return saved

def rating():
    rating_text = 'Ваш список учеников и их средний балл:\n'
    for id in student_id_name:
        marks = student_id_works.get(id)
        if len(marks)==0:
            average=0
        else:
            average = sum(marks.values()) / len(marks) // 0.01
        rating_text += student_id_name.get(id) + ' ' + str(average) + '\n'
    return rating_text
        
def detect_student(name):
    for id in student_id_name:
        if name == student_id_name.get(id):
            return id
    return None

def students_marks_list(name):
    id = detect_student(name)
    if id != None:
        marks_list = student_id_works.get(id)
        if not marks_list:
            return 'У этого ученика еще нет оценок.'
        return 'Список оценок ученика '+name+':\n'+str(marks_list)
    return 'Ученик не найден.'

def changing_mark(name, text, mark):
    id = detect_student(name)
    marks_list = student_id_works.get(id)
    marks_list[text] = mark

def my_rating(id):
    marks_list = student_id_works.get(id)
    if not marks_list:
        return 'У вас еще нет оценок.'
    return 'Список ваших оценок:\n'+str(marks_list)
