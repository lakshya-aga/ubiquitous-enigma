Type: #topic
[[Finance]]
## Derivatives
Nothing new just simple payoffs, when to use which. Tested 5/10 module avg 80%
## Financial Statement Analysis

## Economics

- Intro
- Monetary Policy
- Fiscal Policy
- FX
- FX Caclculations

## Quantitative Methods
- Time value of Money

## Alternative Investments
- Digital Assets
- Hedge Funds
- Real assets

## Ethics

## Equity

---

# <u>Fixed Income</u>

### Macaulay Duration: Weighted Average of time weighted by PV of cashflows on the timestamp
$$
\sum\frac{t.CF}{{(1+r)}^t}
$$
### Modified Duration:
Defined as the change in bond price for change in yield
$$
price  = \sum\frac{CF}{{(1+r)}^i}
$$
$$
\frac{dP}{dr} = \sum{\frac{t.CF}{(1+r)^{(t+1)}}}
$$
Note huge part can be substituted with MCD
 $$
 ModDuration = \frac {MCD}{1+r}
 $$
#### Dollar Value:
$ModDuration * PresentValueOfBond$ 

Note to use full value including accrued interest

### *Convexity of Bond*: 
$$
\frac{PV_+ + PV_- - 2 PV}{\Delta bps_{fromOrignal}^2*PV}
$$

actual:

$$
\frac{1}{P}\frac{dp^2}{d^2y}
$$

the one above can be derived using the definition of differentiation
$$
f''(x) = \frac{f(x+h)+f(x-h)-2f(x)}{h^2}


$$
$$
Use: +h and -h in first and second order to get to the formula
$$


Price changes due to convexity and duration can be calculated using Taylor Formula

$$
\Delta P = \frac{dP}{dy}\Delta y + \frac1 2 \frac{d^2P}{dy^2}*\Delta y^2
$$

## Effective Duration:

Change in rate of price wrt to yield
but approximated as:
$$
\frac{P(v+x)-P(v-x)}{2P(v)x} | x=\Delta y
$$


---

## Portfolio Management

Types of Funds:
- Money Market funds
- Mutual funds
- Bond funds

Formula for beta:
 $$
 \beta = \frac{\sigma_i}{\sigma_m}.\rho_{i,m}
 $$
Weighted average of risks

Teynor Ratio
$$
-
$$

M2: Wight that would make the asset risk equal to market risk
$$
\frac{\sigma_i}{\sigma_m}
$$

Jensen's Alpha
$$
-
$$


---

## Portfolio Management

Strategic Asset Allocation

Tactical Asset Allocation

Absolute Risk

Total Risk

Procedures in IPS

Appendix in IPS

##### Bias
Endowment Bias
Confirmation Bias
Status Quo
Regret Aversion
Conservatism
Framing
Mental Accounting
Halo Effect

##### Risk Management

Effective Risk Governance

Risk management framework Components

Risk Budgeting

Risk Tolerance

---

## Equities

Open end funds
Closed end funds
Warants



## Mock 1 Feedback:

Ethics: 59%
-  Make a list of all the standards and memorise
- GIPS study
- Practice Questions
Economics: 42%
- monetary transmission mechanism channels
FRA: 75%
- Sarbanes Oxeley Act
- Going Concern Projects
Quant 89%

Corp Finance 64%
- DuPont

