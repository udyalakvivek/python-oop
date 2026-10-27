"""Python strings — topic-wise practice notebook.

Run all topics:
    python String/basics.py

Run just one topic from the project root:
    python -c "from String.basics import demo_slicing; demo_slicing()"

Reading order inside each function:
    1. Short explanation in the docstring.
    2. Input and actual operation.
    3. Output, with expected results in comments.

Indentation: function body = 4 spaces; nested loop/if/try body = 8 spaces.
Detailed notes and references: String/String.md
"""

import keyword
import unicodedata
from textwrap import dedent


# ---------------------------------------------------------------------------
# Output helpers: bas notebook ka output readable banane ke liye.
# Actual string operations neeche topic functions ke andar hain.
# ---------------------------------------------------------------------------

def section(number, title):
    """Har topic ko numbered heading do."""
    print(f"\n{number:02d}. {title}")
    print("-" * 72)


def show(label, value):
    """Quotes, spaces aur escape sequences ko output mein visible rakho.

    ascii() representation dikhata hai: newline -> \n, non-ASCII -> escapes.
    Actual string ko change nahi karta. Unicode demo har console par chalega.
    """
    print(f"    {label:<37} -> {ascii(value)}")


# ===========================================================================
# PART A — STRING KI FOUNDATION
# ===========================================================================

def demo_creation():
    """str text hai. Single aur double quotes ka behavior same hai."""
    section(1, "String banana, quotes aur conversion")

    name = "Aman"
    message = 'Python seekh raha hoon'
    apostrophe = "I'm learning Python"
    quoted = 'Usne kaha: "Practice karo"'

    show("name", name)                     # 'Aman'
    show("message", message)
    show("apostrophe", apostrophe)
    show("quoted text", quoted)
    show("empty string", "")
    show("single character ka type", type("A").__name__)  # 'str'
    show("str(250)", str(250))             # '250'
    show("int('250') + 5", int("250") + 5)  # 255
    show("len('A B')", len("A B"))         # 3; space bhi count hua
    show("bool('')", bool(""))             # False
    show("bool(' ')", bool(" "))           # True; space empty nahi
    show("bool('False')", bool("False"))   # True; nonempty text


def demo_escape_and_multiline():
    """Escape sequences text ka part hain; triple quotes indentation rakhte hain."""
    section(2, "Escape sequences, raw aur multiline strings")

    show("newline", "first\nsecond")
    show("tab", "name\tmarks")
    show("backslash", "C:\\notes\\day1")
    show("escaped quote", 'I\'m ready')
    show("raw path", r"C:\notes\day1")
    show("normal newline length", len("\n"))  # 1
    show("raw backslash+n length", len(r"\n"))  # 2

    paragraph = """first line
    second line"""
    show("triple quotes keep spaces", paragraph)
    # Output: 'first line\n    second line'

    cleaned = dedent("""\
        first line
        second line
    """).strip()
    show("dedent + strip", cleaned)  # 'first line\nsecond line'
    # dedent textwrap ka function hai, str method nahi.
    # Raw literal odd number of trailing backslashes par end nahi ho sakta.


def demo_indexing():
    """Index 0 se start; negative index end se count karta hai."""
    section(3, "Positive aur negative indexing")

    text = "PYTHON"
    # Positive:  0  1  2  3  4  5
    # Character: P  Y  T  H  O  N
    # Negative: -6 -5 -4 -3 -2 -1

    show("text[0]", text[0])     # 'P'
    show("text[2]", text[2])     # 'T'
    show("text[-1]", text[-1])   # 'N'
    show("text[-2]", text[-2])   # 'O'
    show("last positive index", len(text) - 1)  # 5


def demo_slicing():
    """[start:stop:step]: stop exclude; omitted bounds direction se decide."""
    section(4, "Slicing aur reverse")

    text = "PYTHON"
    show("text[1:4]", text[1:4])       # 'YTH'
    show("text[:3]", text[:3])         # 'PYT'
    show("text[3:]", text[3:])         # 'HON'
    show("text[::2]", text[::2])       # 'PTO'
    show("text[::-1]", text[::-1])     # 'NOHTYP'
    show("text[4:1:-1]", text[4:1:-1]) # 'OHT'
    show("text[100:]", text[100:])     # ''; bounds clip
    show("text[3:1]", text[3:1])       # ''; direction mismatch
    show("text[:]", text[:])           # Same value; new identity guaranteed nahi
    # text[100] error hai, text[100:] empty string hai.


