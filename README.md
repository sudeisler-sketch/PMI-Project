# PMI-Project

## Project Title
Analyzing Philip Morris International’s Stock Performance with Market and Macroeconomic Indicators

## Project Description
This project analyzes the long-term stock performance of Philip Morris International (PMI) and examines its relationship with broader market trends and selected economic indicators.

Based on the feedback received on the proposal, the project has been revised from monthly data to weekly data in order to increase the sample size and provide a stronger basis for machine learning analysis.

## Files in This Repository
- `DSA210_Project_Proposal.pdf`: project proposal
- `data_collection.py`: downloads PMI and S&P 500 weekly data and creates the merged dataset
- `pmi_weekly_project_data.csv`: cleaned and merged weekly dataset used in the analysis
- `eda.py`: exploratory data analysis and visualizations
- `hypothesis_tests.py`: statistical hypothesis tests

## Data Sources
- Yahoo Finance: PMI stock data
- Yahoo Finance: S&P 500 benchmark data

## Dataset Information
The dataset contains weekly observations from 2008 to 2026.  
Main variables include:
- Date
- PMI adjusted closing price
- PMI trading volume
- S&P 500 adjusted closing price
- PMI weekly returns
- S&P 500 weekly returns

## Milestone 1 Content
This milestone includes:
- Data collection and preparation
- Descriptive statistics and visual analysis
- Correlation analysis
- Hypothesis testing

## Main Preliminary Findings
- PMI weekly returns are statistically significantly different from zero at the 5% significance level.
- PMI weekly returns and S&P 500 weekly returns show a statistically significant positive relationship.

## How to Run
1. Install the required packages listed in `requirements.txt`
2. Run `data_collection.py`
3. Run `eda.py`
4. Run `hypothesis_tests.py`

## AI Disclosure
AI tools were used for brainstorming, debugging, structuring the analysis, and improving language. Final decisions and submission were completed by the student.

## AI Disclosure
AI tools were used for brainstorming, debugging, structuring the analysis, and improving language. Final decisions and submission were completed by the student.
