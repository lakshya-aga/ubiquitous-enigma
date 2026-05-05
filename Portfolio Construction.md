
---
Topics: [[MolecularNotes-master/Topics/Finance|Finance]], [[Probability and Statistics for Finance]]
Reference:
Type: #molecule

The most high value insight that I have derived about this is the fact that during extreme times, the correlation of portfolios tend to change to become 1 often.

In order to estimate this better we employ [[Shrinkage]] which treats covariance as sample covariance and estimates a population covariance from the given sample. The problem lies in the fact that often number of assets > or ~ number of observations. This helps is to not over rely on the estimated covariance. A harder and more precise application comes from [[Copula]] that are specifically used to model this "tail dependence"

[[Cholesky's Decomposition]] is particularly helpful in simulating price paths for correlated assets and helps do a better quantitative modelling or even price options on baskets whose constituents are correlated.