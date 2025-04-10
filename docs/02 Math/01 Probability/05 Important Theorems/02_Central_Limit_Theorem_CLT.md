# Central Limit Theorem (CLT)

## Definition / Introduction
*   The Central Limit Theorem (CLT) is one of the most remarkable and important results in probability theory and statistics.
*   It states that, under certain conditions, the **distribution of the sum (or average) of a large number of independent random variables** will be approximately a **[[05_Normal_Gaussian_Distribution|Normal (Gaussian) distribution]]**, **regardless of the original distribution** from which the variables were drawn.
*   This explains why the Normal distribution appears so frequently in nature and statistical practice.

## Key Concepts

### 1. The Core Idea
*   Let $X_1, X_2, ..., X_n$ be a sequence of independent and identically distributed (i.i.d.) random variables, each with a finite mean $\mu$ and a finite non-zero variance $\sigma^2$.
*   Consider the **sample mean:** $\bar{X}_n = \frac{X_1 + X_2 + \dots + X_n}{n}$.
    *   From [[01_Expected_Value|linearity of expectation]], $E[\bar{X}_n] = \mu$.
    *   From [[02_Variance_and_Standard_Deviation|properties of variance]] (for i.i.d. variables), $Var(\bar{X}_n) = Var\left(\frac{\sum X_i}{n}\right) = \frac{1}{n^2} \sum Var(X_i) = \frac{1}{n^2} (n\sigma^2) = \frac{\sigma^2}{n}$.
    *   The standard deviation of the sample mean (also called the [[../02 Inferential statistics/Estimation/Standard error|Standard Error]]) is $SD(\bar{X}_n) = \sqrt{\frac{\sigma^2}{n}} = \frac{\sigma}{\sqrt{n}}$.
*   The CLT states that as the sample size $n$ becomes sufficiently large ($n \to \infty$), the **distribution of the sample mean $\bar{X}_n$** approaches a Normal distribution with mean $\mu$ and variance $\sigma^2/n$:
    $$ \bar{X}_n \xrightarrow{\text{approx}} N\left(\mu, \frac{\sigma^2}{n}\right) \quad \text{as } n \to \infty $$
*   Equivalently, the distribution of the **standardized sample mean** approaches the Standard Normal distribution $N(0, 1)$:
    $$ Z_n = \frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \xrightarrow{\text{distribution}} N(0, 1) \quad \text{as } n \to \infty $$
*   The theorem also applies to the **sum** $T_n = X_1 + \dots + X_n$. Since $E[T_n] = n\mu$ and $Var(T_n) = n\sigma^2$, the sum approaches $N(n\mu, n\sigma^2)$.

### 2. Conditions
*   **Independence:** The random variables must be independent.
*   **Identically Distributed:** They should be drawn from the same distribution. (This can be relaxed in some versions, e.g., Lindeberg-Lévy CLT requires finite variance and a condition on tail probabilities, but i.i.d. is standard).
*   **Finite Mean and Variance:** The underlying distribution must have a well-defined, finite mean $\mu$ and a finite variance $\sigma^2 > 0$.
*   **Sufficiently Large $n$:** The theorem describes convergence as $n \to \infty$. In practice, "sufficiently large" depends on the shape of the original distribution.
    *   If the original distribution is already symmetric and roughly bell-shaped, smaller $n$ (e.g., $n \ge 15$) might suffice.
    *   If the original distribution is highly skewed, a larger $n$ (e.g., $n \ge 30$ or even $n \ge 50$) might be needed for the approximation to be reasonably good.

### 3. Significance: Why the Normal Distribution is Everywhere
*   Many real-world variables can be thought of as the sum or average of numerous small, independent factors (e.g., height influenced by many genes and environmental factors, measurement errors resulting from many small disturbances). The CLT provides a theoretical reason why such variables often exhibit a Normal distribution.

### 4. Contrast with Law of Large Numbers (LLN)
*   **[[01_Law_of_Large_Numbers_LLN|LLN]]:** Describes the convergence of the *value* of the sample mean $\bar{X}_n$ to a single number (the true mean $\mu$). It tells us *where* the average is heading. $\bar{X}_n \to \mu$.
*   **CLT:** Describes the convergence of the *shape of the distribution* of the sample mean $\bar{X}_n$ (or sum $T_n$) to a specific distribution (the Normal distribution). It tells us *how* the sample average varies around the true mean for large $n$. $\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}} \to N(0,1)$.

## Connections to Other Topics & Relevance
*   **[[../02 Inferential statistics/Hypothesis testing|Hypothesis Testing]] & [[../02 Inferential statistics/Estimation/Confidence Intervals|Confidence Intervals]]:** The CLT is the cornerstone for many common statistical procedures involving sample means. It allows us to assume the sampling distribution of the mean is approximately Normal, even if the population distribution isn't, enabling the use of Z-tests, t-tests (which accounts for estimating $\sigma$), and the calculation of confidence intervals for $\mu$.
*   **[[../02 Inferential statistics/Estimation/Standard error|Standard Error]]:** The $\sigma/\sqrt{n}$ term is the standard deviation of the sampling distribution of the mean, known as the standard error. The CLT gives this distribution its Normal shape.
*   **Approximations:** Justifies using the Normal distribution to approximate others like the [[02_Binomial_Distribution|Binomial]] and [[03_Poisson_Distribution|Poisson]] under certain conditions (large $n$ or $\lambda$).
*   **Quality Control & Process Monitoring:** Understanding the distribution of sample averages is crucial for setting control limits.

## Summary
*   The **Central Limit Theorem (CLT)** states that the **sampling distribution of the sample mean ($\bar{X}_n$) (or sum)** of a large number ($n$) of i.i.d. random variables approaches a **Normal distribution**, regardless of the original distribution's shape.
*   Requires: Independence, identical distribution, finite mean $\mu$, finite variance $\sigma^2$.
*   The distribution of $\bar{X}_n$ approaches $N(\mu, \sigma^2/n)$. The standardized mean $\frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}}$ approaches $N(0,1)$.
*   Explains the ubiquity of the Normal distribution.
*   Crucial foundation for statistical inference (hypothesis tests, confidence intervals) concerning means.
*   Different from LLN (CLT is about distribution shape, LLN is about value convergence).

## Sources
*   [Wikipedia: Central Limit Theorem](https://en.wikipedia.org/wiki/Central_limit_theorem)
*   [Khan Academy: Central Limit Theorem](https://www.khanacademy.org/math/statistics-probability/sampling-distributions-library/sample-means/v/central-limit-theorem)
*   [Seeing Theory: Central Limit Theorem (Interactive)](https://seeing-theory.brown.edu/probability-distributions/index.html#section3)
*   [PennState STAT 414: Central Limit Theorem](https://online.stat.psu.edu/stat414/lesson/24/24.1)
*   *OpenIntro Statistics* (Free PDF textbook) - Check relevant chapters on sampling distributions. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., Walpole et al.; Ross; DeGroot & Schervish) - Consult relevant chapters.

## TAGS
[[Probability]] [[Important Theorems]] [[Central Limit Theorem]] [[CLT]] [[Normal Distribution]] [[Sampling Distribution]] [[Sample Mean]] [[Standard error]] [[Convergence]] [[Statistical Inference]] [[02 Math/index]] [[Statistics]]