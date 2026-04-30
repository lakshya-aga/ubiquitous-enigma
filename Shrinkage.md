Shrinkage regularizes noisy estimates by blending them with a structured target.

For covariance:
$$
\hat{\Sigma}_{shrink} = \delta T + (1-\delta)\hat{\Sigma}
$$

Why use it
- Improves conditioning and invertibility.
- Reduces estimation error in high dimensions.
- Stabilizes [[Markowitz Weighting]] outputs.

Now the mechanics:

Start with the sample Covariance matrix S

Calculate F
$$
F = μI 
$$
(the scaled identity), where μ is the average eigenvalue of S

Then we are looking for a solution to minimise the [[Frobenius Norm]] 

$$
E[F\_Norm(\delta F + (1 - \delta)S - \Sigma)]
$$
here $\Sigma$ is the actual covariance matrix

$$
||\delta(F-S) +(S - \Sigma)||\_F \\



$$

---

Topics: "Portfolio Optimization, Covariance Estimation, Quant", [[Probability and Statistics for Finance]]
Reference: "Ledoit, O. & Wolf, M. (2004) A well-conditioned estimator for large-dimensional covariance matrices"
Type: #atom
