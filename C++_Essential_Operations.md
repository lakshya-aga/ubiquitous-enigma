Literals with user-defined suffixes are called user-defined literals or UDLs. Such literals are defined using literal operators. A literal operator converts a literal of its argument type, followed by a subscript, into its return type.
constexpr complex<double> operator""i(long double arg)   // imaginary literal
{
    return {0,arg};
}
The begin() and end() can also be defined as free-standing functions; see §7.2.
The begin() and end() can also be defined as free-standing functions; see §7.2. The versions of begin() and end() for const containers are called cbegin() and cend().
This iterator model (§13.3) allows for great generality and efficiency
Iterators are used to pass sequences to standard-library algorithms. For example:
Here, c.begin() is an iterator pointing to the first element of c and c.end() points one-beyond-the-last element of c.
However, rather than traversing containers using indices from 0 to size(), the standard algorithms (Chapter 13) rely on the notion of sequences delimited by pairs of iterators
size_t is the name of the type returned by a standard-library size()
The standard-library containers all know their number of elements and we can obtain it by calling size()
In particular, make the container resource safe by implementing it as a handle with appropriate essential operations (§6.1.1, §6.2).
Unless there is a really good reason not to, design containers in the style of the standard-library containers
Older code does not use <=>.
auto operator<=>(const R2& a) const { return a.m == m ? 0 : a.m < m ? -1 : 1; }
auto operator<=>(const R& a) const = default;
Like C’s strcmp(), <=> implements a three-way-comparison. A negative return value means less-than, 0 means equal, and a positive value means greater-than
The “spaceship operator,” <=> is a law onto itself; its rules differ from those for all other operators. In particular, by defining the default <=> the other relational operators are implicitly defined:
The meaning of the equality comparisons (== and !=) is closely related to copying. After a copy, the copies should compare equal:
Input and output operations: >> and << (§6.5.4)

swap() (§6.5.5)

Hash functions: hash<> (§6.5.6)
Function objects: () (§7.3.2)
Iterators and “smart pointers”: ->, *, [], ++, --, +, -, +=, and -= (§13.3, §15.2.1)
Comparisons: ==, !=, <, <=, >, >=, and <=> (§6.5.1)

Container operations: size(), begin(), and end()
Shift: >> and <<
We can define operators for user-defined types (classes and enumerations):

Binary arithmetic operators: +, -, *, /, and %

Binary logical operators: & (bitwise and), | (bitwise or), and ^ (bitwise exclusive or)

Binary relational operators: ==, !=, <, <=, >, >=, and <=>

Logical operators: && and ||

Unary arithmetic and logical operators: +, -, ~ (bitwise complement), and ! (logical negation)

Assignments: =, +=, *=, etc.

Increments and decrements: ++ and --

Pointer operations: ->, unary *, and unary &

Application (call): ()

Subscripting: []

Comma: ,
Resources can be moved from scope to scope using move semantics or “smart pointers,” and shared ownership can be represented by “shared pointers” (§15.2.1).
Before resorting to garbage collection, systematically use resource handles: let each resource have an owner in some scope and by default be released at the end of its owner’s scope. In C++, this is known as RAII (Resource Acquisition Is Initialization) and is integrated with error handling in the form of exceptions
Garbage collection is fundamentally a global memory management scheme. Clever implementations can compensate, but as systems are getting more distributed (think caches, multicores, and clusters), locality is more important than ever.
In C++, you can plug in a garbage collector.
By defining constructors, copy operations, move operations, and a destructor, a programmer can provide complete control of the lifetime of a contained resource 
move constructors are not invoked as often as you might imagine
programmer can be specific:

Click here to view code image

