# Rules of Differentiation

## Simple Idea
*   Calculating [[02_Derivatives|derivatives]] using the limit definition ($\lim [f(x+h)-f(x)]/h$) can be tedious. Thankfully, there are shortcut rules for finding derivatives of common types of functions quickly.

## Formal Definition
*   These rules are derived from the [[01_Functions_Limits_Continuity|limit]] definition of the [[02_Derivatives|derivative]] but allow for mechanical calculation once memorized. We assume $f(x)$ and $g(x)$ are differentiable functions and $c$ is a constant.

## Key Rules

### 1. Constant Rule
*   The derivative of a constant function is zero.
    $$ \frac{d}{dx}(c) = 0 $$
*   *Intuition:* A constant function $f(x)=c$ has a horizontal graph, so its slope ([[02_Derivatives|derivative]]) is always 0.

### 2. Power Rule
*   The derivative of $x$ raised to a power $n$ (where $n$ is any real number) is $n$ times $x$ raised to the power $n-1$.
    $$ \frac{d}{dx}(x^n) = n x^{n-1} $$
*   *Examples:*
    *   $\frac{d}{dx}(x^3) = 3x^2$
    *   $\frac{d}{dx}(x) = \frac{d}{dx}(x^1) = 1x^0 = 1$
    *   $\frac{d}{dx}(\sqrt{x}) = \frac{d}{dx}(x^{1/2}) = \frac{1}{2}x^{-1/2} = \frac{1}{2\sqrt{x}}$
    *   $\frac{d}{dx}(\frac{1}{x}) = \frac{d}{dx}(x^{-1}) = -1x^{-2} = -\frac{1}{x^2}$

### 3. Constant Multiple Rule
*   The derivative of a constant times a function is the constant times the derivative of the function.
    $$ \frac{d}{dx}[c \cdot f(x)] = c \cdot \frac{d}{dx}[f(x)] = c \cdot f'(x) $$
*   *Intuition:* Scaling a function vertically by $c$ scales its slope by $c$.
*   *Example:* $\frac{d}{dx}(5x^3) = 5 \cdot \frac{d}{dx}(x^3) = 5 \cdot (3x^2) = 15x^2$

### 4. Sum/Difference Rule
*   The derivative of a sum (or difference) of functions is the sum (or difference) of their derivatives.
    $$ \frac{d}{dx}[f(x) \pm g(x)] = \frac{d}{dx}[f(x)] \pm \frac{d}{dx}[g(x)] = f'(x) \pm g'(x) $$
*   *Intuition:* Allows differentiating polynomials term by term.
*   *Example:* $\frac{d}{dx}(x^2 + 5x - 3) = \frac{d}{dx}(x^2) + \frac{d}{dx}(5x) - \frac{d}{dx}(3) = 2x + 5 - 0 = 2x + 5$

### 5. Product Rule
*   Used for finding the derivative of a product of two functions.
    $$ \frac{d}{dx}[f(x) g(x)] = f(x) g'(x) + g(x) f'(x) $$
    *"First times derivative of the second, plus second times derivative of the first."*
*   *Example:* $\frac{d}{dx}(x^2 \sin(x)) = x^2 (\cos(x)) + \sin(x) (2x)$

### 6. Quotient Rule
*   Used for finding the derivative of a ratio (quotient) of two functions.
    $$ \frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{g(x) f'(x) - f(x) g'(x)}{[g(x)]^2} $$
    *"Low d-high minus high d-low, square the bottom and away we go!"* (Mnemonic: d-high/d-low means derivative of numerator/denominator). Requires $g(x) \neq 0$.
*   *Example:* $\frac{d}{dx}\left(\frac{x}{x+1}\right) = \frac{(x+1)(1) - x(1)}{(x+1)^2} = \frac{1}{(x+1)^2}$

### 7. Derivatives of Common Functions
*   **Trigonometric:**
    *   $\frac{d}{dx}(\sin x) = \cos x$
    *   $\frac{d}{dx}(\cos x) = -\sin x$
    *   $\frac{d}{dx}(\tan x) = \sec^2 x$
*   **Exponential & Logarithmic:**
    *   $\frac{d}{dx}(e^x) = e^x$ (The exponential function $e^x$ is its own derivative!)
    *   $\frac{d}{dx}(a^x) = a^x \ln(a)$ (where $\ln$ is the natural logarithm)
    *   $\frac{d}{dx}(\ln x) = \frac{1}{x}$ (for $x > 0$)
    *   $\frac{d}{dx}(\log_a x) = \frac{1}{x \ln a}$

## Connections to Other Topics
*   These rules are applied repeatedly when differentiating complex functions.
*   The **[[04_Chain_Rule|Chain Rule]]** is another crucial rule needed for composite functions ($f(g(x))$).
*   Form the basis for symbolic differentiation used in software packages (like SymPy, Mathematica).
*   Essential for finding [[02_Partial_Derivatives|partial derivatives]] in multivariable calculus (treat other variables as constants).

## Summary
*   Differentiation rules provide shortcuts for finding [[02_Derivatives|derivatives]] without using the limit definition.
*   Key rules include: Constant, Power, Constant Multiple, Sum/Difference, Product, Quotient.
*   Knowing derivatives of common functions (trig, exponential, log) is necessary.
*   These rules streamline the process of finding rates of change and slopes.

## Sources
*   Any standard Calculus textbook (e.g., Stewart, Thomas, Anton).
*   [Khan Academy: Differentiation rules](https://www.khanacademy.org/math/calculus-1/cs1-derivatives-rules) (Covers Power, Product, Quotient, etc.)
*   [Paul's Online Math Notes: Differentiation Formulas](https://tutorial.math.lamar.edu/Classes/CalcI/Derivativeulas.aspx)

## TAGS
[[Calculus]] [[Foundations]] [[Derivative]] [[Differentiation Rules]] [[Power Rule]] [[Product Rule]] [[Quotient Rule]] [[02 Math/index]]