from utils import *
import math
from node import Node


def merkle_proof(tx, merkle_tree):
    """Given a tx and a Merkle tree object, retrieve its list of tx's and
    parse through it to arrive at the minimum amount of information required
    to arrive at the correct block header. This does not include the tx
    itself.

    Return this data as a list; remember that order matters!
    """
    #### YOUR CODE HERE
    treeLs = merkle_tree.leaves
    # txIndex = merkle_tree.leaves.index(tx)
    # if len(tx) == 1:
    # 	return []
    # else:
    # 	for i in range(0, len(lves), 2):
    # 		print(lves[i], lves[i+1])

    def rProof(txs, tx, nodes):
    	if len(txs) == 1:
    		return nodes
    	hashed = []
    	H = 0
    	for i in range(0, len(txs), 2):
    		hashed.append(hash_data(txs[i] + txs[i+1]))
    		if (txs[i] == tx):
    			nodes.insert(0, Node('r', txs[i+1]))
    			H = hash_data(tx + txs[i+1])
    		elif (txs[i+1] == tx):
    			nodes.insert(0, Node('l', txs[i]))
    			H = hash_data(txs[i] + tx)
    	return rProof(hashed, H, nodes)

    return rProof(treeLs, tx, [])



def verify_proof(tx, merkle_proof):
    """Given a Merkle proof - constructed via `merkle_proof(...)` - verify
    that the correct block header can be retrieved by properly hashing the tx
    along with every other piece of data in the proof in the correct order
    """
    #### YOUR CODE HERE
    mRev = merkle_proof[::-1]
    ret = tx
    for txn in mRev:
        if txn.direction == 'r':
            ret = hash_data(ret + txn.tx)
        else:
            ret = hash_data(txn.tx + ret)
    return ret
