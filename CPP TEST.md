  

**How to use this**

- Each drill has a difficulty tag: `[warm]` rapid recall · `[core]` standard bar · `[hard]` separator question · `[stretch]` staff/quant-dev territory.

- Cover the **Answer key / talking points** and answer out loud first. Speaking the answer is the actual interview skill.

- For coding drills: write it yourself, compile with `-O2 -Wall -Wextra -fsanitize=address,undefined`, then read the talking points. You compile/review with Claude — keep that loop.

- Target cadence: 1 section/day for review, then full timed mocks (Section 9) in the final week.

  

**Self-grading rubric (use per drill)**

- 0 — couldn't start

- 1 — right idea, fuzzy on mechanism

- 2 — correct + can explain the *why* (cost model, hardware reason)

- 3 — correct + named the trade-off and when you'd choose otherwise

  

You want mostly 2–3 before walking in. A 1 on anything in Sections 2–4 is a flag.

  

---

  

## Section 1 — C++ Core & Mechanics

  

### Rapid-fire (warm-up battery)

Answer each in one or two sentences.

  

1. `[warm]` When is a copy elided guaranteed vs. allowed? (C++17 mandatory copy elision rules.)  

guaranteed when returning a local variable as return from function. Allowed -> if we manually do an rvalue cast or something. I don't know

2. `[warm]` Why should a move constructor be `noexcept`, and what concretely breaks if it isn't?  

So that it can be moved from during container reallocations. The performance would take a hit otherwise and we would end up copying elements as compiler prepares for exception handling

3. `[warm]` Rule of 0/3/5 — state all three and when you reach for each.  

No specials, only move ops and default const, move ops, copy ops and def constructor

4. `[warm]` Difference between `std::move` and `std::forward`. What does each actually *do* (hint: neither moves anything)?  

std move is to cast a single item to rvalue. forward is for variadic templates generally so it will cast each of the args as rvalue/lvalue depending on the rules of universal referencing.

5. `[warm]` What is a "universal/forwarding reference" and the reference-collapsing table?  

& && -> collapses to lvalue ; && is rvalue. It is a template programming practice of using T&& so T may be deduced as type or type& followed y reference collapsing to prevent writing multiple overloads for move and copy.

6. `[warm]` `const` member function — what does it const-qualify, and how does `mutable` interact?  

this will not be modified

7. `[warm]` `emplace_back` vs `push_back` — when is there genuinely zero difference?  

emplace creates inside the container. push_back moves passed element. emplace_back uses forwarding and can delay contructor call thus also delaying copy/move calls. 0 difference when we are actually passing a constructed object instead of rvalue/other sequence where constructor is being invoked

8. `[warm]` What is ADL and give a case where it surprises people (`swap`).  

Argument Deduced lookup can surprise in case of template presence. for e.g. an int version is present and a template version is present. called using short parameter. -> calls template version

9. `[warm]` `std::vector` growth: amortized O(1) push_back — prove the amortization.  

I cannot.

10. `[warm]` Why is `[[nodiscard]]` more than a style nicety on an HFT codebase?  

I don't know.

### Deeper drills

  

**1.1 `[core]` Move semantics trap**

```cpp

std::vector<std::string> make() {

    std::vector<std::string> v;

    v.push_back("hello");

    return std::move(v);   // <-- comment on this line

}

```

Why is the `std::move` here actively harmful? Now change `return std::move(v)` reasoning for a *member* you're returning — when is moving a local correct?  

The return type here is not a reference. NRVO would have almost guaranteed in standard compilers that move would be used for returning this. This cast to rvalue manually, adds a cast overhead as well. The standard vector move would do an element wise move as well compared to the original, which would have written directly in the memory space, thus eliminating even a move operation. same diff as push_back and emplace_back.

**1.2 `[core]` RVO vs NRVO**

Explain why RVO is mandatory in C++17 but NRVO is still only permitted. Write a function where NRVO is impossible and explain what the compiler must do.

```cpp

std::vector<int>(const std::vector<int>& temp){

  return temp;

}

```

in this case it will have to make a copy.

  

**1.3 `[hard]` The strict aliasing / type punning question**

You receive a raw byte buffer off the wire and need to read a `uint32_t` at offset 4. Compare:

- `*reinterpret_cast<uint32_t*>(buf + 4)` -> undefined under strict aliasing

- `union` punning -> undefined under stric aliasing

- `std::memcpy` -> simple mov

- `std::bit_cast` (C++20) -> well-defined and constexpr friendly

  
  

Which are UB, which are well-defined, and which actually compiles to a single `mov`? Tie your answer to the strict aliasing rule and `-fno-strict-aliasing`.

  
  
  

**1.4 `[hard]` Virtual dispatch cost model**

- Draw the memory layout of an object with one vtable. What's the indirection chain for a virtual call?  

The indirection chain for a virtual call would make the functions call resolve at runtime which implementation to run i.e. an extra jump. This will even takeaway the branch prediction benefits and pollute the instruction cache.

- Why is a virtual call hard for the branch predictor / why does it pollute the i-cache?

call -> virtual function -> vtable lookup -> jump to function. Because of vtable lookup, branch prediction does not work. random jumps cause i-cache pollution.

- Three ways HFT code avoids virtual dispatch on the hot path: CRTP, `std::variant` + visit, tag dispatch / function pointers. Sketch CRTP for a `Strategy` base.  

