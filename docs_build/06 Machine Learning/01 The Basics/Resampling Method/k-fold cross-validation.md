Cross-validation is a method of splitting all your data into three parts: training, testing, and validation data. Data is split into k subsets, and the model has trained on k-1 of those datasets.

The last subset is held for testing. This is done for each of the subsets. This is k-fold cross-validation. Finally, the scores from all the k-folds are averaged to produce the final score.

[[k-fold cross-validation]]