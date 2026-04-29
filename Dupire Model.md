Local volatility model for pricing options

The SDE:

$$
\frac{dS}{S} = \mu(t)dt + \sigma(S, t, S_0)dW
$$

Prove Volatility Solution:

$$
\sigma^2(K, T, S_0) = \frac{\frac{\partial C}{\partial T}}{\frac{1}{2} K^2\frac{\partial^2 C}{\partial K^2}}
$$

For Dupire model requirements:
- Interest rate curves/ yield curves - to get $r(t)$
- Matrix of option prices - $C(K_i, T_{ij})$ where i in 1 to N and j in 1 to i
- Dividend data - $q(t)$ if applicable

Methodology:
- From options prices produce the volatility surface
- Get the volatility functional form of $\sigma^2(K,T,S_0)$ 
- Use this to calculate other derivative prices

---

Topics: Derivatives, Math, Financial Engineering, [[DerivativePricing]]
Reference:
Type: #atom