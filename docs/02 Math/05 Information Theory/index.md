# Information Theory

Information Theory provides mathematical tools for quantifying information, uncertainty, and the efficiency of communication systems. Key concepts have found significant applications in machine learning, particularly in defining loss functions and measuring differences between probability distributions.

This section covers:

*   **[[01_Entropy|Entropy]]**: Measuring the average uncertainty or "surprise" associated with a random variable's outcomes. Used as an impurity measure in decision trees.
*   **[[02_Cross_Entropy|Cross-Entropy]]**: Measuring the average message length when encoding data from one distribution using a code based on another. Widely used as a loss function for classification tasks.
*   **[[03_KL_Divergence|KL Divergence (Kullback-Leibler Divergence)]]**: Measuring the "distance" or inefficiency gained when approximating one probability distribution with another. Related to cross-entropy and entropy ($D_{KL}(P||Q) = H(P,Q) - H(P)$), used in variational inference (VAEs).

Use the sidebar navigation to explore specific topics within Information Theory.