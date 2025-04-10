# Cross-Entropy

## Simple Idea
*   Imagine you have a set of possible events (outcomes of a random variable $X$) with a *true* probability distribution $P$. You want to design an efficient coding scheme (using bits/nats) to transmit which event occurred.
*   Ideally, you'd use shorter codes for more probable events (like Morse code uses short codes for common letters). An optimal code is based on the true distribution $P$, requiring an average of [[01_Entropy|Entropy]] $H(P)$ bits/nats per message.
*   Now, suppose you *mistakenly* design your coding scheme based on a *different* probability distribution $Q$. **Cross-entropy** $H(P, Q)$ measures the **average number of bits/nats per message** you would need when using the code designed for $Q$ to transmit events that actually follow distribution $P$.
*   Since the code is suboptimal (based on $Q$ instead of $P$), cross-entropy will be greater than or equal to the true entropy: $H(P, Q) \ge H(P)$. The difference is the [[03_KL_Divergence|KL Divergence]].

## Formal Definition
*   For two [[02 Math/01 Probability/02 Random Variables/01_Definition|discrete probability distributions]] $P = \{p_1, ..., p_n\}$ and $Q = \{q_1, ..., q_n\}$ defined over the same set of events $\{x_1, ..., x_n\}$, the **cross-entropy** of $Q$ relative to $P$ is:
    $$ H(P, Q) = - \sum_{i=1}^n p_i \log(q_i) $$
*   **Logarithm Base:** As with [[01_Entropy|entropy]], the base determines units (bits for $\log_2$, nats for $\ln$). We typically use $\ln$ (nats) in machine learning.
*   **Handling $q_i=0$:** If $p_i > 0$ but $q_i = 0$ for any $i$, the cross-entropy is formally infinite (you can't encode an event that occurred if your assumed distribution gave it zero probability). In practice, often requires smoothing or assumes $q_i$ are never exactly zero if $p_i$ isn't.

## Key Concepts

### 1. Interpretation: Average Message Length with Wrong Code
*   $H(P, Q)$ is the expected value of the "surprise" $-\log(q_i)$ calculated using the *true* probabilities $p_i$: $H(P, Q) = E_P[-\log Q(X)]$.
*   It quantifies the inefficiency introduced by using distribution $Q$ as an approximation for the true distribution $P$ in a coding context.

### 2. Relationship to Entropy and KL Divergence
*   Cross-entropy can be decomposed:
    $$ H(P, Q) = H(P) + D_{KL}(P || Q) $$
    Where:
        *   $H(P) = - \sum p_i \log(p_i)$ is the [[01_Entropy|Entropy]] of the true distribution $P$.
        *   $D_{KL}(P || Q) = \sum p_i \log\left(\frac{p_i}{q_i}\right)$ is the [[03_KL_Divergence|KL Divergence]] of $Q$ from $P$.
*   Since $D_{KL}(P || Q) \ge 0$, this shows $H(P, Q) \ge H(P)$. Equality holds only when $P=Q$.

### 3. Use as a Loss Function in Machine Learning (Crucial!)
*   In classification problems, we want our model's predicted probability distribution $Q$ (e.g., output of a softmax layer) to be as close as possible to the true underlying distribution $P$ (often represented as a one-hot vector, where the correct class has $p_i=1$ and others have $p_i=0$).
*   Minimizing the cross-entropy $H(P, Q)$ between the true labels ($P$) and the model predictions ($Q$) is a common objective.
*   Why? If $P$ is fixed (the true labels), minimizing $H(P, Q)$ is equivalent to minimizing the [[03_KL_Divergence|KL Divergence]] $D_{KL}(P || Q)$, effectively forcing the predicted distribution $Q$ to become similar to the true distribution $P$.
*   **Categorical Cross-Entropy / Log Loss:** When $P$ is a one-hot vector (e.g., for class $k$, $p_k=1$, others $p_i=0$), the formula simplifies:
    $$ H(P, Q) = - \sum_{i=1}^n p_i \log(q_i) = - 1 \cdot \log(q_k) = -\log(q_k) $$
    So, minimizing cross-entropy in this common case means maximizing the log-probability assigned to the correct class $k$. This is often called **Log Loss**.
*   **Binary Cross-Entropy:** Used for binary classification (output $q$, true label $p \in \{0, 1\}$).
    $$ H(P, Q) = - [p \log(q) + (1-p) \log(1-q)] $$

## Connections to Other Topics
*   Directly related to [[01_Entropy|Entropy]] and [[03_KL_Divergence|KL Divergence]].
*   The fundamental **loss function** for most classification tasks in Deep Learning and Logistic Regression.
*   Related to **Maximum Likelihood Estimation (MLE)**. Minimizing cross-entropy loss often corresponds to maximizing the likelihood of the observed data under the model's predicted distribution.

## Summary
*   **Cross-Entropy ($H(P, Q)$)** measures the average message length (in bits/nats) needed to encode events from distribution $P$ using a code optimized for distribution $Q$.
*   Formula: $H(P, Q) = - \sum p_i \log(q_i)$.
*   $H(P, Q) = H(P) + D_{KL}(P || Q)$. Since $D_{KL} \ge 0$, $H(P, Q) \ge H(P)$.
*   Widely used as a **loss function** in classification models, where minimizing $H(P, Q)$ makes the predicted distribution $Q$ similar to the true distribution $P$.
*   Common forms include Categorical Cross-Entropy (Log Loss) and Binary Cross-Entropy.

## Sources
*   [Wikipedia: Cross entropy](https://en.wikipedia.org/wiki/Cross_entropy)
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 3) ([https://www.deeplearningbook.org/](https://www.deeplearningbook.org/))
*   [Blog post on Entropy, Cross-Entropy, KL Divergence](https://towardsdatascience.com/entropy-cross-entropy-and-kl-divergence-explained-b09cdae9114a)
*   [Visual Information Theory](https://colah.github.io/posts/2015-09-Visual-Information/) (Chris Olah)

## TAGS
[[Information Theory]] [[Cross-Entropy]] [[Entropy]] [[KL Divergence]] [[Loss Function]] [[Classification]] [[Log Loss]] [[Maximum Likelihood Estimation]] [[Probability Distribution]] [[02 Math/index]] [[Statistics]] [[Machine Learning]] [[Deep Learning]] [[Foundations]]