## 1. Inheritance:
### Explanation:
- Inheritance is a fundamental concept in object-oriented programming (OOP) where a new class (subclass) is created based on an existing class (superclass). The subclass inherits attributes and methods from the superclass and can also have its own attributes and methods.

### Commentary and Analysis:
-Code (Inheritance.py): In the provided code, we have a superclass cat and two subclasses DomesticCat and WildCat.
Understanding:
- ***DomesticCat*** and WildCat inherit attributes and methods from the cat class, such as name, age, and sound.
- ***DomesticCat*** introduces an additional attribute owner, which is specific to domestic cats.
- ***WildCat*** overrides the sound method from the cat class, demonstrating polymorphism.
### Benefits:
- Promotes code reuse and modularity.
- Allows for hierarchical organization of classes.
- Facilitates polymorphism, where objects of different classes can be treated uniformly.
