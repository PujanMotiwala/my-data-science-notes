## In the principle
> Having two hypotheses (here, decision boundaries) that has the same empirical risk (here, training error), a short explanation (here, a boundary with fewer parameters) tends to be more valid than a long explanation.

You can consider Occam’s razor principle in machine learning as a thumb rule, which says that whenever you have multiple choice for a decision boundary, always choose the simpler one.

## **Simplicity & Complexity**

The simplicity of a model, often understood by defining what the complexity of a model means. Let’s understand them by taking an analogy.

Assume there are two students in a class Student-A and Student-B and let’s consider they have different ways of learning as mentioned below:

**Student A** is interested in grasping the concepts, his high-level picture of subjects is clear, and he is comfortable in explaining the concepts in simple terms. But he does not memorize, not even a simple formula.

**Student B** is interested in scoring more, he prefers memorization to understanding, he solves all the problems from multiple books.

We can say that they have different mental models for learning.

As per their different style of learning, Student A will be good at solving new unseen problems than Student B whereas Student B is good at scoring more as he memorized most of the problems/formulas, here Student A will struggle to score(consider exams are time-bounded and how he will solve questions on time while deriving the formulas instead he could have memorized it to save time).

An ideal student will be one whose learning style is somewhere in between Student A & Student B so that he could score decently and will also be able to solve unseen problems.

This same thing happens with machine learning models also, if our model is too simple then it hasn’t learned enough patterns to give you a good score, but we can achieve good score with a complex model which has memorized all the patterns, but this complex model won't be able to generalize well on unseen data. In machine learning, we call this phenomenon as [[Overfitting]]

## Factors governing model complexity
- The number of parameters required to explain our model completely, i.e for predicting y where we have x1, x2, x3 predictors — the model `y = ax1 +bx2` is simpler than the model `y = ax1 +bx2 +cx3`, the latter requires 3 parameters compared to the 2 required for the first model.
- The degree of the function, if it is a polynomial, the model `y = ax1² +bx2³` would be a more complex model as compared to `y = ax1+bx2+cx3` even it has 3 predictor variables.
-  The size of model representation, `(0.552984567 ∗ x 2 + 932.4710001276)` could be considered to be more complex than `(2x1 +3x2² +1)`, though the latter has more terms in it.