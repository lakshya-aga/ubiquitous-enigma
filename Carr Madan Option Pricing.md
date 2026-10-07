The method that enables us to use Fast Fourier Transform for pricing multiple strikes and build volatility smiles efficiently.

Start with price formula as payoff

$$
C = e^{-rT}E[(S-K)^+]
$$
Here we need $q_c(s)$ - the pdf in order to do the pricing
Let s=log S and k = log K

$$
C = e^{-rT} \int_{k}^{\infty}{q(s).(e^s−e^k)}ds
$$
lower limit is taken as k since otherwise option price is 0

This is somewhat hard to evaluate, thus we


---


citation: https://www.ma.imperial.ac.uk/~ajacquie/IC_Num_Methods/IC_Num_Methods_Docs/Literature/CarrMadan.pdf
Type: #source #academic 
Topics: [[Derivative Pricing]]


