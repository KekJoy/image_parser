from icrawler.builtin import GoogleImageCrawler, BingImageCrawler
import pandas as pd
import os


# Укажите путь к XLS файлу, где содержится список ключевых слов
xls_file_path = '/home/superiorkilljoy/Projects/image_parser/names.xlsx'

# Загрузите данные из XLS файла
df = pd.read_excel(xls_file_path)

# Задайте путь для сохранения изображений
base_storage_path = '/home/superiorkilljoy/Projects/image_parser/images1'

# Создадим отдельную папку для каждого имени
for index, row in df.iterrows():
    name = row['Keyword']  # Предполагается, что в XLS файле есть столбец с названием "Keyword"
    quantity = 350  # Количество загружаемых фотографий
    storage_path = os.path.join(base_storage_path, name)  # Путь для сохранения фотографий для текущего имени

    # Создать папку, если она не существует
    if not os.path.exists(storage_path):
        os.makedirs(storage_path)

    filters_google = dict(
        size="large",
        type="face"
    )

    filters_bing = dict(
        type="photo",
    )

    bing_crawler = BingImageCrawler(downloader_threads=8,
                                    storage={'root_dir': storage_path})
    bing_crawler.crawl(keyword=name, filters=filters_bing, offset=0, max_num=quantity, min_size=(720, 720))

    google_crawler = GoogleImageCrawler(storage={'root_dir': storage_path})
    google_crawler.crawl(keyword=name, max_num=quantity, filters=filters_google, min_size=(720, 720))

    # После загрузки фотографий можно сделать что-то с результатами, например, перейти к следующей строке в XLS файле.
