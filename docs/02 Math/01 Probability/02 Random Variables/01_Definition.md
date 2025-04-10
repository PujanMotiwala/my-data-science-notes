# Random Variables: Definition

## Definition / Introduction
*   In probability, we often care more about a *numerical consequence* of an experiment's random outcome than the outcome itself.
*   A **Random Variable** is a rule (or function) that assigns a unique numerical value to each possible outcome in the [[../01 Basic Probability Theory/01_Definition_and_Terminology|Sample Space]] of a random experiment.
*   **Crucially, it's a *variable* whose value is determined by chance.** We don't know the exact value the random variable will take beforehand, but we can describe the probabilities associated with its possible values.
*   They are typically denoted by uppercase letters (e.g., X, Y, Z), while the specific values they can take are denoted by corresponding lowercase letters (e.g., x, y, z).

## Key Concepts

### 1. Mapping Outcomes to Numbers
*   Think of a random variable as a bridge connecting the often non-numeric outcomes of an experiment to the world of numbers, which allows for mathematical analysis.
*   **Experiment:** Flipping two fair coins.
    *   **Sample Space (S):** `{HH, HT, TH, TT}`
    *   **Possible Random Variable (X):** Let X be the *number of Heads* obtained.
        *   Mapping:
            *   Outcome HH → X = 2
            *   Outcome HT → X = 1
            *   Outcome TH → X = 1
            *   Outcome TT → X = 0
    *   The possible values for the random variable X are `{0, 1, 2}`.

### 2. Types of Random Variables
Random variables are broadly classified based on the types of numerical values they can assume:

*   **Discrete Random Variable:**
    *   **Definition:** Can only take on a finite number of values or a countably infinite number of values (like integers 0, 1, 2, ...). There are gaps between possible values.
    *   **Examples:**
        *   The number of Heads in 3 coin flips (Values: 0, 1, 2, 3).
        *   The number of defective items in a sample of 20 (Values: 0, 1, ..., 20).
        *   The number of cars passing a certain point in an hour (Values: 0, 1, 2, ... potentially infinite, but countable).
        *   The result of rolling a single die (Values: 1, 2, 3, 4, 5, 6).

*   **Continuous Random Variable:**
    *   **Definition:** Can take on any value within a given range or interval. There are infinitely many possible values between any two distinct values.
    *   **Examples:**
        *   The height of a randomly selected student (e.g., any value between 150cm and 190cm).
        *   The exact temperature of a room (e.g., any value between 20°C and 25°C).
        *   The time it takes for a web server to respond (e.g., any value greater than 0 milliseconds).
        *   The exact weight of a product.

### 3. Why Use Random Variables?
*   **Simplification:** They summarize the outcome of a random process with a single number.
*   **Mathematical Analysis:** Allow us to apply mathematical tools (like calculating expected values, variances, probabilities of ranges) to random phenomena.
*   **Modeling:** Form the basis for defining [[00_Overview|Probability Distributions]], which model real-world random processes.

## Connections to Other Topics
*   The possible values of a random variable form the domain over which [[02_Probability_Mass_Function_PMF|Probability Mass Functions (PMF)]] (for discrete RVs) and [[03_Probability_Density_Function_PDF|Probability Density Functions (PDF)]] (for continuous RVs) are defined.
*   The [[04_Cumulative_Distribution_Function_CDF|Cumulative Distribution Function (CDF)]] describes the probability that a random variable takes a value less than or equal to a specific point, regardless of type.
*   Understanding random variables is essential for [[../04 Expectation Variance Covariance/01_Expected_Value|Expected Value]] and [[../04 Expectation Variance Covariance/02_Variance_and_Standard_Deviation|Variance]].

## Summary
*   A **Random Variable (RV)** assigns a numerical value to each outcome in a sample space.
*   It links random experimental outcomes to analysable numbers.
*   **Discrete RVs** take countable values (e.g., number of heads, counts).
*   **Continuous RVs** take any value within an interval (e.g., height, time, temperature).
*   The distinction is crucial for choosing the right probability functions (PMF vs. PDF).

## Sources
*   [Khan Academy: Random Variables](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library)
*   [Wikipedia: Random Variable](https://en.wikipedia.org/wiki/Random_variable)
*   [Stat Trek: Random Variables](https://stattrek.com/probability-distributions/random-variables)
*   [Seeing Theory: Random Variables (Interactive)](https://seeing-theory.brown.edu/basic-probability/index.html#section3)

## TAGS
[[Probability]] [[Random Variable]] [[Discrete Variable]] [[Continuous Variable]] [[Foundations]] [[Math]] [[Statistics]]