<h1 align="center">Парсер картинок из Google</h1>

### Установка и настройка ###

1. Клонируйте репозиторий с GitHub

`$ git clone https://github.com/detouche/detouche-ussc-bot.git`

2. Создайте виртуальное окружение.

`python -m venv /path/to/new/virtual/environment`

3. Установите зависимости

`pip install -r requirements.txt`

4. Укажите путь к файлу `.xlsx` 

В этом файле должны храниться имена людей, фото которых вы хотите скачать. 
![image](https://github.com/KekJoy/image_parser/assets/91479557/f5032d68-2e8f-4633-9edd-81f0b5272203)

5. Укажите путь сохранения изображений. Для каждого имени будет создана отдельная папка.

6. Запустите.

`python main.py` или `python3 main.py`
