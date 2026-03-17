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

```
# Lakshya QAI — Agentic AI Ecosystem for Quant Finance

  

## System Overview

  

An agentic AI ecosystem that takes user requests (text + files: pdf, txt, ipynb, py) and orchestrates a pipeline of specialized agents for quantitative finance research, signal generation, monitoring, and trade advisory.

  

---

  

## High-Level Architecture

  

```

User Request (text + pdf/txt/ipynb/py)

        │

        ▼

┌─────────────────────┐

│   Artifact Classifier│

│   (confidence-gated) │──► confidence < threshold → ask user to confirm

└────────┬────────────┘

         │

    ┌────┴──────────┬──────────────────┐

    ▼               ▼                  ▼

Research Paper   Research Tool      Signal

    │               │                  │

    ▼               ▼                  ▼

Vector Store    Dev Agent         Notebook Pipeline

(Knowledge      (agent branch     (Plan → Code →

 Base)           + human gate)     Test → Extract →

                                   Bias Audit →

                                   Human Gate →

                                   Dashboard)

```

  

---

  

## 1. Infrastructure Layer: MCPs

  

### 1.1 QAI Tools Library MCP (mlfinlab-style)

- Python library with enforced docstring standard (params, return types, examples)

- Docstrings → auto-generated documentation → vectorized and searchable via MCP

- Read-only access for coding/testing agents

- `request_new_tool(sample_code, description)` → routes to Dev Agent (Tools)

  

### 1.2 Data Library MCP

- Wrapper functions with predictable output signatures over:

  - yfinance, blpapi, Fama-French factors, alternative data sources

- Same docstring → documentation → vector search pattern

- Read-only access for coding/testing agents

- `request_new_data_source(sample_code, description)` → routes to Dev Agent (Data)

  

### 1.3 Knowledge Base MCP

- Vector store over research papers (PDFs) and text documents

- Ingestion via structured extraction pipeline (see §3)

- Semantic search for planning and coding agents

  

### 1.4 Good Practices Store

- Growing collection of `.md` files with quant best practices

- Examples: covariance shrinkage, transaction cost modeling, regime detection caveats

- Read access for planning, coding, testing, and bias audit agents

  

---

  

## 2. Agent Layer

  

### 2.1 Artifact Classifier

- Classifies uploaded files into: **research paper**, **research tool**, **signal**

- Outputs a confidence score

- **Below confidence threshold → asks user to confirm classification**

- Routes to appropriate downstream pipeline

  

### 2.2 Dev Agent — Data Library

- Receives requests to add new data sources

- Modularizes sample code into library-standard wrapper functions

- Enforces docstring standard via prompt instructions

- **Commits to `agent/data-lib` branch (creates if not exists)**

- **Human gate: merge request requires manual approval**

  

### 2.3 Dev Agent — Tools Library

- Receives requests to add new quant tools

- Modularizes sample code into library-standard functions

- Enforces docstring standard via prompt instructions

- **Commits to `agent/tools-lib` branch (creates if not exists)**

- **Human gate: merge request requires manual approval**

  

### 2.4 Planning Agent

- **Input:** User request + read access to Knowledge Base MCP + Good Practices

- **Output:** Structured research notebook outline (enforced format)

- Output format:

  

```

## Notebook Plan

### Objective

<one-liner>

### Data Requirements

- source: <mcp_function>, frequency: <>, date_range: <>

### Methodology

- Step 1: ...

- Step 2: ...

### Expected Outputs

- figures: [...]

- tables: [...]

- signal_definition: <if applicable>

### Known Pitfalls

- <from good practices store>

