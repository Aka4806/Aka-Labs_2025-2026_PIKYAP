from library_system import Book, Library, BookLibrary, LibrarySystem

libraries = [
    Library(1, 'Центральная библиотека'),
    Library(2, 'Академическая библиотека'),
    Library(3, 'Детская библиотека'),
    Library(11, 'Арт-библиотека'),
    Library(22, 'Абонемент научной литературы'),
    Library(33, 'Английская библиотека'),
]

books = [
    Book(1, 'Война и мир', 1225, 1),
    Book(2, 'Преступление и наказание', 671, 2),
    Book(3, 'Мастер и Маргарита', 480, 3),
    Book(4, '1984', 328, 3),
    Book(5, 'Гарри Поттер', 500, 3),
]

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
    system = LibrarySystem(libraries, books, books_libraries)

    print('Задание Г1')
    print('Список всех библиотек, у которых название начинается с буквы "А", и список книг в них:')

    result1 = system.get_libraries_starting_with_a()
    for lib, books_list in result1.items():
        print(f'{lib}: {books_list}')

    print('\nЗадание Г2')
    print(
        'Список библиотек с максимальным количеством страниц книг в каждой библиотеке, отсортированный по максимальному количеству страниц:')

    result2 = system.get_libraries_with_max_pages()
    for lib, max_pages in result2:
        print(f'{lib}: {max_pages} стр.')

    print('\nЗадание Г3')
    print('Список всех связанных книг и библиотек, отсортированный по библиотекам:')

    result3 = system.get_all_connections_sorted()
    for lib_name, books_list in result3.items():
        print(f'{lib_name}: {books_list}')


if __name__ == '__main__':
    main()