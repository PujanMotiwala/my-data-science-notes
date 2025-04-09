### Import Packages
```Python
import pandas as pd
import researchpy as rp
import scipy.stats as stats
```

### Getting data
```Python
df = pd.read_csv("https://raw.githubusercontent.com/researchpy/Data-sets/master/blood_pressure.csv")
df.info()
```

### Import Packages
```Python

rp.ttest(group1= df['bp_after'][df['sex'] == 'Male'], group1_name= "Male",
         group2= df['bp_after'][df['sex'] == 'Female'], group2_name= "Female")

```

```Python
summary, results = rp.ttest(group1= df['bp_after'][df['sex'] == 'Male'], group1_name= "Male",
                            group2= df['bp_after'][df['sex'] == 'Female'], group2_name= "Female")
print(summary)
```


```Python
stats.ttest_ind(df['bp_after'][df['sex'] == 'Male'],
                df['bp_after'][df['sex'] == 'Female'])

```
Ttest_indResult(statistic=3.3479506182111387, pvalue=0.0010930222986154283)

*There is a statistically significant difference in the average post blood pressure between males and females, t= 3.3480, p= 0.001.*