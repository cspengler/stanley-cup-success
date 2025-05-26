# NHL Canadian Players and Stanley Cup Success Analysis

## Project Overview

I want to learn more about machine learning, interacting with APIs, and GitHub. I also really like watching hockey. I decided to combine these aspects into a little personal learning project. My goal is to investigate the correlation between the number of Canadian players on NHL teams and their probability of winning the Stanley Cup (or at least having a deep cup run). Eventually I hope to expand to other predictors, but for now I'm focusing on a single parameter of national bragging rights.

## Research Question

**Does the percentage of Canadian players on an NHL team correlate with the team's likelihood of winning the Stanley Cup?**

## Hypothesis

Teams with a higher percentage of Canadian players may have increased chances of playoff success due to factors such as:
- Deep cultural appreciation for hockey and therefore strong desire to hoist the cup
- Higher number of players with similar backgrounds and perhaps better chemistry
- Experience with high-pressure hockey environments

But really, as an American hockey fan living in Canada, I just really want to know if the heckling I get from Canadians is justified...

## Repository Structure [planned]

```
├── data/
│   ├── raw/              # Original JSON data from NHL API
│   ├── processed/        # Cleaned, analysis-ready datasets
│   └── README.md         # Data documentation
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_analysis.ipynb
│   └── 04_modeling.ipynb
├── src/
│   ├── data_collection.py    # NHL API interface functions
│   ├── data_processing.py    # Data cleaning and feature engineering
│   ├── analysis.py           # Statistical analysis functions
│   └── utils.py              # Helper utilities
├── results/
│   ├── figures/          # Generated plots and visualizations
│   └── models/           # Trained model artifacts
└── docs/
    └── methodology.md    # Detailed methodology documentation
```

## Installation and Setup

### Prerequisites
- Python 3.8+
- pip or conda package manager

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/cspengler/stanley-cup-success.git
   cd stanley-cup-success
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Analysis
1. **Data Collection**: Start with `notebooks/01_data_collection.ipynb` to fetch NHL data
2. **Data Processing**: Clean and prepare data using `notebooks/02_data_cleaning.ipynb`
3. **Exploration**: Explore patterns in `notebooks/03_exploratory_analysis.ipynb`
4. **Modeling**: Build and evaluate models in `notebooks/04_modeling.ipynb`

### Reproducing Results
```bash
# Run complete analysis pipeline
python src/data_collection.py
python src/data_processing.py
python src/analysis.py
```

## Key Findings

*[To be updated as analysis progresses]*

### Statistical Results
- Correlation coefficient between Canadian % and Cup wins: [TBD]
- Significance tests: [TBD]

### Model Performance
- Best performing model: [TBD]
- Accuracy metrics: [TBD]
- Feature importance rankings: [TBD]

## Visualizations

Key plots and figures can be found in `results/figures/`:
- Canadian player percentage distributions
- Playoff success rates by nationality composition
- Time series trends
- Model performance comparisons

## Future Work

- Expand analysis to include additional nationalities
- Incorporate player position-specific analysis
- Add salary cap and player value considerations
- Extend to regular season performance prediction

## Contributing

This is a personal learning project, but suggestions and feedback are welcome! Please feel free to:
- Open issues for bugs or enhancement ideas
- Submit pull requests for improvements
- Share insights or alternative approaches

## License

This project is licensed under the MIT License.

---

*Last updated: 26 May 2025*
