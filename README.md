# Python Object-Oriented Programming

My learning journey through Python OOP, from classes and objects to practical design and production practices. This repository is a work in progress, with explanations in English and Hindi written in Roman script.
### Connect with me
[GitHub](https://github.com/udyalakvivek)
## Current lessons

| Lesson | File | Concepts |
| --- | --- | --- |
| 01 | [Classes and objects](class-object/01_class_and_object.py) | Classes, instances, object identity, a `Car` constructor and instance method |
| 02 | [Attributes](class-object/02_attributes.py) | `__init__`, instance attributes, object state |
| 03 | [Instance methods](class-object/03_instance_methods.py) | Reading and changing state, manually assigned attributes |
| 04 | [Credit card](class-object/04_credit.py) | A practical class, `__str__`, `__repr__` |
| 05 | [Student course management](class-object/05_Student.py) | Default arguments, per-instance course lists, duplicate-course checks, `__str__`, `__repr__` |
| 06 | [Encapsulation](class-object/06_encapsulation.py) | Bank-account balance access and deposit validation, name-mangled `__model`, car getter and setter methods, inherited methods |
| 07 | [Polymorphism](class-object/07_polymorphism.py) | Overriding `fuel_type()` in `Electric_car`, a shared instance counter, flexible multiplication arguments, animal method overriding |
| 08 | [Static methods](class-object/08_static_method.py) | `@staticmethod`, calling `general_des()` through a class or instance without `self` or `cls` |
| 09 | [Class methods and properties](class-object/09_class_method.py) | Class counters, `@classmethod`, resetting shared state with `cls`, a read-only `@property` |
| 10 | [Constructors](class-object/10_Constructors%20.py) | Object creation with `__new__`, initialization with `__init__`, returning `None` or an instance of another class |

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

[Lesson 07](class-object/07_polymorphism.py) demonstrates a shared method name with different behavior: `Car` and `Electric_car` implement `fuel_type()`, while `Dog`, `Cat`, and `Animal` implement `sound()`. Calling `sound()` in a loop prints `Bark`, `Meow`, and `Some generic sound` according to the object's class.

The `Calculator.multiply(a=1, b=1, *args)` example accepts different numbers of arguments. Its four calls return `1`, `4`, `6`, and `24`. Although the lesson's comment calls this compile-time polymorphism, Python uses one method with default and variable-length arguments here to mimic overloading; it does not select among separate method definitions by argument signature.

## Object creation and initialization

[Lesson 10](class-object/10_Constructors%20.py) separates the roles of `__new__` and `__init__`:

- `__new__` creates and returns an object; `__init__` initializes it when the returned object is an instance of the requested class.
- If `__new__` returns `None`, initialization is skipped. One example returns `None` implicitly, and another does so when the name is empty.
- If `Person.__new__` returns an `Animal`, `Person.__init__` is skipped and printing the result uses `Animal.__str__`.

The filename currently contains a space before `.py`, so quote its path when running it.

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

## Planned topic structure

Current lessons live in `class-object/` and `Inheritance/`. I plan to organize the examples into four topic folders with simple, numbered folder names. The following is a proposed layout; files have not yet been moved:

```text
python-oop/
|-- README.md
|-- .gitignore
|-- 01_classes_and_objects/
|   |-- 01_class_and_object.py
|   |-- 02_attributes.py
|   |-- 03_instance_methods.py
|   |-- 04_credit_card.py
|   |-- 05_Student.py
|   |-- 06_encapsulation.py
|   |-- 07_polymorphism.py
|   |-- 08_static_method.py
|   |-- 09_class_method.py
|   `-- 10_Constructors .py
|-- 02_dunder_methods/
|-- 03_inheritance/
`-- 04_association_and_encapsulation/
```

The credit-card lesson includes basic string dunder methods but will stay with the introductory class examples. Later dunder lessons will cover operator overloading. Future folders will be added when their first lessons are ready; Git does not track empty folders.

## Learning roadmap

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
- [ ] Handle the deliberate read-only property assignment so lesson 09 runs to completion.
- [ ] Handle the deliberate missing-attribute error so lesson 03 runs to completion.
- [ ] Correct the lesson 02 comment: the updated dictionary contains `Vivek Kumar`, `26`, and `MCA`.
- [ ] Validate credit-card charges and payments, enforce the limit, and define overpayment behavior.
- [ ] Study operator overloading.
- [ ] Study abstract classes and explore method resolution order with overlapping methods and cooperative `super()` calls.
- [ ] Study composition and aggregation.
- [ ] Build a small project using type hints, clear exceptions, and separated demonstration code.
- [ ] Add tests for valid inputs, invalid inputs, and boundary cases; introduce formatting and CI.

For a future money-handling project, use integer minor units or `decimal.Decimal` rather than floating-point balances. Keep all card numbers in examples fictional.

## First push to GitHub

Create an empty repository named `python-oop` in your own GitHub account. Do not initialize it on GitHub with a README, `.gitignore`, or license because this folder already contains the first two files.

In PowerShell, run:

```powershell
Set-Location X:\Python-Opps
git init -b main
git add .
git status
git diff --cached
git commit -m "Add initial Python OOP lessons and documentation"
git remote add origin https://github.com/YOUR_USERNAME/python-oop.git
git remote -v
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username. Review the staged files before committing. If Git requests your identity, set it for this repository and retry the commit:

```powershell
git config user.name "Your Name"
git config user.email "Your GitHub verified or noreply email"
```

Complete GitHub authentication if prompted during the push. The reference repository uses `master`; this project can use `main` with the same folder structure.

For later lessons:

```powershell
git add .
git diff --cached
git commit -m "Add lesson on inheritance"
git push
```

See [GitHub's official guide for pushing local code](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github).
