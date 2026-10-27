# Python List — samajhne wali notebook

Sirf syntax yaad karne se list clear nahi hoti. Har operation par teen cheezein dekho: **kaam kis position/value par hua, original list badli ya nayi bani, aur return kya mila?**

Saare runnable examples [Basics.py](Basics.py) mein hain. Project root se run karo:

```bash
python List/Basics.py
```

## 1. List kya hai?

Ek variable mein multiple values ko order ke saath rakhna ho, to list kaam aati hai.

```python
marks = [80, 65, 90, 65]
student = ['Aman', 21, True]
empty = []
```

- **Ordered:** values apni position rakhti hain. `[30, 10, 20]` ordered hai, lekin sorted nahi.
- **Mutable:** existing list ke andar add, update aur delete kar sakte hain.
- **Indexed:** pehli position `0` hoti hai.
- **Duplicates allowed:** same value multiple baar aa sakti hai.
- **Mixed types allowed:** integer, string, doosri list, object sab aa sakte hain. Lekin har operation har combination par valid nahi hota; `int` aur `str` ko default `sort()` se order nahi kar sakte.

```python
list(range(4))  # [0, 1, 2, 3]
list('abc')     # ['a', 'b', 'c']
list((10, 20))  # [10, 20]
```

`list(...)` ko iterable chahiye: aisi cheez jiske items ek-ek karke mil saken. String, tuple, range aur list iterable hain. `list(10)` par `TypeError` aayega.

## 2. Index aur negative index

```text
values = [10, 20, 30, 40, 50]
index      0   1   2   3   4
negative  -5  -4  -3  -2  -1
```

```python
values[0]   # 10: first
values[2]   # 30: third
values[-1]  # 50: last
values[-2]  # 40: second last
```

`len(values)` yahan `5` hai. Last positive index `len(values) - 1`, yani `4` hai. `values[5]` invalid hai.

Valid negative index ko `len(values) + index` se samajh sakte ho: `5 + (-2) = 3`. Bahut negative index, jaise `values[-6]`, bhi `IndexError` dega. Empty list mein `values[-1]` bhi invalid hai.

## 3. Slicing: list ka ek hissa

Syntax: `values[start:stop:step]`. **Start include, stop exclude** hota hai.

```python
values = [10, 20, 30, 40, 50]
values[1:4]     # [20, 30, 40]
values[:3]      # [10, 20, 30]
values[3:]      # [40, 50]
values[::2]     # [10, 30, 50]
values[::-1]    # [50, 40, 30, 20, 10]
values[:]       # shallow copy
values[100:]    # []
values[3:1]     # []: positive step se peeche nahi chal sakte
values[4:1:-1]  # [50, 40, 30]
```

Positive step mein omitted start beginning aur omitted stop end hota hai. Negative step mein defaults reverse direction ke hisaab se hote hain; isi liye `[::-1]` poori list reverse karta hai. `step=0` invalid hai.

Direct indexing mein missing position error hai, lekin slice ke out-of-range bounds clip ho jaate hain. Slice ek **nayi outer list** banata hai. Nested objects phir bhi shared ho sakte hain; copy section mein iska example hai.

## 4. Start, end aur kahin bhi add karna

Maan lo `items = [10, 20, 30]`. Har row ko fresh list par socho.

| Kahan add karna hai? | Code | Result |
|---|---|---|
| Start par ek item | `items.insert(0, 5)` | `[5, 10, 20, 30]` |
| End par ek item | `items.append(40)` | `[10, 20, 30, 40]` |
| Index 1 par ek item | `items.insert(1, 15)` | `[10, 15, 20, 30]` |
| End par multiple items | `items.extend([40, 50])` | `[10, 20, 30, 40, 50]` |
| Start par multiple items | `items[0:0] = [1, 5]` | `[1, 5, 10, 20, 30]` |
| Index 1 par multiple items | `items[1:1] = [11, 12]` | `[10, 11, 12, 20, 30]` |

