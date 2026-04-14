import pandas as pd
from scipy import stats


df = pd.read_csv("/Users/muude/Desktop/pmi_project_data.csv")



t_stat, p_value = stats.ttest_1samp(df["PM_return"], 0)

print("Hypothesis Test 1: One-sample t-test for PMI monthly returns")
print("H0: Mean PMI monthly return = 0")
print("H1: Mean PMI monthly return != 0")
print("t-statistic:", t_stat)
print("p-value:", p_value)

if p_value < 0.05:
    print("Result: Reject H0 at 5% significance level.")
else:
    print("Result: Fail to reject H0 at 5% significance level.")

print("\n" + "-"*60 + "\n")


corr, p_value_corr = stats.pearsonr(df["PM_return"], df["SP500_return"])

print("Hypothesis Test 2: Pearson correlation test")
print("H0: No linear relationship between PMI and S&P 500 monthly returns")
print("H1: There is a linear relationship between PMI and S&P 500 monthly returns")
print("correlation coefficient:", corr)
print("p-value:", p_value_corr)

if p_value_corr < 0.05:
    print("Result: Reject H0 at 5% significance level.")
else:
    print("Result: Fail to reject H0 at 5% significance level.")