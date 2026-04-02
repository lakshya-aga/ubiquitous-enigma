This `template<Element T>` prefix is C++’s version of mathematic’s “for all T such that Element(T)”; that is, Element is a predicate that checks whether T has all the properties that a Vector requires. Such a predicate is called a concept (§8.2). A
modern program representation techniques (such as “abstract syntax trees”).
The `is_trivially_copyable_v<T>` is a type predicate
compile-time
no runtime overhead. if is not evaluated at runtime
```
template<typename T>
void update(T& target)
{
     // ...
     if constexpr(is_trivially_copyable_v<T>)
           simple_and_fast(target);      // for "plain old data"
     else
           slow_and_safe(target);        // for more complex types
     // ...
}
template<typename C>
using Value_type = C::value_type;     // the type of C's elements

template<typename Container>
void algo(Container& c)
{
     Vector<Value_type<Container>> vec;       // keep results here
     // ...
}
```


is very common for a parameterized type to provide an alias for types related to their template arguments. For example:
```
template<typename T>
class Vector {
public:
     using value_type = T;
     // ...
};
```
In fact, every standard-library container provides value_type as the name for the type of its elements
The standard library uses variable templates to provide mathematical constants, such as pi and log2e
`is_assignable<T&,T2>::value`
`static_asserts` custom checks that are used to terminate prematurely. compile time or runtime? compile time. Only where constexpr can be used
Values dependent on a type: variable templates 

Aliases for types and templates: alias templates

A compile-time selection mechanism: if constexpr 

A compile-time mechanism to inquire about properties of types and expressions: requires-expressions 
scope_exit
Core Guidelines Support Library (the GSL)
explicit
attribute [[nodiscard]] to ensure that users do not forget to copy a generated Final_action into the scope for which its action is intended
nodiscard
auto act = finally([&]{free(p);});  
when act goes out of scope
We can define a function, finally() that takes an action to be executed on the exit from the scope
generally used when destructor cannot be used like C associated programs and structs
Instead, we could convert it to a lambda used as an initializer:


```C++

void user(Init_mode m, int n, vector<int>& arg, Iterator p, Iterator q)
{
     vector<int> v = [&] {
          switch (m) {
          case zero:     return vector<int>(n); // n elements initialized to 0
          case seq:      return vector<int>{p,q}; // copy from sequence [p:q)
          case cpy:      return arg;
          }
     }();

     // ...
}
```
Such code is often messy, deemed essential “for efficiency,” and a source of bugs:

The variable could be used before it gets its intended value.

The “initialization code” could be mixed with other code, making it hard to comprehend.

When “initialization code” is mixed with other code it is easier to forget a case.

This isn’t initialization, it’s assignment (§1.9.2).
enum class Init_mode { zero, seq, cpy, patrn };    // initializer alternatives

```cpp
void user(Init_mode m, int n, vector<int>& arg, Iterator p, Iterator q)
{
     vector<int> v;

     // messy initialization code:

     switch (m) {
     case zero:
          v = vector<int>(n);  // n elements initialized to 0
          break;
     case cpy:
           v = arg;
           break;
     };

     // ...

     if (m == seq)
           v.assign(p,q);    // copy from sequence [p:q)

     // ...
}
```
When needed, we can constrain the parameter with a concept (§8.2). For example, we could define Pointer_to_class to require * and -> and write:

Click here to view code image

`for_each(v,[](Pointer_to_class auto& s){ s->rotate(r); s->draw(); });`

Like a function, a lambda can be generic
```cpp
template<typename C, typename Oper>
void for_each(C& c, Oper op)   // assume that C is a container of pointers
{
     for (auto& x : c)
           op(x);       // pass op() a reference to each element pointed to
}
```
This is a simplified version of the standard-library for_each algorithm.

Now, we can write a version of user() from §5.5 without writing a set of _all functions:


```cpp
void user()
{
     vector<unique_ptr<Shape>> v;
     while (cin)
         v.push_back(read_shape(cin));
     for_each(v,[](unique_ptr<Shape>& ps){ ps->draw(); });       // draw_all()
     for_each(v,[](unique_ptr<Shape>& ps){ ps->rotate(45); });   // rotate_all(45)
}
```
Capture nothing is [ ], capture all local names used by reference is [&], and capture all local names used by value is [=].
Had we wanted to give the generated object a copy of x, we could have said so: [x]
Had we wanted to “capture” only x, we could have said so: [&x].
The [&] is a capture list specifying that all local names used in the lambda body (such as x) will be accessed through references. 
The notation [&](int a){ return a<x; } is called a lambda expressio
Given concepts (§8.2), we can formalize count()’s assumptions about its argument and check them at compile time.

A predicate is something that we can invoke to return true or false. Fo
predicate
can call such an object, just as we call a function:
function object (sometimes called a functor),
The compiler would not know all instantiations of such a template in a program, so it could not generate a vtbl (§5.4).
A function template can be a member function, but not a virtual member.
There are three ways of expressing an operation parameterized by types or values:

A function template

A function object: an object that can carry data and be called like a function

A lambda expression: a shorthand notation for a function object
For those, we need a way of saying “a pair of values of the same type should be considered iterators.” Adding a deduction guide after the declaration of Vector does exactly that:



```
template<typename Iter>
    Vector(Iter,Iter) -> Vector<typename Iter::value_type>;
```
Like all other powerful mechanisms, deduction can cause surprises. Consider:



```
Vector<string> vs {"Hello", "World"};   // OK: Vector<string>
Vector vs1 {"Hello", "World"};          // OK: deduces to Vector<const char[6]> (Surprise?)
Vector vs2 {"Hello"s, "World"s};        // OK: deduces to Vector<string>
Vector vs3 {"Hello"s, "World"};         // error: the initializer list is not homogenous
Vector<string> vs4 {"Hello"s, "World"}; // OK: the element type is explicit
```
parameterize with string values is critically important. Fortunately, we can use an array holding the characters of a string:



```
template<char* s>
void outs() { cout << s; }

char arr[] = "Weird workaround!";

void use()
{
     outs<"straightforward use">();    // error (for now)
     outs<arr>();                      // writes: Weird workaround!
}
```
Unfortunately, for obscure technical reasons, a string literal cannot yet be a template value argument.
```
Buffer<char,1024> glob; // 
```
In addition to type arguments, a template can take value arguments. For example:

Click here to view code image

```
template<typename T, int N>
struct Buffer {
     constexpr int size() { return N; }
     T elem[N];
     // ...
};
```
Value arguments are useful in many contexts. For example, Buffer allows us to create arbitrarily sized buffers with no use of the free store (dynamic memory):
Concept checking is a purely compile-time mechanism and the code generated is as good as that from unconstrained templates.
Thus, concepts lets the compiler to do type checking at the point of use, giving better error messages far earlier than is possible with unconstrained template arguments. C++ did not officially support concepts before C++20, so older code uses unconstrained template
template argument for which a concept is specified is called a constrained argument and a template for which an argument is constrained is called a constrained template.
 