Insert ka matlab existing item replace karna nahi. Us position ke current item aur uske baad wale items right shift hote hain.

### `append(value)` — ek item end mein

```python
items = [10, 20]
answer = items.append(30)
print(items)   # [10, 20, 30]
print(answer)  # None

items.append([40, 50])
print(items)   # [10, 20, 30, [40, 50]]
```

`[40, 50]` khud ek object hai. `append` ne usko ek item ki tarah rakha. Length ab `4` hai, `5` nahi. `append(40, 50)` invalid hai: exactly ek value chahiye.

### `extend(iterable)` — iterable ke items end mein

```python
items = [10, 20]
items.extend([30, 40])  # [10, 20, 30, 40]
items.extend((50, 60)) # tuple bhi chalega

letters = ['a']
letters.extend('bc')   # ['a', 'b', 'c']

items = [1]
items.extend([[2, 3]]) # [1, [2, 3]]
```

`extend` iterable se items leta hai. Ye nested lists ko recursively flatten nahi karta. `extend(30)` invalid hai, kyunki integer iterable nahi hai. Return `None` hai.

Yaad rakhne ka tareeka: `append` mein poori di hui cheez ek item; `extend` mein us cheez ke items alag-alag add hote hain.

### `insert(index, value)` — given position se pehle

```python
items = [10, 20, 30]
items.insert(1, 15)  # [10, 15, 20, 30]
```

Purana index `1` wala `20` ab index `2` par hai. Neeche har line fresh `[10, 20, 30]` par socho:

```python
items.insert(0, 5)           # [5, 10, 20, 30]
items.insert(len(items), 40) # [10, 20, 30, 40]
items.insert(-1, 25)         # [10, 20, 25, 30]
items.insert(999, 40)        # [10, 20, 30, 40]
items.insert(-999, 5)        # [5, 10, 20, 30]
```

`insert(-1, value)` last item **se pehle** insert karta hai. End par add karne ke liye `append` zyada clear hai. Insert ke bounds clip hote hain; oversized position par error nahi aata. Return `None` hai.

## 5. Value update aur slice assignment

```python
items = [10, 20, 30, 40]
items[1] = 200         # [10, 200, 30, 40]
items[1:3] = [7, 8, 9] # [10, 7, 8, 9, 40]
items[1:1] = [100]     # [10, 100, 7, 8, 9, 40]
items[1:2] = []        # [10, 7, 8, 9, 40]
```

Single index assignment position replace karta hai; missing position create nahi karta. `items[len(items)] = 50` par `IndexError` aayega. End par naya item add karna ho to `append(50)`.

Normal slice assignment list ki length badha ya ghata sakta hai. Lekin stepped slice mein jitni selected positions hain utni replacement values chahiye:

```python
items = [10, 20, 30, 40]
items[::2] = [1, 3]  # [1, 20, 3, 40]
# items[::2] = [9]   # ValueError: 2 positions, sirf 1 replacement
```

## 6. Start, end aur kahin se bhi delete karna

Har row ke liye fresh `items = [10, 20, 30, 40]` maan lo.

| Kya karna hai? | Code | List baad mein | Return |
|---|---|---|---|
| Start delete | `items.pop(0)` | `[20, 30, 40]` | `10` |
| End delete | `items.pop()` | `[10, 20, 30]` | `40` |
| Index 1 delete | `items.pop(1)` | `[10, 30, 40]` | `20` |
| Start, value nahi chahiye | `del items[0]` | `[20, 30, 40]` | Statement, no result |
| End, value nahi chahiye | `del items[-1]` | `[10, 20, 30]` | Statement, no result |
| Any index, value nahi chahiye | `del items[2]` | `[10, 20, 40]` | Statement, no result |
| Value `20` delete | `items.remove(20)` | `[10, 30, 40]` | `None` |
| Index 1 se 3 ke pehle tak | `del items[1:3]` | `[10, 40]` | Statement, no result |
| Sab items delete | `items.clear()` | `[]` | `None` |

