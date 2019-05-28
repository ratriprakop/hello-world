class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        sumC = sumP = 0
        startP = endP = startC = endC = -1
        
        Negative = False
        for index, item in enumerate(A):
            if item >= 0:
                Negative = False
                sumC += item
                if startC == -1:
                    startC = endC = index
                else:
                    endC = index
            else:
                
                if not Negative and ((startP == -1 and endP == -1) or (sumP == sumC) or (sumP == sumC and endP - startP < endC - startC)):
                    startP = startC
                    endP = endC
                    sumP = sumC
                    
                startC = endC = -1
                sumC = 0
                Negative = True
        
        if sumP == sumC:
            if endP - startP < endC - startC:
                return A[startC: endC + 1]
            else:
                return A[startP: endP + 1]
        elif sumP < sumC:
            return A[startC: endC + 1]
        else:
            return A[startP: endP + 1]
                    
                
        
