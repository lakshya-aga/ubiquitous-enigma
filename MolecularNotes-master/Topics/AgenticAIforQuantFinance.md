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

Probability of backtest overfitting
Test with forward walk
Test with Cross Validation as backtest
Test against known benchmarks like spy 500 for equities
Autocorrelation

## Collaboration

A unified interface where all team members can scrutinise the research output, point out mistakes, flag bad code, flag look ahead bias, flag, data snooping or overfitting etc. - Critical / preference mapped as configured options
Benefit: Structured feedback generates data for improvement as well as saves time for researchers if they trust their colleagues

Standardise Data naming convention across board to prevent trivial Failure like "close" not found did you mean "CLOSE"


## Final Product:

Steroid Loaded Team of agents with Firm specific data engineering capabilities and internal tools that can build signals, apply models, model market regimes, perform trade analysis, flag any sins of quantitative trading, extract underlying assumptions and provide provenance graphs.




To do in order:
- Switch to LangGraph
- Add a Tool creation agent that adds to the internal library for data manipulation
- Add Factor Validation agent
- Understand the difficulty of Trade analysis include VWAP etc. implement if possible and sample data is available
- Feature provenance and visualisation
- Add a collaboration centric UI that lets you add comments in web interface to improve model and communicate with peers
- once everything is stable - add in a proactive agent that actively goes out, fetches new data sets or research papers for user to review
- 

AI Prompt description
```
I want to build a full agentic AI ecosystem for quant finance that takes in a user request in the form of text + any files. We can support pdf, txt, ipynb and py files.

There are several resources. First: a clear library for code manipulation like mlfinlab by Hudson and Thames. This library will be implemented in python and have docstrings. The doc strings will be used to generate documentation which in turn will be vectorised and searchable via an mcp. Additionally, the MCP will also have a function to request addition of a new tool. The request will require some sample code to be provided which the mcp will route to an agentic AI system to modularise and integrate into the ecosystem.

Second is a similar library which consolidates all data available in the organisation such as prices, alternate data etc. They are essentially wrapper functions that give a predictable output. It includes yfinance, blpapi, Fama Fetch factors etc. They are again exposed as MCPs to read the documentation around them. This too will have an agentic setup to request addition of new data sources.

Thirdly we will have a store of knowledge base which should have the pdf and txt documents. Agent should be able to look up information from this store as well.

Fourth, there will be a set of growing md files, which will extract useful insights which are good as general practice in Quant. Such as Shrinkage should be applied to covariance matrices because large number of combinations will appear to have some relationship at random.

Now for the setup.

The artifact uploaded will be classified as a research paper (send to vector store), research tool (send relevant code to the internal lib MCP), signal (save to research notebooks after validation).

We will have one developer agent to develop the internal data library.

One developer agent to develop new tools for the data manipulation library.

One planning agent to plan the notebook from user request: read access to the knowledgebase. Restrict output format to follow a structure for clear outline

One coding agent to build the notebook: will have access to the MCPs for read only, general good practices MD files, write_cell, delete_cell, edit_cell.

One test and edit agent that will run the notebook and edit notebook until notebook can run with a single run all command without errors. will have access to the MCPs for read only, general good practices MD files, write_cell, delete_cell, edit_cell. It will be allowed to install packages in the python environment as well.

Dashboard: Whenever a new signal is added via research notebooks, it should be available as an API to the dashboard to display both as a timeseries and as the current value.

Trading agent: To access the signals from the APIs and give a final trade decisions.
```

```
1) add an agent for evaluating lookahead bias, survivorship, data snooping after validation: it will only add warnings for potential "sins" After that there will be a human gate to give the green light. Adding to dashboard will happen after that. 

2) The trading agent is only a suggestion system for now. I will add proper details, risk management, position sizing later. I will also give the trading agent a comprehensive suite for microstructure analysis, signals to determine when to use stop losses etc. But that is quite far for now.

3) For the dev agent, we will have a guardrail to make it commit to an agent branch (create one if not there). Then a human gate to approve merge request.

4) Use a detailed extraction pipeline. Search the web for current implementations. I am sure there must be some good parsing tools out there that we can copy.

5) Let us add live PnL on the dashboard for each signal. Also add another agent to see the pnL, analyse it thoroughly + the research notebook(s) that produce it + current events to justify what is going right, what is going wrong and why. it should also suggest whether the strategy needs review or pause temporarily.

6) Add the suggested feature of notebook to py after the testing agent passes.

7)You can implement the docstring quality using the prompts.

8) Add a user after the classifier to route workflow below certain confidence threshold.
```