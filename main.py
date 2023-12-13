from Greedy_FastestFirst import Greedy_FastestFirst
import numpy as np

if __name__ == "__main__":
    
    #number_of_nodes=10
    neighborhood_matrix=  [[0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
                           [0, 0, 0, 0, 0, 1, 1, 0, 1, 0],
                           [0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
                           [1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
                           [0, 0, 1, 0, 0, 1, 1, 0, 1, 1],
                           [1, 1, 0, 0, 1, 0, 0, 1, 1, 0],
                           [1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
                           [1, 0, 0, 1, 0, 1, 0, 0, 1, 0],
                           [1, 1, 0, 1, 1, 1, 0, 1, 0, 1],
                           [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]
    
    #chunks per node=2, and number of chunks=20
    chunks_matrix=[[1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                   [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1],
                   [1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
                   [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0],
                   [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1]] 
    
    uplink_vector=[2, 3, 3, 2, 2, 3, 3, 3, 2, 2]
    downlink_vector=[3, 3, 2, 2, 3, 3, 2, 2, 2, 2]
    Greedy_FastestFirst_instance=Greedy_FastestFirst(neighborhood_matrix, chunks_matrix, uplink_vector, downlink_vector, P_value=30, K_value=5)
    mydict=Greedy_FastestFirst_instance.Operation()
    print(mydict)#output: a dictionary where key is the timeslot index, and the values is a list of triples (communications)
                 #that teach triple is (receiver node, ender node, chunk id)

        
