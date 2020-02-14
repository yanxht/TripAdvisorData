Processed TripAdvisor Data
====

The repo shares TripAdvisor review and rating data that were used in [Yan, X. and Bien, J. (2018) "Rare Feature Selection in High Dimensions"](https://arxiv.org/abs/1803.06675), including training data (Xtrain, ytrain), testing data (Xtest, ytest), adjectives from the reviews, and a binary matrix that encodes a hierarchical tree for the terms. These structured data were processed from raw data crawled by [Wang et.al. (2010)](https://www.cs.virginia.edu/~hw5x/paper/rp166f-wang.pdf). The hierarchical tree for relating the terms was generated with 100-dimensional embeddings that were pre-trained by *GloVe* ([Pennington et al., 2014](https://nlp.stanford.edu/pubs/glove.pdf)) on Gigaword5 and Wikipedia2014 corpora. In constructing the tree, we also leverage NRC Emotion Lexicon ([Mohammad and Turney, 2013](https://www.semanticscholar.org/paper/Crowdsourcing-a-Word-Emotion-Association-Lexicon-Mohammad-Turney/54227c063bb04489caffd65ff9fc6218788ddb25)) to separate positive and negative sentiments. Please refer to Section 6 of [Yan and Bien (2018)](https://arxiv.org/abs/1803.06675) for details of processing the data.

Load the Data
====

- In R
```r
load(“tripadvisor.RData”)
```

- In Python (requires numpy and scipy)
```python
import loadtxtdata
term, A, Xtrain, Xtest, ytrain, ytest = LoadTripAdvisorData()
```

When you are using above dataset in your research, please consider to cite the following paper:

@article{yan2018rare,
  title={Rare feature selection in high dimensions},
  author={Yan, Xiaohan and Bien, Jacob},
  journal={arXiv preprint arXiv:1803.06675},
  year={2018}
}