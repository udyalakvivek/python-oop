# Python String — text ko samajhne wali notebook

String ka sabse zaroori rule: **existing string ke characters change nahi kar sakte.** Text badalne ke liye desired result banao aur variable ko us result se bind karo. Ye baat clear ho gayi to slicing, replace, add/delete aur methods ke return values samajhna easy ho jaata hai.

Topic outline ke liye tumhara diya hua [GeeksforGeeks Python String article](https://www.geeksforgeeks.org/python/python-string/) use kiya hai. Neeche explanations aur examples apne practice cases hain. Exact method signatures ke liye [Python 3.12 string reference](https://docs.python.org/3.12/library/stdtypes.html#string-methods) linked hai; notebook local Python 3.12 ke liye likhi gayi hai.

## 1. Python file ko kaise padhna hai

[basics.py](basics.py) teen parts mein hai:

1. Foundation: creation, indexing, slicing, immutability, add/update/delete.
2. Methods: related methods ek function mein, total **47 public `str` methods**.
3. Mistakes aur practice: caught errors, cleanup, palindrome, receipt.

Har topic ka apna `demo_...()` function hai. Setup, operation aur expected result paas-paas hain. `main()` sirf reading order mein functions call karta hai.

```bash
# Project root se poori notebook:
python String/basics.py

# Sirf slicing topic:
python -c "from String.basics import demo_slicing; demo_slicing()"
```

`section()` heading print karta hai. `show()` indented label aur value ka representation dikhata hai. Quotes, trailing spaces aur `\n` visible rehte hain. Non-ASCII text escapes mein dikhta hai, taaki output kisi console encoding par depend na kare. Actual string badalti nahi.

```python
def demo_example():                 # Top level: no indentation
    text = "cat"                   # Function body: 4 spaces

    for character in text:
        if character == "a":
            print(character)       # Nested blocks: 4 spaces per level
```

Indentation code ke block ke hisaab se hoti hai. Sirf decoration ke liye extra spaces lagane se `IndentationError` aa sakta hai.

## 2. String kya hai?

Python mein text ka type `str` hai. Ye Unicode code points ki ordered, immutable sequence hai. Beginner level par characters ki sequence soch sakte ho; Unicode section mein visible character aur code point ka difference dekhenge.

```python
name = "Aman"
language = 'Python'
empty = ""
single_character = "A"
```

Single aur double quotes ka behavior same hai. Convenient quote choose karo:

```python
message = "I'm learning"
quote = 'Usne kaha: "Practice karo"'
```

Python mein separate `char` type nahi hai. `"A"` bhi string hai, length `1`.

```python
len("A B")     # 3: space bhi count hota hai
str(250)       # '250': text
int("250") + 5 # 255: numeric conversion
"250" + "5"    # '2505': concatenation
```

`""` falsy hai. `" "`, `"0"` aur `"False"` truthy hain, kyunki ye nonempty text hain. `bool("False")` text ko parse karke boolean false nahi banata.

## 3. Escape sequences, raw strings aur multiline text

| Source mein | Meaning | Example |
|---|---|---|
| `\n` | Newline | `"first\nsecond"` |
| `\t` | Tab | `"name\tmarks"` |
| `\\` | One backslash | `"C:\\notes"` |
| `\'` | Single quote | `'I\'m ready'` |
| `\"` | Double quote | `"He said \"Hi\""` |
| `\u00e9` | Unicode code point | `"caf\u00e9"` |

```python
len("\n")   # 1: actual newline
len(r"\n")  # 2: backslash aur n
path = r"C:\notes\day1"
```

Raw string literal mein backslashes normally escape conversion nahi karte. Ye Windows paths aur regex patterns likhne mein useful hai. Raw string bhi ordinary `str` hi hai. Raw literal **odd number of trailing backslashes** par end nahi ho sakta: `r"C:\"` valid Python source nahi hai.

Triple quotes multiline text allow karte hain. Newlines aur indentation preserve hoti hai:

```python
paragraph = """first line
    second line"""
print(repr(paragraph))  # 'first line\n    second line'
```

Function ke andar indented multiline text clean karna ho to `textwrap.dedent()` use kar sakte ho; example Python file mein hai. `.strip()` sirf outer whitespace hataata hai, har line ki indentation nahi.

`print(text)` rendered text dikhata hai. `repr(text)` debugging representation deta hai. `ascii(text)` non-ASCII characters bhi escape karta hai. Ye built-in functions hain, string methods nahi.

## 4. Indexing: positive aur negative

```text
text = "PYTHON"

character    P   Y   T   H   O   N
positive     0   1   2   3   4   5
negative    -6  -5  -4  -3  -2  -1
```

```python
text[0]   # 'P'
text[2]   # 'T'
text[-1]  # 'N'
text[-2]  # 'O'
```

Last positive index `len(text) - 1` hai. `text[len(text)]` invalid hai. Empty string ka first ya last character bhi nahi hota.

Valid negative index ko `len(text) + index` se samjho: `6 + (-2) = 4`. `text[-7]` yahan out of range hai. Invalid index par `IndexError`; `text[1.5]` par `TypeError`.

## 5. Slicing ka dry run

Syntax: `text[start:stop:step]`. Start include, stop exclude.

```python
text = "PYTHON"
text[1:4]     # 'YTH'
text[:3]      # 'PYT'
text[3:]      # 'HON'
text[::2]     # 'PTO'
text[::-1]    # 'NOHTYP'
text[4:1:-1]  # 'OHT'
text[100:]    # ''
text[3:1]     # ''
```

`[4:1:-1]` mein positions `4, 3, 2` li gayi; stop `1` exclude hai. Positive step mein start left aur stop right default hota hai. Negative step mein defaults opposite direction ke hote hain.

Direct index missing ho to error; slice ke out-of-range bounds clip ho jaate hain. `step=0` invalid hai.

`text[:]` same text value deta hai. Strings immutable hain, isliye independent mutable copy ki zarurat nahi. Implementation same object reuse kar sakti hai; full slice ko guaranteed new identity mat samjho.

## 6. Immutability aur reassignment alag hain

```python
text = "cat"
alias = text
changed = text.replace("c", "b")

print(text)     # cat
print(changed)  # bat

text += "s"
print(text)     # cats
print(alias)    # cat
```

Pehle `text` aur `alias` same old value ko refer karte the. `text += "s"` ke baad `text` updated result se bind hua. `alias` abhi old `"cat"` ko refer karta hai.

```text
Before:
    text  ----+
              +----> "cat"
    alias ----+

After text += "s":
    text  ---------> "cats"
    alias ---------> "cat"
```

`text[0] = "b"` aur `del text[0]` valid nahi. Strings mein `append`, `insert`, `remove`, `pop`, `clear`, `sort`, `reverse`, `copy` jaise list methods nahi hain.

String methods original ko mutate nahi karte. Text-returning methods ka result use karna padta hai:

```python
name = "aman"
name.upper()
print(name)  # aman: result ignore kar diya

name = name.upper()
print(name)  # AMAN
```

Har method string return nahi karta: `split` list, `partition` tuple, `find` integer, `isalpha` boolean, `encode` bytes deta hai.

## 7. Start, end aur kahin bhi add karna

Har row mein fresh `text = "abcd"` socho. Result use/store karna hai; original automatically update nahi hota.

| Requirement | Expression | Result |
|---|---|---|
| Start mein add | `"X" + text` | `'Xabcd'` |
| End mein add | `text + "X"` | `'abcdX'` |
| Index 2 se pehle add | `text[:2] + "XY" + text[2:]` | `'abXYcd'` |

Anywhere insert ka formula:

```python
position = 2
new_part = "XY"
text = text[:position] + new_part + text[position:]
```

```text
Old text:  ab | cd
Insert:       XY
Result:    ab XY cd
```

Valid insertion positions `0` se `len(text)` tak hain. Slice bounds oversized ho to clip hote hain, lekin agar tumhare program ko invalid position reject karni hai to explicitly validate karo.

## 8. Update aur delete: index se ya value se

Again, har row fresh `text = "abcd"` par hai.

| Requirement | Expression | Result |
|---|---|---|
| First replace | `"X" + text[1:]` | `'Xbcd'` |
| Last replace | `text[:-1] + "X"` | `'abcX'` |
| Index 2 replace | `text[:2] + "X" + text[3:]` | `'abXd'` |
| Range `[1:3]` replace | `text[:1] + "XY" + text[3:]` | `'aXYd'` |
| First delete | `text[1:]` | `'bcd'` |
| Last delete | `text[:-1]` | `'abc'` |
| Index 2 delete | `text[:2] + text[3:]` | `'abd'` |
| Range `[1:3]` delete | `text[:1] + text[3:]` | `'ad'` |

Known nonnegative index `i` se one character delete: `text[:i] + text[i + 1:]`. Pehle `0 <= i < len(text)` ensure karo. Formula mein `i=-1` blindly plug mat karo: `i+1` zero hoga, jisse wrong result banega. Last remove ke liye `text[:-1]` clear hai; generic negative index ko pehle normalize aur validate karo.

```python
text = "banana"
text.replace("a", "", 1)  # 'bnana': first occurrence
text.replace("a", "")     # 'bnn': all occurrences
```

Many positional edits ke liye list temporarily useful hai:

```python
characters = list("cat")
characters[0] = "b"
characters.append("s")
text = "".join(characters)  # 'bats'
```

`text = ""` variable ko empty string se bind karta hai. `del text` variable binding hataata hai; later access par `NameError`. Agar old string ka koi aur alias hai, wo usable rehta hai. `del` object ko sab jagah se erase karne ka command nahi hai.

## 9. Operators, membership aur loops

```python
"Hello" + " " + "Aman"  # 'Hello Aman'
"ha" * 3                # 'hahaha'
"ha" * 0                # ''
"ha" * -1               # ''
"thon" in "Python"      # True
"python" in "Python"    # False: case-sensitive
"java" not in "Python"  # True
"" in "abc"             # True: empty substring exists
```

`"age=" + 21` invalid hai. `"age=" + str(21)` ya `f"age={21}"` likho.

String comparison lexicographic hota hai: first different code point decide karta hai. `"10" < "2"` true hai, kyunki text compare ho raha hai. Numeric comparison ke liye values convert karo. Human-language alphabetical sorting alag problem hai.

```python
for character in "cat":
    print(character)

for index, character in enumerate("cat"):
    print(index, character)
```

Values compare karne ke liye `==`. `is` same object identity check karta hai; string equality ke liye use mat karo.

## 10. Case methods — 6 methods

For `text = "pYTHON is FUN"`:

| Method | Result | Kya hua? |
|---|---|---|
| `text.lower()` | `'python is fun'` | Lowercase mapping |
| `text.upper()` | `'PYTHON IS FUN'` | Uppercase mapping |
| `text.capitalize()` | `'Python is fun'` | First character titlecase, rest lowercase |
| `text.title()` | `'Python Is Fun'` | Word-like groups titlecase |
| `text.swapcase()` | `'Python IS fun'` | Upper/lower switch |
| `text.casefold()` | `'python is fun'` | Caseless matching ke liye folding |

`capitalize()` leading spaces skip karke first letter nahi dhoondhta. `" hello".capitalize()` mein `h` lowercase hi rahega.

`title()` natural language ko fully understand nahi karta:

```python
"they're ready".title()  # "They'Re Ready"
```

`lower()` aur `casefold()` ASCII text par similar lag sakte hain. Unicode mein difference dikhta hai:

```python
"Straße".lower()     # 'straße'
"Straße".casefold()  # 'strasse'
"Straße".casefold() == "STRASSE".casefold()  # True
```

Case conversion length change kar sakti hai: `"ß".upper()` becomes `"SS"`. Har Unicode character one-to-one map nahi hota; double `swapcase()` ko universal undo mat samjho.

## 11. Edge cleanup — 5 methods

```python
text = "  hello  "
text.strip()   # 'hello'
text.lstrip()  # 'hello  '
text.rstrip()  # '  hello'
```

Default whitespace mein spaces ke alawa tabs/newlines bhi aate hain. Middle spaces preserve rehte hain: `"  a  b  ".strip()` → `'a  b'`.

**`strip(chars)` exact substring nahi hataata.** Wo allowed characters ka set leta hai aur ends se matching characters hataata chala jaata hai.

```python
"xyhelloyx".strip("xy")                 # 'hello'
"Arthur: run".lstrip("Arthur: ")        # 'n'
"Arthur: run".removeprefix("Arthur: ")  # 'run'
"report.csv".removesuffix(".csv")       # 'report'
```

`lstrip` example mein prefix ke baad `r` aur `u` bhi allowed set mein the, isliye delete hue. Exact beginning/ending text ke liye `removeprefix` / `removesuffix` use karo. Missing affix par same text value milti hai. Ye ek matching affix remove karte hain, repeated prefix ko automatically baar-baar nahi.

## 12. Search aur count — 5 methods

For `text = "banana"`:

| Call | Result | Meaning |
|---|---|---|
| `text.find("an")` | `1` | First matching start |
| `text.rfind("an")` | `3` | Last matching start |
| `text.index("an")` | `1` | First match, missing par error |
| `text.rindex("an")` | `3` | Last match, missing par error |
| `text.count("an")` | `2` | Non-overlapping matches |

Search methods optional start/stop bounds lete hain:

```python
text.find("an", 2, 5)  # 3: original string ka index
text.find("z")         # -1
text.rfind("z")        # -1
# text.index("z")      # ValueError
# text.rindex("z")     # ValueError
text.count("z")        # 0
text.count("ana")      # 1: overlapping matches count nahi hote
"abc".count("")        # 4: character boundaries
```

`if text.find(part):` common bug hai. Match at `0` falsy hai aur missing result `-1` truthy hai.

```python
position = text.find("b")
if position != -1:
    print(position)  # 0

# Sirf presence chahiye:
if "b" in text:
    print("Found")
```

## 13. Prefix/suffix check — 2 methods

```python
filename = "notes.py"
filename.startswith("notes")        # True
filename.endswith(".py")            # True
filename.endswith((".py", ".md"))   # True
filename.endswith(".PY")            # False
"abcXYZ".startswith("XYZ", 3, 6)     # True
```

Return boolean hai. Text remove nahi hota. Multiple alternatives ke liye tuple do. Start/end bounds optional hain aur matching case-sensitive hai. Ye regex patterns nahi hain.

## 14. Replacement — 1 method

```python
text = "red red red"
text.replace("red", "blue")     # 'blue blue blue'
text.replace("red", "blue", 2)  # 'blue blue red'
text.replace("green", "blue")   # 'red red red'
"a-b-c".replace("-", "")        # 'abc'
```

`replace(old, new, count)` literal substring replacement hai. Count omitted ho to all non-overlapping occurrences; count `0` ho to no replacements. Empty replacement text deletion jaisa result deta hai. Original unchanged.

Python 3.12 compatibility ke liye count positional diya hai. `replace` ko regex na samjho; `"."` actual dot match karega.

## 15. Split aur lines — 3 methods

```python
"  a   b\tc  ".split()     # ['a', 'b', 'c']
" a  b ".split(" ")       # ['', 'a', '', 'b', '']
"a,,b,".split(",")        # ['a', '', 'b', '']
"a,b,c".split(",", 1)     # ['a', 'b,c']
"a,b,c".rsplit(",", 1)    # ['a,b', 'c']
"".split()                # []
"".split(",")             # ['']
```

Without separator, whitespace runs combine hote hain aur edge whitespace se empty tokens nahi bante. Explicit separator mein adjacent/edge separators empty fields bana sakte hain.

`maxsplit=1` ka matlab maximum one split, normally up to two pieces. `rsplit` right se limited splits karta hai; result pieces ka left-to-right order preserve rehta hai.

`split("")` invalid hai. Characters chahiye to `list(text)`.

```python
"a\r\nb\nc\n".splitlines()               # ['a', 'b', 'c']
"a\nb\n".splitlines(keepends=True)       # ['a\n', 'b\n']
"".splitlines()                          # []
```

`splitlines()` multiple line-boundary forms understand karta hai. Trailing newline extra empty final element nahi banaata; ye `split("\n")` se difference hai. Actual CSV files mein quoted commas ho sakte hain, isliye file parsing ke liye `csv` module use hota hai.

## 16. Join aur partition — 3 methods

### `separator.join(iterable)`

```python
" ".join(["learn", "by", "doing"])  # 'learn by doing'
"-".join(["learn", "by", "doing"])  # 'learn-by-doing'
"".join(["c", "a", "t"])           # 'cat'
"-".join("cat")                      # 'c-a-t'
",".join(str(n) for n in [1, 2, 3]) # '1,2,3'
```

Method separator string par call hota hai. Iterable ke items strings hone chahiye. `",".join([1, 2])` par `TypeError`. Empty iterable ka result `""`.

### `partition(separator)` aur `rpartition(separator)`

```python
"a=b=c".partition("=")   # ('a', '=', 'b=c')
"a=b=c".rpartition("=")  # ('a=b', '=', 'c')
"abc".partition("=")     # ('abc', '', '')
"abc".rpartition("=")    # ('', '', 'abc')
```

Exactly three elements ka tuple: before, matched separator, after. `partition` first match, `rpartition` last match. Missing separator par tuple placement alag hai, table dhyaan se dekho. Empty separator invalid hai.

```python
key, separator, value = "theme=dark".partition("=")
if separator:
    print(key, value)  # theme dark
```

`split` pieces ki list deta hai aur separator drop karta hai. `partition` fixed three parts deta hai aur matched separator preserve karta hai.

## 17. Alignment aur tab expansion — 5 methods

```python
"hi".center(6, "-")    # '--hi--'
"hi".ljust(5, ".")     # 'hi...'
"hi".rjust(5, ".")     # '...hi'
"hello".center(2)      # 'hello': truncate nahi hua
"42".zfill(5)          # '00042'
"-42".zfill(5)         # '-0042'
"-42".rjust(5, "0")    # '00-42'
"a\tb".expandtabs(4)   # 'a   b'
"ab\tc".expandtabs(4)  # 'ab  c'
```

Width total minimum width hai, added spaces ka count nahi. `center/ljust/rjust` ka default fill space hai; custom fill exactly one character hona chahiye.

`zfill` starting sign ke baad zero pad karta hai. Text ko number mein convert nahi karta. `expandtabs` next tab stop tak spaces daalta hai; har tab ko fixed four spaces se replace nahi karta. Unicode display width character count se alag ho sakti hai, isliye terminal alignment har script/emoji par perfect nahi hota.

## 18. Boolean checks — 12 methods

| Method | True example | Kya check karta hai? |
|---|---|---|
| `isalpha()` | `'Python'.isalpha()` | All alphabetic characters, nonempty |
| `isalnum()` | `'Python3'.isalnum()` | Alphabetic/numeric characters, nonempty |
| `isdecimal()` | `'123'.isdecimal()` | Decimal digit characters, nonempty |
| `isdigit()` | `'²'.isdigit()` | Broader digit characters, nonempty |
| `isnumeric()` | `'½'.isnumeric()` | Broader numeric characters, nonempty |
| `isspace()` | `' \t\n'.isspace()` | All whitespace, nonempty |
| `islower()` | `'abc123'.islower()` | All cased characters lowercase; at least one |
| `isupper()` | `'ABC123'.isupper()` | All cased characters uppercase; at least one |
| `istitle()` | `'Hello World'.istitle()` | Cased groups follow titlecase pattern |
| `isprintable()` | `'hello world'.isprintable()` | No nonprintable characters |
| `isascii()` | `'abc123'.isascii()` | All code points within ASCII |
| `isidentifier()` | `'user_name2'.isidentifier()` | Identifier syntax valid |

Alphabetic ka matlab sirf English A-Z nahi; methods Unicode-aware hain. `isalnum()` underscore ko allow nahi karta. `"user_name".isalnum()` false hai, lekin `.isidentifier()` true hai.

Numeric checks ka relation:

```text
decimal characters ⊆ digit characters ⊆ numeric characters
```

```python
"²".isdecimal()  # False
"²".isdigit()    # True
"½".isdigit()    # False
"½".isnumeric()  # True
"-12".isdigit()  # False: sign
"3.5".isnumeric() # False: decimal point
```

Ye full numeric parser nahi hain. `"²".isdigit()` true hone se `int("²")` valid nahi ho jaata. Actual number conversion chahiye to appropriate `int`/`float` conversion aur `ValueError` handling use karo.

`"123".islower()` aur `.isupper()` dono false: koi cased letter nahi. Empty string par `.isascii()` aur `.isprintable()` true hain; baaki listed checks false.

Identifier syntax aur reserved keyword alag cheezein hain:

```python
import keyword

"class".isidentifier()    # True: syntax fits
keyword.iskeyword("class") # True: reserved keyword
```

Isliye `.isidentifier()` akela ordinary variable name usability prove nahi karta.

## 19. Formatting — 2 string methods, aur language syntax

```python
name = "Aman"
marks = 87.456

f"{name}: {marks:.2f}"           # 'Aman: 87.46'
f"Next year: {20 + 1}"          # 'Next year: 21'
f"|{name:<8}|{42:04d}|"          # '|Aman    |0042|'
f"{{score}} = {marks:.1f}"       # '{score} = 87.5'
```

`:.2f` fixed-point output with two decimal places, `<8` left alignment minimum width 8, `04d` integer minimum width 4 with zeros. Formatting output banati hai; original numeric value round karke replace nahi karti. Literal braces ke liye `{{` aur `}}`.

```python
"{} scored {:.1f}".format(name, marks)  # 'Aman scored 87.5'
"{person}: {score}".format(person=name, score=90) # 'Aman: 90'

data = {"name": "Neha", "city": "Delhi"}
"{name} lives in {city}".format_map(data) # 'Neha lives in Delhi'

"%s scored %.1f" % (name, marks)  # 'Aman scored 87.5'
```

`format` positional/named arguments leta hai. `format_map` mapping se named fields leta hai. Missing mapping key par normally `KeyError`. f-string language syntax hai, `%` older formatting operator hai; ye string methods nahi.

## 20. Translation — 2 methods

```python
table = str.maketrans("ae", "@3", "!")
"Please!".translate(table)  # 'Pl3@s3'
```

Yahan `a → @`, `e → 3`, aur `! → delete`. First two arguments equal-length strings hone chahiye. Third string ke characters delete honge.

Mapping form bhi hai:

```python
table = str.maketrans({"@": " at ", "!": None})
"hi@home!".translate(table)  # 'hi at home'
```

`maketrans` translation table banata hai; static method ki tarah `str.maketrans(...)` call karte hain. Mapping keys single characters ya Unicode ordinals ho sakte hain. Values replacement text, ordinal, ya `None` for deletion. `translate` character/code-point mapping apply karta hai. Whole substrings replace karne ke liye `replace` simpler hai.

## 21. Encoding — 1 method, aur Unicode ka important difference

`str` Unicode text hai; `bytes` encoded byte data hai. Encoding text ko bytes mein badalti hai; decoding bytes ko text mein. Details ke liye [Python Unicode HOWTO](https://docs.python.org/3.12/howto/unicode.html) dekho.

```python
text = "café"
payload = text.encode("utf-8")

len(text)                    # 4 Unicode code points
payload                      # b'caf\xc3\xa9'
len(payload)                 # 5 bytes
payload.decode("utf-8")      # 'café'
```

`encode` string method hai. `decode` **bytes method** hai, string method nahi. `str(payload)` decode nahi karta; normally bytes representation ka text milta hai.

Wrong codec/unrepresentable character par `UnicodeEncodeError` ya `UnicodeDecodeError` aa sakta hai. `errors="replace"` replacement markers use kar sakta hai aur `errors="ignore"` data drop kar sakta hai; inhe loss samajhkar choose karo. Examples normal strict behavior use karte hain.

### Length ka matlab screen par visible symbols ka count zaroori nahi

```python
composed = "\u00e9"      # é, one code point
decomposed = "e\u0301"   # e + combining acute accent, two code points

len(composed)            # 1
len(decomposed)          # 2
composed == decomposed  # False
```

Dono visually similar dikh sakte hain. Canonical normalization relevant ho to:

```python
import unicodedata

composed == unicodedata.normalize("NFC", decomposed)  # True
```

`len`/indexing code points par kaam karte hain. Combining marks aur multi-code-point emoji ek visible character jaisa lag sakte hain. `[::-1]` code points reverse karega, complete visible character groups ki guarantee nahi.

`ord("A")` → `65`, `chr(65)` → `'A'`. Ye built-ins hain; `ord` ko one-character string chahiye.

## 22. Behind the scenes

### String list of one-character objects nahi hai

Python language Unicode string behavior define karti hai. CPython representation flexible hai: text ke code points ke hisaab se internal storage commonly 1, 2 ya 4 bytes per code point use karta hai, object overhead alag hota hai. Ye detail language-level guarantee nahi. Internal representation ko UTF-8 encoded bytes ke barabar mat samjho. Is design ka reference [PEP 393](https://peps.python.org/pep-0393/) hai.

`text[2]` one-character string value deta hai. Isse ye conclude nahi hota ki original string ke andar har character ka separate Python object stored tha.

### Immutable hone se sharing simple hoti hai

Do names same string object share kar sakte hain, bina kisi alias ke characters mutate kar dene ke risk ke. Kuch strings intern/cache/reuse ho sakti hain. Isliye `is`, `id()` ya full-slice identity par text logic mat banao. `==` value comparison ke liye hai.

Text transformation ko result-producing operation samjho. Actual different text ke liye result storage chahiye, lekin unchanged results aur full slices jaise cases same immutable object reuse kar sakte hain. Har method call guaranteed fresh allocation nahi hai.

### Concatenation aur repeated building

```python
result = ""
for part in parts:
    result += part
```

Simple copying model mein har step growing prefix ko copy kar sakta hai. Equal-size pieces add karne par work `1 + 2 + 3 + ... + n` jaisa ho sakta hai, yani quadratic. CPython kuch patterns optimize kar sakta hai, lekin us optimization ko guarantee mat maano.

```python
parts = []
for number in range(5):
    parts.append(str(number))

result = ",".join(parts)  # '0,1,2,3,4'
```

`join` many fragments build karne ka clear tareeka hai. CPython pieces ke sizes dekhkar final result ke liye space arrange kar sakta hai aur pieces copy karta hai.

### Rough costs

`n` input code-point count, `k` selected/output size. Ye usual implementation model hai; exact search algorithm aur Unicode processing detail operation par depend karti hai.

| Operation | Rough cost | Reason |
|---|---|---|
| `len(text)` | `O(1)` in CPython | Length stored |
| `text[i]` | `O(1)` in CPython | Direct code-point access |
| Nontrivial slice of k code points | `O(k)` | Result content copy |
| `a + b` | Usually `O(len(a) + len(b))` | Combined text produce |
| `lower`, `upper`, checks | Input scan; worst proportional to input/output | Characters inspect/map |
| `strip` | Edges scan, result copying may add cost | Depends on removed/retained text |
| `find`, `in`, `replace` | Depends on text, pattern and matches | Substring search required |
| `join(parts)` | `O(p + L)` | p pieces inspect, L output copy |
| Repeated growing concatenation | Can be `O(n²)` total | Prefix repeatedly copy |

String hashing first time normally text scan karta hai; CPython cached hash reuse kar sakta hai. Ordinary strings immutable aur hashable hain, isliye dictionary keys/set members ban sakti hain.

## 23. Saare methods ka coverage map

| Python function | Methods covered |
|---|---|
| `demo_case_methods` | `lower`, `upper`, `capitalize`, `title`, `swapcase`, `casefold` |
| `demo_strip_and_affixes` | `strip`, `lstrip`, `rstrip`, `removeprefix`, `removesuffix` |
| `demo_search_and_count` | `find`, `rfind`, `index`, `rindex`, `count` |
| `demo_prefix_suffix_checks` | `startswith`, `endswith` |
| `demo_replace` | `replace` |
| `demo_split_methods` | `split`, `rsplit`, `splitlines` |
| `demo_join_and_partition` | `join`, `partition`, `rpartition` |
| `demo_alignment` | `center`, `ljust`, `rjust`, `zfill`, `expandtabs` |
| `demo_character_checks` | `isalpha`, `isalnum`, `isdecimal`, `isdigit`, `isnumeric`, `isspace`, `islower`, `isupper`, `istitle`, `isprintable`, `isascii`, `isidentifier` |
| `demo_formatting` | `format`, `format_map` |
| `demo_translation` | `maketrans`, `translate` |
| `demo_unicode_and_encoding` | `encode` |

Total: `6 + 5 + 5 + 2 + 1 + 3 + 3 + 5 + 12 + 2 + 2 + 1 = 47` public methods in the local Python 3.12 environment. Special protocol methods like `__len__` normal usage mein `len(text)` ke through use hote hain; unhe separate everyday methods ki list mein nahi rakha.

## 24. Common mistakes ka revision

| Mistake | Kya hoga? | Better approach |
|---|---|---|
| `text[0] = "X"` | `TypeError` | Slice + concatenation |
| `del text[0]` | `TypeError` | Unwanted part skip karke result |
| `text.append("X")` | `AttributeError` | `text = text + "X"` |
| `text.upper()` result ignore | Variable old text rakhega | Result store/use |
| `text[999]` | `IndexError` | Bounds check |
| `text.index(missing)` | `ValueError` | `find` / `in` / exception handling |
| `if text.find(part)` | Position 0 aur -1 wrong interpret | `!= -1` or `in` |
| `strip("prefix")` for exact prefix | Valid edge letters bhi remove | `removeprefix` |
| `split("")` | `ValueError` | `list(text)` for characters |
| `",".join([1, 2])` | `TypeError` | Convert each item with `str` |
| `"age=" + 21` | `TypeError` | f-string or `str(21)` |
| `text[::0]` | `ValueError` | Nonzero step |
| `is` for string equality | Object reuse par depend karega | `==` |
| `isdigit()` as universal numeric parser | Signs/fractions/Unicode confuse | Actual conversion + error handling |

## 25. Practice aur dry runs

### A. Name cleanup

```python
raw = "  nEHA   sHARMA  "
words = raw.split()            # ['nEHA', 'sHARMA']
joined = " ".join(words)       # 'nEHA sHARMA'
clean = joined.title()         # 'Neha Sharma'
```

Ye controlled example hai. Real names ki capitalization har jagah `.title()` se sahi nahi hoti.

### B. Add/delete dry run

```python
text = "code"
text = "[" + text          # '[code'
text = text + "]"          # '[code]'
text = text[:3] + "X" + text[3:]  # '[coXde]'
text = text[1:-1]          # 'coXde'
text = text.replace("X", "", 1)   # 'code'
```

Har line par new current indexes likho. Pehle wale indexes next line par unchanged honge, aisa assume mat karo.

### C. Khud solve karo

1. `"  python,java,cpp  "` ko clean karke `['python', 'java', 'cpp']` banao.
2. `"report.final.csv"` se stem `"report.final"` aur extension `"csv"` nikaalo.
3. `"banana"` mein saare `a` hatao. Expected `'bnn'`.
4. `"Never odd or even"` ko spaces/case ignore karke palindrome check karo. Expected `True`.
5. `[10, 20, 30]` ko `'10 | 20 | 30'` mein convert karo.
6. `'user_name2'` par `isalnum()` aur `isidentifier()` ke results predict karo: `False`, `True`.

Python file ke last topic mein cleanup, filename, palindrome aur receipt examples already runnable hain. Pehle khud result socho, phir function run karke compare karo.
