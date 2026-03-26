const_cast for “casting away const.”
reinterpret_cast and bit_cast (§16.7) for treating an object as simply a sequence of bytes
reinterpret_cast and bit_cast
Unfortunately, the standard-library uses unsigned integers for sizes and subscripts, so we need to use the ugly static_cast to explicitly convert the size of the initializer list to an int. This is pedantic because the chance that the number of elements in a handwritten list is larger than the largest integer (32,767 for 16-bit integers and 2,147,483,647 for 32-bit integers) is rather low
A static_cast does not check the value it is converting; the programmer is trusted to use it correctly.
Note that the member destructor (~Vector()) is implicitly invoked by its class’s destructor (~Vector_container()).
The destructor (~Vector_container()) overrides the base class destructor (~Container()).
Operations similar to dynamic_cast are known as “is kind of” and “is instance of” operations
when we pass an object to some system that accepts an interface specified by a base class
If we can avoid testing type information at run time, we can write simpler and more efficient code, but occasionally type information is lost and must be recovered
Code is cleaner when dynamic_cast is used with restraint.
A leak is the conventional term for the what happens when we acquire a resource and fail to release it. Leaking resources must be avoided because a leak makes the leaked resource unavailable to the system
The curious =0 syntax says the function is pure virtual; that is, some class derived from Container must define the function. Thus, it is not possible to define an object that is just a Container.
Initializer-list constructor: Initialize with a list of elements.

push_back(): Add a new element at the end of (at the back of) the sequence.
allows us to eliminate “naked new operations,” that is, to avoid allocations in general code and keep them buried inside the implementation of well-behaved abstractions.
The technique of acquiring resources in a constructor and releasing them in a destructor, known as Resource Acquisition Is Initialization or RAII
The destructor cleans up by freeing that memory using the delete[] operator. Plain delete deletes an individual object; delete[] deletes an array.
Vector’s constructor allocates some memory on the free store (also called the heap or dynamic memory) using the new operator.
~
~
The name of a destructor is the complement operator, ~, followed by the name of the class; it is the complement of a constructor.
A container is an object holding a collection of elements
void f(complex z)
{
     complex a {2.3};      // construct {2.3,0.0} from 2.3
     complex b {1/a};
     complex c {a+z*complex{1,2.3}};
     if (c != b)
            c = -(b/a)+2*b;
}
The compiler converts operators involving complex numbers into appropriate function calls. For example, c!=b means operator!=(c,b) and 1/a means operator/(complex{1},a).
User-defined operators (“overloaded operators”) should be used cautiously and conventionally (§6.4).
but a non-const member function can only be invoked for non-const objects
A const member function can be invoked for both const and non-const objects
By defining a default constructor you eliminate the possibility of uninitialized variables of that type.
In addition, the standard-library complex has the functions shown here declared constexpr so that we can do complex arithmetic at compile time.
In addition, the standard-library complex has the functions shown here declared constexpr so that we can do complex arithmetic at compile time.
It is possible to explicitly request inlining by preceding a function declaration with the keyword inline.
Functions defined in a class are inlined by default
Here, we consider the basic support for three important kinds of classes:

Concrete classes (§5.2)

Abstract classes (§5.3)

Classes in class hierarchies (§5.5)
Chapter 8 gives an overview of the concepts, techniques, and language features that underlie generic programming. 
introduces templates as a mechanism for parameterizing types and algorithms with other types and algorithms. Computations on user-defined and built-in types are represented as functions, sometimes generalized to function templates and function objects
That allows implementations to be optimally efficient in time and space. In particular, it allows us to

Place objects of concrete types on the stack, in statically allocated memory, and in other objects (§1.5).
Refer to objects directly (and not just through pointers or references).
Initialize objects immediately and completely (e.g., using constructors; §2.3).
Copy and move objects (§6.2).
Place objects of concrete types on the stack, in statically allocated memory, and in other objects (§1.5).
For example, a complex number type and an infinite-precision integer are much like a built-in int,
The basic idea of concrete classes is that they behave “just like built-in types.”
In particular, it presents the basic properties, implementation techniques, and language facilities used for concrete classes, abstract classes, and class hierarchies.
Chapter 6 presents the operations that have defined meaning in C++, such as constructors, destructors, and assignments. It outlines the rules for using those in combination to control the life cycle of objects and to support simple, efficient, and complete resource management.
Variadic templates are introduced for specifying the most general and most flexible interfaces.