```

  

### 2.5 Coding Agent

- **Input:** Structured plan from Planning Agent

- **Access:** QAI Tools MCP (read), Data Library MCP (read), Good Practices (.md)

- **Tools:** `write_cell`, `delete_cell`, `edit_cell`

- Builds the notebook cell by cell following the plan

  

### 2.6 Test & Edit Agent

- **Input:** Completed notebook from Coding Agent

- **Access:** QAI Tools MCP (read), Data Library MCP (read), Good Practices (.md)

- **Tools:** `write_cell`, `delete_cell`, `edit_cell`, `install_package`, `run_notebook`

- Runs notebook with "Run All"

- Iterates on errors until clean execution

- **On success → triggers Notebook-to-Module Extractor**

  

### 2.7 Notebook-to-Module Extractor

- **Triggered after:** Test & Edit Agent passes

- Extracts signal logic from validated notebook into a standalone `.py` module

- Module follows a standard interface:

  

```python

class Signal:

    def __init__(self, config: dict): ...

    def compute(self, as_of_date: date) -> pd.Series: ...

    def backtest(self, start: date, end: date) -> pd.DataFrame: ...

```

  

- Notebook is preserved as documentation/research artifact

- Module is what gets served via the Signal API

  

### 2.8 Bias Audit Agent

- **Triggered after:** Test & Edit Agent passes + module extraction

- **Checks for and warns about:**

  - **Lookahead bias:** Future data leaking into past computations (e.g., using full-sample statistics for normalization, forward-filled data used before publication date)

  - **Survivorship bias:** Universe construction ignoring delisted/bankrupt securities

  - **Data snooping / overfitting:** Excessive parameter tuning, no out-of-sample holdout, too many strategy variants tested without multiple-testing correction (Bonferroni, BHY)

  - **Selection bias:** Cherry-picked backtest windows, favorable market regimes only

  - **Look-ahead in features:** Using data that wouldn't have been available at signal generation time (e.g., restated financials, revised economic data)

- **Output:** Warning report with severity levels (CRITICAL / WARNING / INFO)

- **Does NOT block** — only produces warnings for human review

- **After this → Human Gate**

  

### 2.9 Human Gate (Signal Approval)

- Human reviews:

  - The research notebook

  - The extracted `.py` module

  - The Bias Audit Agent's warning report

- **Approve** → Signal goes live on Dashboard + API

- **Reject** → Feedback loops back to user/planning agent

  

### 2.10 Performance Monitor Agent

- **Runs continuously** on all live signals

- Tracks per-signal: live PnL, Sharpe ratio, drawdown, turnover

- **Analyzes:**

  - PnL attribution and decomposition

  - The original research notebook(s) that produced the signal

  - Current market events / regime context

  - What is going right and why

  - What is going wrong and why

- **Outputs:**

  - Signal health report

  - Recommendation: **CONTINUE** / **REVIEW** / **PAUSE**

  - If REVIEW or PAUSE → notifies user with justification

- Live PnL displayed on Dashboard per signal

  

### 2.11 Trading Agent (Advisory Only)

- **Current scope:** Suggestion system only — no execution

- Accesses signal values via Signal APIs

- Produces trade recommendations with rationale

- **Future additions (not in current scope):**

  - Risk management module

  - Position sizing

  - Microstructure analysis suite

  - Stop-loss signal integration

  - Execution integration with broker

  

---

  

## 3. Document Extraction Pipeline

  

Hybrid approach using best-in-class tools for each dimension:

  

### Pipeline Architecture

  

```

PDF Input

    │

    ├─► GROBID ──────────► Section-level structure

    │                       (abstract, methodology, results,

    │                        conclusions, references, authors)

    │                       Output: TEI-XML → parsed to sections

    │

    ├─► Docling ─────────► High-fidelity table extraction

    │                       (97.9% accuracy on complex tables)

    │                       Output: structured table data

    │

    └─► Nougat ──────────► Mathematical equation extraction

                            (LaTeX output)

                            Output: equations as LaTeX strings

```

  

### Merge & Embed

  

```

Parsed Sections + Tables + Equations

    │

    ▼

Section-aware chunking:

  - Abstract     → single chunk with metadata {type: "abstract"}

  - Methodology  → chunked by subsection {type: "methodology"}

  - Results      → chunked by subsection, tables as separate chunks {type: "results"}

  - Tables       → individual chunks with caption {type: "table"}

  - Equations    → grouped with surrounding context {type: "equation"}

  - References   → structured list {type: "references"}

    │

    ▼

