import numpy as np
import os
import random
import numpy as np


class Greedy_FastestFirst:
    
    def __init__(self,neighborhood_matrix, chunks_matrix, uplink_vector, downlink_vector, P_value, K_value):
        self.neighborhood_matrix=neighborhood_matrix
        self.chunks_matrix=chunks_matrix
        self.uplink_vector=uplink_vector
        self.downlink_vector=downlink_vector
        self.P_value=P_value
        self.K_value=K_value      
        
   
    def add_triple(self,mydict,key, triple):
        if key in mydict:
            mydict[key].append(triple)
        else:
            mydict[key] = [triple]
            
    def Update_Dict(self,round_index,receiver,sender,chunk,mydict):
        self.add_triple(mydict,round_index,(receiver,sender,chunk))
        
            
    def Greedy_FastestFirst_Execution(self,round_index,mydict):
        #neighborhood_matrix, chunks_matrix, uplink_vector, downlink_vector=read_matrices_from_file()
        nodes_Number=len( self.neighborhood_matrix)
        chunks_Number=len(self.chunks_matrix)
        downlink_vector_copy=self.downlink_vector.copy()
        uplink_vector_copy=self.uplink_vector.copy()
        partialtransmission=0
        Chunk_requests = [[] for _ in range(chunks_Number)]
        for i in range (nodes_Number):
            missed_chunks=[index for index, value in enumerate(self.chunks_matrix [i]) if value == 0 ]
            for chunk in missed_chunks:
                chunk_owners= [row for row in range(nodes_Number) if self.chunks_matrix[row][chunk] == 1 and self.neighborhood_matrix[i][row]==1]                
                #print("i:",i, " chunk:",chunk, chunk_owners)
                
                if len(chunk_owners)>0:
                    chunk_owners_uplink=[]
                    for k in range(len(chunk_owners)):
                        chunk_owners_uplink.append(self.uplink_vector[k])
                    target_owner_index=chunk_owners_uplink.index(max(chunk_owners_uplink))
                    sender = chunk_owners[target_owner_index]
                    #print(chunk_owners,chunk_owners_uplink,sender)
                    Chunk_requests[sender].append((i,chunk,self.downlink_vector[i]))
        #print(Chunk_requests)
        #sending------------------------------
        for i in range (nodes_Number):
            #print("request:",Chunk_requests[i])
            sorted_list = sorted(Chunk_requests[i], key=lambda x: x[2], reverse=True)
            for j in range (min(len(sorted_list),self.K_value)):# i is sender
                receiver=sorted_list[j][0]
                chunk=sorted_list[j][1]
                if self.chunks_matrix[receiver][chunk]==0:
                    if downlink_vector_copy[receiver]>0 and uplink_vector_copy[i]>0:
                        self.chunks_matrix[receiver][chunk]+=1   #sending chunk to sender
                        self.Update_Dict(round_index,receiver,i,chunk,mydict)
                        
                        partialtransmission+=1
                        downlink_vector_copy[receiver]-=1
                        uplink_vector_copy[i]-=1
    
        return self.chunks_matrix.copy(),partialtransmission

    def Operation(self):
        mydict={}
        Totaltransmission=0
        round_index=1
        Continue=True
        while(Continue):
            print("---------time slot-Random-Fifo:",round_index," ---------" )
            Nodes_Number=len(self.neighborhood_matrix)
            chunks_matrix,partialtransmission=self.Greedy_FastestFirst_Execution(round_index,mydict)
            count_ones_per_row = [sum(row) for row in chunks_matrix]        
            count_values_greater_than_p = sum(1 for value in count_ones_per_row if value >= self.P_value)
            round_index+=1
            print("Partial Communications:",partialtransmission)
            Totaltransmission+=partialtransmission
            if count_values_greater_than_p>=Nodes_Number or partialtransmission==0:
                Continue=False
            print("count_values_greater_than_p", count_values_greater_than_p)
            #print("Ones", count_ones(chunks_matrix))
                
        print("Total Communications:",Totaltransmission)
        #print("Ones", count_ones(chunks_matrix))
        return mydict
    
    
