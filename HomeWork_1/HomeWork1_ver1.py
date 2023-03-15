# 1. Посмотрите видео Дэвида Бизли про всроенные инструменты Python
# 2. Попробуйте используя встроенные инструменты Python проанализировать таблицу из файла "Vacancy.csv"
# 3. Попробуйте ответить на вопросы:
# Сколько вакансий, которые вам нравятся?
# Насколько свежие эти вакансии?
# Сколько вакансий с позициями на которых вы работаете?
# Сколько вакансий для аналатика данных?
# Сколько вакансий для аналитика данных с использованием Python?

# В задании важно не использовать pandas и numpy, а встроенные инструменты python
# Counter, CSV, defaultdict, sorted

# общее для всех
# Выше было много полей, пока рассуждал, и проверял всякие варианты,
# все удалил. Оставил только ответы на вопросы, отвечал не попорядку
import csv
import sys
import codecs

# это подсказали в группе в телеграмме
csv.field_size_limit(2000000000)
vacs = list(csv.DictReader(codecs.open('Vacancy.csv', 'r', 'utf_8_sig')))

# Все дальнейшее решения основывал на опыте SQL и PowerShell

# Сколько вакансий для аналатика данных?
# записываем в новую переменную название вакансий
vactitles = []
for vac in vacs:
    vactitles.append(vac['vactitle'])

# Вакансии ДА пишем в новый список
vacDA = []
for vac in vactitles:
    exist = 'Data Analyst' in vac
    exist2 = 'Data analyst' in vac
    exist3 = 'Аналитик данных' in vac
    # print(vac)
    if exist == True or exist2 == True or exist3 == True:
        vacDA.append(vac)

# print(vacDA)
# Выводим число вакансий Data Analyst
print("Число вакансий Дата Аналитик: " + str(len(vacDA)))

#
# Сколько вакансий с позициями на которых вы работаете? если тут подразумевалась должность, то вот такое решение, аналогично ДА
# записываем в новую переменную название вакансий
vactitles = []
for vac in vacs:
    vactitles.append(vac['vactitle'])

#
vac_Iam = []
for vac in vactitles:
    exist = 'Руководитель направления' in vac
    # print(vac)
    if exist == True:
        vac_Iam.append(vac)
#
print("Вакансий с позициями на которых я работаю (по должности): " + str(len(vac_Iam)))

# Сколько вакансий для аналитика данных с использованием Python?
# Аналогично как выше, только дополнительный цикл на проверку на слова Python
# записываем в новую переменную название вакансий
vactitles = []
for vac in vacs:
    vactitles.append(vac['vactitle'])

# Вакансии ДА пишем в новый список
vacDAP = []
for vac in vactitles:
    exist = 'Data Analyst' in vac
    exist2 = 'Data analyst' in vac
    exist3 = 'Аналитик данных' in vac
    # print(vac)
    if exist == True or exist2 == True or exist3 == True:
        # Дополнительно проверяем на питон
        existP = 'Python' in vac
        # print(vac)
        if existP == True:
            # print(vac)
            vacDAP.append(vac)

# print(vacDAP)
# Выводим число вакансий Data Analyst + Python
print("Число вакансий Дата Аналитик Python: " + str(len(vacDAP)))
#
# Насколько свежие эти вакансии?
# записываем в новую переменную даты обновления вакансий
updateds = []
for vac in vacs:
    updateds.append(vac['updated_at'])
# Выводим самую свежую дату обновления вакансий:
print("Самая свежая дата обновления вакансий: " + max(updateds)[:max(updateds).index(':') - 3])

# Сколько вакансий, которые вам нравятся?
# Аналогично как выше,
# записываем в новую переменную название вакансий
vactitles = []
for vac in vacs:
    vactitles.append(vac['vactitle'])

# Вакансии со словом Инженер\engineer считаем, что они нам нравятся пишем в новый список
vacLike = []
for vac in vactitles:
    exist = 'Инженер' in vac
    exist2 = 'инженер' in vac
    exist3 = 'engineer' in vac
    exist4 = 'Engineer' in vac

    # print(vac)
    if exist == True or exist2 == True or exist3 == True or exist4 == True:
        # print(vac)
        vacLike.append(vac)

# print(vacDAP)
print('Выводим число вакансий которые нравяться(со словами инженер): ' + str(len(vacLike)))
