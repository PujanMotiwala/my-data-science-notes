# Information Entropy

## Simple Idea
*   **Entropy** measures the **average amount of surprise** or **uncertainty** associated with the possible outcomes of a [[../01 Probability/02 Random Variables/01_Definition|random variable]].
*   Think about predicting the outcome:
    *   A very biased coin (e.g., 99% Heads) has *low entropy*. You're quite certain about the outcome (Heads), so there's little surprise on average.
    *   A fair coin (50% Heads, 50% Tails) has *high entropy*. You are maximally uncertain about the outcome, so the average surprise is high.
*   It can also be interpreted as the **average number of bits** required to encode or communicate the outcome of the random variable, assuming an optimal coding scheme.

## Formal Definition
*   For a [[../01 Probability/02 Random Variables/01_Definition|discrete random variable]] $X$ with possible outcomes $\{x_1, ..., x_n\}$ and [[../01 Probability/02 Random Variables/02_Probability_Mass_Function_PMF|Probability Mass Function (PMF)]] $P(X=x_i) = p_i$, the **Shannon Entropy** $H(X)$ is defined as:
    $$ H(X) = - \sum_{i=1}^n p_i \log(p_i) $$
*   **Logarithm Base:**
    *   If the logarithm base is 2 ($\log_2$), entropy is measured in **bits**. This is common in information theory and computer science.
    *   If the base is $e$ ($\ln$, natural logarithm), entropy is measured in **nats**. This is common in machine learning.
    *   If the base is 10 ($\log_{10}$), entropy is measured in **hartleys** or **dits**.
    *   *Convention:* We often use $\ln$ (nats) in ML contexts.
*   **Handling $p_i=0$:** By convention, $0 \log 0 = 0$ (since $\lim_{p \to 0^+} p \log p = 0$). Outcomes with zero probability contribute nothing to the uncertainty.

## Key Concepts

### 1. Interpretation: Average Surprise
*   The term $-\log(p_i)$ can be thought of as the "surprise" or "information content" associated with observing outcome $x_i$. Low probability events ($p_i$ small) are more surprising ($-\log(p_i)$ is large). High probability events ($p_i$ large) are less surprising ($-\log(p_i)$ is small).
*   Entropy $H(X)$ is the *expected value* (weighted average) of this surprise over all possible outcomes: $H(X) = E[-\log P(X)]$.

### 2. Properties
*   **Non-negativity:** $H(X) \ge 0$. Entropy is always non-negative.
*   **Maximum Entropy:** For a discrete variable with $n$ possible outcomes, entropy is maximized when all outcomes are equally likely ($p_i = 1/n$). The maximum value is $H_{max} = \log(n)$. This represents the highest uncertainty.
*   **Minimum Entropy:** Entropy is minimized ($H(X) = 0$) when one outcome is certain ($p_k=1$ for some $k$, and all other $p_i=0$). This represents complete certainty.

### 3. Units (Bits vs. Nats)
*   **Bits ($\log_2$):** Corresponds to the average number of yes/no questions needed to determine the outcome.
*   **Nats ($\ln$):** More mathematically convenient when dealing with calculus (e.g., derivatives involving entropy). `1 nat ≈ 1.44 bits`.

### 4. Differential Entropy (Continuous Case)
*   For a [[../01 Probability/02 Random Variables/01_Definition|continuous random variable]] $X$ with [[../01 Probability/02 Random Variables/03_Probability_Density_Function_PDF|PDF]] $f(x)$, the **differential entropy** $h(X)$ is defined as:
    $$ h(X) = - \int_{-\infty}^{\infty} f(x) \log(f(x)) \, dx $$
*   **Caution:** Differential entropy shares some properties with discrete entropy but lacks others. It can be negative, is not unitless, and is sensitive to scaling of $x$. It's more about relative uncertainty.

## Connections to Other Topics & Relevance
*   **Information Theory:** A foundational concept developed by Claude Shannon.
*   **Decision Trees:** Used as an **impurity measure** (like Gini impurity) to decide on the best feature splits. Algorithms like ID3 aim to maximize [[Information Gain]], which is the reduction in entropy achieved by splitting on a feature. $IG(S, A) = H(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} H(S_v)$.
*   **[[02_Cross_Entropy|Cross-Entropy]] & [[03_KL_Divergence|KL Divergence]]:** Entropy is a component of these measures, which compare probability distributions.
*   **Thermodynamics:** Related to the concept of entropy in physics (measure of disorder).
*   **Data Compression:** Theoretical lower bound on the average number of bits needed to compress data drawn from a distribution.

## Summary
*   **Entropy ($H(X)$)** measures the average **uncertainty** or **surprise** associated with a random variable $X$.
*   Formula (Discrete): $H(X) = - \sum p_i \log(p_i)$.
*   Maximized for uniform distributions (maximum uncertainty). Minimized (zero) for deterministic outcomes (certainty).
*   Units depend on log base (bits for $\log_2$, nats for $\ln$).
*   Used in decision trees (impurity/information gain) and related to other information-theoretic measures.

## Sources
*   [Wikipedia: Entropy (information theory)](https://en.wikipedia.org/wiki/Entropy_(information_theory))
*   [Khan Academy: Information entropy](https://www.khanacademy.org/computing/computer-science/informationtheory/moderninfotheory/v/information-entropy)
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 3 discusses Information Theory concepts) ([https://www.deeplearningbook.org/](https://www.deeplearningbook.org/))
*   [Visual Information Theory](https://colah.github.io/posts/2015-09-Visual-Information/) (Excellent blog post by Chris Olah)

## TAGS
[[Information Theory]] [[Entropy]] [[Shannon Entropy]] [[Uncertainty]] [[Surprise]] [[Probability Distribution]] [[Decision Tree]] [[Information Gain]] [[Math]] [[Statistics]] [[Foundations]] [[Machine Learning]]