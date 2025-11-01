def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        key = args[0]
        for item in items:
            if key in item and item[key] is not None:
                yield item[key]
    else:
        for item in items:
            result = {}
            for key in args:
                if key in item and item[key] is not None:
                    result[key] = item[key]
            if result:
                yield result

if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
        {'title': None, 'price': 3000},
        {'price': 4000}
    ]

    print("Test 1 - один аргумент:")
    for item in field(goods, 'title'):
        print(item)

    print("\nTest 2 - несколько аргументов:")
    for item in field(goods, 'title', 'price'):
        print(item)