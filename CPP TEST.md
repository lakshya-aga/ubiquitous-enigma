Author: [[ChatGPT]]
Type: #source 
Link: 
Topics: [[CPP]]

---

## 1. Object lifetime, copying, moving

  

### Q1. What happens here?

A1 default constructor will be called, a move operation then destructor on main function end as container's destructor will be called which wil destroy internal elements.

```cpp

#include <iostream>

#include <vector>

using namespace std;

  

struct X {

    X() { cout << "default\n"; }

    X(const X&) { cout << "copy\n"; }

    X(X&&) noexcept { cout << "move\n"; }

    ~X() { cout << "destroy\n"; }

};

  

int main() {

    vector<X> v;

    v.push_back(X{});

}

```

  

Follow-ups:

  

* What changes if `X(X&&)` is not marked `noexcept`?

This makes the compiler generated code slightly bigger as without noexcept, compiler prepares for stack unwinding

* What changes if we call `v.emplace_back()` instead?

Emplace back is generally more efficient as it will save us an extra move operation by constructing the object directly inside the container.

* What happens when the vector reallocates?

a full copy will have to happen so more space can be allocated

  

`This tests: temporary lifetime, move construction, `noexcept`, vector reallocation behavior.`

  

---

  

### Q2. Explain why this can be a bug.

deletion using [] and * is different. * can refer to a character pointer or a character array both. If character pointer is used to initialise, destructor for array destructor may give undefined behaviour. Moreover,, since the char* is shared on construction from same data, we can easily cause double delete-> dangling pointer and particle accelerator ride to undefined behaviour.

```cpp

class Widget {

public:

    Widget(char* data) : data_(data) {}

    ~Widget() { delete[] data_; }

  

private:

    char* data_;

};

```

  

Questions:

  

* What happens if a `Widget` is copied?

will fail as the creation of user defined constructors will prevent default copy constructor.

* Which special member functions should be written?

copy and move constructors. Copy and move assignments. default constructors

* How would you redesign this using RAII?

`explicit Widget(std::string data): _data(std::move(data)){}`

`explicit Widget(std::unique_ptr<string> data): _data(std::move(data)) {}`

  
  

Expected direction:

  

```cpp

class Widget {

public:

    explicit Widget(std::string data) : data_(std::move(data)) {}

  

private:

    std::string data_;

};

```

  

Or:

  

```cpp

class Widget {

public:

    explicit Widget(std::unique_ptr<char[]> data)

        : data_(std::move(data)) {}

  

private:

    std::unique_ptr<char[]> data_;

};

```

  

This tests: Rule of Three, Rule of Five, Rule of Zero.

  

---

  

### Q3. Implement a correct movable, non-copyable file handle wrapper.

  

Requirements:

  

* Owns a `FILE*`

* Closes it in destructor

* Cannot be copied

* Can be moved

* Safe against self-move

* Has `get()` and `release()`

  

```cpp

class FileHandler{
	private: 
		FILE* _f;
	public:
		~FileHandler(){
		_f.close();
		}
		// FileHandler(FileHandler) = deleted; // can keep if elementwise copy is desirable
		FileHandler(FileHandler& f) = deleted;
		FileHandler(FileHandler&& f): _f(std::mve(f)) {};
		FileHandler operator=(FileHandler& f) = deleted;
		FileHandler operator=(FileHandler&& f){
			_f = std::move(f);
		}

		
		FILE get(){
		_f.open();
		return _f;
		}
		
		FILE release(){
		_f.close();
		}
}

```

  

Example skeleton:

  

```cpp

#include <cstdio>

#include <utility>

  

class File {

public:

    explicit File(FILE* f = nullptr) noexcept : f_(f) {}

  

    ~File() {

        if (f_) std::fclose(f_);

    }

  

    File(const File&) = delete;

    File& operator=(const File&) = delete;

  

    File(File&& other) noexcept : f_(other.f_) {

        other.f_ = nullptr;

    }

  

    File& operator=(File&& other) noexcept {

        if (this != &other) {

            if (f_) std::fclose(f_);

            f_ = other.f_;

            other.f_ = nullptr;

        }

        return *this;

    }

  

    FILE* get() const noexcept {

        return f_;

    }

  

    FILE* release() noexcept {

        FILE* temp = f_;

        f_ = nullptr;

        return temp;

    }

  

private:

    FILE* f_;

};

```

  

Follow-ups:

  