### `remove(value)` — pehli matching value

```python
items = [10, 20, 30, 20]
items.remove(20)
print(items)  # [10, 30, 20]
```

Beginning se matching value dhoondhi jaati hai. Pehla match delete hota hai, baaki duplicates bachte hain. Matching equality `==` ke basis par hoti hai.

`remove(1)` ka matlab value `1` delete karna hai, index `1` nahi. Missing value par `ValueError` aata hai.

```python
if 99 in items:
    items.remove(99)

# Saare 20 hataane ke liye new filtered list:
items = [10, 20, 30, 20]
items = [value for value in items if value != 20]  # [10, 30]
```

`if ... in` phir `remove` readable hai, lekin present value ke liye do searches ho sakti hain. Duplicate search avoid karna ho to `try/except ValueError` bhi use kar sakte ho.

### `pop(index=-1)` — position se nikalo aur value lo

```python
items = [10, 20, 30, 40]
last = items.pop()    # last = 40; items = [10, 20, 30]
first = items.pop(0)  # first = 10; items = [20, 30]
other = items.pop(1)  # other = 30; items = [20]
```

`pop` ka argument index hai. Empty list ya invalid index par `IndexError` aata hai. `insert` ki tarah index clip nahi hota.

### `del` — method nahi, Python statement

```python
items = [10, 20, 30, 40, 50]
del items[1:4]  # [10, 50]
del items[:]   # []
```

`del items[::2]` alternate positions delete karega. Stepped deletion mein replacement count match nahi karna; replacement diya hi nahi ja raha.

`del items` naam ki binding hataata hai. Ye `clear()` se alag hai:

```python
items = [10, 20]
other = items
del items
print(other)  # [10, 20]
# print(items) -> NameError: naam ab defined nahi hai
```

### `clear()` vs `items = []`

```python
items = [10, 20]
other = items
items.clear()
print(other)  # []: same object clear hua

items = [10, 20]
other = items
items = []
print(other)  # [10, 20]: items ab nayi list ko refer karta hai
```

`clear()` same list se saare held item references hataata hai. `items = []` is variable ko nayi empty list se jodta hai. Removed item kahin aur referenced hai to woh alive reh sakta hai. Memory turant operating system ko wapas milne ki guarantee bhi nahi hai.

## 7. Search aur counting

### `index(value, start=0, stop=...)`

Pehle matching item ki position deta hai. Optional `start` inclusive aur `stop` exclusive hain; inhe positional arguments do.

```python
items = [10, 20, 30, 20, 40]
items.index(20)        # 1
items.index(20, 2)     # 3
items.index(20, 2, 4)  # 3: original list ka index
# items.index(99)      # ValueError
# items.index(20, 0, 1) # ValueError: selected range mein 20 nahi
```

`index` value search karta hai. `items[2]` direct position read karta hai. Dono alag kaam hain.

### `count(value)`

```python
items = [10, 20, 20, 30, 20]
items.count(20)  # 3
items.count(99)  # 0
[1, True, 1.0].count(1)  # 3
```

Last example mein `1 == True` aur `1 == 1.0` true hain. Count equality check karta hai, exact type count nahi karta.

Sirf presence chahiye to `20 in items` use karo. `count(20) > 0` poori list scan karta hai; `in` pehla match milte hi ruk sakta hai.

## 8. Sort aur reverse

### `sort(*, key=None, reverse=False)`

```python
items = [30, 10, 20]
result = items.sort()
print(items)   # [10, 20, 30]
print(result)  # None
items.sort(reverse=True)  # [30, 20, 10]
```

`sort()` original list badalta hai. `key` aur `reverse` keyword-only arguments hain. Signature ka `*` isi baat ko dikhata hai.

