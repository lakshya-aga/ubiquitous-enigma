
---
Most commonly used closed form solution to the pricing of options where underlying is assumed to follow a Geometric Brownian Motion.

It start with the assumption of the change in asset price being modelled as a combination of 2 terms:
$$
dS_t = \mu . S_t. dt + \sigma . S_t. dW_t
$$
It assumes a constant risk free rate r

It also assumes a constant volatility $$ \sigma $$
The Option PDE is given as follows:
$$ \frac{\delta V}{\delta T}
+ \frac{1}{2}.\sigma ^ 2 . S_t ^2
$$
Topics:
Reference:
Type: #atom