* Why is move constructor `noexcept`? To reduce the bytecode and generate smaller binary.

* Should `get()` return `FILE*` or `const FILE*`? const makes sense as we don't want to modify the file handler itself.

* What invariant does the class maintain? file is not deleted that is being pointed to.

  

---

  

## 2. `const`, references, value categories

  

### Q4. Explain the difference.

  

```cpp

void f(int& x); //a

void f(const int& x);//b

void f(int&& x);

  

int a = 10;

const int b = 20;

  

f(a);

f(b);

f(30);

f(std::move(a));

```

  

Questions:

  

* Which overload is called each time?
1,2,3,3
* Is `std::move(a)` actually moving anything?
It is just a caste from lvalue to rvalue

* Inside `f(int&& x)`, is `x` an lvalue or rvalue?
x itself is an lvalue // Actually what would decltype((x)) resolve to
  

Key point: named rvalue references are lvalues.

  

---

  

### Q5. What is wrong with this?

  

```cpp

class Person {

public:

    Person(const std::string& name) : name_(std::move(name)) {}

  

private:

    std::string name_;

};

```

  

Answer: `name` is `const`, so `std::move(name)` produces `const std::string&&`. The move constructor usually cannot steal from a `const` object, so this copies.

  

Better:

  

```cpp

class Person {

public:

    explicit Person(std::string name)

        : name_(std::move(name)) {}

  

private:

    std::string name_;

};

```

  

Follow-up:

  

* When is pass-by-value-and-move a good constructor pattern?
When performance is not critical or we are using primitives that have low copy cost. We may also want to use universal reference as it would allow both lvalue and rvalue reference to be used for move

* When might `const std::string&` still be better?
When copying is desired
  

---

  

### Q6. Implement perfect forwarding wrapper.

  

Write a function `call_twice` that forwards its arguments to a callable.

  ```cpp
  // Lakshya
  template <typename... T>
  void call_twice(T... &args){
	  some_random_function(std::forward<T>(Args));
  }
  ```

  
Then discuss what may be wrong with it.
No idea
  

Important issue: if an argument is moved during the first call, forwarding it again can reuse a moved-from object.

  

Example:

  

```cpp

call_twice([](std::unique_ptr<int>) {}, std::make_unique<int>(42));

```

  

The first call consumes the pointer. The second call is invalid behavior for the intended logic.

  

Better design may require copying arguments, constraining arguments, or documenting that only reusable arguments are allowed.

  

---

  

## 3. Constructors, assignment, and initialization

  

### Q7. What gets called?

  

```cpp

struct A {

    A() {}

    A(int) {}

    A(std::initializer_list<int>) {}

};

  

A a1;

A a2{};

A a3(10);

A a4{10};

A a5 = 10;

A a6 = {10};

```

  

Questions:

  

* Which constructors are selected?

* Why does braced initialization prefer `initializer_list`?

* How can this surprise API users?

  

This tests Effective Modern C++–style advice around `{}` initialization.

  

---

  

### Q8. What is wrong with this assignment operator?

  

```cpp

class Buffer {

public:

    Buffer(size_t n) : size_(n), data_(new int[n]) {}

  

    ~Buffer() {

        delete[] data_;

    }

  

    Buffer& operator=(const Buffer& rhs) {

        delete[] data_;

        size_ = rhs.size_;

        data_ = new int[size_];

        std::copy(rhs.data_, rhs.data_ + size_, data_);

        return *this;

    }

  

private:

    size_t size_;

    int* data_;

};

```

  

Problems:

  

* Self-assignment bug.

* If `new` throws, object is left with dangling `data_`.

* Copy constructor is missing.

* Move operations are missing.

* Should probably use `std::vector<int>` or `std::unique_ptr<int[]>`.

  

A safer copy-and-swap version:

  

```cpp

#include <algorithm>

#include <cstddef>

#include <memory>

  

class Buffer {

public:

    explicit Buffer(size_t n)

        : size_(n), data_(std::make_unique<int[]>(n)) {}

  

    Buffer(const Buffer& other)

        : size_(other.size_),

          data_(std::make_unique<int[]>(other.size_)) {

        std::copy(other.data_.get(), other.data_.get() + size_, data_.get());

    }

  

    Buffer(Buffer&&) noexcept = default;

  

    Buffer& operator=(Buffer other) noexcept {

        swap(other);

        return *this;

    }

  

    void swap(Buffer& other) noexcept {

        using std::swap;

        swap(size_, other.size_);

        swap(data_, other.data_);

    }

  

private:

    size_t size_;

    std::unique_ptr<int[]> data_;

};

```

  