```python
words = ['banana', 'kiwi', 'apple']
words.sort(key=len)  # ['kiwi', 'apple', 'banana']

names = ['bob', 'Alice', 'carol']
names.sort(key=str.lower)  # ['Alice', 'bob', 'carol']

students = [('Aman', 80), ('Neha', 95), ('Ravi', 80)]
students.sort(key=lambda student: student[1])
# [('Aman', 80), ('Ravi', 80), ('Neha', 95)]
```

`key` function har item se comparison ki value nikaalti hai. Tuple example mein `student[1]` marks hai. `key=len` function pass karta hai; `key=len()` likhne par function bina argument abhi call ho jayega aur error dega.

Sort **stable** hai: same key wale items apna pehle wala relative order rakhte hain. Aman aur Ravi dono ke 80 marks hain, isliye Aman pehle hi rahega. Ye guarantee `reverse=True` ke saath bhi hai.

String ka default order character codes ke hisaab se hai; normal language ke dictionary order ki guarantee nahi. Mixed incomparable types, jaise `[10, '20']`, default sort par `TypeError` denge.

Sort fail ho to original order preserved hone par bharosa mat karo; list partially rearrange ho sakti hai. Sort/key ke dauraan usi list ko mutate mat karo.

```python
original = [3, 1, 2]
new_list = sorted(original)
print(original)  # [3, 1, 2]
print(new_list)  # [1, 2, 3]
```

`sorted(...)` built-in function hai, list method nahi. Ye kisi iterable se nayi sorted list deta hai.

### `reverse()`

```python
items = [30, 10, 20]
items.reverse()
print(items)  # [20, 10, 30]
```

Reverse current order palat ta hai; values ko descending sort nahi karta. Return `None` hai.

| Requirement | Use |
|---|---|
| Original list ka order reverse | `items.reverse()` |
| Nayi reversed list | `items[::-1]` |
| Reverse direction mein iterate | `reversed(items)` |
| Largest-to-smallest sort | `items.sort(reverse=True)` |

`reversed(items)` iterator deta hai, list nahi. List chahiye to `list(reversed(items))`. Iterator snapshot nahi hai; iterate karte waqt original ko mutate karne se unexpected results mil sakte hain.

## 9. `copy()`, alias aur nested lists

### Assignment copy nahi banata

```python
a = [10, 20]
b = a
b.append(30)
print(a)       # [10, 20, 30]
print(a is b)  # True
```

`a` aur `b` same list ke do naam hain. Isko alias kehte hain.

### Shallow copy

```python
a = [10, 20]
b = a.copy()
b.append(30)
print(a)       # [10, 20]
print(b)       # [10, 20, 30]
print(a is b)  # False
```

`a.copy()`, `a[:]` aur `list(a)` nayi outer list banate hain. Andar ke objects ke references copy hote hain.

```python
a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(99)
print(a)  # [[1, 2, 99], [3, 4]]
print(b)  # [[1, 2, 99], [3, 4]]
```

Outer lists alag hain, lekin `a[0]` aur `b[0]` same inner list hain. Inner list mutate karne par dono se change dikha.

```python
b[0] = [7, 8]
print(a)  # [[1, 2, 99], [3, 4]]
print(b)  # [[7, 8], [3, 4]]
```

Ab `b` ke ek slot ka reference replace hua; shared inner list ko mutate nahi kiya.

Ordinary nested mutable data ko independently copy karna ho:

```python
from copy import deepcopy

a = [[1, 2], [3, 4]]
b = deepcopy(a)
b[0].append(99)
print(a)  # [[1, 2], [3, 4]]
print(b)  # [[1, 2, 99], [3, 4]]
```

Custom objects apni copying customize kar sakte hain. Har cheez ko blindly deep copy karna zaroori nahi.

`==` values compare karta hai; `is` same object hona check karta hai. Do separately created lists `[1, 2]` values mein equal ho sakti hain, same object nahi.

## 10. Behind the scenes: list andar kaise kaam karti hai?

Memory layout aur resizing wali baat yahan **CPython**, yani commonly used Python implementation, ke liye hai. Python language list ka behavior define karti hai; exact allocation strategy implementation/version par depend karti hai.

