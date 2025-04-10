# KL Divergence (Kullback-Leibler Divergence)

## Simple Idea
*   **KL Divergence** measures how much one probability distribution $P$ differs from a second, reference probability distribution $Q$. It quantifies the "distance" or "divergence" of $P$ from $Q$.
*   Think back to the [[02_Cross_Entropy|cross-entropy]] scenario: $KL(P || Q)$ represents the **extra average bits/nats** required per message to encode events from distribution $P$ using a code optimized for distribution $Q$, compared to using the optimal code based on $P$ itself. It's the "cost" or "inefficiency" incurred by using the wrong distribution $Q$ as an approximation for $P$.

## Formal Definition
*   For two [[../01 Probability/02 Random Variables/01_Definition|discrete probability distributions]] $P = \{p_1, ..., p_n\}$ and $Q = \{q_1, ..., q_n\}$ defined over the same set of events, the **Kullback-Leibler (KL) divergence** of $Q$ from $P$ (also called the relative entropy of $P$ with respect to $Q$) is:
    $$ D_{KL}(P || Q) = \sum_{i=1}^n p_i \log\left(\frac{p_i}{q_i}\right) $$
*   **Logarithm Base:** Base determines units (bits for $\log_2$, nats for $\ln$). Use $\ln$ (nats) for ML context.
*   **Handling Zeros:**
    *   If $p_i = 0$, the term is $0 \log(0/q_i) = 0$.
    *   If $q_i = 0$ but $p_i > 0$, $D_{KL}$ is infinite (reflecting that $Q$ assigns zero probability to an event that can actually happen under $P$). Requires $Q$ to be absolutely continuous with respect to $P$.

## Key Concepts

### 1. Interpretation: Information Gain / Inefficiency
*   $D_{KL}(P || Q)$ measures the information *lost* when $Q$ is used to approximate $P$.
*   Equivalently, it's the *extra* information needed to specify outcomes from $P$ when only knowledge of $Q$ is available.
*   It's the average difference between the "surprise" using the true distribution ($-\log p_i$) and the "surprise" using the approximate distribution ($-\log q_i$), weighted by the true probabilities $p_i$:
    $D_{KL}(P || Q) = E_P[-\log Q(X)] - E_P[-\log P(X)]$
    $D_{KL}(P || Q) = H(P, Q) - H(P)$ (Cross-Entropy minus Entropy)

### 2. Properties
*   **Non-negativity:** $D_{KL}(P || Q) \ge 0$. (Gibbs' inequality).
*   **Zero Divergence:** $D_{KL}(P || Q) = 0$ if and only if $P = Q$ almost everywhere.
*   **Asymmetry:** Crucially, KL divergence is **not symmetric**:
    $$ D_{KL}(P || Q) \neq D_{KL}(Q || P) $$
    Therefore, it is **not a true distance metric**. Measuring the divergence of Q from P is different from measuring the divergence of P from Q. The choice matters depending on the application.
    *(Example Intuition: If P is sharp and Q is broad, $D_{KL}(P||Q)$ might be large (surprising Q doesn't predict P's sharp peak well). If Q is sharp and P is broad, $D_{KL}(P||Q)$ penalizes Q for assigning low probability where P has mass).*

### 3. Continuous Case
*   For continuous distributions with PDFs $p(x)$ and $q(x)$:
    $$ D_{KL}(P || Q) = \int_{-\infty}^{\infty} p(x) \log\left(\frac{p(x)}{q(x)}\right) \, dx $$

## Connections to Other Topics & Relevance
*   **Relationship to [[01_Entropy|Entropy]] and [[02_Cross_Entropy|Cross-Entropy]]:**
    $$ D_{KL}(P || Q) = H(P, Q) - H(P) $$
    This is why minimizing [[02_Cross_Entropy|cross-entropy]] $H(P, Q)$ when $P$ is fixed (true distribution) is equivalent to minimizing $D_{KL}(P || Q)$.
*   **Variational Inference & Variational Autoencoders (VAEs):** KL divergence is often used as a regularization term in the loss function of VAEs. It encourages the learned approximate posterior distribution $Q$ (often Gaussian) of latent variables to stay close to a prior distribution $P$ (often standard Gaussian $N(0, I)$).
*   **Generative Adversarial Networks (GANs):** While not always explicit in the standard loss, related divergence measures (like Jensen-Shannon divergence, which *is* symmetric and derived from KL) are used to understand GAN training dynamics.
*   **Model Comparison/Selection:** Can be used to quantify how much information is lost when approximating a complex model/distribution ($P$) with a simpler one ($Q$).

## Summary
*   **KL Divergence ($D_{KL}(P || Q)$)** measures the difference or "distance" from a probability distribution $Q$ to a reference distribution $P$.
*   Formula (Discrete): $D_{KL}(P || Q) = \sum p_i \log(p_i/q_i)$.
*   Represents the **extra bits/nats** needed when using $Q$ to encode data from $P$. Also $D_{KL}(P || Q) = H(P, Q) - H(P)$.
*   **Properties:** Non-negative ($D_{KL} \ge 0$), zero iff $P=Q$, **not symmetric** ($D_{KL}(P||Q) \neq D_{KL}(Q||P)$).
*   Used in ML loss functions (implicitly via [[02_Cross_Entropy|Cross-Entropy]]), VAEs, and comparing distributions.

## Sources
*   [Wikipedia: Kullback–Leibler divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence)
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 3) ([https://www.deeplearningbook.org/](https://www.deeplearningbook.org/))
*   [Blog post on Entropy, Cross-Entropy, KL Divergence](https://towardsdatascience.com/entropy-cross-entropy-and-kl-divergence-explained-b09cdae9114a)
*   [Visual Information Theory](https://colah.github.io/posts/2015-09-Visual-Information/) (Chris Olah)

## TAGS
[[Information Theory]] [[KL Divergence]] [[Relative Entropy]] [[Cross-Entropy]] [[Entropy]] [[Probability Distribution]] [[Variational Autoencoder]] [[VAE]] [[Math]] [[Statistics]] [[Machine Learning]] [[Foundations]]