Follow-up:

  

* Why does `operator=(Buffer other)` handle both copy and move assignment?

* Is `noexcept` correct here?

  

---

  

## 4. Polymorphism and inheritance

  

### Q9. Explain the bug.

  

```cpp

struct Base {

    ~Base() {}

};

  

struct Derived : Base {

    ~Derived() {}

    int* p = new int[100];

};

  

int main() {

    Base* b = new Derived;

    delete b;

}

```

  

Problem: deleting a derived object through a base pointer without a virtual destructor is undefined behavior.

  

Fix:

  

```cpp

struct Base {

    virtual ~Base() = default;

};

```

  

Follow-ups:

  

* When should a base destructor be virtual?

* When should it be protected and non-virtual?

* What does a virtual destructor cost?

  

---

  

### Q10. Why is this dangerous?

  

```cpp

class Base {

public:

    Base() {

        init();

    }

  

    virtual void init() {}

};

  

class Derived : public Base {

public:

    void init() override {

        // use Derived fields

    }

  

private:

    int x_ = 42;

};

```

  

During base construction, virtual dispatch does not call the derived override. The object is not yet a `Derived` for virtual dispatch purposes.

  

Follow-up:

  

* How would you redesign this?

  

Possible answers:

  

* Use a non-virtual initialization function after construction.

* Use factory functions.

* Move required initialization into constructors.

* Use composition instead of inheritance.

  

---

  

### Q11. Implement a polymorphic clone.

  

Requirement:

  

```cpp

struct Shape {

    virtual ~Shape() = default;

    virtual std::unique_ptr<Shape> clone() const = 0;

};

```

  

Concrete implementation:

  

```cpp

struct Circle : Shape {

    Circle(int r) : radius(r) {}

  

    std::unique_ptr<Shape> clone() const override {

        return std::make_unique<Circle>(*this);

    }

  

    int radius;

};

```

  

Follow-ups:

  

* Why return `std::unique_ptr<Shape>` instead of raw pointer?

* Why should `clone()` be `const`?

* What happens if `Circle` has non-copyable members?

  

---

  

## 5. RAII and exception safety

  

### Q12. What exception guarantee does this function provide?

  

```cpp

void update(std::vector<int>& v, int x) {

    v.push_back(x);

    do_something();

}

```

  

Questions:

  

* What if `push_back` throws?

* What if `do_something` throws after the vector was modified?

* Does the function provide strong, basic, or no exception guarantee?

  

Follow-up: rewrite to provide a stronger guarantee where possible.

  

Example direction:

  

```cpp

void update(std::vector<int>& v, int x) {

    auto temp = v;

    temp.push_back(x);

    do_something();

    v = std::move(temp);

}

```

  

But this may be expensive and still depends on whether assignment is noexcept or strongly exception-safe.

  

---

  

### Q13. Implement a scope guard.

  

Requirements:

  

* Takes a callable

* Calls it in destructor unless dismissed

* Non-copyable

* Movable

* Destructor must not throw

  

Example:

  

```cpp

#include <utility>

#include <type_traits>

  

template <typename F>

class ScopeGuard {

public:

    explicit ScopeGuard(F f)

        : f_(std::move(f)), active_(true) {}

  

    ~ScopeGuard() noexcept {

        if (active_) {

            try {

                f_();

            } catch (...) {

                // destructors must not throw

            }

        }

    }

  

    ScopeGuard(const ScopeGuard&) = delete;

    ScopeGuard& operator=(const ScopeGuard&) = delete;

  

    ScopeGuard(ScopeGuard&& other) noexcept(

        std::is_nothrow_move_constructible_v<F>)

        : f_(std::move(other.f_)),

          active_(other.active_) {

        other.active_ = false;

    }

  

    ScopeGuard& operator=(ScopeGuard&&) = delete;

  

    void dismiss() noexcept {

        active_ = false;

    }

  

private:

    F f_;

    bool active_;

};

  

template <typename F>

ScopeGuard<F> make_scope_guard(F f) {

    return ScopeGuard<F>(std::move(f));

}

```

  

Follow-ups:

  

* Should destructor swallow exceptions or call `std::terminate`?

* Why delete move assignment?

* What if moving `F` throws?

  

---

  

## 6. Smart pointers and ownership

  

### Q14. What is the ownership bug?

  