def demo_immutability():
    """Existing string ke characters change nahi hote; variable rebind hota hai."""
    section(5, "Immutability, aliases aur reassignment")

    original = "cat"
    alias = original
    changed = original.replace("c", "b")

    show("original", original)  # 'cat'
    show("changed", changed)    # 'bat'

    original += "s"
    show("original after +=", original)  # 'cats'
    show("alias still old text", alias)   # 'cat'
    show("value equality", original == alias)  # False
    # += yahan existing 'cat' ko mutate nahi karta.
    # Text compare karne ke liye ==; is object identity ke liye hai.


def demo_add_update_delete():
    """String mein append/pop nahi. Slices jodkar desired text banao."""
    section(6, "Start, end, anywhere: add / update / delete")

    text = "abcd"

    # ADD: har example same original text se independent result banata hai.
    show("start add", "X" + text)             # 'Xabcd'
    show("end add", text + "X")               # 'abcdX'
    position = 2
    show("index 2 insert", text[:position] + "XY" + text[position:])
    # 'abXYcd': index 2 wale 'c' se pehle insert hua.

    # UPDATE: selected old characters ko result mein include mat karo.
    show("first replace", "X" + text[1:])     # 'Xbcd'
    show("last replace", text[:-1] + "X")     # 'abcX'
    show("index 2 replace", text[:2] + "X" + text[3:])  # 'abXd'
    show("range [1:3] replace", text[:1] + "XY" + text[3:])  # 'aXYd'

    # DELETE: unwanted part ke left aur right ko jod do.
    show("first delete", text[1:])            # 'bcd'
    show("last delete", text[:-1])            # 'abc'
    show("index 2 delete", text[:2] + text[3:])  # 'abd'
    show("range [1:3] delete", text[:1] + text[3:])  # 'ad'
    show("delete first 'a' by value", "banana".replace("a", "", 1))
    # 'bnana'; count omitted hota to saare 'a' delete hote.
    show("original", text)                    # 'abcd'

    # Multiple character edits ho to temporary list useful hai.
    characters = list("cat")
    characters[0] = "b"
    characters.append("s")
    show("list edit then join", "".join(characters))  # 'bats'

    alias = text
    text = ""  # Naam ko empty string se bind kiya.
    show("empty text", text)
    show("old alias", alias)                  # 'abcd'
    del text  # Naam ki binding hataayi; alias abhi bhi usable hai.
    show("alias after del text", alias)


def demo_operators_and_loops():
    """Operators, membership aur loops: str methods se alag concepts."""
    section(7, "Concatenation, repetition, membership aur loops")

    show("concatenation", "Hello" + " " + "Aman")  # 'Hello Aman'
    show("repetition", "ha" * 3)                    # 'hahaha'
    show("repeat zero times", "ha" * 0)             # ''
    show("substring membership", "thon" in "Python") # True
    show("case-sensitive membership", "python" in "Python")  # False
    show("not in", "java" not in "Python")          # True
    show("empty substring", "" in "abc")            # True
    show("lexicographic compare", "apple" < "banana")  # True
    show("numeric text compare", "10" < "2")        # True; text ordering

    for index, character in enumerate("cat"):
        show(f"character at index {index}", character)

    vowels = [character for character in "education" if character in "aeiou"]
    show("vowel collection", vowels)  # ['e', 'u', 'a', 'i', 'o']


# ===========================================================================
# PART B — ALL 47 PUBLIC str METHODS, RELATED METHODS TOGETHER
# ===========================================================================

def demo_case_methods():
    """Case methods return text; original input unchanged rehta hai."""
    section(8, "Case: lower / upper / capitalize / title / swapcase / casefold")

    text = "pYTHON is FUN"
    show("lower()", text.lower())           # 'python is fun'
    show("upper()", text.upper())           # 'PYTHON IS FUN'
    show("capitalize()", text.capitalize()) # 'Python is fun'
    show("title()", text.title())           # 'Python Is Fun'
    show("swapcase()", text.swapcase())     # 'Python IS fun'
    show("title apostrophe trap", "they're ready".title())  # "They'Re Ready"
    show("German sharp-s lower", "Stra\u00dfe".lower())    # 'stra\u00dfe'
    show("German sharp-s casefold", "Stra\u00dfe".casefold()) # 'strasse'
    show("caseless match", "Stra\u00dfe".casefold() == "STRASSE".casefold())
    show("original", text)


