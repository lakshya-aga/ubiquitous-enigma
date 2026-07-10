
Author: [[Euan Sinclair]]
Type: #source #textbook #book
Topics: [[Topics/Volatility Trading|Volatility Trading]]

---

## Chapter 1 - Option Pricing

Chapter 1 introduces how to use models.
Generally identify the assumptions. Most importantly it helps to use models for intuition building rather than quantitative risk control.
For tail risks, either trade far out of the money options or trade a small portion. Hedging will fail when jumps occur otherwise and you are left a sitting duck.
It is a good pricing method to translate price to factor and to compare options to more interpretable parameters. Also good for comparing options. AGAIN NO RISK MEASURE.

## Chapter 2 - Volatility Measurement

Types of historical vols

Close close:
$$
\sigma^\frac{1}{N-1}\sum\limits_{i=1}^N(x_i-\bar{x})
$$

Parkinson
$$
\sigma  =\sqrt{\frac{1}{4N .ln(2)}\sum\limits_{i=1}^{N}{(ln\frac{h_i}{l_{i}}})^2}
$$
Garman Klass
Rogers Stachell
Yang Zhang

#todo $\chi^2$ distribution derivation of sample volatility as a function of N
#todo How to identify bias in estimators
#todo Jensen's inequality for concave functions