```cpp

void f() {

    int* p = new int(42);

    std::shared_ptr<int> a(p);

    std::shared_ptr<int> b(p);

}

```

  

Problem: two separate control blocks manage the same raw pointer. Double delete.

  

Correct:

  

```cpp

auto a = std::make_shared<int>(42);

auto b = a;

```

  

Follow-ups:

  

* What is a control block?

* Why prefer `make_shared`?

* When might `make_shared` be undesirable?

  

---

  

### Q15. Explain why this leaks.

  

```cpp

struct Node {

    std::shared_ptr<Node> next;

    std::shared_ptr<Node> prev;

};

  

auto a = std::make_shared<Node>();

auto b = std::make_shared<Node>();

  

a->next = b;

b->prev = a;

```

  

Problem: reference cycle.

  

Fix:

  

```cpp

struct Node {

    std::shared_ptr<Node> next;

    std::weak_ptr<Node> prev;

};

```

  

Follow-ups:

  

* What does `weak_ptr::lock()` do?

* Does `weak_ptr` affect object lifetime?

* How do you choose which direction is weak?

  

---

  

### Q16. Implement a simple `unique_ptr`.

  

Not production-grade, but enough for interview.

  

```cpp

template <typename T>

class UniquePtr {

public:

    explicit UniquePtr(T* p = nullptr) noexcept : p_(p) {}

  

    ~UniquePtr() {

        delete p_;

    }

  

    UniquePtr(const UniquePtr&) = delete;

    UniquePtr& operator=(const UniquePtr&) = delete;

  

    UniquePtr(UniquePtr&& other) noexcept : p_(other.p_) {

        other.p_ = nullptr;

    }

  

    UniquePtr& operator=(UniquePtr&& other) noexcept {

        if (this != &other) {

            delete p_;

            p_ = other.p_;

            other.p_ = nullptr;

        }

        return *this;

    }

  

    T& operator*() const noexcept {

        return *p_;

    }

  

    T* operator->() const noexcept {

        return p_;

    }

  

    T* get() const noexcept {

        return p_;

    }

  

    T* release() noexcept {

        T* temp = p_;

        p_ = nullptr;

        return temp;

    }

  

    void reset(T* p = nullptr) noexcept {

        if (p_ != p) {

            delete p_;

            p_ = p;

        }

    }

  

    explicit operator bool() const noexcept {

        return p_ != nullptr;

    }

  

private:

    T* p_;

};

```

  

Follow-ups:

  

* Why is copy disabled?

* Why is move `noexcept`?

* What is missing compared with `std::unique_ptr`?

* Why does `unique_ptr<T[]>` need special handling?

  

---

  

## 7. Templates and overload resolution

  

### Q17. What is the problem with this forwarding constructor?

  

```cpp

class Person {

public:

    template <typename T>

    explicit Person(T&& name)

        : name_(std::forward<T>(name)) {}

  

private:

    std::string name_;

};

```

  

Problem: the templated constructor can hijack copy/move construction.

  

Example:

  

```cpp

Person p1("abc");

Person p2(p1);

```

  

The compiler may try to instantiate the template with `T = Person&`, which is not what you want.

  

A constrained version:

  

```cpp

#include <concepts>

#include <string>

#include <type_traits>

  

class Person {

public:

    template <typename T>

        requires std::constructible_from<std::string, T&&> &&

                 (!std::same_as<std::remove_cvref_t<T>, Person>)

    explicit Person(T&& name)

        : name_(std::forward<T>(name)) {}

  

private:

    std::string name_;

};

```

  

Follow-ups:

  

* How would you solve this in C++11?

* Why can universal references be dangerous in constructors?

  

---

  

### Q18. Explain reference collapsing.

  

What are the final types?

  

```cpp

template <typename T>

void f(T&& x);

  

int a = 1;

const int ca = 2;

  

f(a);

f(ca);

f(3);

```

  

Expected:

  

* `f(a)` gives `T = int&`, parameter becomes `int&`

* `f(ca)` gives `T = const int&`, parameter becomes `const int&`

* `f(3)` gives `T = int`, parameter becomes `int&&`

  

Rule:

  

* `& + &` → `&`

* `& + &&` → `&`

* `&& + &` → `&`

* `&& + &&` → `&&`

  

---

  

### Q19. Why can this be inefficient?

  

```cpp

template <typename T>

void setName(T&& name) {

    name_ = std::forward<T>(name);

}

```

  

Question:

  

