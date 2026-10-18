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
| 07 | [Polymorphism](class-object/07_polymorphism.py) | Overriding `fuel_type()` in `Electric_car`, shared `Car.total_car` class variable, counting parent and child instances |
| 08 | [Static methods](class-object/08_static_method.py) | Empty placeholder; implementation planned |

### Inheritance lessons

| Lesson | File | Concepts |
| --- | --- | --- |
| 01 | [Inheritance basics](Inheritance/01_base.py) | Employee/developer and car/electric-car examples, `super()`, constructor extension, method overriding, inherited methods |
| 02 | [Single inheritance](Inheritance/02_single.py) | Notification channel and SMS subclass, inherited state, public/protected/private attribute conventions |
| 03 | [Multilevel inheritance](Inheritance/03_multilevel.py) | Three-level class hierarchy, chained constructors, promotional SMS example |
| 04 | [Hierarchical inheritance](Inheritance/04_hierarchical_inheritance.py) | SMS and email subclasses sharing a parent, subclass-specific attributes and methods |
| 05 | [Multiple inheritance](Inheritance/05_multiple_inheritance.py) | Combining email delivery and audit logging, explicit initialization of both parent classes |

The notification examples print or return simulated messages; they do not contact SMS or email services. In Python, a single leading underscore marks an internal-use convention, while double leading underscores trigger name mangling rather than enforcing access restrictions. The encapsulation lesson demonstrates a `BankAccount`, followed by a `Car` with a getter and setter and an `Electric_car` subclass. Its `get_model()` method appends `!` to the stored model name.

These are learning examples, not production-ready implementations. Lesson 03 deliberately accesses an attribute before assigning it and currently stops with `AttributeError`. Lesson 04 does not yet enforce its credit limit.

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
python Inheritance/01_base.py
python Inheritance/02_single.py
python Inheritance/03_multilevel.py
python Inheritance/04_hierarchical_inheritance.py
python Inheritance/05_multiple_inheritance.py
```

Run each command separately. The error in lesson 03 is an example to study; the remaining code in that file will run only after handling or moving that access. Lesson 08 is currently empty and produces no output.

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
|   `-- 08_static_method.py
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
- [x] Add car examples of polymorphism, getter and setter methods, and a shared instance counter.
- [ ] Implement the static-method lesson in `class-object/08_static_method.py`.
- [ ] Handle the deliberate missing-attribute error so lesson 03 runs to completion.
- [ ] Correct the lesson 02 comment: the updated dictionary contains `Vivek Kumar`, `26`, and `MCA`.
- [ ] Validate credit-card charges and payments, enforce the limit, and define overpayment behavior.
- [ ] Study operator overloading and expand the polymorphism examples.
- [ ] Study abstract classes and method resolution order.
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