### List objects nahi, unke references rakhti hai

```text
items --> list object
           slot 0 --> integer object 10
           slot 1 --> string object 'hi'
           slot 2 --> another list [1, 2]
```

CPython list ek dynamic array of object references use karti hai. Reference slots contiguous hote hain; actual item objects memory mein alag jagah ho sakte hain. Isi wajah se mixed types aur shared nested objects possible hain. Ye linked list nahi hai.

```python
box = []
items = [box]
box.append(10)
print(items)  # [[10]]
```

List mein `box` ka frozen snapshot nahi tha. Same object ka reference tha.

### Direct index fast kyun?

`items[3]` ke liye har previous item ko search nahi karna padta. Slots fixed-size references hain, isliye index se slot locate hota hai. Valid index read/write normally `O(1)` hai.

Lekin `items.index(30)` ke paas position nahi hai. Wo values compare karke search karega, isliye worst case `O(n)`.

### Length aur capacity alag hain

Length actual item count hai. Capacity reference slots ke liye allocated space hai. CPython growth ke waqt aksar zarurat se thodi extra capacity rakhta hai.

```text
Conceptual example, exact allocation promise nahi:

length = 3
slots  = [ref10, ref20, ref30, spare, spare]
```

Spare slots visible list items nahi hain. Length `3` hi hai; index `3` invalid hai.

Append par jagah ho to next slot use hota hai. Jagah kam ho to buffer resize ho sakta hai; kabhi references nayi memory mein move/copy karne padte hain. Objects ka deep copy nahi hota.

Isliye har individual append constant time hone ki guarantee nahi. Bahut saare appends ka average per-operation cost **amortized O(1)** hai; resize wala append `O(n)` ho sakta hai. Exact capacity ko fixed formula samajhkar code mat likho.

### Start ya middle mein insert slow kyun?

```text
Before:       [10, 20, 30, 40]
insert(1, 99):    20, 30, 40 ko right shift karo
After:        [10, 99, 20, 30, 40]
```

Nayi value ke liye jagah banani padti hai. Start par insert karne mein sab existing references shift honge.

### Delete mein kya hota hai?

```text
Before:       [10, 20, 30, 40]
pop(1):           remove 20
After:        [10, 30, 40]
                  30, 40 left shift hue
```

Beech ka gap close karne ke liye baad wale references left shift hote hain. `pop()` end se remove karta hai, isliye baaki items shift nahi hote. Shrinking par allocation change bhi ho sakti hai.

`remove(value)` mein pehle search, phir deletion aur shifting hoti hai. Kisi item ka list reference hatne ka matlab us object ka har jagah se delete hona nahi.

### Sort ke andar kya hota hai?

CPython ka list sort adaptive stable algorithm, Timsort family, use karta hai. Existing ordered runs ka faayda leta hai. General worst-case time `O(n log n)` aur already ordered input par best-case `O(n)` ho sakta hai.

Sort same list object ke reference order ko rearrange karta hai. **In-place** ka matlab result same list mein aata hai; zero extra memory nahi. Sorting temporary memory use kar sakti hai, worst case `O(n)` scale par. `key` di ho to successful sort mein har input item ki key once evaluate karke comparison keys use hoti hain.

## 11. Time complexity: kis operation mein kitna kaam?

`n` = current list length, `k` = add/copy/affect hone wale items. Ye usual CPython model hai, ordinary constant-time equality/comparison maan kar. Custom comparison, iterator aur object cleanup ka apna cost ho sakta hai.

