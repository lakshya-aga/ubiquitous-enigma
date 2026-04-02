iota(&v[0],&v[sz],1);
What does this do?

However, we can also perform simple checks on most properties that are known at compile time and report failures to meet our expectations as compiler error messages.
If an error can be found at compile time, it is usually preferable to do so.
If not in debug mode, the assert() is not checked
If the condition of an assert() fails in “debug mode,” the program terminates
```
void f(const char* p)
{
     assert(p!=nullptr);  // p must not be the nullptr
     // ...
}
```
The standard library offers the debug macro, assert()

constexpr double C = 299792.458;                        // km/s
```

void f(double speed)
{
     constexpr double local_max = 160.0/(60*60);        // 160 km/h == 160.0/(60*60) km/s

     static_assert(speed<C,"can't go that fast");       // error: speed must be a constant
     static_assert(local_max<C,"can't go that fast");   // OK

     // ...
}

```


`static_assert(assert, "string" | default_system_message)
The static_assert mechanism can be used for anything that can be expressed in terms of constant expressions



This will write integers are too small `if 4<=sizeof(int)` does not hold; that is, if an int on this system does not have at least 4 bytes. 
### We call such statements of expectations assertions.

`static_assert(4<=sizeof(int), "integers are too small");  // check integer size`



source_location
used to identify where exactly is the piece of code usage 
```
auto location = std::source_location::current();
    std::cout << "File: " << location.file_name() << std::endl;
    std::cout << "Function: " << location.function_name() << std::endl;
    std::cout << "Line: " << location.line() << std::endl;
    std::cout << "Column: " << location.column() << std::endl;
```
Set action to Error_action::ignore and no action is taken and no code is generated for expect().
The if constexpr tests are done at compile time (§7.4.3) so at most one run-time test is performed for each call of expect().
The condition expected to hold, `0<=i&&i<size()`, is passed to `expect()` as a lambda,
```
[i,this]{return 0<=i&&i<size();}
``` 
`constexpr (action == Error_action::logging)`
runtime optimisation by resolution at compile time
However, for many large programs, there is a need to support users who want to rely on extensive run-time checks while testing, but then deploy code with minimal checks.
RAII (§5.2.2, §6.3) is essential for simple and efficient error-handling using exceptions.
Furthermore, do not believe the myth that exception handling is slow; it is often faster than correct handling of complex or rare error conditions, and of repeated tests of error codes.
throw from anywhere in the function’s implementation will turn into a terminate().
ensure termination is to add
noexcept
there is no reasonable way to recover from memory exhaustion.
An error is of a kind from which we cannot recover
The system is one where error-handling is based on restarting a thread, process, or computer whenever a non-trivial error is detected.
function can indicate that it cannot perform its allotted task by:

### Throwing an exception:
somehow returning a value indicating failure
terminating the program (by invoking a function like terminate(), exit(), or abort() (§16.8)).
Example case: Program properly initialized the Vector members, but it failed to check that the arguments passed to it made sense.
