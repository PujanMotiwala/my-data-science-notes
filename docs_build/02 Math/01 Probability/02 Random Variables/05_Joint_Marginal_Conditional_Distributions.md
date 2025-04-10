---
tags:
- Bayes Theorem
- Conditional Distribution
- Independence
- Joint Distribution
- Machine Learning
- Marginal Distribution
- Multivariate Statistics
- PDF
- PMF
- Probability
- Random Variable
- Statistics
---

# Joint, Marginal, and Conditional Distributions

## Definition / Introduction
*   Often, we are interested in the behavior of **multiple [[02 Math/01 Probability/02 Random Variables/01_Definition|random variables]]** simultaneously. For instance, how are height and weight related? How does the probability of rain depend on temperature?
*   **Joint Distributions** describe the probability of two or more random variables *simultaneously* taking on specific values or falling within specific ranges.
*   **Marginal Distributions** describe the probability distribution of a *single* random variable from the group, ignoring the others.
*   **Conditional Distributions** describe the probability distribution of one random variable *given* that another random variable has taken on a specific value.
*   These concepts are crucial for understanding dependencies, building multivariate models, and performing inference with multiple variables. We'll focus on the two-variable (bivariate) case for simplicity.

## Key Concepts (Discrete Case)

Let $X$ and $Y$ be two [[02 Math/01 Probability/02 Random Variables/01_Definition|discrete random variables]].

### 1. Joint Probability Mass Function (Joint PMF)
*   **Definition:** Gives the probability that $X$ takes the value $x$ *and* $Y$ takes the value $y$ simultaneously.
    $$ p_{X,Y}(x, y) = P(X=x, Y=y) $$
*   **Properties:**
    *   $p_{X,Y}(x, y) \ge 0$ for all $x, y$.
    *   $\sum_x \sum_y p_{X,Y}(x, y) = 1$ (Sum over all possible pairs must be 1).
*   Often represented as a table where rows correspond to values of $X$, columns to values of $Y$, and cell entries are the joint probabilities.

### 2. Marginal Probability Mass Function (Marginal PMF)
*   **Definition:** The probability distribution of one variable alone, obtained by summing the joint PMF over all possible values of the *other* variable.
    *   Marginal PMF of X: $p_X(x) = P(X=x) = \sum_y p_{X,Y}(x, y)$ (Sum across the row for a fixed x).
    *   Marginal PMF of Y: $p_Y(y) = P(Y=y) = \sum_x p_{X,Y}(x, y)$ (Sum down the column for a fixed y).
*   **Intuition:** It collapses the joint information to look at just one variable's probabilities.

### 3. Conditional Probability Mass Function (Conditional PMF)
*   **Definition:** Gives the probability that $X$ takes the value $x$ *given* that $Y$ has taken the value $y$. Defined only if $p_Y(y) > 0$.
    $$ p_{X|Y}(x|y) = P(X=x | Y=y) = \frac{P(X=x, Y=y)}{P(Y=y)} = \frac{p_{X,Y}(x, y)}{p_Y(y)} $$
*   Similarly, the conditional PMF of Y given X=x is:
    $$ p_{Y|X}(y|x) = P(Y=y | X=x) = \frac{P(X=x, Y=y)}{P(X=x)} = \frac{p_{X,Y}(x, y)}{p_X(x)} $$
*   **Properties:** For a fixed $y$, $p_{X|Y}(x|y)$ is a valid PMF in $x$ (non-negative, sums to 1 over all x).
*   **Intuition:** It describes the distribution of one variable within the restricted "slice" where the other variable's value is known.

### 4. Independence
*   Discrete RVs $X$ and $Y$ are [[05_Independence|independent]] if and only if their joint PMF is the product of their marginal PMFs for all $x, y$:
    $$ p_{X,Y}(x, y) = p_X(x) p_Y(y) $$
