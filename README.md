Processed TripAdvisor Data
====

The repo shares TripAdvisor review and rating data that were used in [Yan, X. and Bien, J. (2018) "Rare Feature Selection in High Dimensions"](https://arxiv.org/abs/1803.06675), including training data (Xtrain, ytrain), testing data (Xtest, ytest), terms from the reviews, and a binary matrix that encodes a hierarchical tree for the terms. These structured data were processed from raw data crawled by [Wang et.al. (2010)](https://www.cs.virginia.edu/~hw5x/paper/rp166f-wang.pdf). Please refer to Section 6 of [Yan and Bien (2018)](https://arxiv.org/abs/1803.06675) for details of processing the raw data. 

To Load the Data
====

- In Python (requires numpy and scipy)
```python
import loadtxtdata
term, A, Xtrain, Xtest, ytrain, ytest = LoadTripAdvisorData()
```

- In R
```r
load(tripadvisor.RData)
```