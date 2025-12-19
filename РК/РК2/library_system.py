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


class LibrarySystem:
    def __init__(self, libraries, books, books_libraries):
        self.libraries = libraries
        self.books = books
        self.books_libraries = books_libraries

        self.one_to_many = self._create_one_to_many()
        self.many_to_many = self._create_many_to_many()

    def _create_one_to_many(self):
        return [(b.title, b.pages, lib.name)
                for lib in self.libraries
                for b in self.books
                if b.library_id == lib.id]

    def _create_many_to_many(self):
        many_to_many_temp = [(lib.name, bl.library_id, bl.book_id)
                             for lib in self.libraries
                             for bl in self.books_libraries
                             if lib.id == bl.library_id]

        return [(b.title, b.pages, lib_name)
                for lib_name, lib_id, book_id in many_to_many_temp
                for b in self.books if b.id == book_id]

    def get_libraries_starting_with_a(self):
        libs_with_a = list(filter(lambda i: i[2].startswith('А'), self.many_to_many))

        res_1 = {}
        for book_title, pages, lib_name in libs_with_a:
            if lib_name not in res_1:
                res_1[lib_name] = []
            if book_title not in res_1[lib_name]:
                res_1[lib_name].append(book_title)

        return dict(sorted(res_1.items()))

    def get_libraries_with_max_pages(self):
        res_2_unsorted = []

        for lib in self.libraries:
            lib_books = list(filter(lambda i: i[2] == lib.name, self.many_to_many))

            if len(lib_books) > 0:
                lib_pages = [pages for _, pages, _ in lib_books]
                lib_pages_max = max(lib_pages)
                res_2_unsorted.append((lib.name, lib_pages_max))
            else:
                res_2_unsorted.append((lib.name, 0))

        return sorted(res_2_unsorted, key=itemgetter(1), reverse=True)

    def get_all_connections_sorted(self):
        res_3 = sorted(self.many_to_many, key=itemgetter(2))

        grouped_result = {}
        for book_title, pages, lib_name in res_3:
            if lib_name not in grouped_result:
                grouped_result[lib_name] = []
            grouped_result[lib_name].append(f"{book_title} ({pages} стр.)")

        return dict(sorted(grouped_result.items()))