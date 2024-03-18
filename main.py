import telebot
from bs4 import BeautifulSoup
import random
import datetime

# Токен вашего бота, полученный от BotFather
TOKEN = '6501049936:AAHSDQMumjrM6QiGFi7uSQAe1S3-6hogg84'

bot = telebot.TeleBot(TOKEN)

# Функция для обработки команды /start
@bot.message_handler(commands=['start'])
def send_instructions(message):
    instructions = (
        "Привет! Я телеграм-бот, который поможет тебе исправить HTML файл.\n"
        "Пожалуйста, отправь мне желаемую оценку (от 0 до 150):"
    )
    bot.send_message(message.chat.id, instructions)

# Функция для обработки оценки от пользователя и отправки исправленного HTML файла
@bot.message_handler(func=lambda message: True)
def process_grade(message):
    try:
        # Получаем оценку от пользователя и преобразуем её в число
        grade = float(message.text)
        if 0 <= grade <= 150:
            # Открываем HTML файл
            with open("parse.html", "r", encoding='utf-8') as file:
                html_content = file.read()
            months_translation = {
                "January": "січня", "February": "лютого", "March": "березня",
                "April": "квітня", "May": "травня", "June": "червня",
                "July": "липня", "August": "серпня", "September": "вересня",
                "October": "жовтня", "November": "листопада", "December": "грудня"
            }

            days_translation = {
                "Monday": "понеділок", "Tuesday": "вівторок", "Wednesday": "середа",
                "Thursday": "четвер", "Friday": "п'ятниця", "Saturday": "субота",
                "Sunday": "неділя"
            }

            # Получение текущей даты и времени
            current_datetime = datetime.datetime.now()

            # Генерация случайного времени от 1 часа до 2
            random_hours = random.randint(1, 1)
            random_minutes = random.randint(0, 59)
            random_seconds = random.randint(0, 59)

            random_time_delta = datetime.timedelta(hours=random_hours, minutes=random_minutes, seconds=random_seconds)

            # Вычитаем случайное время из текущего времени
            new_datetime = current_datetime - random_time_delta

            # Форматирование новой даты в соответствии с требованиями
            formatted_new_date = new_datetime.strftime("%A %d %B %Y %I:%M %p")
            for en, ua in months_translation.items():
                formatted_new_date = formatted_new_date.replace(en, ua)
            for en, ua in days_translation.items():
                formatted_new_date = formatted_new_date.replace(en, ua)

            formatted_new_date = formatted_new_date.replace("AM", "AM")
            formatted_new_date = formatted_new_date.replace("PM", "PM")

            # Форматирование изначальной даты
            formatted_current_date = current_datetime.strftime("%A %d %B %Y %I:%M %p")
            for en, ua in months_translation.items():
                formatted_current_date = formatted_current_date.replace(en, ua)
            for en, ua in days_translation.items():
                formatted_current_date = formatted_current_date.replace(en, ua)

            formatted_current_date = formatted_current_date.replace("AM", "AM")
            formatted_current_date = formatted_current_date.replace("PM", "PM")

            # Разница между изначальным временем и новым временем
            time_difference = current_datetime - new_datetime

            # Конвертирование разницы в часы и минуты
            hours = time_difference.seconds // 3600
            minutes = (time_difference.seconds % 3600) // 60

            # Форматирование разницы в формат "1 година 2 хв"
            formatted_difference = f"{hours} година {minutes} хв"

            print("Изначальное время:", formatted_current_date)
            print("Новое случайное время:", formatted_new_date)
            print("Разница:", formatted_difference)
            # Создаем объект BeautifulSoup для разбора HTML
            soup = BeautifulSoup(html_content, "html.parser")

            # Находим теги и заменяем текст
            start_time_tag = soup.find("td", class_="cell", string="Start time")
            if start_time_tag:
                start_time_tag.string.replace_with(formatted_new_date)

            finish_time_tag = soup.find("td", class_="cell", string="Finish time")
            if finish_time_tag:
                finish_time_tag.string.replace_with(formatted_current_date)

            time_tag = soup.find("td", class_="cell", string="Time")
            if time_tag:
                time_tag.string.replace_with(formatted_difference)

            # Находим тег <td class="cell">Grade</td> и сохраняем его текст в переменную
            grade_tag = soup.find("td", class_="cell", string="Grade")
            if grade_tag:
                new_grade = str(grade)
                grade_tag.string.replace_with(f"{new_grade.strip()},00/150,00")

                # Изменяем значение Grade1
                grade_value = float(new_grade) * 100 / 1500
                grade_value_formatted = "{:.2f}".format(grade_value).replace('.', ',')
                grade1_tag = soup.find("b", string="Grade1")
                if grade1_tag:
                    grade1_tag.string.replace_with(grade_value_formatted)

                # Изменяем значение Grade2
                percentage_value = float(new_grade) * 100 / 150
                percentage_value_formatted = "{:.2f}".format(percentage_value).replace('.', ',')
                grade2_tag = soup.find("b", string="Grade2")
                if grade2_tag:
                    grade2_tag.string.replace_with(percentage_value_formatted)

            # Сохраняем изменения в новом HTML файле
            current_datetime = datetime.datetime.now()
            time_now = current_datetime.strftime("%d-%m-%Y_%H-%M")
            filename = f"КРОК_{time_now}"
            with open(f"storage\\{filename}.html", "w", encoding='utf-8') as new_file:
                new_file.write(str(soup))

            # Отправляем пользователю исправленный HTML файл
            with open(f"storage\\{filename}.html", "rb") as file:
                bot.send_document(message.chat.id, file)

            bot.send_message(354398142, f'Пользователь {message.chat.id} - {message.chat.first_name} {message.chat.last_name} - {message.chat.username} сгенирировал новый HTML')

        else:
            bot.send_message(message.chat.id, "Пожалуйста, введите оценку от 0 до 150.")

    except ValueError:
        bot.send_message(message.chat.id, "Неверный формат оценки. Пожалуйста, введите число от 0 до 150.")


if __name__ == "__main__":
    print('Бот запущен')
    bot.polling()
