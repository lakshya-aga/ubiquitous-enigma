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


![[Pasted image 20260625110030.png]]
I don't quite get this part because safety of car in the example can be modelled as being at 100 kmph, 110 kmph as the state. Is it trying to say that 0-100 in 3 seconds is more dangerous than say 0-100 in 30 seconds and we can model that using this new methodology?


Actual experiment is run on CartPole (simple balancing 4 variables) and ANT (more complex 27 variables) RL environments

![[Pasted image 20260625113711.png]]
What is $U$ here?
#todo algorithm tracing to understand methodology


---
Author: [[Dr. Mohit Prashant]], [[Dr. Adrvind Easwaran]]
Type: #source #academic
Topics: [[Reinforcement Learning]]
