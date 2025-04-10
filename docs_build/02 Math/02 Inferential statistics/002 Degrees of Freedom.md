- **Degrees of freedom**, often represented by _v_ or _df_, is the number of independent pieces of information used to calculate a [statistic](https://www.scribbr.com/statistics/test-statistic/). It’s calculated as the sample size minus the number of restrictions.

- Degrees of freedom are normally reported in brackets beside the test statistic, alongside the results of the statistical test.

#### Example

- Suppose you randomly sample 10 American adults and measure their daily calcium intake. You use a one-sample _t_ test to determine whether the [mean](https://www.scribbr.com/statistics/mean/) daily intake of American adults is equal to the recommended amount of 1000 mg.

- The test statistic, _t_, has 9 degrees of freedom:

_df_ = _n_ − 1

_df_ = 10 − 1

_df_ = 9

- You calculate a _t_ value of 1.41 for the sample, which corresponds to a [_p_ value](https://www.scribbr.com/statistics/p-value/) of .19. You report your results:

- “The participants’ mean daily calcium intake did not differ from the recommended amount of 1000 mg, _t_(9) = 1.41, _p_ = 0.19.”

## What are degrees of freedom?

In [inferential statistics](https://www.scribbr.com/statistics/inferential-statistics/), you estimate a [parameter](https://www.scribbr.com/statistics/parameter-vs-statistic/) of a population by calculating a statistic of a sample. The number of independent pieces of information used to calculate the statistic is called the **degrees of freedom**. The degrees of freedom of a statistic depend on the sample size:

-   When the sample size is **small**, there are only a few independent pieces of information, and therefore only a few degrees of freedom.
-   When the sample size is **large**, there are many independent pieces of information, and therefore many degrees of freedom.

- Note: *Although degrees of freedom are closely related to sample size, they’re not the same thing. There are always fewer degrees of freedom than the sample size.*

- When you [estimate](https://www.scribbr.com/statistics/parameter-vs-statistic/#estimating-parameters-from-statistics) a parameter, you need to introduce **restrictions** in how values are related to each other. As a result, the pieces of information are not all independent. To put it another way, the values in the sample are not all **free to vary**.

- [The following analogy](https://www.scribbr.com/statistics/degrees-of-freedom/#dessert-analogy) and [example](https://www.scribbr.com/statistics/degrees-of-freedom/#sum-example) show you what it means for a value to be free to vary and how it’s affected by restrictions.

### Free to vary: Dessert analogy
- Imagine your roommate has a sweet tooth, so she’s thrilled to discover that your college cafeteria offers seven dessert options. One week, she decides that she wants to have a **different** dessert every day.

- By deciding to have a different dessert every day, your roommate is imposing a restriction on her dessert choices.

- On Monday, she can choose any of the seven desserts. On Tuesday, she can choose any of the six remaining dessert options. On Wednesday, she can choose any of the five remaining options, and so on.

- By Sunday, she’s had all the dessert options except one. She doesn’t have any choice to make on Sunday since there’s only one option remaining.

- Due to her restriction, your roommate could only choose her dessert on six of the seven days. Her dessert choice was free to vary on these six day. In contrast, her dessert choice on the last day wasn’t free to vary; it depended on her dessert choices of the previous six days.

### Free to vary: Sum example

Suppose I ask you to pick five integers that sum to 100.

The requirement of summing to 100 is a restriction on your number choices.

For the first number, you can choose any integer you want. Whatever your choice, the sum of the five numbers can still be 100. This is also true of the second, third, and fourth numbers.

You have no choice for the final number; it has only one possible value and it isn’t free to vary. For example, imagine you chose 15, 27, 42, and 3 as your first four numbers. For the numbers to sum to 100, the final number **needs to be** 13.

Due to the restriction, you could only choose four of the five numbers. The first four numbers were free to vary. In contrast, the fifth number wasn’t free to vary; it depended on the other four numbers.

## Degrees of freedom and hypothesis testing

The degrees of freedom of a test statistic determines the critical value of the [hypothesis test](https://www.scribbr.com/statistics/hypothesis-testing/). The critical value is calculated from the [null distribution](https://www.scribbr.com/statistics/probability-distributions/#test-hypotheses) and is a cut-off value to decide whether to reject the [null hypothesis](https://www.scribbr.com/statistics/null-and-alternative-hypotheses/#definition).

The degrees of freedom affect the critical value by changing the shape of the null distribution. The null distributions of [Student’s _t_,](https://www.scribbr.com/statistics/t-distribution/) [chi-square](https://www.scribbr.com/statistics/chi-square-distributions/), and other test statistics change with the degrees of freedom, but they each change in different ways.

### Student’s _t_ distribution

To perform a [_t_ test](https://www.scribbr.com/statistics/t-test/), you calculate _t_ for the sample and compare it to a critical value. To find the right critical value, you need to use the [Student’s _t_ distribution](https://www.scribbr.com/statistics/t-distribution/) with the appropriate degrees of freedom.

The null distribution of Student’s _t_ changes with the degrees of freedom:

-   **When** **_df_** **= 1,** the distribution is strongly [leptokurtic](https://www.scribbr.com/statistics/kurtosis/#leptokurtic), meaning the probability of extreme values is greater than in a normal distribution.
-   **As the** **_df_** **increases,** the distribution becomes narrower and less leptokurtic. It becomes increasing similar to a [standard normal distribution](https://www.scribbr.com/statistics/standard-normal-distribution/)
-   **When** **_df ≥_** **30,** Student’s _t_ distribution is almost the same as a standard normal distribution. If you have a sample size of greater than 30, you can use the standard normal distribution (also known as the _z_ distribution) instead of Student’s _t_ distribution.

![[Pasted image 20230210005746.png]]

This change in the distribution’s shape makes intuitive sense. The _t_ distribution has less spread as the number of degrees of freedom increases because the certainty of the estimate increases. Imagine repeatedly sampling the population and calculating Student’s _t_; the larger the sample size, the less the test statistic will vary between samples.

Refer: [How to Find Degrees of Freedom | Definition & Formula (scribbr.com)](https://www.scribbr.com/statistics/degrees-of-freedom/)


#### Example: Degrees of freedom and hypothesis testing

Suppose you want to use a one-sample [_t_ test](https://www.scribbr.com/statistics/t-test/) to test the [null hypothesis](https://www.scribbr.com/statistics/null-and-alternative-hypotheses/#definition) that the mean daily calcium intake of American adults is equal to the recommended amount of 1000 mg.

You take a [random sample](https://www.scribbr.com/methodology/simple-random-sampling/) of 10 adults and measure their daily calcium intake.

The one-sample _t_ test determines when a population mean is different from a certain value. However, you don’t know the population mean, so first you need to estimate it using the sample mean. You calculate that the sample mean is 820 mg.

By assuming the population mean has a certain value, you impose a restriction on the sample: the values in the sample must have a mean of 820 mg. Consequently, the final value isn’t free to vary; it only has one possible value.

For example, imagine the nine of the ten people in the sample have daily calcium intakes of 410, 1230, 870, 1110, 570, 390, 1030, 1080, and 630 mg. The tenth person must have a daily calcium intake of 880 mg for the sample to have a mean of 820 mg.

Because of the restriction, only nine values in the sample are free to vary. The test statistic, _t_, has nine degrees of freedom.

To find the critical value, you need to use the [_t_ distribution](https://www.scribbr.com/statistics/t-distribution/) for nine degrees of freedom. If the sample’s _t_ is greater than the critical value, then you reject the null hypothesis.


### Chi-square distribution

To perform a [chi-square test](https://www.scribbr.com/statistics/chi-square-tests/), you compare a sample’s chi-square to a critical value. To find the right critical value, you need to use the [chi-square distribution](https://www.scribbr.com/statistics/chi-square-distributions/) with the appropriate degrees of freedom.

The [null distribution](https://www.scribbr.com/statistics/probability-distributions/#test-hypotheses) of chi-square changes with the degrees of freedom, but in a different way than Student’s _t_ distribution:

-   **When** **_df_** **< 3,** the probability distribution is shaped like a backwards “J.”
-   **When** **_df ≥_** **3,** the probability distribution is hump-shaped, with the peak of the hump located at Χ2 = _df_ − 2. The hump is [right-skewed](https://www.scribbr.com/statistics/skewness/#right-skew), meaning that the distribution is longer on the right side of its peak.
-   **When** **_df_** **>** **90,** the chi-square distribution is approximated by a [normal distribution](https://www.scribbr.com/statistics/normal-distribution/).

![[Pasted image 20230210005837.png]]

## How to calculate degrees of freedom

The degrees of freedom of a [statistic](https://www.scribbr.com/statistics/test-statistic/) is the sample size minus the number of restrictions. Most of the time, the restrictions are [parameters](https://www.scribbr.com/statistics/parameter-vs-statistic/) that are estimated as intermediate steps in calculating the statistic.

_n_ − _r_

Where:

-   _n_ is the sample size

-   _r_ is the number of restrictions, usually the same as the number of parameters estimated

The degrees of freedom can’t be negative. As a result, the number of parameters you estimate can’t be larger than your sample size.

### Test-specific formulas

It can be difficult to figure out the number of restrictions. It’s often easier to use test-specific formulas to figure out the degrees of freedom of a test statistic.

The table below gives formulas to calculate the degrees of freedom for several commonly-used tests.

![[Pasted image 20230210005912.png]]

