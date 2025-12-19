import unittest
from library_system import Book, Library, BookLibrary, LibrarySystem


class TestLibrarySystem(unittest.TestCase):

    def setUp(self):
        self.libraries = [
            Library(1, 'Центральная библиотека'),
            Library(2, 'Академическая библиотека'),
            Library(3, 'Детская библиотека'),
            Library(11, 'Арт-библиотека'),
        ]

        self.books = [
            Book(1, 'Война и мир', 1225, 1),
            Book(2, 'Преступление и наказание', 671, 2),
            Book(3, 'Мастер и Маргарита', 480, 3),
        ]

        self.books_libraries = [
            BookLibrary(1, 1),
            BookLibrary(2, 2),
            BookLibrary(3, 3),
            BookLibrary(11, 1),
        ]

        self.system = LibrarySystem(self.libraries, self.books, self.books_libraries)

    def test_get_libraries_starting_with_a(self):
        result = self.system.get_libraries_starting_with_a()

        self.assertIsInstance(result, dict)

        self.assertIn('Академическая библиотека', result)
        self.assertIn('Арт-библиотека', result)

        self.assertNotIn('Центральная библиотека', result)
        self.assertNotIn('Детская библиотека', result)

        self.assertEqual(len(result['Академическая библиотека']), 1)
        self.assertEqual(result['Академическая библиотека'][0], 'Преступление и наказание')

    def test_get_libraries_with_max_pages(self):
        result = self.system.get_libraries_with_max_pages()

        self.assertIsInstance(result, list)
        self.assertTrue(all(isinstance(item, tuple) for item in result))

        self.assertEqual(len(result), len(self.libraries))

        for i in range(len(result) - 1):
            self.assertGreaterEqual(result[i][1], result[i + 1][1])

        self.assertEqual(result[0][0], 'Центральная библиотека')
        self.assertEqual(result[0][1], 1225)

    def test_get_all_connections_sorted(self):
        result = self.system.get_all_connections_sorted()

        self.assertIsInstance(result, dict)

        library_names = [lib.name for lib in self.libraries]
        for lib_name in library_names:
            self.assertIn(lib_name, result)

        keys = list(result.keys())
        self.assertEqual(keys, sorted(keys))

        for lib_name, books_list in result.items():
            self.assertIsInstance(books_list, list)
            for book_str in books_list:
                self.assertIn('(', book_str)
                self.assertIn(' стр.)', book_str)

    def test_empty_system(self):
        empty_system = LibrarySystem([], [], [])

        result1 = empty_system.get_libraries_starting_with_a()
        self.assertEqual(result1, {})

        result2 = empty_system.get_libraries_with_max_pages()
        self.assertEqual(result2, [])

        result3 = empty_system.get_all_connections_sorted()
        self.assertEqual(result3, {})


if __name__ == '__main__':
    unittest.main()