def demo_strip_and_affixes():
    """strip(chars) characters ka set hai; exact prefix/suffix nahi."""
    section(9, "strip / lstrip / rstrip / removeprefix / removesuffix")

    text = "  hello  "
    show("strip()", text.strip())    # 'hello'
    show("lstrip()", text.lstrip())  # 'hello  '
    show("rstrip()", text.rstrip())  # '  hello'
    show("middle spaces stay", "  a  b  ".strip())  # 'a  b'
    show("strip character set", "xyhelloyx".strip("xy"))  # 'hello'
    show("lstrip is not exact prefix", "Arthur: run".lstrip("Arthur: "))
    # 'n': 'r' and 'u' also belong to the supplied character set!
    show("exact removeprefix", "Arthur: run".removeprefix("Arthur: "))
    # 'run'
    show("exact removesuffix", "report.csv".removesuffix(".csv")) # 'report'
    show("missing prefix", "report.csv".removeprefix("data_"))


def demo_search_and_count():
    """find returns -1 on failure; index raises ValueError."""
    section(10, "find / rfind / index / rindex / count")

    text = "banana"
    show("find('an')", text.find("an"))         # 1
    show("rfind('an')", text.rfind("an"))       # 3
    show("index('an')", text.index("an"))       # 1
    show("rindex('an')", text.rindex("an"))     # 3
    show("find('an', 2, 5)", text.find("an", 2, 5)) # 3; absolute index
    show("find missing", text.find("z"))        # -1
    show("count('an')", text.count("an"))      # 2
    show("non-overlapping count", text.count("ana")) # 1
    show("count missing", text.count("z"))     # 0
    show("count empty substring", "abc".count("")) # 4; boundaries

    position = text.find("b")
    if position != -1:
        show("correct find check", position)  # 0 is a VALID position
    # if text.find('b'): galat test; 0 falsy aur -1 truthy hai.


def demo_prefix_suffix_checks():
    """startswith/endswith boolean dete hain, text remove nahi karte."""
    section(11, "startswith / endswith")

    filename = "notes.py"
    show("startswith('notes')", filename.startswith("notes")) # True
    show("endswith('.py')", filename.endswith(".py"))         # True
    show("multiple possible suffixes", filename.endswith((".py", ".md")))
    show("bounded prefix check", "abcXYZ".startswith("XYZ", 3, 6)) # True
    show("case sensitive", filename.endswith(".PY"))          # False


def demo_replace():
    """Literal substring replacement; count limit positional rakha hai (3.12)."""
    section(12, "replace(old, new, count)")

    text = "red red red"
    show("replace all", text.replace("red", "blue"))  # 'blue blue blue'
    show("replace first two", text.replace("red", "blue", 2)) # 'blue blue red'
    show("delete matching text", "a-b-c".replace("-", ""))    # 'abc'
    show("no match", text.replace("green", "blue"))
    show("original", text)                              # 'red red red'
    # replace regex nahi hai. '.' literal dot ko match karega.


def demo_split_methods():
    """split/rsplit return list[str]; whitespace aur explicit separator alag hain."""
    section(13, "split / rsplit / splitlines")

    show("split whitespace", "  a   b\tc  ".split())   # ['a', 'b', 'c']
    show("split exact space", " a  b ".split(" "))   # ['', 'a', '', 'b', '']
    show("split comma", "a,,b,".split(","))          # ['a', '', 'b', '']
    show("split maxsplit=1", "a,b,c".split(",", 1))   # ['a', 'b,c']
    show("rsplit maxsplit=1", "a,b,c".rsplit(",", 1)) # ['a,b', 'c']
    show("empty default split", "".split())          # []
    show("empty explicit split", "".split(","))     # ['']
    show("splitlines", "a\r\nb\nc\n".splitlines())     # ['a', 'b', 'c']
    show("keep line endings", "a\nb\n".splitlines(keepends=True))
    # ['a\n', 'b\n']; trailing newline extra empty line nahi banata.


def demo_join_and_partition():
    """join combines strings; partition splits once into exactly three pieces."""
    section(14, "join / partition / rpartition")

    words = ["learn", "by", "doing"]
    show("space join", " ".join(words))       # 'learn by doing'
    show("hyphen join", "-".join(words))      # 'learn-by-doing'
    show("join characters", "-".join("cat")) # 'c-a-t'
    show("join converted numbers", ",".join(str(n) for n in [1, 2, 3]))
    # '1,2,3'; join ke items strings hone chahiye.

    show("partition first =", "a=b=c".partition("="))   # ('a', '=', 'b=c')
    show("rpartition last =", "a=b=c".rpartition("="))  # ('a=b', '=', 'c')
    show("partition missing", "abc".partition("="))    # ('abc', '', '')
    show("rpartition missing", "abc".rpartition("="))   # ('', '', 'abc')

    key, separator, value = "theme=dark".partition("=")
    if separator:
        show("unpacked key", key)      # 'theme'
        show("unpacked value", value)  # 'dark'