*   Equivalently, independence means $p_{X|Y}(x|y) = p_X(x)$ (knowing Y doesn't change the distribution of X) and $p_{Y|X}(y|x) = p_Y(y)$.

## Key Concepts (Continuous Case)

Let $X$ and $Y$ be two [[02 Math/01 Probability/02 Random Variables/01_Definition|continuous random variables]].

### 1. Joint Probability Density Function (Joint PDF)
*   **Definition:** A function $f_{X,Y}(x, y)$ such that the probability of $(X, Y)$ falling within a region $A$ in the xy-plane is found by integrating the joint PDF over that region.
    $$ P((X, Y) \in A) = \iint_A f_{X,Y}(x, y) \, dx \, dy $$
*   **Properties:**
    *   $f_{X,Y}(x, y) \ge 0$ for all $x, y$.
    *   $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dx \, dy = 1$ (Total volume under the surface is 1).
*   $f_{X,Y}(x, y)$ itself is *not* a probability.

### 2. Marginal Probability Density Function (Marginal PDF)
*   **Definition:** Obtained by integrating the joint PDF over all possible values of the *other* variable.
    *   Marginal PDF of X: $f_X(x) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dy$
    *   Marginal PDF of Y: $f_Y(y) = \int_{-\infty}^{\infty} f_{X,Y}(x, y) \, dx$

### 3. Conditional Probability Density Function (Conditional PDF)
*   **Definition:** Describes the density of $X$ given $Y=y$. Defined only if $f_Y(y) > 0$.
    $$ f_{X|Y}(x|y) = \frac{f_{X,Y}(x, y)}{f_Y(y)} $$
*   Similarly, the conditional PDF of Y given X=x is:
    $$ f_{Y|X}(y|x) = \frac{f_{X,Y}(x, y)}{f_X(x)} $$
*   **Properties:** For a fixed $y$, $f_{X|Y}(x|y)$ is a valid PDF in $x$ (non-negative, integrates to 1 over all x).

### 4. Independence
*   Continuous RVs $X$ and $Y$ are [[05_Independence|independent]] if and only if their joint PDF is the product of their marginal PDFs for all $x, y$:
    $$ f_{X,Y}(x, y) = f_X(x) f_Y(y) $$
*   Equivalently, $f_{X|Y}(x|y) = f_X(x)$ and $f_{Y|X}(y|x) = f_Y(y)$.

## Connections to Other Topics & Relevance
*   **[[03_Covariance_and_Correlation|Covariance and Correlation]]:** Defined based on the joint distribution. $E[XY]$ is calculated using the joint PMF/PDF: $E[XY] = \sum_x \sum_y xy \, p_{X,Y}(x,y)$ or $E[XY] = \iint xy \, f_{X,Y}(x,y) \, dx \, dy$.
*   **[[06_Bayes_Theorem|Bayes' Theorem for RVs]]:** Can be expressed using conditional and marginal distributions: $f_{X|Y}(x|y) = \frac{f_{Y|X}(y|x) f_X(x)}{f_Y(y)}$. Crucial for Bayesian inference.
*   **Multivariate Models:** Concepts extend to more than two variables (Multivariate Distributions, e.g., Multivariate Normal). Foundational for understanding relationships in complex datasets.
*   **Machine Learning:** Understanding conditional distributions is key to generative models (e.g., generating an image $X$ given a class label $Y$), sequence models (probability of next word given previous words), and graphical models (e.g., Bayesian Networks represent conditional independencies).
*   **Feature Engineering/Selection:** Analyzing joint and conditional distributions helps understand how features interact and influence a target variable.

## Summary
*   **Joint Distribution:** Describes simultaneous behavior of multiple RVs ($p_{X,Y}(x,y)$ or $f_{X,Y}(x,y)$).
*   **Marginal Distribution:** Distribution of a single RV, ignoring others (sum/integrate out other variables).
*   **Conditional Distribution:** Distribution of one RV given a specific value of another ($p_{X|Y}(x|y)$ or $f_{X|Y}(x|y) = \text{joint} / \text{marginal}$).
*   **Independence:** Joint = Product of Marginals.
*   Fundamental for modeling dependencies and relationships between variables in multi-dimensional data.

## Sources
*   [PennState STAT 414: Joint, Marginal, Conditional Distributions](https://online.stat.psu.edu/stat414/lesson/20) (Discrete) & Lesson 26 (Continuous)
*   [Wikipedia: Joint Distribution](https://en.wikipedia.org/wiki/Joint_probability_distribution), [Marginal Distribution](https://en.wikipedia.org/wiki/Marginal_distribution), [Conditional Distribution](https://en.wikipedia.org/wiki/Conditional_probability_distribution)
*   *OpenIntro Statistics* (Free PDF textbook) - Check sections on joint distributions/contingency tables. ([https://www.openintro.org/book/os/](https://www.openintro.org/book/os/))
*   Classic Texts: (e.g., Ross; DeGroot & Schervish; Casella & Berger "Statistical Inference") - Consult relevant chapters.