"""
List is a built-in data structure used to store an ordered collection of items. They are dynamic, resizable and capable of storing multiple data types.

List elements can be changed, updated, added, or removed after the list is created.
Elements maintain the order in which they are inserted.
Elements are accessed using their position, starting from index 0.
"""

from copy import deepcopy


def heading(title):
    print('\n' + '=' * 65)
    print(title)
    print('=' * 65)


def main():
    heading('01. List banana aur properties')
    # Ordered: input ka order rahega. Ordered ka matlab sorted nahi.
    # Mutable: existing list ke andar add/update/delete kar sakte hain.
    # Duplicates aur mixed types allowed hain.
    numbers = [30, 10, 20, 10]
    mixed = ['Aman', 21, True, None, 9.5]
    print('numbers:', numbers)
    print('mixed:', mixed)
    print('empty:', [])
    print('range se:', list(range(4)))  # [0, 1, 2, 3]
    print('string se:', list('hi'))     # ['h', 'i']
    # list(...) ko iterable chahiye. list(10) -> TypeError.

    heading('02. Index, negative index aur slicing')
    values = [10, 20, 30, 40, 50]
    # Index:    0   1   2   3   4
    # Negative: -5  -4  -3  -2  -1
    print('first:', values[0])          # 10
    print('last:', values[-1])          # 50
    print('second last:', values[-2])   # 40
    # [start:stop:step]: stop include nahi hota.
    print('[1:4]:', values[1:4])        # [20, 30, 40]
    print('[:3]:', values[:3])          # [10, 20, 30]
    print('[3:]:', values[3:])          # [40, 50]
    print('[::2]:', values[::2])        # [10, 30, 50]
    print('[::-1]:', values[::-1])      # [50, 40, 30, 20, 10]
    print('[100:]:', values[100:])      # []; bounds clip hote hain
    print('[4:1:-1]:', values[4:1:-1])  # [50, 40, 30]
    print('original unchanged:', values)

    heading('03. Update aur slice assignment')
    values = [10, 20, 30, 40]
    values[1] = 200
    print('index replace:', values)  # [10, 200, 30, 40]
    values[1:3] = [7, 8, 9]
    print('slice replace:', values)  # [10, 7, 8, 9, 40]
    values[1:1] = [100, 200]
    print('empty slice mein insert:', values)
    values[1:3] = []
    print('slice delete:', values)   # [10, 7, 8, 9, 40]
    values[::2] = [1, 2, 3]
    print('stepped replace:', values)  # [1, 7, 2, 9, 3]
    # Step 1 ke alawa replacement count exactly match hona chahiye.

    heading('04. append(value): END mein ek item')
    items = [10, 20]
    result = items.append(30)
    print('append:', items)  # [10, 20, 30]
    print('return:', result)  # None
    items.append([40, 50])
    print('list bhi ek item:', items)  # [10, 20, 30, [40, 50]]
    # append(40, 50) invalid: sirf one argument chahiye.
    # items = items.append(60) mat karo: items phir None ho jayega.

    heading('05. extend(iterable): END mein multiple items')
    items = [10, 20]
    result = items.extend([30, 40])
    print('extend list:', items, 'return:', result)
    items.extend((50, 60))  # tuple bhi iterable hai
    print('extend tuple:', items)
    letters = ['a']
    letters.extend('bc')
    print('extend string:', letters)  # ['a', 'b', 'c']
    nested = [1]
    nested.extend([[2, 3], [4, 5]])
    print('recursive flatten nahi:', nested)  # [1, [2, 3], [4, 5]]

    heading('06. insert(index, value): START ya KAHIN BHI')
    items = [10, 20, 30]
    items.insert(0, 5)
    print('start:', items)  # [5, 10, 20, 30]
    items.insert(2, 15)
    print('index 2 se pehle:', items)  # [5, 10, 15, 20, 30]
    items.insert(len(items), 40)
    print('end:', items)  # [5, 10, 15, 20, 30, 40]
    items.insert(-1, 35)
    print('last se pehle:', items)  # [5, 10, 15, 20, 30, 35, 40]
    items.insert(999, 50)    # oversized index -> end
    items.insert(-999, 0)   # very negative -> start
    print('bounds clip:', items)
    items[2:2] = [6, 7]
    print('anywhere multiple insert:', items)
    items[:0] = [-2, -1]
    print('start multiple insert:', items)
    # insert replaces nahi karta: current aur next items right shift hote hain.

    heading('07. remove(value): pehli matching VALUE delete')
    items = [10, 20, 30, 20]
    result = items.remove(20)
    print('remove(20):', items, 'return:', result)  # [10, 30, 20]; None
    # remove(1) value 1 dhoondhta hai, index 1 nahi.
    if 99 in items:
        items.remove(99)
    print('missing ko guard:', items)
    items = [10, 20, 30, 20]
    filtered = [value for value in items if value != 20]
    print('saare 20 remove, new list:', filtered)  # [10, 30]

    heading('08. pop(index=-1): POSITION se delete + value return')
    items = [10, 20, 30, 40, 50]
    removed = items.pop()
    print('end:', removed, 'remaining:', items)  # 50; [10, 20, 30, 40]
    removed = items.pop(0)
    print('start:', removed, 'remaining:', items)  # 10; [20, 30, 40]
    removed = items.pop(1)
    print('any index:', removed, 'remaining:', items)  # 30; [20, 40]
    removed = items.pop(-1)
    print('negative index:', removed, 'remaining:', items)  # 40; [20]
    # pop(20) value 20 nahi, index 20 par kaam karega.

    heading('09. del: index, range ya variable binding delete')
    # del keyword hai, list method nahi. Koi return value nahi milti.
    items = [10, 20, 30, 40, 50, 60]
    del items[0]
    print('start delete:', items)  # [20, 30, 40, 50, 60]
    del items[-1]
    print('end delete:', items)  # [20, 30, 40, 50]
    del items[1]
    print('any index delete:', items)  # [20, 40, 50]
    del items[1:3]
    print('range delete:', items)  # [20]
    items = list(range(8))
    del items[::2]
    print('alternate delete:', items)  # [1, 3, 5, 7]

    heading('10. clear(): poori list empty, same object')
    items = [10, 20, 30]
    alias = items
    result = items.clear()
    print('items:', items, 'alias:', alias, 'return:', result)  # [] [] None
    print('same object?', items is alias)  # True
    items = [10, 20]
    alias = items
    items = []  # Nayi list bind ki, purani ko clear nahi kiya.
    print('rebind: items:', items, 'alias:', alias)  # [] [10, 20]
    del items  # Sirf naam hata. Alias ki wajah se old list reachable hai.
    print('del naam ke baad alias:', alias)  # [10, 20]

    heading('11. index(value, start, stop): pehli matching position')
    items = [10, 20, 30, 20, 40]
    print('index(20):', items.index(20))             # 1
    print('index(20, 2):', items.index(20, 2))       # 3
    print('index(20, 2, 4):', items.index(20, 2, 4)) # 3
    # Stop excluded. Result original list ka index, subrange ka nahi.
    # Missing value ya search range mein no match -> ValueError.

    heading('12. count(value): kitni baar aaya?')
    items = [10, 20, 20, 30, 20]
    print('count(20):', items.count(20))  # 3
    print('count(99):', items.count(99))  # 0
    print('equality matching:', [1, True, 1.0].count(1))  # 3
    # Matching == se hoti hai, identity is se nahi.

    heading('13. sort(*, key=None, reverse=False)')
    items = [30, 10, 20, 10]
    result = items.sort()
    print('ascending:', items, 'return:', result)  # [10, 10, 20, 30]; None
    items.sort(reverse=True)
    print('descending:', items)  # [30, 20, 10, 10]
    words = ['banana', 'kiwi', 'apple']
    words.sort(key=len)
    print('length se:', words)  # ['kiwi', 'apple', 'banana']
    names = ['bob', 'Alice', 'carol']
    names.sort(key=str.lower)
    print('case-insensitive:', names)  # ['Alice', 'bob', 'carol']
    students = [('Aman', 80), ('Neha', 95), ('Ravi', 80)]
    students.sort(key=lambda student: student[1])
    print('marks se stable sort:', students)
    # Equal marks par Aman, Ravi ka original relative order bacha.
    original = [3, 1, 2]
    ordered = sorted(original)
    print('sorted() new list:', ordered, 'original:', original)
    # key=len pass karo, key=len() nahi. key/reverse keyword-only hain.

    heading('14. reverse(): current order ulta, sorting nahi')
    items = [30, 10, 20]
    result = items.reverse()
    print('reverse:', items, 'return:', result)  # [20, 10, 30]; None
    print('slice se reversed copy:', items[::-1])
    print('reversed iterator ko list:', list(reversed(items)))

    heading('15. copy(): alias, shallow copy aur deepcopy')
    original = [10, 20]
    alias = original
    copied = original.copy()
    alias.append(30)
    copied.append(99)
    print('original:', original)  # [10, 20, 30]
    print('alias:', alias)        # [10, 20, 30]
    print('copy:', copied)        # [10, 20, 99]
    print('alias is original:', alias is original)  # True
    print('copy is original:', copied is original)  # False
    original = [[1, 2], [3, 4]]
    shallow = original.copy()
    deep = deepcopy(original)
    shallow[0].append(99)
    print('nested original:', original)  # [[1, 2, 99], [3, 4]]
    print('nested shallow:', shallow)    # [[1, 2, 99], [3, 4]]
    print('nested deep:', deep)          # [[1, 2], [3, 4]]
    print('shared inner?', shallow[0] is original[0])  # True
    shallow[0] = [7, 8]  # Outer slot replace; shared inner ko mutate nahi kiya.
    print('slot replace ke baad original:', original)
    print('slot replace ke baad shallow:', shallow)
    # original[:] aur list(original) bhi shallow copies hain.

    heading('16. Built-ins, operators aur comprehension')
    items = [10, 20, 30]
    print('len/min/max/sum:', len(items), min(items), max(items), sum(items))
    print('membership:', 20 in items, 99 not in items)  # True True
    print('concatenate:', items + [40, 50])  # New list
    print('repeat:', [1, 2] * 3)  # [1, 2, 1, 2, 1, 2]
    alias = items
    items += [40]  # Existing list extend
    print('+= alias:', alias)  # [10, 20, 30, 40]
    items = items + [50]  # Naya object bind
    print('+ items:', items, 'old alias:', alias)
    for position, value in enumerate(['pen', 'book']):
        print('position:', position, 'value:', value)
    squares = [number * number for number in range(1, 6)]
    evens = [number for number in range(1, 7) if number % 2 == 0]
    print('squares:', squares)  # [1, 4, 9, 16, 25]
    print('evens:', evens)      # [2, 4, 6]
    rows = [[1, 2], [3, 4]]
    print('one-level flatten:', [value for row in rows for value in row])
    # len, sorted, reversed, del etc. list methods nahi hain.

    heading('17. Nested list: repetition ka shared-reference trap')
    wrong_grid = [[0] * 3] * 2
    wrong_grid[0][0] = 9
    print('shared rows:', wrong_grid)  # [[9, 0, 0], [9, 0, 0]]
    print('same row?', wrong_grid[0] is wrong_grid[1])  # True
    grid = [[0] * 3 for _ in range(2)]
    grid[0][0] = 9
    print('independent rows:', grid)  # [[9, 0, 0], [0, 0, 0]]
    print('row 1 column 2:', grid[1][2])  # 0

    heading('18. Loop ke beech remove: item skip kyun?')
    values = [2, 4, 6, 7]
    for value in values:
        if value % 2 == 0:
            values.remove(value)
    print('problem demo:', values)  # [4, 7], 4 shift hokar skip hua
    values = [2, 4, 6, 7]
    values = [value for value in values if value % 2 != 0]
    print('filtered:', values)  # [7]
    values = [2, 4, 6, 7]
    alias = values
    values[:] = [value for value in values if value % 2 != 0]
    print('same object filter, alias:', alias)  # [7]

    heading('19. Common errors: jaan-bujhkar trigger karke dekho')
    try:
        print([10, 20][5])
    except IndexError:
        print('IndexError: direct access mein index bahar hai.')
    try:
        [].pop()
    except IndexError:
        print('IndexError: empty list se pop nahi kar sakte.')
    try:
        [10, 20].remove(99)
    except ValueError:
        print('ValueError: remove ko matching value nahi mili.')
    try:
        [10, 20].index(99)
    except ValueError:
        print('ValueError: index ko matching value nahi mili.')
    try:
        [10, 20].extend(30)
    except TypeError:
        print('TypeError: extend ko iterable chahiye, integer nahi.')
    try:
        [10, '20'].sort()
    except TypeError:
        print('TypeError: int aur str ki default ordering nahi hai.')
    try:
        values = [1, 2, 3, 4]
        values[::2] = [9]
    except ValueError:
        print('ValueError: stepped slice ki 2 positions ko 2 values chahiye.')
    try:
        print([10, 20][::0])
    except ValueError:
        print('ValueError: slice step zero nahi ho sakta.')

    heading('20. Mini practice: shopping list')
    cart = ['milk', 'bread']
    cart.insert(0, 'eggs')             # Start
    cart.append('rice')                # End
    cart.insert(2, 'butter')           # Beech mein
    cart.extend(['tea', 'sugar'])      # Multiple at end
    print('cart:', cart)
    print('start removed:', cart.pop(0))
    print('end removed:', cart.pop())
    cart.remove('bread')               # Known value
    del cart[1]                        # Current index 1: butter
    print('remaining:', cart)  # ['milk', 'rice', 'tea']
    cart.sort()
    print('sorted:', cart)
    cart.clear()
    print('empty:', cart)


if __name__ == '__main__':
    main()
