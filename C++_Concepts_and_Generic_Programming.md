
Topics: [[C++]]
Reference: [[A tour of C++]]
Type: #atom

---
The standard-library function forward() (§16.6) is used to move the arguments unchanged from the InputChannel constructor to the Transport constructor.

The point here is that the writer of InputChannel can construct an object of type Transport without having to know what arguments are required to construct a particular Transport. The implementer of InputChannel needs only to know the common user interface for all Transport objects.

Forwarding is very common in foundational libraries where generality and low run-time overhead are necessary and very general interfaces are common.
template<concepts::InputTransport Transport>
transport(std::forward<TransportArgs>(transportArgs)...)
   {}
Passing arguments unchanged through an interface is an important use of variadic templates. Consider a notion of a network input channel for which the actual method of moving values is a parameter. 
Here, (v+...+0) means add all the elements of v starting with the initial value 0. The first element to be added is the “rightmost” (the one with the highest index): (v[0]+(v[1]+(v[2]+(v[3]+(v[4]+0))))). That is, starting from the right where the 0 is. It is called a right fold. Alternatively, we could have used a left fold:
The recursive implementations can be tricky to get right.

The type checking of the interface is a possibly elaborate template program.

The type checking code is ad hoc, rather than defined in the standard.

The recursive implementations can be surprisingly expensive in compile time and compiler memory requirements.
parameter declared with a ... is called a parameter pack
first argument from the rest and then recursively call the variadic template for the tail of the arguments
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
Good, useful concepts are fundamental and are discovered more than they are designed. Examples are integer and floating-point number (as defined even in Classic C [Kernighan,1978]), sequence, and more general mathematical concepts, such as ring and vector space. They represent the fundamental concepts of a field of application. That is why they are called “concepts.” Identifying and formalizing concepts to the degree necessary for effective generic programming can be a challenge.
Unfortunately, the notational support for that is not yet perfect: we have to use a concept as an adjective, rather that a noun.
Says nothing about the layout of the object
Enables the use of a set of types
Relies on function declarations and language rules
Relies on use patterns reflecting function declarations and language rules
Specifies the set of operations that can be applied to an object, implicitly and explicitly
Specifies the set of operations that can be applied to an object, implicitly and explicitly
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
auto ch1 = open_channel("foo");                 // works with whatever open_channel() returns
Arithmetic auto ch2 = open_channel("foo");      // error: a channel is not Arithmetic
Channel auto ch3 = open_channel("foo");
In addition to their use for constraining function arguments, concepts can constrain the initialization of variables:
int f(auto x) { /* ... */ }        // take an argument of any type
Taking an auto parameter makes a function into a function template.
Changing an interface can cause massive recompilation.
Delaying the final check of the template definition until instantiation time gives two benefits:

We can use incomplete concepts during development. That allows us to gain experience while developing concepts, types, and algorithms, and to gradually improve checking.

We can insert debug, tracing, telemetry, etc. code into a template without affecting its interface. Changing an interface can cause massive recompilation.
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
. If you see requires requires in your code, it is probably too low level and will eventually become a problem.
Like assembly code, requires-expressions should not be seen in ordinary code.
A requires-expression is a predicate that is true if the statements in it are valid code and false if not.
requires requires is not a typo. The first requires starts the requirements-clause and the second requires starts the requires-expression
Using a requires-expression, we can check if a set of expressions is valid. For example, we might try to write advance() without the use of the standard-library concept random_access_iterator:
requires requires(Iter p, int i) { p[i]; p+i; }    // Iter has subscripting and integer addition
a match for all of its arguments, and

at least an equally good match for all arguments as other alternatives, and

a better match for at least one argument.
If the argument doesn’t match the concept, that alternative cannot be chosen.

If the argument matches the concept for just one alternative, that alternative is chosen.

If arguments from two alternatives match a concept and one is stricter than the other (match all the requirements of the other and more), that alternative is chosen.

If arguments from two alternatives are equally good matches for a concept, we have an ambiguity.
The compiler will select the template with the strongest requirements met by the arguments. In this case, a list only supplies forward iterators, but a vector offers random-access iterators, so we get:
// a forward iterator has ++, but not + or +=
// a random-access iterator has +=
}
random_access_iterator
forward_iterator
Whatever notation we choose, it is important to design a template with semantically meaningful constraints on its arguments
Number<Num>
Arithmetic<range_value_t<Seq>> Num
What about Number Num constraint
requires Sequence<Seq>
just replace template<typename Seq> with template<Sequence Seq>
The template<Sequence Seq> notation is simply a shorthand for an explicit use of requires Sequence<Seq>.
In particular, we might someday want to express sum() in terms of + and = rather than +=, and then we’d be happy that we used a general concept (here, Arithmetic) rather than a narrow requirement to “have +=.”
In this example, we needed only +=, but for simplicity and flexibility, we should not constrain our template argument too tightly
. Arithmetic<X,Y> is a concept specifying that we can do arithmetic with numbers of types X and Y.
range_value_t (§16.4.4) of a sequence is the type of the elements in that sequence; it comes from the standard library where it names the type of the elements of a range
template<Sequence Seq, Number Num>
    requires Arithmetic<range_value_t<Seq>,Num>
Once we have defined what the concepts Sequence and Number mean, the compiler can reject bad calls by looking at sum()’s interface only
The type-name introducer typename is the least constraining, requiring only that the argument be a type
We could say that the sum() algorithm is generic in two dimensions: the type of the data structure used to store elements (“the sequence”) and the type of elements.
A sequence, Seq, that supports begin() and end()
supports auto
The abstractions that represent the fundamental operations and data structures are called concepts.
template<Sequence Seq, Number Num>
    requires Arithmetic<range_value_t<Seq>,Num>
Arithmetic<X,Y> is a concept specifying that we can do arithmetic with numbers of types X and Y.
The ability to pass types (as well as values and templates) as arguments without loss of information. This implies great flexibility in what can be expressed and excellent opportunities for inlining, of which current implementations take great advantage.

Opportunities to weave together information from different contexts at instantiation time. This implies optimization opportunities.

The ability to pass values as template arguments. This implies opportunities for compile-time computation.
