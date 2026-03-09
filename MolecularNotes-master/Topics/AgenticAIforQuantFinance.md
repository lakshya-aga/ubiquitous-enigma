Type: #topic

---

The Current Problem of agentic AI in quant finance is identified as follows:
- Quant researchers using AI for trading are limited by the scope of documentation and reusability of internal tools
- For example a researcher understands his or her own process of processing a problem - they generally throw clustering algorithms like [[OPTICS]] or [[Hierarchical Clustering]] based on some [[greedy heuristics]]. That is they sort of know a path to be taken in the Maze
- The agentic AI will not be personalised to them if used in a chat fashion. So the idea is as follows:
	- Setup an [MCP for the agent to search internal tools](https://github.com/lakshya-aga/fruit-thrower)
	- Setup a proper instructions file personalised to the researcher so a general pattern may be extrapolated
Desired Setup:
	- Agents currently use raw numbers via MCPs to make trade decisions. We get rid of guessing and give a ***trader agent*** access to proprietary quant research which it can pick, choose and execute to get information via graphs, p-values etc.
	- We give ***Research agents*** access to internal libraries and data via MCP to find, generate and test hypothesis.
	- We give a ***Developer agent*** access to any piece of literature that we come across to build tools e.g. Advances in financial machine learning, Hudson and thames Libraries
	- The trickiest part is to get the Research agent right - leakage, lookahead bias, overfitting are silent killers which will trickle down to trader as well

Current status:
- MCP for library code setup
To do:
- High Priority
	- Add MCP connection tool for the research agent
- Low Priority
	- Add a tool for researcher to request new function to be added to library if implementation would be more than 10 lines and reusability is high
- Target
	- Simulate the probability of backtesting overfitting paper

Full AI powered hedge fund below![[IMG_20260308_125014565 (1) (1) (1).jpg]]

Current Job:

Test against Claude Code

Next Improvements:
## Adding New Workflows
- Add an extraction and classifier layer first - fetches the content as per user request and breaks down into 1 of the following workflows:
	1. Signal Extraction
	2. Tool building
	3. Regime Modelling
	4. Setup an event monitoring, insight generator and possibly trade executioner - such as 
		- earnings release,
		- tariff announcements
		- missile launch 
	5. Execution cost / Hypothetical Trade analysis with liquidity constraints
		- order logs
		- fill data
		- quote/trade market data
		- clear benchmark definition, such as arrival price, VWAP, implementation shortfall
	6. Factor validation
		- Use backtests, robustness and Probability of overfitting
		- Check correlation with known factors
		- Test across time, sectors, regions, liquidity buckets
		- Evaluate turnover, decay, implementation feasibility
		- Compare against benchmarks with similar risk profiles
## Switching to LangGraph

- More models - apparently GPT is moving backwards

## Building Tests that Claude code cannot do




## Research-state awareness across a notebook

Not just editing cells, but understanding the notebook as a research object.

For example:

- which cells are data loading, feature engineering, labelling, modelling, evaluation
- which variables are “authoritative” outputs
- whether a change invalidates downstream cells
- whether results shown later were produced before or after a material code change
- whether the notebook is still internally consistent

## Auditable

Feature Provenance. Find a way? Any other way: track dependency till API call top-down

## Lookahead Bias flagging

See the feature provenance to check if the information was available at the time. Would the same universe be chose if it was done today.

## Evaluation System

P of backtest overfitting
Test with forward walk
Test with CV
Test against known benchmarks
Autocorrelation

## Collaboration

A unified interface where all team members can scrutinise the research output, point out mistakes, flag bad code, flag look ahead bias, flag, data snooping or overfitting etc. - Critical / preference mapped as configured options
Benefit: Structured feedback generates data for improvement as well as saves time for researchers if they trust their colleagues

Standardise Data naming convention across board to prevent trivial Failure like "close" not found did you mean "CLOSE"


## Final Product:

Steroid Loaded Team of agents with Firm specific data engineering capabilities and internal tools that can build signals, apply models, model market regimes, perform trade analysis, flag any sins of quantitative trading, extract underlying assumptions and provide provenance graphs.




To do in order:
- Switch to langgraph
- Add a tool creation agent
- Add Factor Validation agent
- Understand the difficulty of Trade analysis include VWAP etc. implement if possible and sample data is available
- Feature provenance and visualisation
- 