Embedding + Vector Store (with section-type metadata for filtered search)

```

  

### Tool Selection Rationale

  

| Tool | Role | Why |

|------|------|-----|

| **GROBID** | Section structure | Purpose-built for academic papers; 68 label types; understands paper anatomy natively; production-proven at scale (ResearchGate, CERN) |

| **Docling** | Table extraction | 97.9% accuracy on complex tables (best-in-class); runs locally; MIT license; fast on CPU |

| **Nougat** | Equation parsing | Best tool for LaTeX equation extraction from PDFs; trained on arXiv/PubMed |

  

For non-PDF text files (.txt): direct chunking with overlap, no special parsing needed.

  

---

  

## 4. Dashboard

  

### Signal Dashboard

- **Per signal:**

  - Timeseries chart of signal values over time

  - Current signal value (latest)

  - Live PnL timeseries

  - Signal health status from Performance Monitor Agent (CONTINUE / REVIEW / PAUSE)

  - Link to source research notebook

  - Bias Audit warnings summary

  

### API Layer

- Each approved signal exposed as a REST API:

  - `GET /signals/{signal_id}/current` → current value

  - `GET /signals/{signal_id}/timeseries?start=&end=` → historical values

  - `GET /signals/{signal_id}/pnl?start=&end=` → PnL timeseries

  - `GET /signals/{signal_id}/health` → latest health report

- Trading Agent consumes these APIs

  

---

  

## 5. Workflow: End-to-End Signal Lifecycle

  

```

1. User uploads file + request

       │

2. Artifact Classifier (confidence-gated, user fallback)

       │

       ├── Research Paper → Extraction Pipeline → Vector Store

       ├── Research Tool  → Dev Agent → agent branch → human merge gate

       └── Signal Request ──┐

                            │

3. Planning Agent (KB + good practices) → structured outline

       │

4. Coding Agent (MCPs read-only + good practices) → notebook

       │

5. Test & Edit Agent → run all → fix errors → clean notebook

       │

6. Notebook-to-Module Extractor → Signal class in .py

       │

7. Bias Audit Agent → warning report (lookahead, survivorship, snooping)

       │

8. ═══ HUMAN GATE ═══ (review notebook + module + warnings)

       │

9. Signal API deployed + Dashboard updated

       │

10. Performance Monitor Agent (continuous)

       │    - PnL tracking + attribution

       │    - Cross-reference with research + market events

       │    - Health recommendations (CONTINUE / REVIEW / PAUSE)

       │

11. Trading Agent (advisory) → trade suggestions from signal APIs

```

  

---

  

## 6. Guardrails Summary

  

| Guardrail | Where | Type |

|-----------|-------|------|

| Confidence threshold on classification | Artifact Classifier | Automated + user fallback |

| Agent branch + merge request | Dev Agents | Automated + human gate |

| Docstring quality enforcement | Dev Agents | Prompt-enforced |

| Structured output format | Planning Agent | Prompt-enforced |

| Run-all-without-errors | Test Agent | Automated |

| Bias audit warnings | Bias Audit Agent | Automated (advisory) |

| Human approval for signal go-live | Signal Approval | Human gate |

| Signal health monitoring | Performance Monitor | Automated + human notification |

| Trading agent is advisory only | Trading Agent | Architectural constraint |

  

---

  

## 7. Tech Stack (Planned)

  

| Component | Technology |

|-----------|-----------|

| Agent framework | Claude Agent SDK |

| MCP servers | Python (FastMCP or similar) |

| PDF parsing | GROBID + Docling + Nougat |

| Vector store | TBD (ChromaDB / Qdrant / Weaviate) |

| Notebook execution | nbformat + nbconvert / Jupyter kernel |

| Dashboard | TBD (Streamlit / Dash / custom React) |

| Signal API | FastAPI |

| Version control | Git (agent branches with merge gates) |

| Python environment | conda / venv with agent install permissions |
```