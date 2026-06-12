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



Item 5:
Use auto whenever possible

The most important use of this is for closures( Lambda expressions ):
The general function template may not suffice in space allocation for a closure, thus it will allocate memory on the heap. This can somehow lead to 

Item 6:

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