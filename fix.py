import os
import re

url = 'https://github.com/abadd00d/web-for-juniors/blob/main/' 
url2 = 'https://github.com/abadd00d/web-for-juniors/blob/main/img/' 

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Регулярное выражение для поиска вхождений
    pattern = r'(?<!!)\[\[(.*?)\]\]'  # Исключаем "![[...]]"
    pattern_exclamation = r'!\[\[(.*?)\]\]'  # Для "![[...]]"

    # Функция для обработки найденных вхождений
    def replacer(match):
        inner_text = match.group(1)  # Извлекаем текст внутри [[...]]
        return f'[{inner_text}](<{url}{inner_text}.md>)'

    # Функция для обработки вхождений с "![[...]]"
    def replacer_exclamation(match):
        inner_text = match.group(1)  # Извлекаем текст внутри ![[...]]
        return f'![{inner_text}](<{url2}{inner_text}>)'

    # Заменяем вхождения
    new_content = re.sub(pattern, replacer, content)
    new_content = re.sub(pattern_exclamation, replacer_exclamation, new_content)

    # Записываем изменения обратно в файл
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def process_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                process_file(file_path)
if __name__ == '__main__':
    current_directory = os.getcwd()  # Текущий каталог
    process_directory(current_directory)
    print("Обработка завершена.")

