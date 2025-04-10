---
tags:
- Batch Gradient Descent
- Calculus
- Deep Learning
- Foundations
- Gradient Descent
- Learning Rate
- Machine Learning
- Mini-batch Gradient Descent
- Optimization
- SGD
- Stochastic Gradient Descent
---

# Gradient Descent Variants (SGD, Mini-batch)

## Simple Idea
*   Basic [[02_Gradient_Descent|Gradient Descent]] (sometimes called "Batch Gradient Descent") calculates the [[03_Gradient|gradient]] using the *entire* training dataset in every single step. This can be extremely slow and computationally expensive for large datasets.
*   Gradient Descent variants were developed to speed up training and improve convergence by using only a *subset* of the data for each gradient calculation and parameter update.

## Formal Definitions & Concepts

### 1. Batch Gradient Descent (BGD)
*   **Process:** Computes the gradient of the loss function $L(\mathbf{w})$ using the **full training dataset** at each iteration before updating the parameters $\mathbf{w}$.
    $$ \nabla L(\mathbf{w}) = \frac{1}{N} \sum_{i=1}^N \nabla L_i(\mathbf{w}) \quad (\text{where } L_i \text{ is loss for i-th sample, N is total samples}) $$
    $$ \mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla L(\mathbf{w}_t) $$
*   **Pros:**
    *   Smooth convergence towards the minimum (less noisy updates).
    *   Guaranteed to converge to the global minimum for [[04_Convexity|convex]] problems and a local minimum for non-convex problems.
*   **Cons:**
    *   Very slow and memory-intensive for large datasets (requires processing all data for one update).
    *   Cannot update model online (with new data arriving).

### 2. Stochastic Gradient Descent (SGD)
*   **Process:** Computes the gradient and updates the parameters using **only one randomly chosen training sample** at each iteration.
    $$ \text{Pick random sample } i $$
    $$ \nabla L_i(\mathbf{w}_t) \quad (\text{Gradient for sample i only}) $$
    $$ \mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla L_i(\mathbf{w}_t) $$
*   **Pros:**
    *   Much faster updates (computationally cheap per iteration).
    *   Can update online as new data arrives.
    *   The noise in updates can help escape shallow local minima or saddle points in non-convex problems.
*   **Cons:**
    *   High variance in updates (noisy gradient estimate), leading to a fluctuating convergence path ("zig-zagging").
    *   May never converge perfectly to the minimum, might just oscillate around it.
    *   Loss function can fluctuate significantly between iterations.
    *   Requires careful tuning of the [[02_Gradient_Descent|learning rate]] $\eta$, often needing a learning rate schedule (decreasing $\eta$ over time).

### 3. Mini-Batch Gradient Descent
*   **Process:** Computes the gradient and updates parameters using a **small, random batch of samples** (e.g., 32, 64, 128 samples) at each iteration.
    $$ \text{Pick random batch } B \text{ of size } b $$
    $$ \nabla L_B(\mathbf{w}_t) = \frac{1}{b} \sum_{i \in B} \nabla L_i(\mathbf{w}_t) $$
    $$ \mathbf{w}_{t+1} = \mathbf{w}_t - \eta \nabla L_B(\mathbf{w}_t) $$
*   **Pros:**
    *   Strikes a balance between the speed of SGD and the stability of BGD.
    *   Smoother convergence than SGD due to reduced variance in the gradient estimate.
    *   Allows for efficient computation using vectorized operations on modern hardware (GPUs).
*   **Cons:**
    *   Introduces a new hyperparameter: the batch size `b`.
    *   Still doesn't guarantee convergence to the global minimum for non-convex problems.
*   **Dominant Method:** Mini-batch GD is the **most common variant** used in training [[../../07 Deep Learning/01 Foundational Models/Neural Networks/01 The Basics/01_Introduction|Deep Learning]] models today. Often, when people just say "SGD" in the context of deep learning, they actually mean Mini-batch SGD.

*(Visual Idea: Excalidraw contour plot showing the paths: BGD smooth descent, SGD very noisy zig-zag, Mini-batch less noisy zig-zag).*

## Connections to Other Topics
*   All variants rely on calculating the [[03_Gradient|gradient]] (often via backpropagation).
*   The choice of variant impacts convergence speed, stability, memory usage, and potentially the quality of the final minimum found.
*   Leads into **Adaptive Optimization Algorithms** (like Momentum, RMSprop, Adam) which further refine how the gradient information is used in the update step, building upon SGD/Mini-batch GD. These will be covered in [[Optimizer Variants / Adaptive Methods]].

## Summary
*   **Batch GD (BGD):** Uses **all** data per update. Smooth but slow/memory-intensive.
*   **Stochastic GD (SGD):** Uses **one** sample per update. Fast but noisy/unstable.
*   **Mini-Batch GD:** Uses a **small batch** of samples per update. **Best compromise** for speed, stability, and hardware efficiency. The standard in Deep Learning.
*   These variants trade off gradient accuracy (variance) for computational efficiency per update.

## Sources
*   *Deep Learning* by Goodfellow, Bengio, and Courville (Chapter 8) ([https://www.deeplearningbook.org/](https://www.deeplearningbook.org/))
*   [Overview of Gradient Descent variants](https://ruder.io/optimizing-gradient-descent/) (Excellent blog post by Sebastian Ruder)
*   [Wikipedia: Stochastic gradient descent](https://en.wikipedia.org/wiki/Stochastic_gradient_descent) (Often covers mini-batch too)