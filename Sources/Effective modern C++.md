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

Item 18: Use `std::unique_ptr` for exclusive ownership
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