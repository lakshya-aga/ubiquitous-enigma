
Topics: [[C++]]
Reference: [[A tour of C++]]
Type: #atom

---
Important things to review:
- Type Predicates: restrict template usage
- functors
- general syntax
- What can be parameterised - value, type, even functions including lambda

This `template<Element T>` prefix is C++’s version of mathematic’s “for all T such that Element(T)”; 



modern program representation techniques (such as “abstract syntax trees”).
The `is_trivially_copyable_v<T>` is a type predicate

## benefit of constexpr
no runtime overhead. if is not evaluated at runtime
```cpp
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



## nodiscard:
```cpp

#include <iostream>
using namespace std;
[[nodiscard]] int  get_some(){
    return 1;
    
}
int main()
{
get_some(); // compiler warning
int x = get_some(); //okay
cout<<x<<endl;
}
```



## Avoiding leak using finally and managing resources 
Implemented using finally
```cpp
auto act = finally([&]{free(p);}); 
```
Triggers free: when act goes out of scope

We can define a function, finally() that takes an action to be executed on the exit from the scope
generally used when destructor cannot be used like C associated programs and structs
Instead, we could convert it to a lambda used as an initializer:





## Like a function, a lambda can be generic
```cpp
template<typename C, typename Oper>
void for_each(C& c, Oper op)   // assume that C is a container of pointers
{
     for (auto& x : c)
           op(x);       // pass op() a reference to each element pointed to
}
```


## Restrictions

A function template can be a member function, but not a virtual member.
The compiler would not know all instantiations of such a template in a program, so it could not generate a vtbl (§5.4).



Unfortunately, for obscure technical reasons, a string literal cannot yet be a template value argument.
```
Buffer<char,1024> glob; // 
```
In addition to type arguments, a template can take value arguments. For example:



```c++
template<typename T, int N>
struct Buffer {
     constexpr int size() { return N; }
     T elem[N];
     // ...
};
```
Value arguments are useful in many contexts. For example, Buffer allows us to create arbitrarily sized buffers with no use of the free store (dynamic memory):


## Endnotes:
Concept checking is a purely compile-time mechanism and the code generated is as good as that from unconstrained templates.
Thus, concepts lets the compiler to do type checking at the point of use, giving better error messages far earlier than is possible with unconstrained template arguments. C++ did not officially support concepts before C++20, so older code uses unconstrained template
template argument for which a concept is specified is called a constrained argument and a template for which an argument is constrained is called a constrained template.


## Definitions:

Predicate: True or false evaluation statement

`[[nodiscard]]`: keyword to mark a function as a returning function. i.e. compiler will throw errors when used without use of returned value.

vbtl:

A function object: an object that can carry data and be called like a function

A lambda expression: a shorthand notation for a function object

Functor: any object that can be called as if calling a function. Generally by implementing the `bool operator()(const T& x){...}` 