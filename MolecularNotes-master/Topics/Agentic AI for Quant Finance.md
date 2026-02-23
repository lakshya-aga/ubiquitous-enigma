Type: #topic

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