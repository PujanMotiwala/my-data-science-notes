# Chain Rule

## Simple Idea
*   The Chain Rule is used to find the [[02_Derivatives|derivative]] of **composite functions** – functions that are nested inside other functions (like $f(g(x))$).
*   Think of layers: the Chain Rule tells you how a change in the input $x$ affects the *outer* function $f$ by considering how $x$ affects the *inner* function $g$, and how $g$ in turn affects $f$. It links the rates of change through the "chain" of functions.

## Formal Definition
*   If $y = f(u)$ is a differentiable function of $u$, and $u = g(x)$ is a differentiable function of $x$, then the composite function $y = f(g(x))$ is a differentiable function of $x$, and its derivative is:
    $$ \frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} $$
*   In Lagrange's notation: If $h(x) = f(g(x))$, then
    $$ h'(x) = f'(g(x)) \cdot g'(x) $$
*   **In words:** The derivative of the composite function is the derivative of the *outer function* (evaluated at the *inner function*) multiplied by the derivative of the *inner function*.

## Key Concepts

### 1. Identifying Outer and Inner Functions
*   To apply the rule, you must correctly identify the "outer" function $f$ and the "inner" function $g$.
*   Example: $y = \sin(x^2)$. Outer function $f(u) = \sin(u)$. Inner function $u = g(x) = x^2$.
*   Example: $y = (x^3 + 1)^5$. Outer function $f(u) = u^5$. Inner function $u = g(x) = x^3 + 1$.

### 2. Applying the Rule
*   **Example 1:** Find the derivative of $y = \sin(x^2)$.
    *   $f(u) = \sin(u) \implies f'(u) = \frac{dy}{du} = \cos(u)$
    *   $g(x) = x^2 \implies g'(x) = \frac{du}{dx} = 2x$
    *   $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = \cos(u) \cdot (2x)$
    *   Substitute back $u = x^2$: $\frac{dy}{dx} = \cos(x^2) \cdot 2x = 2x \cos(x^2)$
*   **Example 2:** Find the derivative of $y = (x^3 + 1)^5$.
    *   $f(u) = u^5 \implies f'(u) = \frac{dy}{du} = 5u^4$
    *   $g(x) = x^3 + 1 \implies g'(x) = \frac{du}{dx} = 3x^2$
    *   $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx} = (5u^4) \cdot (3x^2)$
    *   Substitute back $u = x^3 + 1$: $\frac{dy}{dx} = 5(x^3 + 1)^4 \cdot 3x^2 = 15x^2(x^3 + 1)^4$

### 3. Multiple Nested Functions
*   The rule extends to multiple compositions: If $y = f(g(h(x)))$, then
    $$ \frac{dy}{dx} = f'(g(h(x))) \cdot g'(h(x)) \cdot h'(x) $$
    You multiply the derivatives of each "layer", evaluating outer derivatives at the inner function results.

## Connections to Other Topics & Relevance
*   **Backpropagation in Neural Networks:** The Chain Rule is the **mathematical heart of backpropagation**, the algorithm used to train deep neural networks. The loss function depends on the output layer, which depends on the hidden layers, which depend on the weights and inputs. Backpropagation uses the chain rule repeatedly to calculate the [[../02 Multivariable Calculus/03_Gradient|gradient]] of the loss with respect to each weight and bias throughout the network, allowing [[../03 Optimization/02_Gradient_Descent|Gradient Descent]] to update the parameters.
*   **Related Rates Problems:** Used in physics and engineering to find the rate of change of one quantity in terms of the rate of change of another related quantity.
*   **Implicit Differentiation:** A technique that relies on the chain rule to find derivatives of implicitly defined functions.
*   **[[../02 Multivariable Calculus/03_Gradient|Multivariable Chain Rule]]:** Extends the concept to functions involving multiple variables.

## Summary
*   The **Chain Rule** is used to differentiate **composite functions** ($f(g(x))$).
*   Formula: $\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$ or $[f(g(x))]' = f'(g(x)) \cdot g'(x)$.
*   **Derivative of outer (evaluated at inner) TIMES derivative of inner.**
*   Absolutely **fundamental for training neural networks** via backpropagation.

## Sources
*   Any standard Calculus textbook (e.g., Stewart, Thomas, Anton).
*   [Khan Academy: Chain rule](https://www.khanacademy.org/math/calculus-1/cs1-derivatives-rules/cs1-chain-rule/v/chain-rule-introduction)
*   [Paul's Online Math Notes: Chain Rule](https://tutorial.math.lamar.edu/Classes/CalcI/ChainRule.aspx)

## TAGS
[[Calculus]] [[Foundations]] [[Derivative]] [[Differentiation Rules]] [[Chain Rule]] [[Composite Function]] [[Backpropagation]] [[Neural Networks]] [[02 Math/index]]