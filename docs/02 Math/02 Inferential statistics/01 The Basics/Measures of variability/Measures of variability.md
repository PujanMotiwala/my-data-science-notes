- **Variability** describes how far apart data points lie from each other and from the center of a distribution. Along with measures of [central tendency](https://www.scribbr.com/statistics/central-tendency/), measures of variability give you [descriptive statistics](https://www.scribbr.com/statistics/descriptive-statistics/) that summarize your data.

- Variability is also referred to as spread, scatter or dispersion. It is most commonly measured with the following:
	-   **[Range](https://www.scribbr.com/statistics/range/):** the difference between the highest and lowest values
	-   **[Interquartile range](https://www.scribbr.com/statistics/interquartile-range/):** the range of the middle half of a distribution
	-   **[Standard deviation](https://www.scribbr.com/statistics/standard-deviation/):** average distance from the mean
	-   **[Variance](https://www.scribbr.com/statistics/variance/):** average of squared distances from the mean

### Why does variability matter?

While the [central tendency](https://www.scribbr.com/statistics/central-tendency/), or average, tells you where most of your points lie, variability summarizes how far apart they are. This is important because the amount of variability determines how well you can [generalize](https://www.scribbr.com/research-bias/generalizability/) results from the sample to your population.

Low variability is ideal because it means that you can better predict information about the [population](https://www.scribbr.com/methodology/population-vs-sample/) based on sample data. High variability means that the values are less consistent, so it’s harder to make predictions.

Data sets can have the same central tendency but different levels of variability or [vice versa](https://www.scribbr.com/definitions/vice-versa/). If you know only the central tendency or the variability, you can’t say anything about the other aspect. Both of them together give you a complete picture of your data.

### Example

#### Variability in normal distributions

You are investigating the amounts of time spent on phones daily by different groups of people.

Using [simple random samples](https://www.scribbr.com/methodology/simple-random-sampling/), you collect data from 3 groups:

-   Sample A: high school students,
-   Sample B: college students,
-   Sample C: adult full-time employees.

![[Pasted image 20230210003927.png]]

- All three of your samples have the same average phone use, at 195 minutes or 3 hours and 15 minutes. This is the x-axis value where the peak of the curves are.

- Although the data follows a [normal distribution](https://www.scribbr.com/statistics/normal-distribution/), each sample has different spreads. Sample A has the largest variability while Sample C has the smallest variability.


## Range

The **range** tells you the spread of your data from the lowest to the highest value in the distribution. It’s the easiest measure of variability to calculate.

To [find the range](https://www.scribbr.com/statistics/range/), simply subtract the lowest value from the highest value in the data set.

- Because only 2 numbers are used, the range is influenced by [outliers](https://www.scribbr.com/statistics/outliers/) and doesn’t give you any information about the distribution of values. It’s best used in combination with other measures.

Range example

You have 8 data points from Sample A.

| Data (minutes) |
| -------------- |
| 72             |
| 110            |
| 134            |
| 190            |
| 238            |
| 287            |
| 305            |
| 324            |

- The highest value (_H_) is **324** and the lowest (_L_) is **72**.

- _R_ = _H_ – _L_

- _R_ = 324 – 72 = **252**

The range of your data is **252 minutes**.

- Because only 2 numbers are used, the range is influenced by [outliers](https://www.scribbr.com/statistics/outliers/)and doesn’t give you any information about the distribution of values. It’s best used in combination with other measures.

## Interquartile range

The **[interquartile range](https://www.scribbr.com/statistics/interquartile-range/)** gives you the spread of the middle of your distribution.

For any distribution that’s ordered from low to high, the interquartile range contains half of the values. While the first [quartile](https://www.scribbr.com/statistics/quartiles-quantiles/) (Q1) contains the first 25% of values, the fourth quartile (Q4) contains the last 25% of values.

![[Pasted image 20230210004328.png]]

- The interquartile range is the third quartile (Q3) minus the first quartile (Q1). This gives us the range of the middle half of a data set.

#### Example

To find the **interquartile range** of your 8 data points, you first find the values at Q1 and Q3.

Multiply the number of values in the data set (8) by 0.25 for the 25th percentile (Q1) and by 0.75 for the 75th percentile (Q3).

Q1 position: 0.25 x 8 = 2

Q3 position: 0.75 x 8 = 6

Q1 is the value in the 2nd position, which is **110**. Q3 is the value in the 6th position, which is **287**.

IQR = Q3 – Q1

IQR = 287 – 110 = **177**

The interquartile range of your data is **177 minutes**.

- Just like the range, the interquartile range uses only 2 values in its calculation. But the IQR is less affected by [outliers](https://www.scribbr.com/statistics/outliers/): the 2 values come from the middle half of the data set, so they are unlikely to be extreme scores.

- The IQR gives a consistent measure of variability for [skewed](https://www.scribbr.com/statistics/skewness/) as well as normal distributions.

### Five-number summary

Every distribution can be organized using a **five-number summary**:

-   Lowest value
-   Q1: 25th percentile
-   Q2: the [median](https://www.scribbr.com/statistics/median/)
-   Q3: 75th percentile
-   Highest value (Q4)

These five-number summaries can be easily visualized using box and whisker plots.

Box and whisker plot example

For each of our samples, the horizontal lines in a box show Q1, the median and Q3, while the whiskers at the end show the highest and lowest values.

![[Pasted image 20230210004503.png]]

## Standard deviation

The **[standard deviation](https://www.scribbr.com/statistics/standard-deviation/)** is the average amount of variability in your dataset.

It tells you, on average, how far each score lies from the mean. The larger the standard deviation, the more variable the data set is.

There are six steps for finding the standard deviation by hand:

1.  List each score and [find their mean](https://www.scribbr.com/statistics/mean/).
2.  Subtract the mean from each score to get the deviation from the mean.
3.  Square each of these deviations.
4.  Add up all of the squared deviations.
5.  Divide the sum of the squared deviations by _n_ – 1 (for a [sample](https://www.scribbr.com/methodology/population-vs-sample/)) or _N_ (for a population).
6.  Find the square root of the number you found.

![[Pasted image 20230210004609.png]]

![[Pasted image 20230210004631.png]]

![[Pasted image 20230210004649.png]]

### Standard deviation formula for populations

If you have data from the entire population, use the population standard deviation formula:
![[Pasted image 20230210004709.png]]

### Standard deviation formula for samples

If you have data from a sample, use the sample standard deviation formula:
![[Pasted image 20230210004725.png]]

### Why use _n_ – 1 for sample standard deviation?
[Samples](https://www.scribbr.com/methodology/population-vs-sample/) are used to make [statistical inferences](https://www.scribbr.com/statistics/inferential-statistics/) about the population that they came from.

When you have population data, you can get an exact value for population standard deviation. Since you [collect data](https://www.scribbr.com/methodology/data-collection/) from every population member, the standard deviation reflects the precise amount of variability in your distribution, the population.

But when you use sample data, your sample standard deviation is always used as an estimate of the population standard deviation. Using _n_ in this formula tends to give you a biased estimate that consistently underestimates variability.

Reducing the sample _n_ to _n_ – 1 makes the standard deviation artificially large, giving you a conservative estimate of variability.

While this is not an unbiased estimate, it is a less biased estimate of standard deviation: it is better to overestimate rather than underestimate variability in samples.

The difference between biased and conservative estimates of standard deviation gets much smaller when you have a large sample size.
