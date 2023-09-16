"""
-> Interaction between class objects

While inheritance represents a relationship between classes, there are situations
where there are relationships between objects.

Now we have to use different class objects to create the design of an application.
This means that independent class objects will have to find a way to interact
with each other.

-> Relationships between classes#
There are three main class relationships we need to know:

1.- IS A
2.- Part-of
3.- Has-a

-> Part-of
In this relationship, one class object is a component of another class object.
Given two classes, class A and class B, they are in a part-of relation if a
class A object is a part of class B object, or vice-versa.

An instance of the component class can only be created inside the main class.
In the example to the right, class B and class C have their own implementations,
but their objects are only created once a class A object is created. Hence,
part-of is a dependent relationship.

-> Has-a
This is a slightly less concrete relationship between two classes. Class A and
class B have a has-a relationship if one or both need the other’s object to
perform an operation, but both class objects can exist independently of each
other.

This implies that a class has a reference to an object of the other class but
does not decide the lifetime of the other class’s referenced object.

-> Association
In object-oriented programming, association is the common term for both the
has-a and part-of relationships but is not limited to these. Two objects are in
an association relationship is a generic statement, which means that we don’t
worry about the lifetime dependency between the objects.
"""