_CRTP_ allows us to write templates instead of using virtual to call indirection. Essentially, do the same thing as general inheritance `Derived: Base<Derived>` but do not declare the functions virtual. Once that is done. Implement the Base class as a template (the derived is passed as template argument), then downcast inside function calls to call the function of the derived class.  

Tag dispatch and function pointers in preventing virtual dispatch -> adding a random argument in parameter list to force choosing of the desired function.

`std::variant` + visit -> calling using an auto deduced lambda function instead of checking type

```cpp

std::visit([](auto &v){

  cout<<v<<"\n";

  }, input)

```

  

**1.5 `[core]` CRTP**

Implement a CRTP base `Comparable<Derived>` that gives `operator!=`, `<=`, `>=`, `>` for free given the derived type defines `operator<` and `operator==`. Why is this zero-overhead vs a virtual interface?

```cpp

<typename Derived>

class Comparable{

    friend bool operator<(const Derived& lhs, const Derived& rhs)

    {

        return (lhs < rhs);

    }

  

    friend bool operator>(const Derived& lhs, const Derived& rhs)

    {

        return (rhs < lhs);

    }

  

    friend bool operator==(const Derived& lhs, const Derived& rhs)

    {

        return (lhs == rhs);

    }

  

    friend bool operator<=(const Derived& lhs, const Derived& rhs)

    {

        return !(lhs > rhs);

    }

  

    friend bool operator>=(const Derived& lhs, const Derived& rhs)

    {

        return !(lhs < rhs);

    }

}

```

**1.6 `[core]` `noexcept` and the cost of exceptions**

- What is the runtime cost of a `try` block on the *happy path* with zero-cost (table-based) exception handling?  

-> Nothing. It stores most information in the tables outside which translates to vv heavy penalties on exceptions, but little to no cost on main path.  

- Why do many HFT shops compile with `-fno-exceptions`? What replaces error handling?

This flag generates less binary as it would remove code to handle exceptions. try catch blocks now give compilation errors  

*Side note:* Even with `-fno-exceptions` the noecept requirement stands as containers decide move or copy based on type traits such as `std::is_nothrow_move_contructible_v<T>`

- What is the relationship between `noexcept` and `std::vector` reallocation?

marking noexcept for move constructors for custom functions allows vector reallocation to move instead of copy. This is because when the reallocation expects exceptions, it needs to abort and restore object to its original state for which it needs copy instead of move. Thus, using copy even when move construction is possible.

  

**1.7 `[hard]` Object lifetime / placement new**

```cpp

alignas(Order) std::byte storage[sizeof(Order)];

Order* p = new (storage) Order{...};

// ... use p ...

p->~Order();

```

Why is the explicit destructor call required? When is `std::launder` needed and what problem does it solve? Why does an object pool need exactly this machinery?  

new (storage) does not allocate memory. It is a "placement new". It simply states to use the memory in storage as raw memory. So destructor is required explicitly because the memory is not owned by an Order object. Just that its values are written there. Assume order has a container type inside which allocates memory on the heap. Then without destruction, the container pointer may be wiped out but destruction and free of container will not happen.

launder would be useful in

- iterating through the object list in the memory

- replacing with derived or base class instance

- reuse the same memory as an object -> overwrite when things are const => get pointer, destroy, reconstruct

  

**1.8 `[stretch]` Templates: `if constexpr` vs SFINAE vs concepts**

Write a `serialize(T)` that takes a different path for trivially-copyable types (one `memcpy`) vs. types with a custom `.serialize()` method. Do it three ways (tag dispatch, SFINAE/`enable_if`, C++20 concepts) and argue which you'd ship.

  

**1.9 `[core]` Small buffer optimization**

- What is SSO in `std::string` and roughly how many chars fit inline on libstdc++/libc++?

- Why does SSO matter enormously for a system that constructs millions of short strings/symbols? (And why HFT often uses fixed-size `char[8]` symbol types instead.)  

  

sso is 2 different implementations under the hood for strings. around 15 chars inline.  It implements short strings around 15 chars in stack as that would be the memory needed in a 64 bit system to store 2 pointers (start and end). 15 bytes + 1 byte can be used to save size and object location is in the variable itself.  

Reading and writing to heap is an expensive operation. so stack allocation and destruction is faster when number of strings is large.

#TODO: `I don't know why HFT uses char[8]`

  

**1.10 `[stretch]` The `const`/`constexpr`/`consteval` ladder**

Distinguish `const`, `constexpr`, `consteval`, `constinit`. Give a use for `consteval` in parsing a fixed message schema at compile time.

const - to mark something as immutable for variables throughout its lifetime, mark fucntions as readonly.

constexpr - to mark expression as (optionally) evaluated during compile time instead of runtime.

consteval - to mark expression as always evaluatable dring compile time

constinit - initialised during compilation, but can change later

---

  

### Answer key / talking points — Section 1

  

- **Rapid-fire 2:** A throwing move means `std::vector` reallocation can't safely move elements (it would leave the container in a broken state mid-move with no strong guarantee), so it silently **falls back to copying**. `noexcept` move is the difference between O(n) moves and O(n) copies on every growth — measurable.

- **Rapid-fire 4:** `std::move` is an unconditional cast to rvalue reference. `std::forward<T>` is a *conditional* cast that preserves value category based on `T`'s deduced reference-ness. Both are pure casts; the actual moving happens in a move ctor.

