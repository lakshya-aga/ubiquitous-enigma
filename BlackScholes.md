
Most commonly used closed form solution to the pricing of options where underlying is assumed to follow a Geometric Brownian Motion.

It start with the assumption of the change in asset price being modelled as a combination of 2 terms:
$$
dS_t = \mu . S_t. dt + \sigma . S_t. dW_t
$$
It assumes a constant risk free rate: $r$

It also assumes a constant volatility: $\sigma$

To derive:

Let $$price = V(S_t, t) $$
Applying Ito's Lemma
$$ d V= \frac{\partial V}{\partial t}. dt
+ \frac{\partial V}{\partial S}.dS + \frac{1}{2}\frac{\partial^2 V}{\partial S^2}. dS^2
$$

But: from the asset price equation we can substitute dS dW.dW = dt and all other combinations are zero. This one rearrangement, we get

---

The Option PDE is given as follows:
$$ \frac{\partial V}{\partial T}
+ \frac{1}{2}\sigma ^ 2  S_t ^2. \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
$$

It can logically be broken down into Theta decay, gamma related term with volatility, risk neutral drift term, and discounting based on the risk free rate

Topics:
Reference:
Type: #atom