* What happens if assignment to `name_` throws?

* What if `name` is a braced initializer?

* What constraints should be applied?

* Should this instead be overloads?

  

Possible overloads:

  

```cpp

void setName(const std::string& name) {

    name_ = name;

}

  

void setName(std::string&& name) noexcept {

    name_ = std::move(name);

}

```

  

Or pass-by-value:

  

```cpp

void setName(std::string name) {

    name_ = std::move(name);

}

```

  

---

  

## 8. Concrete class design questions

  

### Q20. Implement a fixed-size stack.

  

Requirements:

  

* Template over `T` and capacity `N`

* No dynamic allocation

* `push`, `pop`, `top`, `empty`, `size`

* Correct object lifetime handling

* Should work for non-default-constructible `T`

  

Good interview version:

  

```cpp

#include <cstddef>

#include <new>

#include <stdexcept>

#include <type_traits>

#include <utility>

  

template <typename T, std::size_t N>

class FixedStack {

public:

    FixedStack() noexcept = default;

  

    ~FixedStack() {

        clear();

    }

  

    FixedStack(const FixedStack&) = delete;

    FixedStack& operator=(const FixedStack&) = delete;

  

    template <typename... Args>

    void emplace(Args&&... args) {

        if (size_ == N) {

            throw std::overflow_error("FixedStack full");

        }

  

        void* addr = &storage_[size_];

        new (addr) T(std::forward<Args>(args)...);

        ++size_;

    }

  

    void push(const T& value) {

        emplace(value);

    }

  

    void push(T&& value) {

        emplace(std::move(value));

    }

  

    void pop() {

        if (empty()) {

            throw std::underflow_error("FixedStack empty");

        }

  

        --size_;

        ptr(size_)->~T();

    }

  

    T& top() {

        if (empty()) {

            throw std::underflow_error("FixedStack empty");

        }

        return *ptr(size_ - 1);

    }

  

    const T& top() const {

        if (empty()) {

            throw std::underflow_error("FixedStack empty");

        }

        return *ptr(size_ - 1);

    }

  

    bool empty() const noexcept {

        return size_ == 0;

    }

  

    std::size_t size() const noexcept {

        return size_;

    }

  

    void clear() noexcept {

        while (!empty()) {

            pop_noexcept();

        }

    }

  

private:

    using Storage = std::aligned_storage_t<sizeof(T), alignof(T)>;

  

    T* ptr(std::size_t i) noexcept {

        return std::launder(reinterpret_cast<T*>(&storage_[i]));

    }

  

    const T* ptr(std::size_t i) const noexcept {

        return std::launder(reinterpret_cast<const T*>(&storage_[i]));

    }

  

    void pop_noexcept() noexcept {

        --size_;

        ptr(size_)->~T();

    }

  

    Storage storage_[N];

    std::size_t size_ = 0;

};

```

  

Follow-ups:

  

* Why not use `T storage_[N]`?

* What is placement new?

* Why use `std::launder`?

* What exception guarantee does `emplace` provide?

  

---

  

### Q21. Implement a minimal copy-on-write string-like object.

  

This is a tricky question. A good answer should mention that COW strings are usually a bad fit for modern C++ because of threading, iterator invalidation, and move semantics.

  

Still, a minimal sketch:

  

```cpp

#include <memory>

#include <string>

  

class CowString {

public:

    CowString() : data_(std::make_shared<std::string>()) {}

  

    explicit CowString(std::string s)

        : data_(std::make_shared<std::string>(std::move(s))) {}

  

    char operator[](std::size_t i) const {

        return (*data_)[i];

    }

  

    char& operator[](std::size_t i) {

        detach();

        return (*data_)[i];

    }

  

    const std::string& str() const noexcept {

        return *data_;

    }

  

private:

    void detach() {

        if (!data_.unique()) {

            data_ = std::make_shared<std::string>(*data_);

        }

    }

  

    std::shared_ptr<std::string> data_;

};

```

  

Follow-ups:

  

* Why is non-const `operator[]` problematic?

* Is `shared_ptr::unique()` enough for thread safety?

* Why did modern standard libraries move away from COW `std::string`?

  

---

  

### Q22. Implement a small RAII lock wrapper.

  

Do not use `std::lock_guard` internally.

  