def demo_alignment():
    """Width minimum hai; chhota width text truncate nahi karta."""
    section(15, "center / ljust / rjust / zfill / expandtabs")

    show("center(6, '-')", "hi".center(6, "-")) # '--hi--'
    show("ljust(5, '.')", "hi".ljust(5, "."))  # 'hi...'
    show("rjust(5, '.')", "hi".rjust(5, "."))  # '...hi'
    show("width smaller than text", "hello".center(2)) # 'hello'
    show("zfill(5)", "42".zfill(5))             # '00042'
    show("zfill respects sign", "-42".zfill(5)) # '-0042'
    show("rjust zero is different", "-42".rjust(5, "0")) # '00-42'
    show("tabs to next tab stop", "a\tb".expandtabs(4))   # 'a   b'
    show("different starting column", "ab\tc".expandtabs(4)) # 'ab  c'


def demo_character_checks():
    """is... methods boolean dete hain; actual data convert nahi karte."""
    section(16, "All 12 character / identifier checks")

    show("'Python'.isalpha()", "Python".isalpha())    # True
    show("'Python3'.isalnum()", "Python3".isalnum())  # True
    show("'123'.isdecimal()", "123".isdecimal())    # True
    show("superscript isdigit", "\u00b2".isdigit())  # True
    show("superscript isdecimal", "\u00b2".isdecimal()) # False
    show("fraction isnumeric", "\u00bd".isnumeric()) # True
    show("fraction isdigit", "\u00bd".isdigit())     # False
    show("'-12'.isdigit()", "-12".isdigit())        # False
    show("'3.5'.isnumeric()", "3.5".isnumeric())     # False
    show("whitespace only", " \t\n".isspace())      # True
    show("lowercase check", "abc123".islower())     # True
    show("uppercase check", "ABC123".isupper())     # True
    show("titlecase check", "Hello World".istitle()) # True
    show("no cased letters", "123".islower())        # False
    show("printable", "hello world".isprintable())   # True
    show("newline not printable", "hello\n".isprintable()) # False
    show("ASCII check", "abc123".isascii())          # True
    show("non-ASCII check", "caf\u00e9".isascii())    # False
    show("identifier syntax", "user_name2".isidentifier()) # True
    show("keyword syntax still valid", "class".isidentifier()) # True
    show("keyword check separately", keyword.iskeyword("class")) # True

    # Most checks need at least one qualifying character.
    # isascii and isprintable are True for the empty string.
    show("empty isalpha", "".isalpha())         # False
    show("empty isascii", "".isascii())         # True
    show("empty isprintable", "".isprintable()) # True


def demo_formatting():
    """f-string, format, format_map aur old %-style ko compare karo."""
    section(17, "Formatting aur placeholders")

    name = "Aman"
    marks = 87.456

    show("f-string", f"{name}: {marks:.2f}")  # 'Aman: 87.46'
    show("expression inside braces", f"Next year: {20 + 1}")
    show("alignment", f"|{name:<8}|{42:04d}|") # '|Aman    |0042|'
    show("literal braces", f"{{score}} = {marks:.1f}")
    show("format positional", "{} scored {:.1f}".format(name, marks))
    show("format named", "{person}: {score}".format(person=name, score=90))

    data = {"name": "Neha", "city": "Delhi"}
    show("format_map dictionary", "{name} lives in {city}".format_map(data))
    show("old %-style", "%s scored %.1f" % (name, marks))
    # f-strings language syntax hain; format/format_map str methods hain.


def demo_translation():
    """maketrans table banata hai; translate us table ko characters par apply."""
    section(18, "maketrans / translate")

    table = str.maketrans("ae", "@3", "!")
    show("replace chars + delete !", "Please!".translate(table)) # 'Pl3@s3'
    # First two strings equal length: a -> @, e -> 3. Third string deletes.

    table = str.maketrans({"@": " at ", "!": None})
    show("dict mapping", "hi@home!".translate(table)) # 'hi at home'
    # Mapping values: string, Unicode ordinal, ya None (delete).
    # translate per code point hai; full substring replace ke liye replace().