| Operation | Usual time | Reason |
|---|---|---|
| `len(items)` | `O(1)` | Length stored hai |
| `items[i]`, `items[i] = x` | `O(1)` | Direct slot access |
| `append(x)` | Amortized `O(1)` | End slot; occasional resize `O(n)` |
| `extend(iterable)` | Amortized `O(k)` for k new items | New items add; individual resize costly ho sakta hai |
| `insert(0, x)` | `O(n)` | Sab references shift |
| `insert(i, x)` | Worst `O(n)` | Shifting, possible resize |
| `pop()` | Amortized `O(1)` | End removal; occasional shrink |
| `pop(0)`, `del items[0]` | `O(n)` | Baaki references left shift |
| `remove(x)` | `O(n)` | Search + shifting |
| `x in items`, `index(x)` | Worst `O(n)` | Pehla match dhoondhna |
| `count(x)` | `O(n)` | Saare items check |
| `copy()`, full slice | `O(n)` | References copy |
| Slice read with k items | `O(k)` | Selected references copy |
| General slice assignment/deletion | Worst `O(n + k)` | Replacement/deletion plus shifting |
| `clear()` | `O(n)` | Held item references release |
| `reverse()` | `O(n)` | References ka order reverse |
| `sort()` | Worst `O(n log n)` | Comparisons/reordering |
| `a + b` | `O(len(a) + len(b))` | New list mein references |

`O(n)` milliseconds nahi hai. Matlab input size badhne par kaam roughly us proportion mein badhta hai. Beginning se baar-baar remove karoge to total cost `O(n²)` tak ja sakti hai. Queue jaisa frequent front add/remove ka kaam ho to `collections.deque` ke `appendleft()` / `popleft()` better choice hote hain.

## 12. Methods ke alawa useful operations

```python
items = [10, 20, 30]
len(items)       # 3
min(items)       # 10
max(items)       # 30
sum(items)       # 60
20 in items      # True
99 not in items  # True
items + [40]     # [10, 20, 30, 40], new list
[1, 2] * 2       # [1, 2, 1, 2], references repeat
```

`min([])` aur `max([])` bina default ke `ValueError` dete hain. `sum([])` ka result `0` hai. Numeric aggregation ke liye compatible values honi chahiye.

```python
items = [10]
other = items
items += [20]        # Existing list extend hoti hai
print(other)         # [10, 20]
items = items + [30] # New list banti hai, items usko refer karta hai
print(other)         # [10, 20]
print(items)         # [10, 20, 30]
```

Lists `+` se lists ke saath concatenate hoti hain. `items + (30,)` invalid hai, lekin `items.extend((30,))` valid hai.

### Loop aur comprehension

```python
for value in [10, 20, 30]:
    print(value)

for index, value in enumerate(['pen', 'book']):
    print(index, value)

squares = [number * number for number in range(1, 6)]
# [1, 4, 9, 16, 25]

evens = [number for number in range(1, 7) if number % 2 == 0]
# [2, 4, 6]
```

Comprehension ko aise padho: har number lo; condition pass ho to expression ki value nayi list mein rakho.

```python
rows = [[1, 2], [3, 4]]
flat = [value for row in rows for value in row]  # [1, 2, 3, 4]
```

Iska equivalent outer loop rows par aur inner loop har row ke values par hai. Ye one-level flatten hai, arbitrary depth ka recursive flatten nahi.

## 13. Common mistakes

### Mutating method ka result original variable mein rakh diya

```python
items = [10, 20]
items = items.append(30)
print(items)  # None
```

Append ne purani list modify ki, phir `None` return kiya. Assignment ne `items` naam ko `None` se bind kar diya. Sahi: bas `items.append(30)`.

Ye baat `extend`, `insert`, `remove`, `clear`, `sort`, `reverse` par bhi apply hoti hai. Lekin `pop()` removed value deta hai aur `copy()` nayi list. Har method ko blindly `None` return karne wala mat samjho.

### Loop ke andar same list se remove

```python
values = [2, 4, 6, 7]
for value in values:
    if value % 2 == 0:
        values.remove(value)
print(values)  # [4, 7], expected [7] nahi mila
```

Pehle `2` remove hua, to `4` index `0` par shift ho gaya. Iterator next index `1` par chala, jahan ab `6` hai. `4` skip ho gaya.

