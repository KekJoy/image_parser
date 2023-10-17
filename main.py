from icrawler.builtin import GoogleImageCrawler
import pandas as pd
import os
import asyncio

# Укажите путь к XLS файлу, где содержится список ключевых слов
xls_file_path = '/home/superiorkilljoy/Projects/image_parser/names.xlsx'

# Загрузите данные из XLS файла
df = pd.read_excel(xls_file_path)

# Задайте путь для сохранения изображений
base_storage_path = '/home/superiorkilljoy/Projects/image_parser/images'

async def crawl_images(name, quantity):
    storage_path = os.path.join(base_storage_path, name)

    # Создать папку, если она не существует
    if not os.path.exists(storage_path):
        os.makedirs(storage_path)

    google_crawler = GoogleImageCrawler(storage={'root_dir': storage_path})
    google_crawler.crawl(keyword=name, max_num=quantity)

async def main():
    tasks = []

    for index, row in df.iterrows():
        name = row['Keyword']
        quantity = 100
        tasks.append(crawl_images(name, quantity))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
