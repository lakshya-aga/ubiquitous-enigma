
Author: [[Euan Sinclair]]
Type: #source #textbook #book
Topics: [[Topics/Volatility Trading|Volatility Trading]]

---

## Option Pricing

Chapter 1 introduces how to use models.
Generally identify the assumptions. Most importantly it helps to use models for intuition building rather than quantitative risk control.
For tail risks, either trade far out of the money options or trade a small portion. Hedging will fail when jumps occur otherwise and you are left a sitting duck.
It is a good pricing method to translate price to factor and to compare options to more interpretable parameters. Also good for comparing options. AGAIN NO RISK MEASURE.

## Volatility Measurement

Types of historical vols

Close close:
$$
\sigma^{2}= \frac{1}{N-1}\sum\limits_{i=1}^N(x_i-\bar{x})
$$

Parkinson
$$
\sigma  =\sqrt{\frac{1}{4N .ln(2)}\sum\limits_{i=1}^{N}{(ln\frac{h_i}{l_{i}}})^2}
$$
Garman Klass
$$
\sigma ^{2}= \frac{1}{N}\sum\limits_{i=1}^{N}{\frac{1}{2}(ln\frac{h}{l})^2} - \frac{1}{N}\sum\limits_{i=1}^{N}(2ln2-1)(ln\frac{c}{c_{i-1}})^2
$$
Rogers Stachell

$$
\sigma^2 = \frac{1}{N}\sum\limits{ln(\frac{h}{o}).ln\left(\frac{h}{c}\right)+ ln(\frac{l}{c}).ln(\frac{l}{o})}
$$
Yang Zhang: some weighted average formula, will likely be unable to remember unless derived



#todo $\chi^2$ distribution derivation of sample volatility as a function of N [[Chi Squared Distribution]]
#todo How to identify bias in estimators
#todo Jensen's inequality for concave functions
#todo Derive Parkinson's estimators and build intuition about them
#todo Derive Garman Klass' estimators and build intuition about them
#todo Derive Yang Zhang estimators and build intuition about them


## Volatility Forecasting

For forecasting 
- Take mean of last N days -> plateaued vols until jump slides out of window -> bad
- EWMA -> doesn't make any sense for earnings release as it implies something like that will happen again in smaller magnitude such as a small earnings release, followed by a smaller and smaller one each day. More correct way would be to take it out or price it in properly.
- GARCH:
$$
\sigma_t^{2}= \gamma V + \alpha \sigma_{t-1}^{2}+ \beta r_{t-1}^{2}
$$
$\alpha+\beta+\gamma=1$
here V = long term variance, sigma and r are volatility and returns respectively

#todo understand the rationale behind the overlap adjustment formula

## Trade Logging

Taking trade logs and regularly adjusting for the target is important. It is also important to have your backtest data well defined with different risk params that you can check whether the observed drawdowns and volatility in returns is within expectations. Use a variety of metrics - Hurst exponential, Calmar ratio, Sharpe, MDD and Sortino.
Regularly check your systems, brokerage fees etc. edge is but a haircut.
## Psychology

Sinclair does a great job here to flip the script. Traders are nervous or under confident usually because of lack of preparedness. There is no trader who will master psychology but be bad at trading that can make money either. The biases are important indicators. Additionally, always have "good" trades. i.e. well-reasoned trades that may not necessarily make profits. As long as trades are well-reasoned, they may be scrutinised and reviewed for improvements or can more correctly be attributed to bad luck if applicable.

