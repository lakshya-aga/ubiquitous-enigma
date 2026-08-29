These models are a good unsupervised learning framework to model the state trajectory of a timeseries with the underlying assumption that the draws are done from certain sets of probability distributions.

Given a state transition matrix: A of size S x S
States: S
Prob of starting in State $S_i = \pi_i$
Probability distributions:
$P(O_j|S_i)$
Observations: 
$$O :({O_1, O_2...})$$
So given an observations set O: We can maximise the probability by adjusting the trajectory. Naively, calculate the probability of seeing the given observations for all possible state trajectories and choose the maximising trajectory: 
$$P(O_1|S_1)*\pi_1 * A_{12} * P(O_2|S_2)...$$

---

Topics: [[Machine Learning]]
Reference:
Type: #atom