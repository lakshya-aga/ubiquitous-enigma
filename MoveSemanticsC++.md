Move semantics lets C++ transfer ownership of resources instead of copying them.

Core mechanism:
- lvalues: named objects (usually copied)
- rvalues: temporary objects (can be moved)
- `std::move` casts to an rvalue reference and enables move operations

Why it matters:
- avoids deep copies for vectors/strings/containers,
- improves performance in return values and container reallocation.

Rule of thumb:
- If your class manages resources, define or default move constructor and move assignment appropriately (Rule of 5 context).

---

Topics: [[C++]], Performance, Resource Management
Reference: [[Effective Modern C++]] + [[A tour of C++]]
Type: #atom
