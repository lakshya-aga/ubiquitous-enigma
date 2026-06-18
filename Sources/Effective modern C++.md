Author: [[Scott Meyers]]
Type: #source #book
Link: 
Topics: [[CPP]]

---

## Item 1
Understanding Template Type deduction

## Item 2
Understanding auto type deduction
- The key difference really between template and auto type deduction is in deducing type of `{1,2,3}` as auto deduces as type initialiser list while Template throws error

## Item 3:
Understanding `decltype` (declared type)
Most useful in deducing type for return types and checking type properties in template programming


## Item 5:
Use auto whenever possible

The most important use of this is for closures( Lambda expressions ):
The general function template may not suffice in space allocation for a closure, thus it will allocate memory on the heap. This can somehow lead to slower times
### _Item 5 may have changed in C++20_

## Item 6:

Understand when not to use auto or use it wisely
Some calls return proxy classes. such as 
```cpp
vector<bool> temp(10);
auto x = temp[5];
```
Other classes return T& but bool returns T::reference which does not behave quite the way you want it to
Instead we should use:
```cpp
auto x = static_cast<bool>(temp[5]);
```


## Item 7:

Differentiate between braced and parenthesized initialization


## Item 9:
Defining special behaviour
```cpp
template<typename T>
class Allocator<T>{
typename Allocator<T>::type x;
}

// vs


template<>
class Allocator<Wine>{
int type;
}
```


---
# Smart Pointers

## Item 18: Use `std::unique_ptr` for exclusive ownership
- Assignment operation sets RHS to null
- ```cpp
  auto delInvmt = [](Investment* pInvestment){
	  makeLogEntry(pInvestment);
	  delete pInvestment;
  };
  
  template <typename ...Ts>
  std::unique_ptr<Investment, decltype(delInvmt)>
  makeInvestment(Ts&& ...params){
	  std::unique_ptr<Investment, decltype(delInvmt)> 
	  pInv(new Investment, delInvmt);
	  if ( /* a Stock object should be created */ )
	  {
	    pInv.reset(new Stock(std::forward<Ts>(params)...));
	  }
	  else if ( /* a Bond object should be created */ )
	  {
	    pInv.reset(new Bond(std::forward<Ts>(params)...));
	  }
	  else if ( /* a RealEstate object should be created */ )
	  {
	    pInv.reset(new RealEstate(std::forward<Ts>(params)...));
	  }
	  return pInv;
  }
  
  
  ```
  #todo learn perfect forwarding
unique ptrs (generally) have 2 items -> the pointer and the function pointer for deletion. Thus, they may differ in size as delete pointer may be stateless or stateful function and may grow to be arbitrarily large also. This is true for custom deleters only. For default delete, same size as raw pointer

## Item 19: How to use `shared_ptr`
- They do not take deleters
- They increment the number of `shared_ptr`s
- Very easy to get Undefined behavior (free ride on the particle accelerator to undefined behavior) if you use same raw pointer to initialise 2 shared_ptrs
- It has 2 objects. Raw pointer and control block (which has reference count, weal count, custom deleter, allocator etc.) so constant size
- CRTP (Curiously recurring template pattern) is introduced. e.g.
```cpp
class Widget: public std::enable_shared_from_this<Widget>{
	public:
		void process()
}
// ...
void Widget::process(){
	processWidgets.emplace_back(shared_from_this());
}
```
This is needed as 
```cpp
void process(){
processWidgets.emplace_back(this); 
}
```
would lead to undefined behavior due to multiple shared pointers from same raw pointer

## Item 20: Using Weak_ptr

weak_ptrs do not update reference count
You can check for expiry as
`wpw.expired()` -> bool

then create  a shared_ptr as

`std::shared_ptr<Widget> spw1 = wpw.lock();`

## Item 21: Using make functions
there are 3 make functions. `make_shared`, `make_unique` and `allocate_shared`.
Make shared has an advantage of allocating control block together with the object which leads to compiler doing only one memory allocation. This is also a disadvantage. Because `shared_ptr` may be referenced to by `weak_ptr`. unless all `weak_ptr`s are deleted, the control block (+ the object) can not be deallocated.
Additionally, we cannot use custom deleters. The advantage I can only understand to be avoiding code duplication. However, there is a case where exception may happen between object creation and `shared_ptr` creation, leading to a good case for `make_shared`/`make_unique`

## Item 22: When using the Pimpl idiom, define special member functions in the implementation file

Pointer to Implementation (Pimpl)
## Item 25: using `std::move` and `std::forward`
- Do not use them for local variables, it will cause pre mature optimisation and actually end up handicapping the compiler
- `forward` for universal references and `move` for rvalues
## Item 26: Avoid overloading on universal references
take the code here:

```cpp
#include <iostream>
using namespace std;

void function(int a){
    cout<<"a+1"<<"\n";
}

template<typename T>
void function(T&& a){
    cout<<"now"<<endl;
}
int main()
{
    short random_idx = 1;

    function(random_idx);
}

```
function will execute universal reference as it provides perfect match, even though semantically int version is what you were likely going for
## Item 27: Alternatives to overloading on universal references
- Using `enable_if` to disable template functions conditionally
```cpp
class Person{
public:
template <typename T, 
typename = std::enable_if_t<!std::is_base_of<Person, std::decay_t<T>>::value>
explicit Person(T&& n);
}
```
- Use tag dispatch
```cpp
//implement 2 versions
template<typename T>
void logAndAddImpl(T&& param, std::false_type){
blah do blah;
}

template<typename T>
void logAndAddImpl(T&& param, std::true_type){
blah do blah2;
}

template<typename T>
void logAndAdd(T&& param){
logAndAddImpl(std::forward<T>(param), std::is_integral<T>()); //is_integral is type_trait
}
```
- Pass by value: boringggg

## Item 28: Reference collapsing
when using universal reference i.e.
```cpp
template <typename T>
void function_x(T&& param);
```
This will resolve T to `Widget&` or `Widget` if passed an `lvalue` or `rvalue` respectively. If resolved to `Widget&` internally, there will be reference collapsing to convert `W& &&` to `lvalue`.

## Item 29: When does move fail
- Some types such as SSO strings and std::array are stack allocated objects so move is essentially of a fully contained object which is not as efficient as moving a pointer.

## Item 30: When does Perfect Forwarding fail
It fails when attempting to use function pointers of template functions or passing to functions that are templates as type deduction becomes impossible.

Another failure point is using bit fields as they cannot have a pointer and must always be passed by value or reference to const which also does the copy under the hood.

---
# Lambda Expressions
## Item 31: avoid default capture
- default capture does not copy variables inside classes as expected. More problems can arise for static variable pointers. `int a = 10; [=](){return 1+a;}`
## Item 32: Use init captures to move variables into closures
- ```cpp
  auto func = [pw = std::move(pw)]               // init data mbr
            { return pw->isValidated()         // in closure w/
                     && pw->isArchived(); };
  ```



---
# List of standalone items
- A type that has been declared, but not defined, is known as an _incomplete type_
- CRTP
- SFINAE
- egress
