# Тема 1. Работа с Git
Отчем по теме #1 выполнил(а):
- Клейн Денис Романович
- АИС-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | - |
| Задание 2 | - | - |
| Задание 3 | - | - |
| Задание 4 | - | - |
| Задание 5 | - | - |
| Задание 6 | - | - |
| Задание 7 | - | - |
| Задание 8 | - | - |
| Задание 9 | - | - |
| Задание 10 | - | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1
### Установка Git.

```bash
git --version
```
### Результат.
![1 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/1.1.png)

## Выводы

Данная команда выводит текущую версию Git.

## Лабораторная работа №2
### Настройка.

```bash
git config --global user.name "Denis Klenze"
git config --global user.email "disbalancertram@gmail.com"
git config --list
```
### Результат.
![2 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/2.1.png)

## Выводы.

Эти команды устанавливают имя пользователя и адрес электронной почты.

## Лабораторная работа №3
### Создание нового репозитория.

```bash
cd Desktop/temp
git init
```
### Результат.
![3 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/3.1.png)

## Выводы.

Я перешел в нужную папку, инициализировал репозиторий локально в текущей папке.

## Лабораторная работа №4
### Подготовка файлов.

```bash
git add proba.txt
git status
```
### Результат.
![4 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/4.1.png)

## Выводы.

Был подготовлен файл proba.txt к коммиту

## Лабораторная работа №5
### Фиксация изменений.

```bash
git commit -m "First version of the Project"
git log
```
### Результат.
![5 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/5.1.png)

## Выводы.

Был создан первый коммит, а также просмотрена история изменений в Git.

## Лабораторная работа №6
### Подключение к удаленному репозиторию.

```bash
git remote add github https://github.com/Necsiato/Software_Engineering_Private.git
git branch -M main
git push github main
```
```bash
git pull github main
git pull --rebase github main
```
```bash
git stash
git stash apply
```
### Результат.
![6 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/6.1.png)
![6 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/6.2.png)
![6 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/6.3.png)

## Выводы.

Был создан репозиторий Software_Engineering_Private и запушен файл proba.txt

## Лабораторная работа №7
### Ветвление.

```bash
git branch tema_1
git checkout tema_1
git checkout main
git rebase tema_1
```
### Результат.
![7 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/7.1.png)

## Выводы.

Создана новая ветка tema_1, которая была впоследствии была объединена с веткой main.

## Лабораторная работа №8
### Особенности применения «Фетч»

```bash
git fetch github
git merge github/main
```
### Результат.
![8 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/8.1.png)

## Выводы.

Локальный репозиторий был синхронизирован с удаленным репозиторием.

## Лабораторная работа №9
### Удаление файлов, веток, локальных и удаленных репозиториев.

Удаление файла
```bash
git rm WaypointData.dat
```
Удаление локальной ветки
```bash
git branch -D tema_1
```
Удаление удаленной ветки
```bash
git push github --delete tema_1
```
### Результат.
![9 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/9.1.png)
![9 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/9.2.png)
![9 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/9.3.png)

## Выводы.

Были удалены локальные файлы, локальная ветка и удаленная ветка.

## Лабораторная работа №10
### Отслеживание изменений в коммитах.

```bash
git log
git diff
git diff 5489a667eebf7881a5b26a74fe7be501089a4235 1a6ac0262c7f4950d0e6ce4b1cc102cdf0b2c6a5
```
### Результат.
![10 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/10.1.png)
![10 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/10.2.png)

## Выводы.

Были просмотрены все коммиты в репозитории и просмотрены все изменения между ними.

## Лабораторная работа №11
### Возвращение файла к предыдущему (определенному) состоянию.

```bash
git log
git checkout 09e2a9c98934946b3fe89b55aa2ba6e44834b648 -- proba.txt
```
### Результат.
![11 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/11.1.png)
![11 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/11.2.png)

## Выводы.

Измененный файл proba.txt был восстановлен до предыдущего состояния (к коммиту 09e2a9c98934946b3fe89b55aa2ba6e44834b648)

## Лабораторная работа №12
### Возвращение к предыдущему коммиту.

```bash
git reset --hard HEAD^
```
```bash
git log
git reset --hard c364e7ab260800ae997767d520976288a54a9a9c
```
```bash
git log
git reset --soft HEAD^
```
### Результат.
![12 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/12.1.png)
![12 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/12.2.png)
![12 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/12.3.png)
## Выводы.

Были произведены откаты с потерей изменений и с сохранением до предыдущих коммитов.

## Лабораторная работа №13
### Исправление коммита.

```bash
git log
git commit --amend
```
### Результат.
![13 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/13.1.png)

## Выводы.

Было изменено название предыдущего коммита.

## Лабораторная работа №14
### Разрешение конфликтов при слиянии.

```bash
git merge test
```
### Результат.
![14 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/14.1.png)

## Выводы.
При слиянии конфликтов не возникло.

## Лабораторная работа №15
### Настройка. gitignore

```bash
cat .gitignore
```
### Результат.
![15 Задание](https://github.com/Necsiato/Software_Engineering/blob/Tema_1/pic/15.1.png)

## Выводы.

Был создан файл .gitignore, в который были внесены файлы .png.