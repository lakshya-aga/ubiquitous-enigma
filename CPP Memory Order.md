implemented as enum

```cpp
enum class memory_order{
	relaxed, consume, acquire, release, acq_rel, seq_cast
};
inline constexpr memory_order memory_order_relaxed = memory_order::relaxed;
inline constexpr memory_order memory_order_consume = memory_order::consume;
inline constexpr memory_order memory_order_acquire = memory_order::acquire;
inline constexpr memory_order memory_order_release = memory_order::release;
inline constexpr memory_order memory_order_acq_rel = memory_order::acq_rel;
inline constexpr memory_order memory_order_seq_cst = memory_order::seq_cst;
```

for any atomic variable you may use:
```cpp
std::atomic<int> one_piece = {0};

one_piece.fetch_add(1, memory_order_relaxed); // anything goes within the control block
one_piece.fetch_add(1, memory_order_release); // no reordering before this
one_piece.fetch_add(1, memory_order_acquire); // no reordering after this
one_piece.fetch_add(1, memory_order_acq_rel); // no reordering before or after involving the same variable within the thread;
one_piece.fetch_add(1, memory_order_seq_cst); // no reordering before or after, default order
```
---

Topics: [[CPP]]
Reference: https://en.cppreference.com/cpp/atomic/memory_order
Type: #atom

