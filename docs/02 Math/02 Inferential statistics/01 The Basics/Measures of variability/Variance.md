### Definition
- The **variance** is a measure of [variability](https://www.scribbr.com/statistics/variability/). It is calculated by taking the average of squared deviations from the mean.
- Variance tells you the degree of spread in your data set. The more spread the data, the larger the variance is in relation to the [mean](https://www.scribbr.com/statistics/mean/).

### Variance vs. standard deviation

The [standard deviation](https://www.scribbr.com/statistics/standard-deviation/) is derived from variance and tells you, on average, how far each value lies from the mean. It’s the square root of variance.

Both measures reflect [variability](https://www.scribbr.com/statistics/variability/) in a distribution, but their units differ:

-   **Standard deviation** is expressed in the same units as the original values (e.g., meters).
-   **Variance** is expressed in much larger units (e.g., meters squared)

Since the units of variance are much larger than those of a typical value of a data set, it’s harder to interpret the variance number intuitively. That’s why standard deviation is often preferred as a main measure of variability.

However, the variance is more informative about variability than the standard deviation, and it’s used in making [statistical inferences](https://www.scribbr.com/statistics/inferential-statistics/).

## Population vs. sample variance

Different formulas are used for calculating variance depending on whether you have data from a whole population or a sample.

#### Population variance

When you have collected data from every member of the [population](https://www.scribbr.com/methodology/population-vs-sample/) that you’re interested in, you can get an exact value for population variance.

The **population variance** formula looks like this:

$$\sigma^2 = \frac{\Sigma(X - \mu)^2}{N}$$
$$\mathcal{Where,} \ \sigma^2 = population\ variance $$
 $$\mu = population\ mean $$
 $$N = number \ of \ records \ in\ population$$

#### Sample variance

When you collect data from a sample, the sample variance is used to make estimates or [inferences](https://www.scribbr.com/statistics/inferential-statistics/) about the population variance.

The **sample variance** formula looks like this:

$$s^2 = \frac{\Sigma(X - \hat{x})^2}{n - 1}$$
$$\mathcal{Where,} \ s^2 = sample\ variance $$
$$\hat{x} = sample\ mean $$
$$n = number \ of \ records \ in\ sample$$

With samples, we use _n_ – 1 in the formula because using n would give us a biased estimate that consistently underestimates variability. The sample variance would tend to be lower than the real variance of the population.

Reducing the sample _n_ to _n_ – 1 makes the variance artificially large, giving you an unbiased estimate of variability: it is better to overestimate rather than underestimate variability in samples.

It’s important to note that doing the same thing with the standard deviation formulas doesn’t lead to completely unbiased estimates. Since a square root isn’t a linear operation, like addition or subtraction, the unbiasedness of the sample variance formula doesn’t carry over the sample standard deviation formula.

### Steps 
1. Find the mean: To [find the mean](https://www.scribbr.com/statistics/mean/), add up all the scores, then divide them by the number of scores.
2. Find each score’s deviation from the mean: Subtract the mean from each score to get the deviations from the mean. Since x̅ = 50, take away 50 from each score.
3. Square each deviation from the mean: Multiply each deviation from the mean by itself. This will result in positive numbers.
4. Find the sum of squares: Add up all of the squared deviations. This is called the sum of squares.
5. Divide the sum of squares by _n_ – 1 or _N_: Divide the sum of the squares by _n_ – 1 (for a [sample](https://www.scribbr.com/methodology/population-vs-sample/)) or _N_ (for a population).
Since we’re working with a sample, we’ll use  _n_ – 1, where _n_ = 6.

### Variance matters for two main reasons:
-   Parametric statistical tests are sensitive to variance.
-   Comparing the variance of samples helps you assess group differences.