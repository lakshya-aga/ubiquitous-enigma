Sinkhorn operator is used to soften hard permutations. Sinkhorn is actually just the iterative process to get the doubly stochastic matrix.
But to apply this to a unitary matrix, we use a temperature scaling
So matrix X becomes exp(X/tau) where tau is the temperature. Lower temps collapse towards a single choice.
Higher temps almost makes it uniform.