def demo_unicode_and_encoding():
    """str Unicode text; encode -> bytes, bytes.decode -> str."""
    section(19, "Unicode, encode, decode aur visible-character trap")

    text = "caf\u00e9"
    payload = text.encode("utf-8")
    show("text", text)                 # 'caf\xe9' representation
    show("Unicode code points", len(text))  # 4
    show("UTF-8 bytes", payload)        # b'caf\xc3\xa9'
    show("byte count", len(payload))    # 5
    show("decoded text", payload.decode("utf-8")) # 'caf\xe9'
    show("ord('A')", ord("A"))         # 65
    show("chr(65)", chr(65))            # 'A'

    composed = "\u00e9"
    decomposed = "e\u0301"
    show("composed length", len(composed))       # 1
    show("decomposed length", len(decomposed))   # 2
    show("raw equality", composed == decomposed) # False
    show("NFC normalized equality", composed == unicodedata.normalize("NFC", decomposed))
    # True. Screen par same dikhne ka matlab same code points nahi.
    # String reverse [::-1] code points reverse karta hai, grapheme clusters nahi.


# ===========================================================================
# PART C — MISTAKES, REAL PRACTICE, RUNNER
# ===========================================================================

def demo_common_errors():
    """Expected errors ko catch kiya hai, taaki notebook aage bhi chale."""
    section(20, "Common mistakes aur unka reason")

    text = "cat"

    try:
        text[0] = "b"
    except TypeError:
        show("item assignment", "TypeError: str immutable hai")

    try:
        del text[0]
    except TypeError:
        show("item deletion", "TypeError: slice se result banao")

    try:
        text.append("s")
    except AttributeError:
        show("append", "AttributeError: str par append nahi hai")

    try:
        show("invalid index", text[99])
    except IndexError:
        show("invalid index", "IndexError: position bahar hai")

    try:
        show("missing index", text.index("z"))
    except ValueError:
        show("missing substring", "ValueError: index ko match nahi mila")

    try:
        show("mixed concatenation", "age=" + 21)
    except TypeError:
        show("str + int", "TypeError: str(21) ya f-string use karo")

    try:
        show("join non-strings", ",".join([1, 2]))
    except TypeError:
        show("join integers", "TypeError: pehle items ko str mein convert karo")

    try:
        show("empty separator", text.split(""))
    except ValueError:
        show("split empty separator", "ValueError: characters chahiye to list(text)")

    try:
        show("zero slice step", text[::0])
    except ValueError:
        show("slice step zero", "ValueError: step nonzero chahiye")

    try:
        show("ASCII encoding", "caf\u00e9".encode("ascii"))
    except UnicodeEncodeError:
        show("unsupported encoding", "UnicodeEncodeError: ASCII mein e-acute nahi")

    try:
        show("ASCII decoding", b"\xff".decode("ascii"))
    except UnicodeDecodeError:
        show("invalid bytes", "UnicodeDecodeError: codec aur bytes match nahi")

    try:
        show("missing format key", "{name}".format_map({}))
    except KeyError:
        show("missing placeholder", "KeyError: mapping mein name key nahi")


def demo_practice():
    """Chhote real examples: input -> operation -> readable result."""
    section(21, "Practice: cleanup, filename, palindrome aur receipt")

    # 1. Whitespace clean karo, phir case normalize karo.
    raw_name = "  nEHA   sHARMA  "
    clean_name = " ".join(raw_name.split()).title()
    show("clean name", clean_name)  # 'Neha Sharma'
    # title() yahan practice ke liye hai; har real name par blindly mat lagao.

    # 2. Last dot se extension separate karo.
    filename = "report.final.csv"
    stem, dot, extension = filename.rpartition(".")
    if dot:
        show("filename stem", stem)     # 'report.final'
        show("extension", extension)    # 'csv'
    # Ye string exercise hai; real filesystem paths ke liye pathlib useful hai.

    # 3. Simple ASCII palindrome: spaces/case ignore.
    phrase = "Never odd or even"
    normalized = "".join(phrase.split()).casefold()
    show("palindrome?", normalized == normalized[::-1])  # True

    # 4. Bahut saare parts build karne ke liye list + join.
    lines = []
    for product, quantity in [("Pen", 2), ("Book", 1)]:
        lines.append(f"{product:<6} x {quantity}")
    receipt = "\n".join(lines)
    show("receipt", receipt)  # 'Pen    x 2\nBook   x 1'


def main():
    """Reading order: foundation -> methods -> mistakes -> practice."""
    demo_creation()
    demo_escape_and_multiline()
    demo_indexing()
    demo_slicing()
    demo_immutability()
    demo_add_update_delete()
    demo_operators_and_loops()

    demo_case_methods()
    demo_strip_and_affixes()
    demo_search_and_count()
    demo_prefix_suffix_checks()
    demo_replace()
    demo_split_methods()
    demo_join_and_partition()
    demo_alignment()
    demo_character_checks()
    demo_formatting()
    demo_translation()
    demo_unicode_and_encoding()

    demo_common_errors()
    demo_practice()


if __name__ == "__main__":
    main()
