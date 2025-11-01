# Вариант Г 13
from operator import itemgetter

class Book:
    def __init__(self, id, title, pages, library_id):
        self.id = id
        self.title = title
        self.pages = pages
        self.library_id = library_id

class Library:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class BookLibrary:
    def __init__(self, library_id, book_id):
        self.library_id = library_id
        self.book_id = book_id

# Библиотеки
libraries = [
    Library(1, 'Центральная библиотека'),
    Library(2, 'Академическая библиотека'),
    Library(3, 'Детская библиотека'),
    Library(11, 'Арт-библиотека'),
    Library(22, 'Абонемент научной литературы'),
    Library(33, 'Английская библиотека'),
]

# Книги
books = [
    Book(1, 'Война и мир', 1225, 1),
    Book(2, 'Преступление и наказание', 671, 2),
    Book(3, 'Мастер и Маргарита', 480, 3),
    Book(4, '1984', 328, 3),
    Book(5, 'Гарри Поттер', 500, 3),
]

# Связи многие-ко-многим
books_libraries = [
    BookLibrary(1, 1),
    BookLibrary(2, 2),
    BookLibrary(3, 3),
    BookLibrary(3, 4),
    BookLibrary(3, 5),
    BookLibrary(11, 1),
    BookLibrary(22, 2),
    BookLibrary(33, 3),
    BookLibrary(33, 4),
    BookLibrary(33, 5),
]


def main():
    # Соединение данных один-ко-многим
    one_to_many = [(b.title, b.pages, lib.name)
                   for lib in libraries
                   for b in books
                   if b.library_id == lib.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(lib.name, bl.library_id, bl.book_id)
                         for lib in libraries
                         for bl in books_libraries
                         if lib.id == bl.library_id]

    many_to_many = [(b.title, b.pages, lib_name)
                    for lib_name, lib_id, book_id in many_to_many_temp
                    for b in books if b.id == book_id]

    print('Задание Г1')
    print('Список всех библиотек, у которых название начинается с буквы "А", и список книг в них:')

    libs_with_a = list(filter(lambda i: i[2].startswith('А'), many_to_many))

    # Группируем по библиотекам
    res_1 = {}
    for book_title, pages, lib_name in libs_with_a:
        if lib_name not in res_1:
            res_1[lib_name] = []

        if book_title not in res_1[lib_name]:
            res_1[lib_name].append(book_title)

    for lib, books_list in sorted(res_1.items()):
        print(f'{lib}: {books_list}')

    print('\nЗадание Г2')
    print('Список библиотек с максимальным количеством страниц книг в каждой библиотеке, отсортированный по максимальному количеству страниц:')

    res_2_unsorted = []

    # Перебираем все библиотеки
    for lib in libraries:

        lib_books = list(filter(lambda i: i[2] == lib.name, many_to_many))


        if len(lib_books) > 0:
            lib_pages = [pages for _, pages, _ in lib_books]
            lib_pages_max = max(lib_pages)
            res_2_unsorted.append((lib.name, lib_pages_max))
        else:
            res_2_unsorted.append((lib.name, 0))

    # Сортировка по максимальному количеству страниц (по убыванию)
    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)

    for lib, max_pages in res_2:
        print(f'{lib}: {max_pages} стр.')

    print('\nЗадание Г3')
    print('Список всех связанных книг и библиотек, отсортированный по библиотекам:')

    # Сортируем по названию библиотеки
    res_3 = sorted(many_to_many, key=itemgetter(2))

    grouped_result = {}
    for book_title, pages, lib_name in res_3:
        if lib_name not in grouped_result:
            grouped_result[lib_name] = []
        grouped_result[lib_name].append(f"{book_title} ({pages} стр.)")

    for lib_name, books_list in sorted(grouped_result.items()):
        print(f'{lib_name}: {books_list}')


if __name__ == '__main__':
    main()