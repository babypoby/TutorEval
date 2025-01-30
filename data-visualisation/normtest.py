import math
import numpy as np
from scipy.stats import shapiro 
from scipy.stats import lognorm
from scipy.stats import ttest_rel


r1 = [ 0.121, 0.309, 0.155, 0.063, 0.053, 0.048, 0.058, 0.126, 0.725, 0.541, 0.126, 0.101, 0.058, 0.058]
r1_nex = [0.193, 0.338, 0.547, 0.058, 0.048, 0.068, 0.087, 0.261, 0.483, 0.874, 0.073, 0.087, 0.106, 0.087]

r2 = [0.684, 0.403, 0.273, 0.091, 0.104, 0.078, 0.052, 0.675, 0.489, 0.818, 0.186, 0.169, 0.126, 0.130]
r2_nex = [0.931, 0.853, 0.991, 0.169, 0.121, 0.667, 0.173, 0.896, 1, 1, 0.472, 0.844, 0.896, 0.273]

r4 = [0.54, 0.364, 0.182, 0.131, 0.131, 0.116, 0.146, 0.34, 0.424, 0.273, 0.177, 0.192, 0.131, 0.172]
r4_nex = [0.7, 0.303, 0.177, 0.197, 0.167, 0.131, 0.202, 0.727, 0.318, 0.419, 0.182, 0.146, 0.157, 0.217]

r5 = [0.65, 0.414, 0.255, 0.331, 0.318, 0.299, 0.217, 0.656, 0.408, 0.287, 0.369, 0.325, 0.363, 0.261]
r5_nex = [0.847, 0.49, 0.293, 0.414, 0.293, 0.516, 0.229, 0.834, 0.529, 0.325, 0.478, 0.382, 0.586, 0.261]

r1_detailed = [0.121, 0.309, 0.155, 0.063, 0.053, 0.048, 0.058, 0.193, 0.338, 0.547, 0.058, 0.048, 0.068, 0.087]
r1_simple = [0.126, 0.725, 0.541, 0.126, 0.101, 0.058, 0.058, 0.261, 0.483, 0.874, 0.073, 0.087, 0.106, 0.087]

r2_detailed = [0.684, 0.403, 0.273, 0.091, 0.104, 0.078, 0.052, 0.931, 0.853, 0.991, 0.169, 0.121, 0.667, 0.173]
r2_simple = [0.675, 0.489, 0.818, 0.186, 0.169, 0.126, 0.130, 0.896, 1, 1, 0.472, 0.844, 0.896, 0.273]

r4_detailed =  [0.54, 0.364, 0.182, 0.131, 0.131, 0.116, 0.146, 0.7, 0.303, 0.177, 0.197, 0.167, 0.131, 0.202]
r4_simple = [0.34, 0.424, 0.273, 0.177, 0.192, 0.131, 0.172, 0.727, 0.318, 0.419, 0.182, 0.146, 0.157, 0.217]

r5_detailed = [0.65, 0.414, 0.255, 0.331, 0.318, 0.299, 0.217, 0.847, 0.49, 0.293, 0.414, 0.293, 0.516, 0.229]
r5_simple = [0.656, 0.408, 0.287, 0.369, 0.325, 0.363, 0.261, 0.834, 0.529, 0.325, 0.478, 0.382, 0.586, 0.261]

ex = r1 + r2 + r4 + r5
nex = r1_nex + r2_nex + r4_nex + r5_nex

de = r1_detailed + r2_detailed + r4_detailed + r5_detailed
si = r1_simple + r2_simple + r4_simple + r5_simple

exnex = ex + nex
desi = de + si


#make this example reproducible
np.random.seed(1)

#perform Shapiro-Wilk test for normality
shapiro_test_ex = shapiro(exnex)
shapiro_test_de = shapiro(desi)

print(shapiro_test_ex)
print(shapiro_test_de)

# Calculate means and standard deviations
mean_ex = np.mean(ex)
mean_nex = np.mean(nex)
std_ex = np.std(ex, ddof=1)
std_nex = np.std(nex, ddof=1)

mean_de = np.mean(de)
mean_si = np.mean(si)
std_de = np.std(de, ddof=1)
std_si = np.std(si, ddof=1)

# Calculate the mean difference and standard deviation of the differences
mean_diff_ex = np.mean(np.array(nex) - np.array(ex))
std_diff_ex = np.std(np.array(nex) - np.array(ex), ddof=1)

mean_diff_de = np.mean(np.array(si) - np.array(de))
std_diff_de = np.std(np.array(si) - np.array(de), ddof=1)



# Output the results
print(f"Ex mean: {mean_ex}, Nex mean: {mean_nex}")
print(f"Ex std: {std_ex}, Nex std: {std_nex}")
print(f"De mean: {mean_de}, Si mean: {mean_si}")
print(f"De std: {std_de}, Si std: {std_si}")

# Perform a paired t-test
t_stat_ex, p_value_ex = ttest_rel(ex, nex)
t_stat_de, p_value_de = ttest_rel(de, si)

# Output the results
print(f"T-statistic ex: {t_stat_ex}")
print(f"P-value ex: {p_value_ex}")


print(f"T-statistic de: {t_stat_de}")
print(f"P-value de: {p_value_de}")

# APA report
print("\nAPA Format Report:")
print(f"A paired-sample t-test was conducted to compare the measurements before and after the treatment. The results indicated that there was a significant difference in the scores before (M = {mean_ex:.2f}, SD = {std_ex:.2f}) and after the treatment (M = {mean_nex:.2f}, SD = {std_nex:.2f}); t({len(ex)-1}) = {t_stat_ex:.2f}, p = {p_value_ex:.4f}.")

print(f"A paired-sample t-test was conducted to compare the measurements before and after the treatment. The results indicated that there was a significant difference in the scores before (M = {mean_de:.2f}, SD = {std_de:.2f}) and after the treatment (M = {mean_si:.2f}, SD = {std_si:.2f}); t({len(de)-1}) = {t_stat_de:.2f}, p = {p_value_de:.4f}.")

