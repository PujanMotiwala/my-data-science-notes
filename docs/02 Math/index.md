# Mathematics Overview

This section covers the essential mathematical concepts that form the foundation for data science, machine learning, and AI. It includes probability theory, statistical inference, linear algebra, calculus, and information theory. Understanding these areas is crucial for building intuition and applying techniques effectively.

## Key Topics Covered:

*   **[[01 Probability/01 Basic Probability Theory/01_Definition_and_Terminology|Probability Theory]]**: The framework for reasoning about uncertainty.
    *   [[01 Probability/01 Basic Probability Theory/01_Definition_and_Terminology|Basic Concepts]]: Sample spaces, events, axioms.
    *   [[01 Probability/02 Random Variables/01_Definition|Random Variables]]: Discrete and Continuous variables, PMFs, PDFs, CDFs.
    *   [[01 Probability/03 Common Probability Distributions/00_Overview|Common Distributions]]: Overview of key distributions.
    *   [[01 Probability/04 Expectation Variance Covariance/01_Expected_Value|Expectation, Variance, Covariance]]: Measures of central tendency, spread, and relationships.
    *   [[01 Probability/05 Important Theorems/01_Law_of_Large_Numbers_LLN|Key Theorems]]: Law of Large Numbers (LLN), Central Limit Theorem (CLT).

*   **[[02 Inferential statistics/001 Inferential Statistics|Inferential Statistics]]**: Drawing conclusions about populations from sample data.
    *   [[02 Inferential statistics/001 Inferential Statistics|Core Concepts]]: Estimation, hypothesis testing.
    *   [[02 Inferential statistics/Hypothesis testing|Hypothesis Testing Framework]]: Null/Alternative hypotheses, p-values, significance levels. ([See Map](./02%20Inferential%20statistics/maps/hyp_testing_map.excalidraw.svg)).
    *   [[02 Inferential statistics/Estimation/Standard error|Estimation]]: Point estimates, confidence intervals, standard error.
    *   [[02 Inferential statistics/parametric tests/Parametric Tests|Parametric Tests]]: Assumptions and applications (e.g., [[02 Inferential statistics/parametric tests/01 t test/t test|T-tests]], [[02 Inferential statistics/parametric tests/02 ANOVA/ANOVA|ANOVA]]).
    *   [[02 Inferential statistics/Tradeoffs/Tradeoffs|Model Tradeoffs]]: [[02 Inferential statistics/Tradeoffs/Bias|Bias]] vs. [[02 Inferential statistics/Tradeoffs/Variance|Variance]].

*   **[[03 Linear Algebra/01 Core Objects/01_Scalars|Linear Algebra]]**: The mathematics of vectors, matrices, and linear transformations.
    *   [[03 Linear Algebra/01 Core Objects/03_Matrices|Core Objects]]: Scalars, Vectors, Matrices, Tensors.
    *   [[03 Linear Algebra/02 Basic Operations/02_Matrix_Operations|Basic Operations]]: Vector/Matrix addition, multiplication, dot products.
    *   [[03 Linear Algebra/04 Vector Spaces and Concepts/02_Span_and_Basis|Vector Spaces]]: Span, Basis, Linear Independence, Rank.
    *   [[03 Linear Algebra/05 Norms/01_Definition|Norms]]: Measuring vector/matrix size (L1, L2, Frobenius).
    *   [[03 Linear Algebra/06 Decompositions and Factorizations/03_Overview|Decompositions]]: Eigenvalues/Eigenvectors, SVD.

*   **[[04 Calculus/01 Foundations/01_Functions_Limits_Continuity|Calculus]]**: The mathematics of change and accumulation.
    *   [[04 Calculus/01 Foundations/02_Derivatives|Derivatives]]: Rates of change, slopes, differentiation rules, Chain Rule.
    *   [[04 Calculus/02 Multivariable Calculus/03_Gradient|Multivariable Calculus]]: Partial Derivatives, Gradient, Hessian, Jacobian.
    *   [[04 Calculus/03 Optimization/02_Gradient_Descent|Optimization]]: Finding Maxima/Minima, Gradient Descent, Convexity.
    *   [[04 Calculus/05 Integrals/01_Definite_and_Indefinite_Integrals|Integrals]]: Antiderivatives, area under curve, applications in probability.
    *   [[04 Calculus/06 Matrix Calculus/01_Matrix_Calculus_Essentials|Matrix Calculus]]: Essentials for ML optimization.

*   **[[05 Information Theory/01_Entropy|Information Theory]]**: Quantifying information and uncertainty.
    *   [[05 Information Theory/01_Entropy|Entropy]]: Measuring uncertainty in distributions.
    *   [[05 Information Theory/02_Cross_Entropy|Cross-Entropy]]: Comparing distributions, used as loss function.
    *   [[05 Information Theory/03_KL_Divergence|KL Divergence]]: Measuring the difference between distributions.

---

*Internal links like `[[...]]` rely on the `roamlinks` plugin being active in `mkdocs.yml` to function correctly in the built website.*

Browse the sidebar under the **Mathematics** heading (as defined in your `mkdocs.yml nav:` section) for a full list of notes within this topic.