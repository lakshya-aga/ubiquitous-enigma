
Topics: [[CPP]]
Reference: [[A Tour of CPP]]
Type: #atom

---
The standard-library function forward() (§16.6) is used to move the arguments unchanged from the InputChannel constructor to the Transport constructor.

The point here is that the writer of InputChannel can construct an object of type Transport without having to know what arguments are required to construct a particular Transport. The implementer of InputChannel needs only to know the common user interface for all Transport objects.

Forwarding is very common in foundational libraries where generality and low run-time overhead are necessary and very general interfaces are common.
```cpp
template<concepts::InputTransport Transport>
transport(std::forward<TransportArgs>(transportArgs)...)
   {}
```
Passing arguments unchanged through an interface is an important use of variadic templates. Consider a notion of a network input channel for which the actual method of moving values is a parameter. 
Here, (v+...+0) means add all the elements of v starting with the initial value 0. The first element to be added is the “rightmost” (the one with the highest index): (v[0]+(v[1]+(v[2]+(v[3]+(v[4]+0))))). That is, starting from the right where the 0 is. It is called a right fold. Alternatively, we could have used a left fold:
The recursive implementations can be tricky to get right.

The type checking of the interface is a possibly elaborate template program.

The type checking code is ad hoc, rather than defined in the standard.

The recursive implementations can be surprisingly expensive in compile time and compiler memory requirements.
parameter declared with a ... is called a parameter pack
first argument from the rest and then recursively call the variadic template for the tail of the arguments
```cpp

template<typename T>
concept Printable = requires(T t) { std::cout << t; } // just one operation!



void print()
{
     // what we do for no arguments: nothing
}

template<Printable T, Printable... Tail>
void print(T head, Tail... tail)
{
     cout << head << ' ';       // first, what we do for the head
     print(tail...);            // then, what we do for the tail
}

```

template can be defined to accept an arbitrary number of arguments of arbitrary types. Such a template is called a variadic template
range is a standard-library concept representing a sequence with begin() and end()
Conversely, the best way to develop a template is often to

first, write a concrete version

then, debug, test, and measure it

finally, replace the concrete types with template arguments.

The process of generalizing from a concrete piece of code (and preferably from several) while preserving performance is called lifting.

A string is another example of a regular type. Like int, string is also totally_ordered (§14.5). That is, two strings can be compared using <, <=, >, >=, and <=> with the appropriate semantics.

doesn’t suffer technical problems from overly clever programming tricks.

can be compared using == and !=

can be copied (with the usual semantics of copy, yielding two objects that are independent and compare equal) using a constructor or an assignment.

can be default constructed.

A type is regular when it behaves much like an int or a vector

Says nothing about the layout of the object
Enables the use of a set of types
Relies on function declarations and language rules
Relies on use patterns reflecting function declarations and language rules
Specifies the set of operations that can be applied to an object, implicitly and explicitly

```cpp
	auto some_function(int x)
	{
	     // ...
	     Number auto y = fct(x);  // an error unless fct(x) returns a Number
	     return y;
	     // ...
	}
	Number auto some_function(int x)
	{
	    // ...
	    return fct(x);  // an error unless fct(x) returns a Number
	    // ...
	}
```


We can use incomplete concepts during development. That allows us to gain experience while developing concepts, types, and algorithms, and to gradually improve checking.

We can insert debug, tracing, telemetry, etc. code into a template without affecting its interface. Changing an interface can cause massive recompilation.
```cpp
template<class S>
using Value_type = typename S::value_type;
range_value_t
template<typename T, typename T2 =T>
static_assert(Equality_comparable<int>);
concept Equality_comparable =
    requires (T a, T b) {
         { a == b } -> Boolean;   // compare Ts with ==
         { a != b } -> Boolean;   // compare Ts with !=
    };
```
If you see requires requires in your code, it is probably too low level and will eventually become a problem.

