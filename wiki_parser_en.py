# importing the module
import wikipediaapi

wiki = wikipediaapi.Wikipedia(user_agent='ZooPy (nikitabakutov2008@gmail.com)', language='ru')

# Получаем страницу животного (например, "Кошка")
page = wiki.page("Кошка")

for section in page.sections:
    # Если название раздела содержит слово "Таксономия"
    if "Таксономия" in section.title:
        print("Название раздела:", section.title)
        print("Текст раздела:\n", section.text)