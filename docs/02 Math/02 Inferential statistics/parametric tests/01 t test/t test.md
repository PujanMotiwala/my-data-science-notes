![t_test Diagram](../../../../../Excalidraw/t_test.excalidraw.svg)

### Definitions
- A **_t_ test** is a [statistical test](https://www.scribbr.com/statistics/statistical-tests/) that is used to compare the means of two groups. 
### Application
- It is often used in [hypothesis testing](https://www.scribbr.com/statistics/hypothesis-testing/) to determine whether a process or treatment actually has an effect on the population of interest, or whether two groups are different from one another.
### Example
- You want to know whether the mean petal length of iris flowers differs according to their species. You find two different species of irises growing in a garden and measure 25 petals of each species. You can test the difference between these two groups using a _t_ test and [null and alterative hypotheses](https://www.scribbr.com/statistics/null-and-alternative-hypotheses/).

-   The null hypothesis (H_0) is that the true difference between these group means is zero.
-   The alternate hypothesis (H_a) is that the true difference is different from zero.
### When to use a t test
- A _t_ test can only be used when comparing the [means](https://www.scribbr.com/statistics/mean/) of two groups (a.k.a. pairwise comparison). If you want to compare more than two groups, or if you want to do multiple pairwise comparisons, use an [ANOVA test](https://www.scribbr.com/statistics/one-way-anova/) or a post-hoc test.

- The _t_ test is a [parametric test](https://www.scribbr.com/statistics/statistical-tests/#parametric) of difference, meaning that it makes the same assumptions about your data as other parametric tests. The _t_ test assumes your data:

1.  are independent
2.  are (approximately) [normally distributed](https://www.scribbr.com/statistics/normal-distribution/)
3.  have a similar amount of variance within each group being compared (a.k.a. homogeneity of variance)

- If your data do not fit these assumptions, you can try a [nonparametric](https://www.scribbr.com/statistics/statistical-tests/#nonparametric) alternative to the _t_ test, such as the Wilcoxon Signed-Rank test for data with unequal [variances](https://www.scribbr.com/statistics/variance/).
### Types of t test
- When choosing a _t_ test, you will need to consider two things: whether the groups being compared come from a single [population](https://www.scribbr.com/methodology/population-vs-sample/) or two different populations, and whether you want to test the difference in a specific direction.

![[Pasted image 20230209165228.png]]
#### One-sample, two-sample, or paired _t_ test?

-   If the groups come from a single population (e.g., measuring before and after an experimental treatment), perform a **paired _t_ test**. This is a [within-subjects design](https://www.scribbr.com/methodology/within-subjects-design/).
-   If the groups come from two different populations (e.g., two different species, or people from two separate cities), perform a **two-sample _t_ test** (a.k.a. **independent _t_ test**). This is a [between-subjects design](https://www.scribbr.com/methodology/between-subjects-design/).
-   If there is one group being compared against a standard value (e.g., comparing the acidity of a liquid to a neutral pH of 7), perform a **one-sample _t_ test**.

#### One-tailed or two-tailed _t_ test?

-   If you only care whether the two populations are different from one another, perform a **two-tailed _t_ test**.
-   If you want to know whether one population mean is greater than or less than the other, perform a **one-tailed _t_ test.**
#### Example
- In your test of whether petal length differs by species:
	- Your observations come from two separate populations (separate species), so you perform a two-sample _t_ test.
	- You don’t care about the direction of the difference, only whether there is a difference, so you choose to use a two-tailed _t_ test.
## Performing a _t_ test

- The _t_ test estimates the true difference between two group means using the ratio of the difference in group means over the pooled [standard error](https://www.scribbr.com/statistics/standard-error/) of both groups. You can calculate it manually using a formula, or use statistical analysis software.

### _T_ test formula

- The formula for the two-sample _t_ test (a.k.a. the Student’s t-test) is shown below.
$$t = \frac{\hat{x_1} - \hat{x_2}}{\sqrt{(s^2({\frac{1}{n_1}}+{\frac{1}{n_2}}))}}$$
- In this formula, _t_ is the _t_ value, _x_1 and _x_2 are the means of the two groups being compared, _s_2 is the pooled standard error of the two groups, and _n_1 and _n_2 are the number of observations in each of the groups.

- A larger t value shows that the difference between group means is greater than the pooled standard error, indicating a more significant difference between the groups.

- You can compare your calculated _t_ value against the values in a critical value chart (e.g., [Student’s _t_ table)](https://www.scribbr.com/statistics/students-t-table/) to determine whether your _t_ value is greater than what would be expected by chance. If so, you can reject the null hypothesis and conclude that the two groups are in fact different.

### Interpreting test results
- The output provides:
	1.  An explanation of what is being compared, called **data** in the output table.
	2.  The **_t_ value**: -33.719. Note that it’s negative; this is fine! In most cases, we only care about the absolute value of the difference, or the distance from 0. It doesn’t matter which direction.
	3.  The [**degrees of freedom**](https://www.scribbr.com/statistics/degrees-of-freedom/): 30.196. Degrees of freedom is related to your sample size, and shows how many ‘free’ data points are available in your test for making comparisons. The greater the degrees of freedom, the better your statistical test will work.
	4.  The [**_p_ value**](https://www.scribbr.com/statistics/p-value/): 2.2e-16 (i.e. 2.2 with 15 zeros in front). This describes the probability that you would see a _t_ value as large as this one by chance.
	5.  A statement of the [**alternative hypothesis**](https://www.scribbr.com/statistics/null-and-alternative-hypotheses/#alternative) (_H_a). In this test, the _H_a is that the difference is not 0.
	6.  The 95% [**confidence interval**](https://www.scribbr.com/statistics/confidence-interval/). This is the range of numbers within which the true difference in means will be 95% of the time. This can be changed from 95% if you want a larger or smaller interval, but 95% is very commonly used.
	7.  The [**mean**](https://www.scribbr.com/statistics/mean/) petal length for each group.
#### Example
From the output table, we can see that the difference in means for our sample data is −4.084 (1.456 − 5.540), and the confidence interval shows that the true difference in means is between −3.836 and −4.331. So, 95% of the time, the true difference in means will be different from 0. Our _p_ value of 2.2e–16 is much smaller than 0.05, so we can **reject the null hypothesis** of no difference and say with a high degree of confidence that the **true difference in means is not equal to zero**.

### Presenting the results of a *t* test
- When reporting your _t_ test results, the most important values to include are the **_t_ value**, the **_p_ value**, and the **degrees of freedom** for the test. These will communicate to your audience whether the difference between the two groups is [statistically significant](https://www.scribbr.com/statistics/statistical-significance/) (a.k.a. that it is unlikely to have happened by chance).
- You can also include the summary statistics for the groups being compared, namely the mean and [standard deviation](https://www.scribbr.com/statistics/standard-deviation/).
#### Example
- The difference in petal length between iris species 1 (_M_ = 1.46; _SD_ = 0.206) and iris species 2 (_M_ = 5.54; _SD_ = 0.569) was significant (_t_ (30) = −33.7190; _p_ < 2.2e-16).