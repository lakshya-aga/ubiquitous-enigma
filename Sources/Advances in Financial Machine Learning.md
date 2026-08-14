Author: [[Lopez de Prado]]
Type: #source #book
Link: 
Topics: [[Finance]], Trading

---

## Review

I like the width and cases of how some of these techniques are useful. Code snippets really get rid of any ambiguity. The book needs better semantic explanations. It relies on code to actually get the algorithms across and barely touches on the why and when. Too much focus on the "how" which can be found fairly easily on demand.

Notes:

Tick Bars: Sample every X trades and sample OHLCV instead of the time intervals. More normal and stable returns than time sampling
Volume bars: Sample every X volume of traded security and sample OHLCV instead of the time intervals. More robust than ticks as one trade could be 100 shares, 10 shares or broken down for logistical reasons into multiple orders. More normal and stable returns than time sampling
Dollar bars: Sample every X money of traded security and sample OHLCV instead of the time intervals. Robust to stock splits and corporate actions. More normal and stable than time sampling

Imbalance ticks: Take the expected value of "buy" (sell) ticks where $p_t$ > $p_{t-1}$  ($p_t$ < $p_{t-1}$ ) to quantify what is the expected move. If move is deviating from the expected, you can say that an informed trader has entered.

CUSUM filters: CUSUM filters are a way to generate down-sampled data. trigger -> take rolling sum of diffs from last min. When a movement has occurred from last min over a certain threshold, mark that as an event. Start sampling at this point for possibly a triple barrier event. -> +5% change happened first, -5% change happened first or 20 days passed first, for example. denoted each by +1, -1 or 0
The positive side can be flipped to trigger a negative CUSUM filter and combined with the positive version to build the symmetric filter.

Labeling


The novel sampling techniques to build bars using dollars and volumes, did not stabilise much for me. I would attribute it to constant threshold however. [article [https://hudsonthames.org/machine-learning-trading-essentials-part-1-financial-data-structures/]] from Hudson and thames dicusses dynamic thresholding. 

After following this article, I found more normality in 20 bars per day, non splitting mid tick, and day end cutoff. These properties make volume bars possibly more informative than time bars.
## Why cusum filtering?
[[Lopez de Prado]] argues that financial data needs to be filtered using these methods to down sample to relevant observations.


Fractional Differenc