- **1.1:** `return std::move(v)` defeats NRVO — the compiler would have constructed `v` directly in the return slot, but `std::move` forces a move construction instead (and turns a potential elision into a guaranteed move). Rule: never `std::move` a local you're returning by value. *Do* `std::move` a **member** or a function **parameter** you're returning, since NRVO can't apply there.

- **1.3:** `reinterpret_cast` and `union` punning are **UB under strict aliasing** (union punning is a common-but-nonstandard GCC/Clang extension; technically reading the inactive member is UB in C++). `memcpy` is **well-defined** and modern compilers fold it into a single `mov` at `-O2`. `std::bit_cast` is the C++20 well-defined, `constexpr`-friendly answer. The whole point: you get correctness *and* the single instruction; there's no perf reason to invoke UB. Mention `-fno-strict-aliasing` as the blunt escape hatch and why you'd rather not need it.

- **1.4:** call → load vptr from object → load function pointer from vtable at fixed offset → indirect call. Hurts because the target is data-dependent (indirect-branch mispredict ~15–20 cycles) and spreads call targets across the i-cache. CRTP resolves the call at compile time (static polymorphism, inlinable). `variant`+visit gives a jump table over a *closed* set.

- **1.6:** Zero-cost EH means **no cost on the happy path** — the cost is paid only when an exception is thrown (table lookup + unwind, can be microseconds to ms). Shops still ban them because (a) throw cost is unbounded/non-deterministic = tail latency poison, (b) binary size / i-cache from unwind tables, (c) `-fno-exceptions` lets the optimizer assume more. Replacement: error codes, `std::expected` (C++23), `Result`-style types, or "can't happen → terminate."

- **1.7:** Destructor isn't called automatically because you used placement new on raw storage (no owning object). `std::launder` is needed when you reuse storage and the new object differs in `const`/reference members or the compiler might cache the old object's representation — it tells the compiler "the pointer now refers to a *new* object." Object pools live and die on this: construct/destroy in place, reuse the slab, never deallocate on the hot path.

- **1.9:** SSO ≈ 15 chars on libstdc++ (22 on libc++) before heap allocation. Exchange symbols are short and fixed-ish, so a `struct Symbol { char c[8]; }` (trivially copyable, fits in a register pair, hashes trivially) beats `std::string` for the order map key.

  

---

  

## Section 2 — Memory Model & Concurrency

  

This section is where C++ HFT interviews are won or lost. Be able to *draw* the reordering, not just name the enum.

  

**2.1 `[core]` The six memory orders**

