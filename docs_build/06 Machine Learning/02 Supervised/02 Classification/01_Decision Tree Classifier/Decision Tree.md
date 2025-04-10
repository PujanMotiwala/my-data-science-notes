---
tags:
- Classification
- Decision Tree
- ML model
- Supervised
---

## Introduction
- A binary tree which recursively splits datasets until we are left with pure leaf nodes. i.e. data with only one type of class.
- A decision tree is a structure that includes a *root node*, *branches*, and *leaf* nodes. Each internal node denotes a test on an attribute, each branch denotes the outcome of a test, and each leaf node holds a class label. The topmost node in the tree is the root node.
In simpler terms,
- Each **Internal node** corresponds to a ***Test***
- Each **Branch** corresponds to ***Result of the Test***
- Each **Leaf Node** ***Assigns a Classification***

#### Steps:
1. Choose an attribute from your dataset
2. Calculate the significance of attribute in splitting of data
3. Split data based on the value of the best attribute
4. Go each branch and repeat it for the rest of the attributes or go to step 1

### Building Decision Tree Process
- Built by using recursive partitioning to classify the data or by splitting the training set into distinct nodes.
- The algorithm chooses the most predictive feature to split the data on.
- Important task for good decision tree is to select best attribute 

#### How to select “Best Attribute”?
- Best Attribute will have more predictiveness with less impurity and lower entropy
	- For instance, while classifying patients for Drug A and Drug B. If you go for attribute ***Sex***, choosing Male or Female gives go separation to which drug A or B to assign for patients than ***Cholesterol*** as attribute. Then we can say ***Sex*** attribute is more significant than ***Cholesterol***.
- It’s all about purity of the leaves 
- By using recursive partitioning on training records into segments by minimizing the impurity at each step. 
- Impurity is Entropy present in the node. 

#### What is [[Entropy]]?
- Entropy is the amount of information disorder or the measure of randomness or uncertainty
- Entropy is calculated for each node, we are usually looking for smallest entropy in the tree’s nodes. 
- Entropy = 0 when it is pure, or say based on our labels of Drug A & B, we find that for particular node all labels are drug A and none for Drug B when dividing data between Male & Female.
- Entropy = 1 when it has impurity, or say between Drug A & B we get equal number of labels for both for that particular node. 

$$
\text{Entropy} = - p(A) \log_2(p(A)) - p(B) \log_2(p(B))
$$

![[Pasted image 20240615185609.png]]

- In above example, we go entropy by calculating with he given equation on each node. 
- But how do we select best attribute between ***Sex*** and ***Cholesterol***?
#### What is [[Information Gain]]?
- The answer is the tree with the higher information gain after splitting.
- Definition: The information that can increase the level of certainty after splitting. 

**Information Gain = (Entropy before split) - (weighted entropy after split)**

![[Pasted image 20240615190432.png]]

Here, Information Gain for ***Sex*** attribute (0.151) s higher than ***Cholesterol*** attribute (0.048)
Thus, More suitable for first or root node will be ***Sex*** attribute. Then we can carry on the process for rest of the attributes to come as second layer of the tree. 

### When to use decision tree? 
Use a decision tree when you need a clear, interpretable model that can handle both numerical and categorical data. It’s suitable for:

1. **Classification and Regression Tasks**: Decision trees can solve classification problems (e.g., spam detection) and regression problems (e.g., predicting house prices).
2. **Handling Non-linear Relationships**: Decision trees can capture non-linear relationships between features and target variables.
3. **Feature Importance**: To determine the importance of different features in your dataset.
4. **Small to Medium-Sized Datasets**: They work best with smaller datasets where they can be visualized and interpreted easily.  

Avoid using decision trees with very large datasets or when the data is prone to overfitting, unless combined with techniques like ensemble methods (e.g., Random Forests).
### Assumptions
1.  At the beginning, the whole training set is considered as the root.
2.  Feature values need to be categorical. If the values are continuous then they are discretized prior to building the model.
3.  Records are distributed recursively on the basis of attribute values.
4.  Order to placing attributes as root or internal node of the tree is done by using some statistical approach.