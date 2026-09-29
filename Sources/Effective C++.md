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
- Might accidentally delete `this` when deleting `rhs`
- Copy and swap, identity check on top, and careful ordering to prevent delete before assignment are some ways of achivieng this
## 12. Copy All parts of an object
- Notoriously, for derived classes, if you write a copy constructor, it will not call the copy constructor by default for the base class. You have to call that manually using example
```cpp
#include <string>

using namespace std;

class Customer{
    public:
    string name;
    int id;
    Customer(const Customer &c): name(c.name) {}
    Customer() {}
};

class PriorityCustomer : public Customer{

    public:
    int priority;
    PriorityCustomer(const PriorityCustomer &pc): priority(pc.priority), Customer(pc){};
    PriorityCustomer() {};
};

  

int main(){
    PriorityCustomer person;
}
```


---
## 13. Use Objects to manage resources
## 14. Think carefully about copying behavior in resource-managing classes.
## 15. Allow access to raw resource when using resource management classes. E.g. 
 ```cpp
 public class FontHandle{
	 public:
	 Font f;
	 const Font operator(){return f;}
 }
 ```
 This makes use of language easier for other programmers
## 16. Use same kind of new and delete e.g. `[]`
## 17. Use Smart pointers in standalone statements 
Because compilers can reorder function call order sometimes in C++
```cpp
int priority();  
void processWidget(std::tr1::shared_ptr<Widget> pw, int priority);	

...

processWidget(std::tr1::shared_ptr<Widget>(new Widget), priority());

```
This may have the compiler generate code that calls priority between `Widget` creation and `shared_ptr` constructor call. If `priority` throws exception, we have undefined behaviour


---

Generalised copy constructors:

Allowing smart pointers to inherit from a base class smart pointer:
```cpp

template <typename T>
class SmartPointer{
public:
	template <typename U>
	SmartPointer(const SmartPointer<U>& obj):heldPtr(obj.getPtr());
	T* get(){return heldPtr;}
private:
	T* heldPtr;
	
};
```
