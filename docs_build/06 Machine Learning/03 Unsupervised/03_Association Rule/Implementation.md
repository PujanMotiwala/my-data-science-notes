>Apriori algorithm is a popular algorithm used in data mining and machine learning to discover frequent item sets and association rules in a dataset. The Apriori algorithm is based on the principle that any subset of a frequent item set must also be frequent.

>Here's an example of how to perform Apriori algorithm in Python using the `apyori` library:

```python
from apyori import apriori

# Define the transactions
transactions = [
    ['milk', 'bread', 'butter'],
    ['milk', 'coffee', 'sugar'],
    ['milk', 'bread', 'butter', 'coffee'],
    ['milk', 'bread', 'sugar'],
    ['milk', 'bread', 'butter', 'sugar'],
    ['milk', 'coffee']
]

# Define the minimum support level
min_support = 0.3

# Perform the Apriori algorithm
results = list(apriori(transactions, min_support=min_support))

# Print the results
for itemset in results:
    print(itemset)
```

>In this example, we first define a list of transactions, where each transaction is represented as a list of items. Then we define the minimum support level, which is the minimum proportion of transactions that an item set must appear in. The `apriori()` function from the `apyori` library takes the transactions and minimum support level as input and returns the frequent item sets and association rules as output.

>It's also worth mentioning that, the `apyori` library has some optional parameters such as minimum threshold for lift and confidence for association rules, which can be passed to the `apriori()` function to fine-tune the results.
