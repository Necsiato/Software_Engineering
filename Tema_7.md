# Тема 7. Работа с файлами (ввод, вывод).
Отчем по теме #7 выполнил(а):
- Клейн Денис Романович
- АИС-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + | - |
| Задание 7 | + | - |
| Задание 8 | + | - |
| Задание 9 | + | - |
| Задание 10 | + | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.

```txt 
Hello World!
Goodbye World!
```

### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/1.png)

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readline())
f.close()
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/2.png)

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readlines())
f.close()
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/3.png)

## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    print(f.readlines())
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/4.png)

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    for line in f:
        print(line)
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/5.png)

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
with open('input.txt', 'a+') as f:
    f.write('\nHow are you, world?')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/6.png)

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.

```python
lines = ['one','two','three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/7.1.png)
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/7.2.png)
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/7.3.png)

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).

```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит: ')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)

print_docs('/Users/user/Desktop/world/logs')
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/8.png)

## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст: Приветствие, Спасибо, Извините, Пожалуйста, До свидания, Ты готов? Как дела? С днем рождения! Удача! Я тебя люблю.

### Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).

```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key = len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len (sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_words('input.txt'))
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/9.png)

## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
• № - номер по порядку (от 1 до 300);

• Секунда – текущая секунда на вашем ПК;

• Микросекунда – текущая миллисекунда на часах.

### Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for line in range (1,301):
        writer.writerow([line, datetime.datetime.now().second,datetime.datetime.now().microsecond])
        time.sleep(0.01)
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/10.1.png)
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/10.2.png)

## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

```python
def word_counter(file):
    words = []
    summa = []
    count = {}

    with open (file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.lower().split()
            len_line = len(line)
            words.append((line, len_line))

            for word in line:
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1
        for i, v in words:
            summa.append(v)
        print(f'Всего слов: {sum(summa)}')
    word_max = max(count, key=count.get)
    max_count = max(count.values())
    print(f'Самое популярное слово: {word_max}\nПовторяется: {max_count}')
word_counter('ind1_input.txt')
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/11.1.png)
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/11.2.png)

## Выводы.
В данном коде реализована функция, которая считает кол-во слов и определяет самое популярное слово. Текст разбивается на слова при помощи split.

## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
def add_expense():
    expense_info = input("Инфорамция о расходах - ")
    expense_count = input("Сумма расходов - ")
    with open('ind2_input.txt', 'a', encoding='utf-8') as f:
        f.write(f'{expense_info} = {expense_count}\n')

def input_expense():
    with open('ind2_input.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip(' '))

while True:
    user_command = input('1 - add, \n2 - show \n')
    if user_command == '1':
        add_expense()
    elif user_command == '2':
        input_expense()
    else:
        print('error')
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/12.1.png)
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/12.2.png)

## Выводы.

В данном коде реализовано 2 функции - добавление расходов и вывод расходов из файла. Пользователь вводит команды (1 или 2 ) и в зависимости от нее вызывается определенная функция.

## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.
• Текст в файле:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

• Ожидаемый результат: Input file contains:
108 letters
20 words
4 lines

```python
def stats():
    with open('ind3_input.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    lines = text.count('\n') + 1
    words = len(text.split())
    letters = sum(1 for char in text if char.isalpha())

    print(f'{letters} символов')
    print(f'{words} слов')
    print(f'{lines} строк')

stats()
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/13.png)

## Выводы.

В этом коде реализована функция stats. Она расчитывает количество символов, слов и строк в файле.

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.
• Запрещенные слова:

hello email python the exam wor is

• Предложение для проверки:

Hello, world! Python IS the programming language of thE future. My EMAIL is....

PYTHON is awesome!!!!

• Ожидаемый результат:

*****, ***ld! ****** ** *** programming language of *** future. My ***** **....

****** ** awesome!!!!

```python
import re
def new_text(old_text, ban_word):
    for word in ban_word:
        sample = re.compile(re.escape(word), re.IGNORECASE)
        old_text = sample.sub('*' * len(word), text)
    return old_text
text = 'Hello, world! Python IS the programming language of thE future. My EMAIL is....\nPYTHON is awesome!!!!'
with open('ind4_input.txt', 'r') as file:
    ban_word = file.read().strip().split()
result = new_text(text, ban_word)
print(result)
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/14.png)

## Выводы.
В коде реализована функция new_text, которая принимает строку (старый текст) и список забаненных слов. Библиотека re используется для замен в строке. Все забаненные слова заменяются на звездочки и зацензуренный текст выводится в консоль.

## Самостоятельная работа №5
### В текстовом файле находится информация о товарах (Название товара, количество продаж и цена продажи). Нужно написать программу, которая прочитает файл и подсчитает общую выручку при продаже всех товаров и вывести результат в консоль. 

```python
def calculate_revenue():
    total_revenue = 0
    with open('ind5_input.txt', 'r', encoding='utf-8') as file:
        for line in file:
            product, quantity, price = line.strip().split(', ')
            quantity = int(quantity)
            price = float(price)
            revenue = quantity * price
            total_revenue += revenue
    return total_revenue
revenue = calculate_revenue()
print(f'Выручка: {revenue}')
```
### Результат.
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/15.1.png)
![Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_7/pic/15.2.png)

## Выводы.
В этом коде из текстового файла с информацией о продажах извлекается информация о количестве и цене проданных товаров. После этого высчитывается общая выручка за продажи всех товаров, и результат выводится в консоль.