```python
values = [2, 4, 6, 7]
values = [value for value in values if value % 2 != 0]  # [7]

# Same list object preserve karna ho, taaki aliases bhi update dekhen:
values[:] = [value for value in values if value % 2 != 0]
```

### Repetition se independent nested lists samajh li

```python
grid = [[0] * 3] * 2
grid[0][0] = 9
print(grid)  # [[9, 0, 0], [9, 0, 0]]
```

`* 2` ne same inner row ka reference repeat kiya. Independent rows ke liye:

```python
grid = [[0] * 3 for _ in range(2)]
grid[0][0] = 9
print(grid)  # [[9, 0, 0], [0, 0, 0]]
```

### Empty list check

```python
items = []
if items:
    last = items.pop()
else:
    print('List empty hai')
```

Empty list falsy hai. `items is []` empty check nahi hai; wo identity compare karta hai.

## 14. Saare 11 public list methods ek jagah

Ye normal public methods hain. `__len__`, `__getitem__` jaise special methods Python ke protocol hooks hain; normal use `len(items)` aur `items[i]` se hota hai.

| Method | Kaam | Original change? | Return |
|---|---|---|---|
| `append(x)` | End par ek item | Haan | `None` |
| `extend(iterable)` | End par items | Haan | `None` |
| `insert(i, x)` | Position se pehle item | Haan | `None` |
| `remove(x)` | First matching value delete | Haan | `None` |
| `pop(i=-1)` | Index se delete | Haan | Removed item |
| `clear()` | Sab delete | Haan | `None` |
| `index(x[, start[, stop]])` | First matching index | Nahi | Integer; missing par error |
| `count(x)` | Matches count | Nahi | Integer |
| `sort(*, key=None, reverse=False)` | Values/key se order | Haan | `None` |
| `reverse()` | Current order reverse | Haan | `None` |
| `copy()` | Shallow copy | Nahi | New list |

`append(x)`, `insert(i, x)` mein names samjhane ke placeholders hain. In positional methods ko `items.append(value=10)` jaisa keyword syntax mat do. `pop(i=-1)` table mein default batata hai; actual call `items.pop()` ya `items.pop(2)` hai. `sort(key=..., reverse=...)` mein keywords supported aur required hain.

## 15. Common errors ko pehchaano

| Example | Error | Reason |
|---|---|---|
| `[10, 20][5]` | `IndexError` | Position list ke bahar |
| `[].pop()` | `IndexError` | Empty list |
| `[10].remove(99)` | `ValueError` | Value missing |
| `[10].index(99)` | `ValueError` | Value missing |
| `[10].extend(30)` | `TypeError` | Integer iterable nahi |
| `[10, '20'].sort()` | `TypeError` | Default comparison unsupported |
| `[10, 20][::0]` | `ValueError` | Step zero |
| Wrong-size stepped replacement | `ValueError` | Selected positions aur values ka count different |

`Basics.py` mein ye errors `try/except` ke andar intentionally trigger kiye hain, taaki ek error par baaki notebook ruk na jaaye.

## 16. Khud dry run karo

Pehle output likho, phir Python mein check karo. Har line ke baad current list banao; old indexes ko next line par blindly use mat karo.

```python
items = [10, 20, 30]
items.insert(1, 15)
items.append(40)
removed = items.pop(2)
items.remove(10)
items.extend([50, 60])
del items[1:3]
```

```text
start         [10, 20, 30]
insert        [10, 15, 20, 30]
append        [10, 15, 20, 30, 40]
pop(2)        [10, 15, 30, 40]       removed = 20
remove(10)    [15, 30, 40]
extend        [15, 30, 40, 50, 60]
del [1:3]     [15, 50, 60]
```

Practice: `[5, 10, 15]` se shuru karo. Start mein `0`, end mein `20`, aur `10` ke baad `12` add karo. Phir first, last aur value `10` remove karo. Expected final list `[5, 12, 15]` hai. Isko ek baar `pop`, aur ek baar `del` ke saath solve karo.
