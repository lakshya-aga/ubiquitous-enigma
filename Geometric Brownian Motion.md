
---

Topics: [[MolecularNotes-master/Topics/Finance|Finance]]
Reference:
Type: #atom

---

The GBM is one of the most common ways to model asset prices. This is because it enables randomness with condition of strict positive values which is required for asset prices

$$
S_t = S_0e^{X_t}
$$
where
$$
X_t = \sigma B(t) + \mu t
$$
is Brownian motion with drift

Its PDE is given by 

$$
dS_{t}= \mu S_{t}dt + \sigma S_{t}dB_t
$$

This differential sets the tone for different option pricing solutions. Most popularly the [[Black Scholes]]

