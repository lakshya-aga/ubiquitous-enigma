Shrinkage regularizes noisy estimates by blending them with a structured target.

For covariance:
$$
\hat{\Sigma}_{shrink} = \delta T + (1-\delta)\hat{\Sigma}
$$
where:
- \(\hat{\Sigma}\): sample covariance
- \(T\): target matrix (e.g., diagonal or constant-correlation)
- \(\delta \in [0,1]\): shrinkage intensity

Why use it:
- Improves conditioning and invertibility.
- Reduces estimation error in high dimensions.
- Stabilizes [[MarkowitzWeighting]] outputs.

---

Topics: "Portfolio Optimization, Covariance Estimation, Quant"
Reference: "Ledoit, O. & Wolf, M. (2004) A well-conditioned estimator for large-dimensional covariance matrices"
Type: #atom
