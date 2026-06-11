Author: [[Scott Meyers]]
Type: #source #book
Link: 
Topics: [[CPP]]

---

## 1. Treat C++ as a confederation of 4 languages

- C
- OOP
- Templates
- STL

## 2. Prefer const, enum, inline to `#define`

We can create class constants as
```cpp
class GamePlayer {
private:
  static const int NumTurns = 5;
  int scores[NumTurns];};
```

as saying:

> Every `GamePlayer` has an array of 5 scores. The number 5 is stored as a class-level constant called `NumTurns`.

But unless we do something like take its address, the compiler may never need to create an actual variable named `NumTurns`.

So this:

```cpp
const int GamePlayer::NumTurns;
```
in implementation file creates a storage. The one above does not need a storage but may substitute `NumTurns` as just a class level constant
- __Declaration vs Definition__ : Definition allocates memory, declaration does not -> only tells compiler about the type and name e.g.:
```cpp
// Declaration
extern int bar;
// Definition
int foo
```
same principle applies above as well

For older compiler we can use the _enum hack_ 

  ```cpp
  enum { NumTurns = 5 };        // "the enum hack" — makes  
                                // NumTurns a symbolic name for 5  
  
  int scores[NumTurns];         // fine
  ```
  As we are allowed to actually use enums where int are expected
## 3. Use const whenever Possible
- `char * const p //const pointer
- `char const *p //const data
- `const char *p //const data
- Iterators are like `T* const iter`


## 5. Know C++ implicit constructors and destructors
## 6. Explicitly disallow use of compiler generated constructors/destructors by declaring them private
## 7. Use pure virtual destructors for polymorphic base classes
## 8. Prevent Exceptions form leaving destructors
## 9. Never call virtual functions inside constructors/destructors
## 10. Have assignment operators return a reference to `*this`

## 11. Handle assignment to self in `operator=` 


