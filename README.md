# Laboratory work

## **George Golubev** *21PMI-2*

## Список тем

> ### 1. [**System Info**](#1-system-info-1 "Задания 1 - 12")
>- [CPU](#cpu)
>- [RAM](#ram)
>- [DISK USAGE](#disk-usage)
>- [GPU](#gpu)
>- [NETWORK](#network)
>- [PROCESS INFO](#process-info)
> ###  2. [**System&nbsp;Environment**](#2-system-environment)
> ###  3. [**Grep**](#3-grep-1)
> ###  4. [**Find**](#4-find-1)
> ###  5. [**Bash**](#5-bash-1)
> ###  6. [**Administration**](#6-administration-1)

# 1. System Info
## **CPU**

**1.** Какими способами можно узнать информацию о CPU?



***Ответ:***  
  
**a)** 1. Вывести содержимое файла *cpuinfo* в директории *~/proc*: `cat /proc/cpuinfo`  
2. Используя комманду: `lscpu`.  
3. Используя комманду: `inxi -Cxa`

**b)** Команда для вывода: `inxi -Cx` . *Вывод команды:*  
![Пример вывода](/images/cpu/1.b.png)

----

## **RAM**


**2.** Что такое RAM и Swap?

***Ответ:***  
  
**RAM** *(Random Access Memory)* - память с произвольным доступом, то есть запрос к требуемой ячейке памяти происходит напрямую, другие блоки не затрагиваются. Также этот вид памяти называют энергозависимым, а значит, данные сохраняются в ней до тех пор, пока включено устройство, в котором она установлена.

**SWAP** *(от англ. swapping)* - один из механизмов виртуальной памяти, при котором отдельные фрагменты памяти (обычно неактивные) перемещаются из ОЗУ во вторичное хранилище (жёсткий диск или другой внешний накопитель, такой как флеш-память), освобождая ОЗУ для загрузки других активных фрагментов памяти. Такими фрагментами в современных ЭВМ являются страницы памяти.

---

**3.** Написать команду, которая выводит объем RAM/Swap.

***Ответ:*** `free`

---

**4.** Написать bash-script, который меняет размер Swap.  
  
***Ответ:***  
  
[*`./scripts/ram/change_swap_size.sh`*](/scripts/ram/change_swap_size.sh):
```bash
swapfile=$1
new_swap_size=$2

if [ $# -eq 0 ]; then
    echo "No arguments"
    exit
fi

if [ -z "$1" ]; then
    echo "No swapfile name"
    exit
fi

if [ -z "$2" ]; then
    echo "No swapfile size"
    exit
fi


swapoff $swapfile

dd if=/dev/zero of=$swapfile bs=1M count=$new_swap_size status=progress

chmod 600 $swapfile

mkswap $swapfile

swapon $swapfile
```

----

**5.** Для тех, у кого не гостевая Linux-система (т.е. основная). Написать команду, которая выводит информацию о типе используемой RAM (название, производитель, серийный номер, формат, объем, текущую частоту работы).  
  
***Ответ:*** `sudo dmidecode -t memory`  

***Вывод:***  
![dmidecode](/images/ram/4.png)

----

## **DISK USAGE**

**6.** Написать команду, которая выводит размер свободного месте на диске.

***Ответ:***  `df`

----

**7.** Написать команду, которая выводит размер вашей home директории.

***Ответ:***  `sudo du -hs /home`

----


**8.** Написать команду, которая выводит список процессов.  

***Ответ:*** `ps -A`

----

## **GPU**  
  
**9.** Вывести инфу о GPU (как правило команда зависит от типа GPU, необходима установка доп. пакетов. Хотя можно и системными средствами, хоть и не удобно)  
***Ответ:*** `sudo lshw -C display`

----

## **NETWORK**


**10.** Написать команду, которая выводит IP-адресс компьютера  
***Ответ:*** `wget -qO- eth0.me`

----

**11.** Написать команду, которая выводит MAC-адресс компьютера  
***Ответ:*** `ifconfig -a | grep ether | gawk '{print $2}'`

----

**12.** Какие еще есть способы узнать эту информацию? Написать альтернативные варианты  
***Ответ:*** Используя комманды `ifconfig -a`, `ip a`, `ip r l`

----

## **PROCESS INFO**


**13.** Вывести активные процессы в системе минимум двумя способами.  
***Ответ:***  
`ps -ef`:  
![](/images/process_info/ps.png)  

`top`:  
![](/images/process_info/top.png)  

`htop`:  
![](/images/process_info/htop.png )


----

# 2. **System Environment**

**14.** Создать переменную окружения любым способом
```shell
$ export MY_VAR=1
```

----

**15.** Модифицировать PATH, добавив туда свою home директорию
```shell
$ export PATH="$HOME:$PATH"
```
или
```shell
$ echo "export PATH=\"\$HOME:\$PATH\"" >> ~/.bashrc    
```

----

**16.** Обновить имеющиеся системные библиотеки с помощью любого CLI менеджера пакетов
```shell
$ sudo pacman -Syu
```

----

**18.** Создать alias к любой команде, сохранить его в конфигурационном файле
```shell
$ alias c="clear"
$ echo "alias c=\"clear\"" >> ~/.bashrc
```

---- 

**20.** Создать внутри своего home пространства virtual environment. Добавить в bashrc возможность его активировать.  
```shell
$ python3 -m venv ~/venv
$ echo "alias activate=\"source ~/venv/bin/activate\"" >> .bashrc 
```
---


# 3. **Grep**

**21.** Что такое grep?  
***Ответ:*** grep — утилита командной строки, которая находит на вводе строки, отвечающие заданному регулярному выражению, и выводит их, если вывод не отменён специальным ключом.

**a.** 
----

**i.** Написать команду поиска паттерна в файле.  
`grep [OPTION...] PATTERNS [FILE]`  
**ii.** Написать команду поиска паттерна в нескольких файлах сразу.  
`grep [OPTION...] PATTERNS [FILE1] [FILE2]...`  
**iii.** Написать команду поиска нескольких паттернов в одном/нескольких файлах.  
`gpep [OPTION...] PATTERN_FILE [FILE...]`  

----

**22.** Какой ключ делает команду не чувствительной к регистру?  
***Ответ:*** `-i`

----

**23.** Проверить с помощью grep наличие слова в файле. (т.е паттерн является словом целиком. Словоформы не в счет)  
***Ответ:***  
![23](/images/grep/23.png)  

----

**24.** Написать команду вывода всех строк в файле, не содержащих паттерн.  
***Ответ.*** `grep -v PATTERN [FILE...]`

----
**25.** Найти все info файлы в /proc директории с помощью grep  
***Ответ:***
```shell
$ ls /proc | grep -i info
```

**a.**  
[*`./scpripts/grep/25/25.py`*](/scripts/grep/25/25.py)
```python
import os 

proc_files = os.listdir("/proc")

with open("output.txt", "w+") as of:
    for file in proc_files:
        if "info" not in file:
            continue
            
        with open(f"/proc/{file}", "r") as f:
            of.write(f.read())
```

---

**26.** Добавить к команде из пункта 21.а.i номер строки, в которой нашлась подстрока  
***Ответ:***  `grep -n PATTERN [FILE...]`

---
**27.** Поддерживает ли grep regex выражения? `Да, поддерживает`  

***b.*** Описать базовый regex синтаксис. (что означают ‘*’ ‘.’ ‘?’ ‘\’ и тд)  

| **Символ** | **Описание** |
| :---: | :---: |
| **’\.’** | Любой одиночный символ |
| **’\\’** | Экранирование символа. Например (`\.` - будет символ `'.'`) |
| **’\?’** | Предшествующий символ может присутствовать или отсутствовать <br> (`/hell?o/`, будет соответсвовать  **`hello`** или **`helo`**)| 
| **’\*’** | Допускается любое количество предшествующих символов <br> (Включает в себя пустую строку)|
| **’\+’** | Допускается один или несколько предшествующих символов |
| **’\|’** | "или" соответсвует выражению до '|' или после '|' | 
| **’()’** | Группирование выражений |
| **’{}’** | Указывает на количество предшествующих символов|
| **’[]’** | Сопоставляет любой символ в заданном наборе. <br> - определяет диапазоны|
| **’\^’** | Начало строки |
| **’\$’** | Конец строки | 

---
**28.** Написать команду вывода всех файлов с расширением ‘.so’ в директории /lib  

***a.*** Без обхода поддиректорий  
```shell
$ ls /lib | grep -e '.*\.so'
```
или
```shell
$ ls /lib | grep -e '\.so$'
```

***b.*** С обходом поддиректорий
```shell
$ ls -R /lib | grep -e '.*\.so'
```

---

**29.** Скачать [<u>датасет</u>](https://www.kaggle.com/datasets/kaggle/hillary-clinton-emails?resource=download&select=Emails.csv).  
***a.*** Отдельный + тому, кто разберется с kaggle API для загрузки датасетов и сделает это через терминал.  
```shell
$ kaggle datasets download kaggle/hillary-clinton-emails
$ unzip hillary-clinton-emails.zip -d ./datasets 
```

**b.** Найти в Emails.csv все email с помощью grep  
```shell
$ grep -xE '([a-zA-z0-9]|[-_])+@[a-z]+\.[a-z]+' datasets/Emails.csv 
```
или для вывода всех уникальных имейлов
```shell
$ grep -xE '([a-zA-z0-9]|[-_])+@[a-z]+\.[a-z]+' datasets/Emails.csv | sort | uniq
```

---
**30.** Модифицировать команду в п.29 так, чтобы регулярка читалась из файла  
```shell
$ grep -xEf regex Emails.csv | sort | uniq      
```

---
**31.** Вывести процессы, запущенные системой, владельцем которых являетесь вы c помощью grep  

```shell
$ ps -ef | grep -w "$USER"
```
---
# 4. **Find**

**32.** Написать команду поиска с заданным именем файла в заданной директории. Проверить работоспособность.  
```shell
$ find ~ -name "University"  
```
***Вывод:***  
![32.png](/images/find/32.png)

---

**33.** Написать команду поиска файлов по маске
```shell
$ find FOLDER -name MASK 
```
например
```shell
$ find /lib/ -name "*.so"
```

---

**34.** Найти ключик, отвечающий за чувствительность к регистру.
***Ответ:*** `-iname`

---

**35.** Найти все файлы с набором прав доступа 777 (или любой другой комбинацией)  
```shell
$ find / -perm 777
```
---

**36.** Найти все файлы с доступом только на чтение
```shell
$ find / -perm 444
```

---
**37.** Найти все пустые директории
```shell
$ find / -type d -empty
```

---
**38.** Найти все скрытые файлы
```shell
$ find / -type f -name ".*"
```

---
**39.** Найти все файлы, модифицированные за последние 3 часа/дня
```shell
$ find / -type f -mmin 180
$ find / -type f -mtime 3
```

---
**40.** Найти все файлы, которые были открыты за последние 3 часа / дня 
```shell
$ find / -type f -amin 180
$ find / -type f -atime 3
```

---
**41.** Найти все файлы объемом от 10 до 15 Мбайт
```shell
$ find / -type -f -size +10M -size -15M
```

---
**42.** Скопировать файлы из задания 32 (если они нашлись) в свою home директорию в поддиректорию tmp. (Find + cp)
```shell
$ mkdir tmp
$ find ~ -name "University" -exec cp -r "{}" tmp \; 
```

---
**43.** Найти в home директории все скопированные файлы и удалить. (find + rm)
```shell
$ find tmp -type f -exec rm -f "{}" \;
```

# 5. **Bash**

**44.** Создать директорию в своем home пространстве, где вы будете хранить все скрипты.
```shell
$ mkdir ~/scripts
```

----

**45.** Написать «hello world» скрипт, запустить, убедиться, что он работает корректно.Написать «hello world» скрипт, запустить, убедиться, что он работает корректно.  
[*`./scripts/bash/hello_world.py`*](/scripts/bash/hello_word.py):  
```python
#!/usr/bin/python
print("Hello world!")
```

----

**46.** Написать скрипт/функцию, который проверял бы существование файла или директории с заданным именем.  
[`./scripts/bash/dir_file_exist.py`](/scripts/bash/dir_file_exist.py):
```python
#!/usr/bin/python
import sys
import os
import os.path

PATH = sys.argv[1]
PATH_TO_FIND = sys.argv[2]

PATH = os.path.expanduser(PATH) + "/"

PATH_TO_FIND_L = PATH_TO_FIND.split("/")
PATH += "/".join(PATH_TO_FIND_L[:-1])
TO_FIND = PATH_TO_FIND_L[-1]

ldir = os.listdir(PATH)

for el in ldir:
    if TO_FIND in el:
        if os.path.isdir(PATH + "/" + el):
            print("It's directory")

        if os.path.isfile(PATH + "/" + el):
            print("It's file")

        print(os.path.abspath(PATH + "/" + TO_FIND))
        exit(0)
else:
    print("No such file or directory")
```

----

**47.** Написать функцию, которая проверяла бы ваши (*или любого другого пользователя) права доступа к заданному файлу или директории.
[scripts/bash/check_permissions](/scripts/bash/check_permissions.py)
```python
#!/usr/bin/python
import os
import sys

FILE_NAME = sys.argv[1]
if not os.path.exists(FILE_NAME):
    print("No such file or directory")
    exit(-1)

if os.access(FILE_NAME, os.R_OK):
    print("Read", end=" ")
if os.access(FILE_NAME, os.W_OK):
    print("Write", end=" ")
if os.access(FILE_NAME, os.X_OK):
    print("Execute", end=" ")
print()

```
----

**48.** На лабораторных по другим предметам, когда вы используете C/C++ вы часто пишите консольные приложения. Возьмите любую вашу лабу и сделайте из нее утилиту.
  
Я использую компилятор `cmake` поэтому программы просто скопировал из cmake-build-debug  
[scripts/bash/utilits/Calculator](/scripts/bash/utilits/Calculator)  
[scripts/bash/utilits/HuffmanCode](/scripts/bash/utilits/HuffmanCode)

----

**49.** Написать скрипт, который бы:  
Определял ваш регион  
Подключался к сервису погоды, брал погоду для вашего региона  
Показывал ее в stdout / при указании файла в качестве параметра – сохранял бы результат в файл.
```python
#!/usr/bin/python
import geocoder
import json
import requests
import sys

API_KEY = "d42027c53bdcc122e7f74bcc8f84a5ef"
g = geocoder.ip("me")
lat = g.latlng[0]
lon = g.latlng[1]

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_KEY}"

req = requests.get(url=url)
data = req.json()
info = f"City: {data['name']}.\n\
    Weather: \n\
        Main: {data['weather'][0]['main']}\n\
        Description: {data['weather'][0]['description']}\n\
        Temperature: {data['main']['temp']}℃ \n\
        Feels Like: {data['main']['feels_like']}℃\n"

if len(sys.argv) >= 2:
    with open(sys.argv[1], "w") as f:
        f.write(info)
else:
    print(info)

```

----

**50.** Обновлять информацию о погоде в файле, с помощью вашего скрипта, используя системный планировщик задач cron.  
```shell
$ crontab -e 
```
открывается редактор `nano`. Пропписываем следующую строку (скрипт активируется каждые 30 минут и записывает информацию в файл `weather.txt` в `home` дирректории)

```
*/30 * * * * ~/scripts/get_weather.py ~/weather.txt
```

----

**51.** Написать скрипт, реализующий адрессную книгу. В качестве хранилища информации можете использовать все что угодно: от текстового файла до БД. Скрипт должен поддерживать следующие функции  

[scripts/bash/address_book.py](/scripts/bash/address_book.py)

----

# 6. **Administration**