For each of `relaxed`, `consume` (and why it's effectively dead), `acquire`, `release`, `acq_rel`, `seq_cst`: state (a) what reordering it permits/forbids, (b) a concrete use, (c) rough hardware cost on x86 vs ARM.
relaxed -> within its block scope, free reordering
consume -> reorder after the release (same as acquire so deprecated)
acquire -> after release
release -> before consume and acquire if reading writing same atomic variable
#### ==Sequentially-consistent ordering==
  

**2.2 `[core]` x86 is "almost" sequentially consistent**

- What is the *one* reordering x86's TSO memory model allows? (StoreLoad.)

- Therefore: on x86, what does `acquire`/`release` cost in actual instructions? What does `seq_cst` store cost? (`mov` vs `xchg`/`mfence`.)

- Why does this mean "it worked on my x86 laptop" is a dangerous test for lock-free code?

  

**2.3 `[hard]` Store buffer / Dekker litmus test**

```

// Thread 1            // Thread 2

x.store(1, ???);       y.store(1, ???);

r1 = y.load(???);      r2 = x.load(???);

```

With all relaxed, can `r1 == 0 && r2 == 0`? With seq_cst? Explain via the store buffer. This is the canonical "why StoreLoad matters" question.

  

**2.4 `[core]` Acquire/release pairing**

Explain the message-passing pattern: producer fills `data` then `flag.store(true, release)`; consumer spins on `flag.load(acquire)` then reads `data`. Why is this correct? What breaks with `relaxed` on either side?

  

**2.5 `[hard]` Build an SPSC lock-free ring buffer**

Single producer, single consumer, fixed capacity, power-of-two size. Requirements:

- No locks, no allocation in push/pop.

- Correct memory orders (this is the graded part).

- Avoid false sharing between head and tail.

  

Write `push` and `pop`. Then defend: which loads/stores are `relaxed`, which `acquire`/`release`, and why each can be relaxed.

  

**2.6 `[hard]` False sharing**

- Define it precisely (two threads, two variables, one cache line, MESI ping-pong).

- How do you fix it? (`alignas(std::hardware_destructive_interference_size)` / pad to 64B.)

- Why does padding the SPSC head/tail to separate lines give a real throughput jump? Estimate the cost of a cross-core cache line bounce (~tens to ~100+ ns).

  

**2.7 `[core]` CAS, compare_exchange_weak vs strong**

- When does `compare_exchange_weak` spuriously fail and why does that make it *faster* in a loop?

- Write the canonical CAS loop for an atomic max: `while(!a.compare_exchange_weak(expected, std::max(expected, val)))`.

  

**2.8 `[hard]` The ABA problem**

- Construct the scenario in a lock-free stack pop.

- Solutions: tagged pointers / generation counters, hazard pointers, RCU, epoch-based reclamation. One sentence each on the trade-off.

  

**2.9 `[core]` Spinlock**

Implement a TTAS (test-and-test-and-set) spinlock with `_mm_pause()` / `__builtin_ia32_pause` backoff. Then answer: why TTAS over plain TAS? Why `PAUSE`? When is even a perfect spinlock the *wrong* choice vs a futex/mutex?

  

**2.10 `[stretch]` Why `std::mutex` is banned on the hot path**

Walk the cost: uncontended mutex is cheap (one CAS), but contention → futex syscall → context switch → scheduler → potential priority inversion → unbounded tail latency. Contrast with a spinlock's CPU-burn trade-off. What's the actual decision rule?

  

**2.11 `[stretch]` Sequential consistency isn't composable / the difference from linearizability**

Be ready to distinguish C++ `seq_cst` (about a single total order of atomic ops) from linearizability of a data structure. Subtle, asked at the top end.

  

---

  

### Answer key / talking points — Section 2

  

- **2.1:** `relaxed` = atomicity only, no ordering (counters, stats). `acquire` = no later op moves before it (load side of a handoff). `release` = no earlier op moves after it (store side). `acq_rel` for RMW. `seq_cst` adds a single global total order across all seq_cst ops. `consume` is intended to be a cheaper acquire for dependency chains but every compiler promotes it to acquire — don't use it. x86: acquire/release are *free* (plain mov), seq_cst store needs `xchg`/`mfence`. ARM: all of them cost real fence instructions (`ldar`/`stlr`/`dmb`).

- **2.2/2.3:** x86 allows only **StoreLoad** reordering (a later load can pass an earlier store to a different address, because the store sits in the store buffer). That's exactly why `r1==0 && r2==0` is possible even on x86 with relaxed/acquire-release — each thread's load can read the old value before the other's store drains. `seq_cst` forbids it by forcing the store buffer to flush (`mfence`/locked instruction) before the load. The "works on my laptop" trap: x86's strong model hides bugs that explode on ARM (Apple Silicon, Graviton, mobile).

- **2.5 — model answer shape:**

```cpp

template <class T, size_t N>  // N power of two

class SpscQueue {

  static_assert((N & (N-1)) == 0);

  alignas(64) std::atomic<size_t> head_{0};  // consumer writes

  alignas(64) std::atomic<size_t> tail_{0};  // producer writes

  alignas(64) std::array<T, N> buf_;

public:

  bool push(const T& v) {

    const size_t t = tail_.load(std::memory_order_relaxed);

    const size_t next = (t + 1) & (N - 1);

    if (next == head_.load(std::memory_order_acquire)) return false; // full

    buf_[t] = v;

    tail_.store(next, std::memory_order_release);  // publishes buf_[t]

    return true;

  }

  bool pop(T& out) {

    const size_t h = head_.load(std::memory_order_relaxed);

    if (h == tail_.load(std::memory_order_acquire)) return false;    // empty

    out = buf_[h];

    head_.store((h + 1) & (N - 1), std::memory_order_release);

    return true;

  }

};

```

  Defense: producer owns `tail_` so it reads it `relaxed`; it reads `head_` `acquire` to see the consumer's progress. The `release` store of `tail_` publishes the slot write to the consumer's `acquire` load. Symmetric for the consumer. `alignas(64)` kills false sharing between head and tail. (Caching the opposite index to reduce cross-line loads is the next optimization — mention it.)

- **2.6:** Two threads writing two distinct variables that land on the same 64B line force MESI invalidation traffic each write — the line ping-pongs between cores even though there's no logical sharing. Fix = pad/align to a full line. A cross-core bounce is ~40–100ns depending on topology (same socket vs cross-socket / L3 vs memory) — orders of magnitude over an L1 hit (~1ns).

- **2.7:** `weak` may fail even when `expected` matches, on LL/SC architectures (ARM) where the reservation gets cleared by an interrupt/context switch. In a retry loop you're looping anyway, so the cheaper instruction wins; use `strong` only when a single try must be authoritative.

- **2.9:** TAS spins by repeatedly *writing* (RMW) → keeps the line in M state bouncing. TTAS spins on a plain *read* (shared state, no invalidation) and only attempts the RMW when it sees the lock free → far less coherence traffic. `PAUSE` hints the CPU it's a spin loop (saves power, avoids memory-order-violation pipeline flush, yields to the SMT sibling). A spinlock is wrong when hold times can be long or when you can oversubscribe cores — then you burn a core spinning while the holder is descheduled.

  

---

  

## Section 3 — Low-Latency Techniques & Performance

  

**3.1 `[core]` Cache hierarchy numbers**

Recite the latency ladder (rough, order-of-magnitude): register, L1, L2, L3, main memory, NVMe, network round trip same DC. Why does "know your numbers" matter for design decisions?

  

**3.2 `[core]` AoS vs SoA**

Given you process one field across a million records, why is structure-of-arrays faster? Tie it to cache lines and the prefetcher and SIMD. When is AoS actually better?

  

**3.3 `[hard]` Branchless programming**

- Rewrite `int m = (a > b) ? a : b;` branchlessly and say when it helps vs hurts.

- What does `[[likely]]`/`[[unlikely]]` / `__builtin_expect` do, and what does it *not* do?

- Why can a branch be cheaper than branchless if it's >99% predictable?

  

**3.4 `[core]` Hot/cold path splitting**

What does it mean to move error handling / logging / rare branches "off the hot path"? How do `[[unlikely]]` and `__attribute__((cold))` help the layout? Why does this improve i-cache and branch prediction?

  

**3.5 `[hard]` Avoiding allocation on the hot path**

Name five sources of hidden allocation in "normal" C++ and the replacement:

- `std::string` → ?

- `std::vector` push past capacity → ?

- `std::function` → ?

- `std::map`/`std::unordered_map` node allocation → ?

- exceptions / `std::shared_ptr` control block → ?

  

**3.6 `[stretch]` Arena / monotonic allocator and `std::pmr`**

You already did the pmr deep-dive — here's the interview version: explain the two-layer (allocator interface vs memory_resource) design, when `monotonic_buffer_resource` is the right tool (per-message-burst, reset between events), and the type-erasure cost vs a templated allocator. When would you *not* use pmr and hand-roll instead?

  

**3.7 `[core]` Measuring latency correctly**

- Why is mean latency a lie? What do you report instead? (p50/p99/p99.9/max, and *why tail*.)

- `rdtsc`/`rdtscp` vs `std::chrono::steady_clock` — when do you need the former and what are its hazards (out-of-order, invariant TSC, core migration)?

- What is coordinated omission and why does it wreck naive benchmarks?

  

**3.8 `[hard]` Sources of jitter (tail latency)**

List the usual suspects and the mitigation for each: page faults (→ prefault + mlock), TLB misses (→ huge pages), context switches (→ pin + isolate cores `isolcpus`/`nohz_full`), interrupts (→ IRQ affinity away from hot cores), C-states/frequency scaling (→ disable, fix governor), NUMA remote access (→ pin memory + thread), the allocator, the kernel network stack (→ kernel bypass).

  

**3.9 `[core]` Branch prediction + the order book**

In your matching engine, where are the unpredictable branches? (e.g., crossing vs resting, side, order type.) How would you restructure to make the common case predictable / branch-light?

  

**3.10 `[stretch]` Prefetching**

When does manual `__builtin_prefetch` help and when does it hurt? Why is the hardware prefetcher usually enough, and what access pattern defeats it (pointer chasing — i.e., why intrusive/flat beats node-based)?

  

**3.11 `[stretch]` Kernel bypass**

One-paragraph each: why the kernel network stack adds latency/jitter, what DPDK / Solarflare Onload / io_uring each do differently, and busy-poll vs interrupt-driven trade-off.

  

---

  

### Answer key / talking points — Section 3

  

- **3.1:** Register <1ns · L1 ~1ns (~4 cyc) · L2 ~4ns · L3 ~10–20ns · RAM ~60–100ns · NVMe ~10–100µs · same-DC network ~µs+. The 100× cliff from L1 to RAM is *the* reason data layout dominates algorithmic cleverness at small n.

- **3.2:** SoA puts the field you touch contiguously → every cache line is 100% useful payload, prefetcher streams linearly, vectorizes cleanly. AoS wins when you touch *most fields of one record together* (locality per object) or for random single-record access.

- **3.3:** `max` branchless via masking/cmov, but at `-O2` the compiler already emits `cmov` for that ternary. Branchless helps when the branch is *unpredictable* (~50/50); it hurts when predictable because you always compute both sides and lose speculation. `__builtin_expect` only reorders code layout / hints the predictor's static guess — it does **not** remove the branch.

- **3.5:** string→fixed `char[N]` or `string_view`/arena; vector→`reserve` upfront or fixed `std::array`/ring; `std::function`→template/function pointer/`inplace_function`; node maps→open-addressing flat hash (e.g. `absl::flat_hash_map`-style) or `boost::flat_map`; shared_ptr→avoid shared ownership on hot path, use pools + raw pointers.

- **3.7:** Mean hides the tail that actually costs money; report percentiles and max, and design to the p99.9. `rdtscp` gives cycle granularity (chrono can be ~20ns+ overhead and coarser), but beware non-invariant TSC on old chips, OOO execution (use `rdtscp` or fence), and TSC differences across cores (pin!). Coordinated omission: if your load generator waits for each response it under-counts latency during stalls — fix by recording intended send time.

- **3.8:** Know that "average is fine, tail is everything" — every item on the list is a known cause of a p99.9 spike, and naming the mitigation (mlockall, hugepages, `isolcpus`, IRQ affinity, `performance` governor, NUMA pinning, kernel bypass) is exactly the senior signal.

  

---

  

## Section 4 — Data Structures (HFT-flavored)

  

**4.1 `[core]` Design a limit order book**

You've built one — now defend the design under questioning:

- Requirements: O(1)-ish best bid/ask, fast insert at a price level, **O(1) cancel by order ID**, FIFO time priority within a level.

- Walk your data structures: price→level map, level→FIFO list, orderID→location index.

- Why does storing the list iterator in the orderID index turn cancel from O(n) into O(1)? (Your ~6.7× win — be ready to narrate it.)

- Next optimization: why is `std::map<price, level>` a bottleneck and what replaces it? (Sorted vector / flat map for dense prices, or an **array indexed by price ticks** when the price range is bounded — the classic "price level array" design.)

  

**4.2 `[hard]` Order book follow-ups**

- How do you keep best bid/ask in O(1) under inserts/cancels at arbitrary levels?

- How do you handle a price-level array when prices are sparse / wide? (Hybrid: array for near-touch, map for far.)

- Market-by-order vs market-by-price book — when each?

  

**4.3 `[core]` Why not `std::unordered_map` on the hot path**

- Node-based, separate allocation per node, pointer chasing, poor cache behavior, `load_factor` rehash spikes.

- Open addressing (linear probing / Robin Hood / hopscotch) — why it's cache-friendlier. Trade-offs (tombstones, clustering, resize cost).

- Hash function for integer order IDs — why identity/multiplicative is fine and why you avoid `std::hash` surprises.

  

**4.4 `[core]` Intrusive containers**

Why does an intrusive linked list (node embedded in the object) beat `std::list`? (No separate allocation, one cache line, O(1) erase given the node.) Sketch the intrusive list node.

  

**4.5 `[hard]` Moving median / sliding window stats**

Maintain the median of the last K prices in O(log K) per update. (Two heaps, or order-statistics tree.) Then: how would you do a sliding-window max in O(1) amortized? (Monotonic deque.)

  

**4.6 `[hard]` Top-K by volume**

Stream of (symbol, volume) updates; report top-K symbols by cumulative volume at any time. Data structure choices and their update costs.

  

**4.7 `[stretch]` Fixed-capacity flat hash map for orderID→node**

Implement (or pseudocode) an open-addressing map with linear probing, no allocation, for `uint64_t` keys → `Order*`. Handle erase with tombstones or backward-shift deletion. Argue tombstone vs backshift.

  

---

  

### Answer key / talking points — Section 4

  

- **4.1:** The killer insight is the **orderID → (level, list-node-iterator)** index. Cancel = look up the iterator, splice it out of the intrusive FIFO list in O(1), decrement level volume, erase the index entry — no scanning the level. The `std::map` price tree is O(log n) per op *and* node-based (cache-hostile, pointer chasing); a **direct-indexed price array** (`level[price_in_ticks - base]`) makes best-price tracking and insertion O(1) when the tick range is bounded, with two cursors tracking current best bid/ask. That's the standard production layout (e.g., the canonical "How to Build a Fast Limit Order Book" design).

- **4.2:** Maintain best bid/ask cursors updated lazily: on cancel that empties the touch level, walk inward until a non-empty level (rare, amortized cheap); on insert better than current best, update the cursor in O(1). Sparse/wide prices → hybrid: dense array around the touch, fallback map for tails.

- **4.3:** Be specific: `unordered_map` is a chained hash with a node allocation per insert and a `Node*` per bucket → random memory per lookup. Flat/open-addressed maps keep entries inline → typically one cache line per probe. Robin Hood bounds probe-length variance; linear probing is simplest and prefetch-friendly.

- **4.5:** Two-heap median: max-heap (lower half) + min-heap (upper half), rebalance so sizes differ by ≤1, median is the top(s). Sliding window max: deque of indices kept monotonically decreasing; front is the max, pop expired from front, pop smaller from back — O(1) amortized.

  

---

  

## Section 5 — Algorithms & Coding (timed)

  

These are the LeetCode-flavored screens, but expect a performance follow-up. Solve, then state complexity *and* the memory-access cost. Target: medium in <15 min, hard in <30 min, then optimize for cache.

  

**5.1 `[core]` Two-sum / k-sum** — hash map vs sorted two-pointer; which has better constant factors and why.

**5.2 `[core]` Sliding window maximum** — monotonic deque, O(n).

**5.3 `[core]` Merge K sorted streams** — min-heap of iterators; relevant to merging feed sources.

**5.4 `[core]` LRU cache** — hashmap + intrusive doubly linked list, all O(1). (Classic; do it intrusive.)

**5.5 `[hard]` Median of a data stream** — two heaps (ties to 4.5).

**5.6 `[hard]` Min stack / max stack in O(1)** — auxiliary stack or store deltas.

**5.7 `[hard]` Trapping rain water / largest rectangle in histogram** — monotonic stack; common Optiver/IMC ask.

**5.8 `[hard]` Design a rate limiter / token bucket** — and make it lock-free.

**5.9 `[hard]` Reconstruct order book from a stream of add/cancel/execute messages** — direct HFT mapping of 5.x skills.

**5.10 `[stretch]` Lowest-latency "find the kth smallest in a stream"** — quickselect vs heap vs order-statistic tree, with the constant-factor discussion.

**5.11 `[core]` String/bit manipulation battery** — count set bits (`popcount`), reverse bits, next power of two, check power of two (`x & (x-1)`), `__builtin_clz/ctz` uses.

**5.12 `[hard]` Implement `memcpy`** and then explain why the libc one is faster (alignment, SIMD, `rep movsb` on modern x86).

  

> For each: after solving, ask yourself "where do the cache misses happen, and can I make the layout linear?" That follow-up is the differentiator.

  

---

  

## Section 6 — Systems & OS

  

**6.1 `[core]` Virtual memory & page faults** — minor vs major fault; why the *first* touch of mapped memory stalls; how prefaulting + `mlockall` removes it from the hot path.

**6.2 `[core]` System call cost** — why a syscall is ~hundreds of ns to µs (mode switch, possible context switch); how to avoid them on the hot path (busy poll, batch, kernel bypass, `io_uring`).

**6.3 `[core]` Context switch** — what it costs (direct register/TLB save + indirect cache/TLB cold-start); why pinning + core isolation matters.

**6.4 `[hard]` TCP vs UDP for market data** — why market data feeds are UDP multicast (fan-out, no per-consumer state, lower latency) with sequence numbers + gap recovery; why orders go over TCP. `TCP_NODELAY` / Nagle's algorithm — what it does and why you disable it.

**6.5 `[core]` epoll vs poll vs select** — O(1) readiness vs O(n) scans; edge- vs level-triggered; why busy-polling can still beat epoll on latency.

**6.6 `[hard]` Shared memory IPC** — `mmap`/`shm_open`, lock-free SPSC over shared memory for inter-process feed distribution; pitfalls (no pointers across address spaces → use offsets).

**6.7 `[core]` NUMA** — what it is, why a thread reading another node's memory pays a penalty, how `numactl`/first-touch policy/pinning fix it.

**6.8 `[stretch]` Huge pages & TLB** — TLB reach, why 2MB/1GB pages cut TLB misses for big working sets, transparent vs explicit huge pages trade-offs.

**6.9 `[stretch]` CPU isolation stack** — `isolcpus`, `nohz_full`, `rcu_nocbs`, IRQ affinity, disabling hyperthreading on hot cores, frequency governor — what each removes from your tail.

  

---

  

### Answer key / talking points — Section 6

  

- **6.4:** Multicast UDP lets the exchange send one packet that the switch fans out to all subscribers with no per-client state and minimal latency; the cost is no reliability, so feeds carry sequence numbers and you run an arbitration/gap-fill (request retransmit or use an A/B redundant feed and take whichever arrives first). Orders need reliability/ordering → TCP, with `TCP_NODELAY` to defeat Nagle (Nagle coalesces small writes to save bandwidth — exactly wrong when you want the packet out *now*).

- **6.5:** `select`/`poll` rescan the whole fd set each call (O(n)); `epoll` maintains a ready list (O(1) per ready fd). Edge-triggered fires once per state change (you must drain fully), level-triggered fires while data remains. At the very lowest latencies people skip epoll entirely and busy-poll the NIC.

  

---

  

## Section 7 — Math, Probability & Brainteasers

  

Optiver/IMC/Jane Street-style firms gate on these even for dev roles. Speed + clean reasoning matters more than exotic math.

  

**7.1 `[core]` Expected value of a die game** — You roll a die; you may re-roll once if you want, payoff = final face value. Optimal strategy and EV? (Re-roll if first ≤3; EV = 4.25.)

**7.2 `[core]` Two envelopes / conditional EV** — state the paradox and resolve it.

**7.3 `[core]` Probability of A before B** — geometric/competing-events reasoning (e.g., P(roll a 6 before a 5)).

**7.4 `[hard]` Gambler's ruin** — probability of reaching N before 0 from k with a fair/biased coin.

**7.5 `[hard]` Expected number of coin flips to get HH vs HT** — Markov chain on states; the classic "they differ — why?" (HH = 6, HT = 4).

**7.6 `[hard]` Birthday-problem style collision** — approximate when collision probability hits 50%.

**7.7 `[core]` Bayes** — false-positive medical test framing; compute posterior.

**7.8 `[hard]` Random walk / Brownian** — expected max, hitting times qualitatively (ties to your Black-Scholes background).

**7.9 `[stretch]` Make-a-market on a quantity** — they ask you to quote a bid/ask on, e.g., "number of windows in this building"; show you understand spread, inventory risk, and updating on their trades.

**7.10 `[stretch]` 100 prisoners / hat puzzles** — at least one classic combinatorial strategy puzzle; the 100-prisoners-and-boxes loop-following solution is a favorite.

  

> Method note: narrate your reasoning, define states/random variables explicitly, sanity-check with extremes. They grade the *process*.

  

---

  

### Answer key — Section 7 (spot checks)

- **7.1:** Re-roll when first roll < its-own-EV(3.5) → re-roll on 1,2,3. EV = ½·(avg of 4,5,6) + ½·3.5 = ½·5 + ½·3.5 = 4.25.

- **7.5:** HH needs 6 flips, HT needs 4 — because after a failed HH attempt (you got H then T) you've made no progress, but after H you're "primed," whereas for HT a leading H is never wasted. Set up two 3-state Markov chains and solve the linear system.

- **7.7:** posterior = (sens·prev) / (sens·prev + (1−spec)·(1−prev)); the point is that with low prevalence even a good test yields a low posterior.

  

---

  

## Section 8 — System Design (low-latency)

  

Whiteboard these end-to-end: components, data flow, where latency lives, where the lock-free boundaries are, how you'd measure and fail-safe.

  

**8.1 `[core]` Market data feed handler** — NIC (kernel bypass) → parse binary protocol → normalize → publish to strategies via SPSC/shared memory. Cover: A/B feed arbitration, sequence gap detection/recovery, zero-copy parsing, backpressure, multicast.

**8.2 `[core]` Matching engine** — order gateway → validation → matching core (single-threaded hot loop, your order book) → execution reports → market data out. Cover: why the core is single-threaded (determinism, no locks), how you scale (shard by symbol), persistence/recovery (event sourcing / sequenced journal), determinism for replay.

**8.3 `[hard]` Low-latency logging** — you must log on the hot path without paying I/O cost. Design: lock-free SPSC ring per thread → background flusher thread → deferred formatting (log the args, format off-thread). This is a known interview favorite (NanoLog-style). Why is *deferred formatting* the key trick?

**8.4 `[hard]` Risk / position keeper** — pre-trade risk checks in the order path under a tight latency budget; how to keep position state consistent without locking the hot path (single-writer, snapshot reads).

**8.5 `[hard]` Time-series / tick store** — write-heavy ingest, columnar layout, compression, fast range queries; why columnar + SoA.

**8.6 `[stretch]` Strategy framework** — plug-in strategies without virtual-call cost on the hot path (CRTP/variant), event dispatch, backtest/live parity (same code path, swap the feed/clock).

  

---

  

### Answer key / talking points — Section 8

  

- **8.2:** The matching core is single-threaded on purpose — one thread, no locks, fully deterministic so you can journal the input sequence and *replay* to reconstruct exact state (crash recovery, debugging, audit). You scale horizontally by **sharding symbols across cores/processes**, not by multithreading one book.

- **8.3:** Deferred formatting: on the hot path you only copy the raw arguments + a format-string ID into the ring buffer (a few bytes, no `printf`); the expensive `snprintf`/string work happens on the background thread. This moves ~microseconds of formatting off the critical path. Per-thread SPSC rings avoid contention; the consumer drains and writes to disk asynchronously. Bonus points: bounded ring + drop-or-block policy for overflow.

  

---

  

## Section 9 — Timed Mock Drills

  

Simulate the real thing. No notes. Speak aloud / write on paper or a bare editor (no autocomplete).

  

**Mock A — Phone/CoderPad screen (45 min)**

1. (10 min) Rapid-fire: pick 6 from Section 1's battery, answer aloud.

2. (20 min) Implement an LRU cache, all ops O(1) (5.4). Then make the node intrusive.

3. (15 min) "Now there are concurrent readers and one writer — how do you make reads lock-free?" Discuss (don't necessarily code).

  

**Mock B — C++ deep dive (60 min)**

1. (15 min) Build the SPSC ring buffer (2.5), justify every memory order.

2. (15 min) Fix the false sharing, explain MESI, estimate the saved nanoseconds (2.6).

3. (15 min) "Walk me through your order book and the cancel optimization" (4.1) — narrate the 6.7× win.

4. (15 min) Profiling story: a function got slower after a 'harmless' change — how do you find why? (perf, cache-misses counter, `perf stat`, godbolt the asm.)

  

**Mock C — Design + brainteaser (60 min)**

1. (30 min) Design a market data feed handler (8.1) end to end.

2. (15 min) Latency budget: "you have 1µs tick-to-trade — allocate it across the stages."

3. (15 min) Two brainteasers from Section 7, narrated.

  

**Mock D — Pure problem solving (45 min)**

- Trapping rain water (5.7) + sliding window max (5.2), then a cache-layout follow-up on each.

  

Score each mock with the rubric. Track which sections produce 0s and 1s and re-drill those the next morning.

  

---

  

## Section 10 — Behavioral & Market Knowledge

  

Short but they ask. Have crisp, specific answers (use *your* projects).

  

1. `[warm]` "Walk me through a performance problem you solved." → Your O(n) cancel → iterator-in-index → 6.7× story. Have the numbers.

2. `[warm]` "Most interesting bug?" → pick a concurrency or UB one; explain how you diagnosed it (sanitizers, tooling).

3. `[warm]` "Why HFT / why this firm?" → specific, not generic.

4. `[core]` "What's your debugging process for a heisenbug / a once-an-hour latency spike?" → systematic: reproduce, measure, bisect, perf counters, the jitter checklist (3.8).

5. `[core]` Basic market literacy: what is the bid-ask spread, what's a market maker's edge, what's adverse selection, what's a limit vs market order, what's latency arbitrage at a high level. You don't need to be a trader, but blank stares hurt.

6. `[warm]` "Tell me about a time you disagreed on a technical approach." → STAR format, one concrete story.

  

---

  

## Appendix — Final-week checklist & resources

  

**Two weeks out**

- [ ] Sections 1–4 at rubric 2+ across the board (these are non-negotiable for C++ HFT)

- [ ] SPSC ring buffer from memory, correct orders, in <15 min

- [ ] Order book cancel-optimization narration polished

  

**One week out**

- [ ] One timed mock per day (A→D), re-drill the 0/1 sections each morning

- [ ] Brainteasers: 30-min daily set, narrate aloud

- [ ] Reread your weak spot in *C++ Concurrency in Action* (memory model chapter)

  

**Day before**

- [ ] Light review only. Re-skim this doc's answer keys. Sleep.

  

**Resource map (you already have most)**

- *C++ Concurrency in Action* (Williams) — the memory model + lock-free chapters are your Section 2.

- Preshing on Programming — acquire/release, memory ordering intuition (Section 2/3).

- *Effective Modern C++* (Meyers) — Section 1 mechanics.

- Drepper, "What Every Programmer Should Know About Memory" — Section 3.

- Carl Cook, "When a Microsecond Is an Eternity" (CppCon) — the canonical hot-path talk.

- Optional add: agner.org optimization guides; Chandler Carruth's CppCon perf talks; "How to Build a Fast Limit Order Book" (WK Selph) for Section 4.

  

---

  

*Grind order suggestion:* 2 → 4 → 3 → 1 → 6 → 5 → 8 → 7 → 10, then mocks. Sections 2–4 are where C++ HFT offers are decided; everything else is supporting fire.