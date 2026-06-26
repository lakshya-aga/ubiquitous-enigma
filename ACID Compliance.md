Strong form of database compliance required for OLTP (Online transaction processing).

- _Atomicity_ - If one part of a transaction fails, the entire operation is rolled back, leaving the database unchanged
- _Consistency_ - always abides by rules such as balance not going below 0
- _Isolation_ - No race conditions i.e. Order of transactions is preserved
- _Durability_ - Once a transaction is successfully committed, its changes are permanent . They will survive even in the event of system crashes, power loss, or hardware failures

---

Topics:
Reference:
Type: #atom