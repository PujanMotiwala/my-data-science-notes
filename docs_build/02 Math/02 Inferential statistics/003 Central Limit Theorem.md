The **central limit theorem** states that if you take sufficiently large samples from a population, the samples’ means will be [normally distributed](https://www.scribbr.com/statistics/normal-distribution/), even if the population isn’t normally distributed.

### Example
A **population** follows a [**Poisson distribution**](https://www.scribbr.com/statistics/poisson-distribution/) (left image). If we take 10,000 **samples** from the population, each with a sample size of 50, the sample means follow a normal distribution, as predicted by the **central limit theorem** (right image).

![[Pasted image 20230210010102.png]]

## What is the central limit theorem?

The central limit theorem relies on the concept of a **sampling distribution**, which is the [probability distribution](https://www.scribbr.com/statistics/probability-distributions/) of a **statistic** for a large number of [samples](https://www.scribbr.com/methodology/population-vs-sample/) taken from a population.

Imagining an experiment may help you to understand sampling distributions:

-   Suppose that you draw a [random sample](https://www.scribbr.com/methodology/simple-random-sampling/) from a population and calculate a [statistic](https://www.scribbr.com/statistics/parameter-vs-statistic/) for the sample, such as the mean.
-   Now you draw another random sample of the same size, and again calculate the [mean](https://www.scribbr.com/statistics/mean/).
-   You repeat this process many times, and end up with a large number of means, one for each sample.

The distribution of the sample means is an example of a **sampling distribution.**

The central limit theorem says that the sampling distribution of the mean will always be **normally distributed**, as long as the sample size is large enough. Regardless of whether the population has a normal, Poisson, binomial, or any other distribution, the sampling distribution of the mean will be normal.

A normal distribution is a symmetrical, bell-shaped distribution, with increasingly fewer observations the further from the center of the distribution.

## Central limit theorem formula

Fortunately, you don’t need to actually repeatedly sample a population to know the shape of the sampling distribution. The [parameters](https://www.scribbr.com/statistics/parameter-vs-statistic/) of the sampling distribution of the mean are determined by the parameters of the population:

-   The [mean](https://www.scribbr.com/statistics/mean/) of the sampling distribution is the mean of the population.

  ![\begin{equation*}\mu_{\bar{x}}=\mu\end{equation*}](https://cdn.scribbr.com/wp-content/ql-cache/quicklatex.com-7f19c78f3ab7a25bf9edd19b8ba36367_l3.png "Rendered by QuickLaTeX.com")

-   The [standard deviation](https://www.scribbr.com/statistics/standard-deviation/) of the sampling distribution is the standard deviation of the population divided by the square root of the sample size.

  ![\begin{equation*}\sigma_{\bar{x}} = \dfrac{\sigma}{\sqrt{n}}\end{equation*}](https://cdn.scribbr.com/wp-content/ql-cache/quicklatex.com-6443a361247d9c6f5764e4503e390634_l3.png "Rendered by QuickLaTeX.com")

We can describe the sampling distribution of the mean using this notation:

  ![\begin{equation*}\bar{X}\sim N (\mu,\dfrac{\sigma}{\sqrt{n}})\end{equation*}](https://cdn.scribbr.com/wp-content/ql-cache/quicklatex.com-34ffb4548c9499a6e0972093a9d2b1ae_l3.png "Rendered by QuickLaTeX.com")

Where:

-   X̄ is the sampling distribution of the sample means
-   ~ means “follows the distribution”
-   _N_ is the [normal distribution](https://www.scribbr.com/statistics/normal-distribution/)
-   µ is the mean of the population
-   σ is the standard deviation of the population
-   _n_ is the sample size

## Sample size and the central limit theorem

The **sample size** (_n_) is the number of observations drawn from the population for each sample. The sample size is the same for all samples.

The sample size affects the sampling distribution of the mean in two ways.

### 1. Sample size and normality

The larger the sample size, the more closely the sampling distribution will follow a [normal distribution](https://www.scribbr.com/statistics/normal-distribution/).

When the sample size is small, the sampling distribution of the mean is sometimes non-normal. That’s because the central limit theorem only holds true when the sample size is “sufficiently large.”

By convention, we consider a sample size of 30 to be “sufficiently large.”

-   **When** **_n_** **< 30**, the central limit theorem doesn’t apply. The sampling distribution will follow a similar distribution to the population. Therefore, the sampling distribution will only be normal if the population is normal.

-   **When** **_n_** **≥ 30**, the central limit theorem applies. The sampling distribution will approximately follow a normal distribution.

### 2. Sample size and standard deviations

The sample size affects the standard deviation of the sampling distribution. Standard deviation is a measure of the [variability](https://www.scribbr.com/statistics/variability/) or spread of the distribution (i.e., how wide or narrow it is).

-   **When** **_n_** **is low**, the standard deviation is high. There’s a lot of spread in the samples’ means because they aren’t precise estimates of the population’s mean.

-   **When** **_n_** **is high**, the [standard deviation](https://www.scribbr.com/statistics/standard-deviation/) is low. There’s not much spread in the samples’ means because they’re precise estimates of the population’s mean.

## Conditions of the central limit theorem

The central limit theorem states that the sampling distribution of the mean will always follow a [normal distribution](https://www.scribbr.com/statistics/normal-distribution/) under the following conditions:

1.  The sample size is **sufficiently large**. This condition is usually met if the sample size is _n_ ≥ 30.

2.  The samples are **independent and identically distributed (i.i.d.) random variables**. This condition is usually met if the [sampling is random](https://www.scribbr.com/methodology/simple-random-sampling/).

3.  The population’s distribution has **finite** [**variance**](https://www.scribbr.com/statistics/variance/). Central limit theorem doesn’t apply to distributions with infinite variance, such as the Cauchy distribution. Most distributions have finite variance.

## Importance of the central limit theorem

The central limit theorem is one of the most fundamental statistical theorems. In fact, the “central” in “central limit theorem” refers to the importance of the theorem.

Note: *[**Parametric tests**](https://www.scribbr.com/statistics/statistical-tests/#parametric), such as [_t_ tests](https://www.scribbr.com/statistics/t-test/), [ANOVAs](https://www.scribbr.com/statistics/one-way-anova/), and [linear regression](https://www.scribbr.com/statistics/simple-linear-regression/), have more statistical power than most [non-parametric tests](https://www.scribbr.com/statistics/statistical-tests/#nonparametric). Their [statistical power](https://www.scribbr.com/statistics/statistical-power/) comes from assumptions about populations’ distributions that are based on the central limit theorem.*


## Central limit theorem examples

Applying the central limit theorem to real distributions may help you to better understand how it works.

### Continuous distribution

Suppose that you’re interested in the age that people retire in the United States. The [**population**](https://www.scribbr.com/methodology/population-vs-sample/) is all retired Americans, and the distribution of the population might look something like this:

![[Pasted image 20230210010203.png]]

Age at retirement follows a [left-skewed](https://www.scribbr.com/statistics/skewness/#left-skew) distribution. Most people retire within about five years of the mean retirement age of 65 years. However, there’s a “long tail” of people who retire much younger, such as at 50 or even 40 years old. The population has a standard deviation of 6 years.


![[Pasted image 20230210010309.png]]

If you repeat the procedure many more times, a histogram of the sample means will look something like this:

![[Pasted image 20230210010359.png]]

Although this sampling distribution is more normally distributed than the population, it still has a bit of a [left skew](https://www.scribbr.com/statistics/normal-distribution/).

Notice also that the spread of the sampling distribution is less than the spread of the population.

The **central limit theorem** says that the sampling distribution of the mean will always follow a normal distribution when the sample size is sufficiently large. This sampling distribution of the mean isn’t normally distributed because its sample size isn’t sufficiently large.

Now, imagine that you take a large sample of the population. You randomly select 50 retirees and ask them what age they retired.


![[Pasted image 20230210010436.png]]

![[Pasted image 20230210010503.png]]
![[Pasted image 20230210010607.png]]

The population mean is the proportion of people who are left-handed (0.1). The population standard deviation is 0.3.

Imagine that you take a [random sample](https://www.scribbr.com/methodology/simple-random-sampling/) of five people and ask them whether they’re left-handed.

Example: Central limit theorem; sample of _n_ = 5

0

0

0

1

0

The mean of the sample is an estimate of the population mean. It might not be a very precise estimate, since the sample size is only 5.  

Example: Central limit theorem; mean of a small sample

mean = (0 + 0 + 0 + 1 + 0) / 5

mean = 0.2

Imagine you repeat this process 10 times, randomly sampling five people and calculating the mean of the sample. This is a **sampling distribution of the mean**.

Example: Central limit theorem; means of 10 small samples

0

0

0.4

0.2

0.2

0

0.4

0

If you repeat this process many more times, the distribution will look something like this:

![Central Limit Theorem - Theorem-discrete-distribution](https://cdn.scribbr.com/wp-content/uploads/2022/07/central-limit-theorem-small-samples.png)

The sampling distribution isn’t normally distributed because the sample size isn’t sufficiently large for the central limit theorem to apply.

As the sample size increases, the sampling distribution looks increasingly similar to a normal distribution, and the spread decreases:

-   [_n_ = 10](https://www.scribbr.com/statistics/central-limit-theorem/#)
 -   [_n_ = 20](https://www.scribbr.com/statistics/central-limit-theorem/#)
 -   [_n_ = 30](https://www.scribbr.com/statistics/central-limit-theorem/#)
 -   [_n_ = 100](https://www.scribbr.com/statistics/central-limit-theorem/#)

![Central Limit Theorem - n=10](https://cdn.scribbr.com/wp-content/uploads/2022/07/central-limit-theorem-n10.png)

The sampling distribution of the mean for samples with _n_ = 30 approaches normality. When the sample size is increased further to _n_ = 100, the sampling distribution follows a normal distribution.

We can use the central limit theorem formula to describe the sampling distribution for _n_ = 100.

![\bar{X} \sim N (\mu,\dfrac{\sigma}{\sqrt{n}})](https://cdn.scribbr.com/wp-content/ql-cache/quicklatex.com-8a8299367f3bafc9ded6b4b151f2cbc6_l3.png "Rendered by QuickLaTeX.com")

µ = 0.1

σ = 0.3

_n_ = 100

![\bar{X} \sim N (0.1,\dfrac{0.3}{\sqrt{100}})](https://cdn.scribbr.com/wp-content/ql-cache/quicklatex.com-d9b84c5604bb23b5830a2deee4872381_l3.png "Rendered by QuickLaTeX.com")

![\bar{X} \sim N (0.1,0.03)](https://cdn.scribbr.com/wp-content/ql-cache/quicklatex.com-3e8ab9abb7207f6044a9873b22db8681_l3.png "Rendered by QuickLaTeX.com")



- [Central Limit Theorem | Formula, Definition & Examples (scribbr.com)](https://www.scribbr.com/statistics/central-limit-theorem/)