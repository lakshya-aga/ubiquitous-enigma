Objective: Creating safe state transitions for industry use cases where safety is critical

Current gap: Models need to know about the state transition dynamics for evaluation

Methodolgy:

The paper formulates the problem as a CCP (Chance Constraint Programming) problem with different barrier certificates. For simplicity assume these are just params representing the allowed probability of constraint violation. Constraint violation - ending up in an unsafe space, the CCP constraint.


### MDP parameters:

(S,A, T, R, $\gamma$ , H) -> 
- state,
- action, 
- T is a function that determines the transition probability to a state given a state-action $[S\times A\times S]$ -> `[0, 1]`
- R -> expected reward `[S x A]`
- $\gamma$ is discount factor for discounting rewards for future times
- H -> length of episode ( I guess number of steps agent is allowed to take or something)

---
Author: [[Dr. Mohit Prashant]]
Type: #source #textbook
Topics: [[Reinforcement Learning]]
