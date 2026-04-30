Markowitz weighting finds portfolio weights that optimize expected return vs variance.

Canonical optimization:
$$
\min_w \quad w^\top \Sigma w
$$
subject to:
$$
w^\top \mu = \mu^*, \quad \mathbf{1}^\top w = 1
$$

Key inputs:
- $(\mu)$: expected returns.
- $(\sigma)$: covariance matrix.

Practical caveat:
Small estimation errors in \(\mu,\Sigma\) can create unstable weights, so this is often paired with [[Shrinkage]] and constraints (turnover, long-only, max position).

---

Topics: "Portfolio Optimization, Quant Finance, Risk", [[Probability and Statistics for Finance]]
Reference: "Markowitz, H. (1952) Portfolio Selection"
Type: #atom
