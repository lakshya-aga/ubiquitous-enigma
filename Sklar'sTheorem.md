Sklar's theorem formalizes the separation of marginals and dependence.

For a joint CDF \(F\) with marginals \(F_1,\dots,F_d\), there exists a copula \(C\) such that:
$$
F(x_1,\dots,x_d)=C(F_1(x_1),\dots,F_d(x_d))
$$

If marginals are continuous, this copula is unique.

Why this matters:
- Model each marginal distribution separately (heavy tails, skew, etc.).
- Model dependence structure independently using a copula family.
- Build flexible multivariate models for risk and portfolio applications.

Inverse direction:
If \(C\) is a copula and \(F_1,\dots,F_d\) are valid marginals, the equation defines a valid multivariate joint distribution.

---

Topics: "[[Copula]], Probability Theory, Quant Finance" [[Probability And Statistics for Finance]]
Reference: "Sklar, A. (1959). Fonctions de repartition a n dimensions et leurs marges."
Type: #atom
