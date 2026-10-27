# Python Fundamentals and Object-Oriented Programming

My Python learning notebook: lists, strings, classes, objects, and inheritance. The examples include comments, expected outputs, and explanations in English and Hindi written in Roman script. Each topic is meant to be read, run, and changed while practicing.
### Connect with me
[GitHub](https://github.com/udyalakvivek)
## List and string notebooks

Start with the Markdown notes for explanations, then run the matching Python file to follow the examples.

| Topic | Notes | Runnable examples | What is covered |
| --- | --- | --- | --- |
| Lists | [List notebook](List/List.md) | [Basics.py](List/Basics.py) | All 11 public list methods; add, update, and delete at the start, end, or any position; indexing, slicing, shallow/deep copying, nested lists, common mistakes, and time complexity |
| Strings | [String notebook](String/String.md) | [basics.py](String/basics.py) | All 47 public string methods in Python 3.12; quotes, escapes, indexing, slicing, immutability, text editing, formatting, Unicode, encoding, and practice exercises |

The list file has 20 sequential sections. The string file has 21 separate topic functions, grouped into foundations, methods, and practice. Each string topic can also run independently. Both notebooks explain what happens behind the scenes and include deliberately caught errors so the examples can finish running.

```powershell
python List/Basics.py
python String/basics.py

# Run just one string topic from the repository root:
python -c "from String.basics import demo_slicing; demo_slicing()"
```

The string examples display values with quotes and escaped whitespace, making spaces, tabs, and newlines easier to inspect. The notes include the reference links used for the topic outline and technical details.

## Classes and objects

| Lesson | File | Concepts |
| --- | --- | --- |
| 01 | [Classes and objects](class-object/01_class_and_object.py) | Classes, instances, object identity, a `Car` constructor and instance method |
| 02 | [Attributes](class-object/02_attributes.py) | `__init__`, instance attributes, object state |
| 03 | [Instance methods](class-object/03_instance_methods.py) | Reading and changing state, manually assigned attributes |
| 04 | [Credit card](class-object/04_credit.py) | A practical class, `__str__`, `__repr__` |
| 05 | [Student course management](class-object/05_Student.py) | Default arguments, per-instance course lists, duplicate-course checks, `__str__`, `__repr__` |
| 06 | [Encapsulation](class-object/06_encapsulation.py) | Bank-account balance access and deposit validation, name-mangled `__model`, car getter and setter methods, inherited methods |
| 07 | [Polymorphism](class-object/07_polymorphism.py) | Payment-system analogy, overriding `fuel_type()` in `Electric_car`, a shared instance counter, flexible multiplication arguments, animal method overriding |
| 08 | [Static methods](class-object/08_static_method.py) | `@staticmethod`, calling `general_des()` through a class or instance without `self` or `cls` |
| 09 | [Class methods and properties](class-object/09_class_method.py) | Class counters, `@classmethod`, resetting shared state with `cls`, a read-only `@property` |
| 10 | [Constructors](class-object/10_Constructors%20.py) | Object creation with `__new__`, initialization with `__init__`, returning `None` or an instance of another class |
| 11 | [Abstraction](class-object/11_Abstraction.py) | Abstract base classes with `ABC` and `@abstractmethod`, requiring payment subclasses to implement `pay()` |

### Inheritance lessons

| Lesson | File | Concepts |
| --- | --- | --- |
| 01 | [Inheritance basics](Inheritance/01_base.py) | Employee/developer and car/electric-car examples, `super()`, constructor extension, method overriding, inherited methods |
| 02 | [Single inheritance](Inheritance/02_single.py) | Notification channel and SMS subclass, inherited state, public/protected/private attribute conventions |
| 03 | [Multilevel inheritance](Inheritance/03_multilevel.py) | Three-level class hierarchy, chained constructors, promotional SMS example |
| 04 | [Hierarchical inheritance](Inheritance/04_hierarchical_inheritance.py) | SMS and email subclasses sharing a parent, subclass-specific attributes and methods |
| 05 | [Multiple inheritance](Inheritance/05_multiple_inheritance.py) | Combining email delivery and audit logging, explicit initialization of both parent classes, inheriting from `Car`, `Battery`, and `Engine` |

The notification examples print or return simulated messages; they do not contact SMS or email services. In Python, a single leading underscore marks an internal-use convention, while double leading underscores trigger name mangling rather than enforcing access restrictions. The encapsulation lesson demonstrates a `BankAccount`, followed by a `Car` with a getter and setter and an `Electric_car` subclass. Its `get_model()` method appends `!` to the stored model name.

These are learning examples, not production-ready implementations. Lesson 03 deliberately accesses an attribute before assigning it and currently stops with `AttributeError`. Lesson 04 does not yet enforce its credit limit. Lesson 09 demonstrates a read-only `model` property: assigning `res.model = "Safari"` raises `AttributeError` because no setter is defined, so the subsequent print statements do not run.

## Run a lesson

Install Python 3.12 or later. No third-party packages are required for the current examples.

From the repository root:

```powershell
python class-object/01_class_and_object.py
python class-object/02_attributes.py
python class-object/03_instance_methods.py
python class-object/04_credit.py
python class-object/05_Student.py
python class-object/06_encapsulation.py
python class-object/07_polymorphism.py
python class-object/08_static_method.py
python class-object/09_class_method.py
python "class-object/10_Constructors .py"
python -X utf8 class-object/11_Abstraction.py
python Inheritance/01_base.py
python Inheritance/02_single.py
python Inheritance/03_multilevel.py
python Inheritance/04_hierarchical_inheritance.py
python Inheritance/05_multiple_inheritance.py
```

Run each command separately. The errors in lessons 03 and 09 are examples to study; the remaining code in each file will run only after handling or moving the failing access or assignment. Lesson 08 prints the same general car description twice, once through an instance and once through the class.

## Instance, static, and class methods

| Method type | First parameter | Use in these lessons |
| --- | --- | --- |
| Instance method | `self` | Read an individual car's brand and model with `full_name()` |
| Static method | No automatic first parameter | Return a general description with `Car.general_des()` |
| Class method | `cls` | Reset the class counter with `Car.reset_count()` |

A property exposes a method through attribute-style access. In lesson 09, `res.model` reads the private model value through its getter. Updating that property requires a setter; `@property` alone does not make every attribute on the object read-only.

## Polymorphism

The lesson introduces polymorphism with an online-payment analogy: credit cards, UPI, wallets, and net banking can expose the same `processPayment()` method while each payment type supplies its own behavior. This is a conceptual example in the lesson notes; the executable examples use cars, a calculator, and animals.

[Lesson 07](class-object/07_polymorphism.py) demonstrates a shared method name with different behavior: `Car` and `Electric_car` implement `fuel_type()`, while `Dog`, `Cat`, and `Animal` implement `sound()`. Calling `sound()` in a loop prints `Bark`, `Meow`, and `Some generic sound` according to the object's class.

The `Calculator.multiply(a=1, b=1, *args)` example accepts different numbers of arguments. Its four calls return `1`, `4`, `6`, and `24`. Although the lesson's comment calls this compile-time polymorphism, Python uses one method with default and variable-length arguments here to mimic overloading; it does not select among separate method definitions by argument signature.

## Object creation and initialization

[Lesson 10](class-object/10_Constructors%20.py) separates the roles of `__new__` and `__init__`:

- `__new__` creates and returns an object; `__init__` initializes it when the returned object is an instance of the requested class.
- If `__new__` returns `None`, initialization is skipped. One example returns `None` implicitly, and another does so when the name is empty.
- If `Person.__new__` returns an `Animal`, `Person.__init__` is skipped and printing the result uses `Animal.__str__`.

The filename currently contains a space before `.py`, so quote its path when running it.

## Abstraction

[Lesson 11](class-object/11_Abstraction.py) first shows ordinary inheritance: `UpiPayment` and `CardPayment` inherit `Payment.pay()` and therefore use the same implementation. It then defines `Payment` as an abstract base class with `ABC` and marks `pay()` with `@abstractmethod`. Each concrete payment subclass must implement its own `pay()` method, so UPI and card payments can provide distinct behavior. The examples print simulated payment messages; they do not process real transactions.

## Multiple inheritance

[Inheritance lesson 05](Inheritance/05_multiple_inheritance.py) contains two examples:

- `SecureCorporateEmail(EmailChannel, AuditLogger)` explicitly initializes both parents, then combines simulated email delivery with an audit log.
- `ElectricCarTwo(Car, Battery, Engine)` inherits the `Car` constructor and the `battery_info()` and `engine_info()` methods. The subclass uses `pass` because it adds no behavior of its own.

In the car example, `ElectricCarTwo("Tata", "Punch")` stores the brand and model through `Car.__init__`. The two method calls print:

```text
This is Battery info!
This is engine info!
```

Python searches inherited methods using the method resolution order (MRO). For this example, the order is `ElectricCarTwo`, `Car`, `Battery`, `Engine`, then `object`. You can inspect it with `ElectricCarTwo.__mro__`.

## Repository structure

Current folders and their purpose:

```text
python-oop/
|-- README.md
|-- .gitignore
|-- List/
|   |-- List.md
|   `-- Basics.py
|-- String/
|   |-- String.md
|   `-- basics.py
|-- class-object/                 # 11 lessons: classes through abstraction
`-- Inheritance/                  # 5 lessons: basic through multiple inheritance
```

Filename casing matters on case-sensitive systems: the list example is `List/Basics.py`, while the string example is `String/basics.py`. Future topic folders will be added when their first lessons are ready.

## Learning roadmap

- [x] Add a list notebook with all 11 public methods, positional edits, copying, and behind-the-scenes explanations.
- [x] Add a string notebook with all 47 public methods, separate topic functions, Unicode, and practice exercises.
- [x] Write initial examples of classes, attributes, and instance methods.
- [x] Write a basic credit-card example with string representations.
- [x] Write a Student class with a default age, a course list, and duplicate-course checks.
- [x] Add encapsulation examples with controlled balance access and deposit validation.
- [x] Add basic, single, multilevel, hierarchical, and multiple inheritance examples, including `super()` and method overriding.
- [x] Combine `Car`, `Battery`, and `Engine` in a multiple-inheritance example with an inherited constructor and methods.
- [x] Add car examples of polymorphism, getter and setter methods, and a shared instance counter.
- [x] Add a static-method example callable through both a class and an instance.
- [x] Add a class-method example that resets a shared counter and a read-only property example.
- [x] Expand polymorphism with flexible multiplication arguments and an animal method-overriding example.
- [x] Demonstrate object creation and initialization with `__new__` and `__init__`, including skipped initialization.
- [x] Demonstrate abstraction with an abstract `Payment` base class and concrete UPI and card implementations.
- [ ] Handle the deliberate read-only property assignment so lesson 09 runs to completion.
- [ ] Handle the deliberate missing-attribute error so lesson 03 runs to completion.
- [ ] Correct the lesson 02 comment: the updated dictionary contains `Vivek Kumar`, `26`, and `MCA`.
- [ ] Validate credit-card charges and payments, enforce the limit, and define overpayment behavior.
- [ ] Study operator overloading.
- [ ] Explore method resolution order with overlapping methods and cooperative `super()` calls.
- [ ] Study composition and aggregation.
- [ ] Build a small project using type hints, clear exceptions, and separated demonstration code.
- [ ] Add tests for valid inputs, invalid inputs, and boundary cases; introduce formatting and CI.

For a future money-handling project, use integer minor units or `decimal.Decimal` rather than floating-point balances. Keep all card numbers in examples fictional.

## Saving new lessons

This repository is hosted at [udyalakvivek/python-oop](https://github.com/udyalakvivek/python-oop) on the `main` branch. After updating a lesson, run its examples and update this README if the topic list has changed. Review the staged files before committing:

```powershell
git add .
git status
git diff --cached
git commit -m "Add notes and examples for a new Python topic"
git push origin main
```

Python bytecode, virtual environments, and local credentials are excluded through `.gitignore`.
