import scipy.stats as stats

# Kwantyl 0.95 dla rozkładu normalnego
quantile_normal = stats.norm.ppf(0.95)
print("Kwantyl 0.95 dla rozkładu normalnego:", quantile_normal)

# Kwantyl 0.95 dla rozkładu t-Studenta z 10 stopniami swobody
quantile_t = stats.t.ppf(0.95, df=10)
print("Kwantyl 0.95 dla rozkładu t-Studenta z 10 stopniami swobody:", quantile_t)

# Kwantyl 0.95 dla rozkładu chi-kwadrat z 10 stopniami swobody
quantile_chi2 = stats.chi2.ppf(0.95, df=10)
print("Kwantyl 0.95 dla rozkładu chi-kwadrat z 10 stopniami swobody:", quantile_chi2)