```cpp

#include <mutex>

  

class LockGuard {

public:

    explicit LockGuard(std::mutex& m)

        : m_(m), owns_(true) {

        m_.lock();

    }

  

    ~LockGuard() {

        if (owns_) {

            m_.unlock();

        }

    }

  

    LockGuard(const LockGuard&) = delete;

    LockGuard& operator=(const LockGuard&) = delete;

  

    LockGuard(LockGuard&& other) noexcept

        : m_(other.m_), owns_(other.owns_) {

        other.owns_ = false;

    }

  

    LockGuard& operator=(LockGuard&&) = delete;

  

private:

    std::mutex& m_;

    bool owns_;

};

```

  

Follow-ups:

  

* Should this type be movable?

* Why is `std::lock_guard` non-movable?

* What happens if `unlock()` throws?

* Why store a reference instead of a pointer?

  

---

  

## 9. “Find the bug” questions

  

### Q23. Returning a reference to a local

  

```cpp

const std::string& getName() {

    std::string name = "abc";

    return name;

}

```

  

Bug: dangling reference.

  

Better:

  

```cpp

std::string getName() {

    return "abc";

}

```

  

---

  

### Q24. Iterator invalidation

  

```cpp

std::vector<int> v = {1, 2, 3, 4};

  

for (auto it = v.begin(); it != v.end(); ++it) {

    if (*it % 2 == 0) {

        v.erase(it);

    }

}

```

  

Bug: `erase` invalidates `it`; loop increments invalid iterator.

  

Fix:

  

```cpp

for (auto it = v.begin(); it != v.end(); ) {

    if (*it % 2 == 0) {

        it = v.erase(it);

    } else {

        ++it;

    }

}

```

  

---

  

### Q25. Capturing by reference

  

```cpp

std::function<int()> makeCounter() {

    int x = 0;

    return [&] {

        return ++x;

    };

}

```

  

Bug: lambda captures local variable by reference; returned lambda dangles.

  

Fix:

  

```cpp

std::function<int()> makeCounter() {

    int x = 0;

    return [x]() mutable {

        return ++x;

    };

}

```

  

---

  

### Q26. Bad `shared_ptr` from `this`

  

```cpp

class Widget {

public:

    std::shared_ptr<Widget> getPtr() {

        return std::shared_ptr<Widget>(this);

    }

};

```

  

Bug: creates a new control block for `this`.

  

Correct:

  

```cpp

#include <memory>

  

class Widget : public std::enable_shared_from_this<Widget> {

public:

    std::shared_ptr<Widget> getPtr() {

        return shared_from_this();

    }

};

```

  

Follow-up:

  

* What happens if `shared_from_this()` is called before the object is owned by a `shared_ptr`?

  

---

  

## 10. High-signal conceptual questions

  

Use these for mock interviews:

  

1. Explain Rule of Zero, Rule of Three, and Rule of Five.

2. Why should move operations usually be `noexcept`?

3. When should you use `unique_ptr` vs `shared_ptr`?

4. What is RAII, and why is it central to C++?

5. What is object slicing?

6. Why should base classes often have virtual destructors?

7. Why should destructors generally not throw?

8. What is the difference between `std::move` and `std::forward`?

9. What are universal/forwarding references?

10. What does `const` mean on a member function?

11. What is the difference between logical constness and bitwise constness?

12. What is undefined behavior? Give examples.

13. What are the risks of macros compared with templates or `constexpr`?

14. What is the difference between initialization and assignment?

15. Why prefer composition over inheritance?

16. What does `explicit` prevent?

17. Why can `std::initializer_list` overloads surprise you?

18. What is the pImpl idiom?

19. What are the exception safety guarantees?

20. What is type erasure?

  

## 11. Concrete implementation drills to practice

  

These are worth coding from scratch:

  

1. `UniquePtr<T>`

2. `SharedPtr<T>` with reference count

3. `ScopeGuard`

4. `File` RAII wrapper

5. `Mutex LockGuard`

6. `FixedStack<T, N>` without default-constructing all elements

7. `RingBuffer<T>`

8. `SmallVector<T, N>` simplified

9. `Observer` pattern with safe lifetime handling

10. `polymorphic clone()`

11. `pImpl` class with correct copy/move

12. `ThreadPool` simplified

13. `LRUCache` without focusing on DSA, focusing on ownership and iterator validity

14. `Any` or `Function` simplified type-erasure wrapper

15. `Expected<T, E>` simplified error-return type

  

A strong interview strategy is to practice each implementation with these four constraints: **copy behavior, move behavior, destructor behavior, and exception safety**. That is the Scott Meyers mindset.


  