Vector f()
{
    Vector x(1000);
    Vector y(2000);
    Vector z(3000);
    z = x;             // we get a copy (x might be used later in f())
    y = std::move(x);  // we get a move (move assignment)
    // ... better not use x here ...
    return z;          // we get a move
}
After a move, the moved-from object should be in a state that allows a destructor to be run. Typically, we also allow assignment to a moved-from object. The standard-library algorithms (Chapter 13) assume that. Our Vector does that.
move operation is applied when an rvalue reference is used as an initializer or as the right-hand side of an assignment.
an rvalue reference is a reference to something that nobody else can assign to, so we can safely “steal” its value.
So an rvalue is – to a first approximation – a value that you can’t assign to, such as an integer returned by a function call.
The && means “rvalue reference” and is a reference to which we can bind an rvalue
We didn’t really want a copy; we just wanted to get the result out of a function: we wanted to move a Vector rather than copy it. Fortunately, we can state that intent
class Vector {
     // ...

     Vector(const Vector& a);               // copy constructor
     Vector& operator=(const Vector& a);    // copy assignment

     Vector(Vector&& a);                    // move constructor
     Vector& operator=(Vector&& a);         // move assignment
};
Given that definition, the compiler will choose the move constructor to implement the transfer of the return value out of the function. This means that r=x+y+z will involve no copying of Vectors. Instead, Vectors are just moved.
We can control copying by defining a copy constructor and a copy assignment, but copying can be costly for large containers. We avoid the cost of copying when we pass objects to a function by using references, but we can’t return a reference to a local object as the result (the local object would be destroyed by the time the caller got a chance to look at it)
A suitable definition of a copy constructor for Vector allocates the space for the required number of elements and then copies the elements into it so that after a copy each Vector has its own copy of the elements:

Click here to view code image

Vector::Vector(const Vector& a)     // copy constructor
     :elem{new double[a.sz]},       // allocate space for elements
     sz{a.sz}
{
     for (int i=0; i!=sz; ++i)      // copy elements
           elem[i] = a.elem[i];
}
Copying of an object of a class is defined by two members: a copy constructor and a copy assignment:
Fortunately, the fact that Vector has a destructor is a strong hint that the default (memberwise) copy semantics is wrong and the compiler should at least warn against this example. We need to define better copy semantics.
When we design a class, we must always consider if and how an object might be copied. For simple concrete types, memberwise copy is often exactly the right semantics for copy. For some sophisticated concrete types, such as Vector, memberwise copy is not the right semantics for copy; for abstract types it almost never is.
The default meaning of copy is memberwise copy: copy each member. For example, using complex from §5.2.1:
This is typically considered unfortunate, and the standard-library vector does not allow this int-to-vector “conversion.”

The way to avoid this problem is to say that only explicit “conversion” is allowed; that is, we can define the constructor like this:

Click here to view code image

class Vector {
public:
     explicit Vector(int s);    // no implicit conversion from int to Vector
     // ...
};
To complement =default, we have =delete to indicate that an operation is not to be generated. A base class in a class hierarchy is the classic example where we don’t want to allow a memberwise copy. For example:

Click here to view code image

class Shape {
public:
     Shape(const Shape&) =delete;             // no copying
     Shape& operator=(const Shape&) =delete;
     // ...
};

void copy(Shape& s1, const Shape& s2)
{
     s1 = s2;  // error: Shape copy is deleted
}
good rule of thumb (sometimes called the rule of zero) is to either define all of the essential operations or none (using the default for all
Here, the compiler will synthesize memberwise default construction, copy, move, and destructor as needed, and all with the correct semantics.
When a class is a resource handle – that is, when the class is responsible for an object accessed through a pointer – the default memberwise copy is typically a disaster
The reason is that a pointer may point to something that the class needs to delete, in which case the default memberwise copy would be wrong.
you are explicit about some defaults, other default definitions will not be generated
If you want to be explicit about generating default implementations, you can:

Click here to view code image

class Y {
public:
     Y(Sometype);
     Y(const Y&) = default;    // I really do want the default copy constructor
     Y(Y&&) = default;         // and the default move constructor
     // ...
};
a copy or move constructor invocation is often optimized away by constructing the object used to initialize right in the target object.
There are five situations in which an object can be copied or moved:

As the source of an assignment

As an object initializer

As a function argument

As a function return value

As an exception
We must define them as a matched set or suffer logical or performance problems
Constructors, destructors, and copy and move operations for a type are not logically separate.
