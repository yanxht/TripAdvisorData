import numpy as np
from scipy.sparse import csr_matrix

def LoadTripAdvisorData():
	# Load terms from triadvisor reviews
	term = np.loadtxt('tripadvisor_txt/term.txt', dtype = bytes).astype(str)
	nterm = len(term)
	# Load A matrix that encodes ancestor-descendant relations
	Atxt = np.loadtxt('tripadvisor_txt/A.txt', dtype='int32', delimiter=',')
	nnode = max(Atxt[:,1])+1
	A = csr_matrix((Atxt[:,2], (Atxt[:,0], Atxt[:,1])), shape=(nterm, nnode))
	# Load training design matrix
	Xtraintxt = np.loadtxt('tripadvisor_txt/X_train.txt', dtype='int32', delimiter=',')
	ntrain = max(Xtraintxt[:,0])+1
	Xtrain = csr_matrix((Xtraintxt[:,2], (Xtraintxt[:,0], Xtraintxt[:,1])), shape=(ntrain, nterm))
	# Load testing design matrix
	Xtesttxt = np.loadtxt('tripadvisor_txt/X_test.txt', dtype='int32', delimiter=',')
	ntest = max(Xtesttxt[:,0])+1
	Xtest = csr_matrix((Xtesttxt[:,2], (Xtesttxt[:,0], Xtesttxt[:,1])), shape=(ntest, nterm))
	# Load training ratings
	ytrain = np.loadtxt('tripadvisor_txt/y_train.txt', dtype='int32')
	# Load testing ratings
	ytest = np.loadtxt('tripadvisor_txt/y_test.txt', dtype='int32')
	return term, A, Xtrain, Xtest, ytrain, ytest