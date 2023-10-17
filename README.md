<h1 align="center">Парсер картинок из Google</h1>

### Установка и настройка ###

1. Клонируйте репозиторий с GitHub

`$ git clone https://github.com/KekJoy/image_parser.git`

2. Создайте виртуальное окружение.

`python -m venv /path/to/new/virtual/environment`

3. Установите зависимости

`pip install -r requirements.txt`

4. Укажите путь к файлу `.xlsx`

В этом файле должны храниться имена людей, фото которых вы хотите скачать. Столбик, в котором находятся имена, должен называться `Keyword`

![image](https://github.com/KekJoy/image_parser/assets/91479557/c8ff60e7-f531-43e1-b404-72fb9daee20c)


5. Укажите путь сохранения изображений. Для каждого имени будет создана отдельная папка, т.е. для каждого имени в списке не нужно создавать отдельную папку.

6. Запустите.

`python main.py` или `python3 main.py`
