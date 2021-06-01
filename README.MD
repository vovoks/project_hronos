# Инструкция по организации стенда разработки

[![Join the chat at https://gitter.im/project_hronos/community](https://badges.gitter.im/project_hronos/community.svg)](https://gitter.im/project_hronos/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

1. Установить python 3.8.* для своей платформы([python.org](https://www.python.org/downloads/)]).
1. Открыть терминал и выполнить команду:
    ```shell
    python --version
    ```
    2.1. В случае успеха в терминале будет отображено (в случае установки версии Python 3.8.7):
   ```shell
   Python 3.8.7
    ```
1. Скачать и установить среду разработки [PyCharm Community](https://www.jetbrains.com/ru-ru/pycharm/download/).
1. Сделать форк проекта, далее клонировать проект к себе на компьютер.
1. Запустить PyCharm, нажать Open, выбрать каталог с проектом.
1. Выбрать в меню Pycharm -> Preferences.
   1. В строке поиска набрать python interpreter.
   1. Нажать иконку с шестеренкой и выбрать Add.
   1. В открывшемся окне Add Python interpreter проверить, что каталог виртуального окружения (venv) создается внутри проекта.
   1. Нажать кнопку Apply, что приведет к созданию нового виртуального окружения.
   1. Вернуться в окно выбора интерперетатора (первый пункт настоящего списка) и установить вновь созданное окужение по умолчнанию. 
      
1. На нижней панели нажать Terminal, в отобразившеся окне в строке приглашения должно быть написано имя вирутального окружения, которое активируется по умолчанию средой разработки (например, venv).
1. Установить требуемые пакеты введя команду:
   ```shell
   pip install -r requirements.txt
    ```
1. Перейти в каталог проекта и выполнить установку базы данных (SqLite) командами:
   ```shell
   python manage.py makemigrations
   python manage.py migrate
    ```
1. Выполнить загрузку фикстур командами:
   ```shell
   python manage.py loaddata ./fixtures/week_alt.json 
   python manage.py loaddata ./fixtures/times.json 
    ```
1. Выполнить команду создания суперпользователя (для работы с адиминистративной частью):
   ```shell
   python manage.py createsuperuser <пользователь>
    ```
1. Запустить сервер разработки командой:
   ```shell
   python manage.py runserver
    ```
