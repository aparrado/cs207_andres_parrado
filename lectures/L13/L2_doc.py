import numpy as np

def L2(v, *args):
    """Compute the weighted L2 norm.
    
    INPUTS
    =======
    v: a real-valued vector. Should be a numpy array
    
    *args: If provided, this argument needs to be a vector and will be 
    interpreted as weights. Should be an numpy array of the same dimensions
    as the vector v
    
    RETURNS
    ========
    A positive integer representing the L2 norm of the inputed vector

    EXAMPLES
    =========
    v = np.array([1,2,3])
    w = np.array([1,1,0.5])
    L2(v,w) = 2.692582403567252
    """
    
    s = 0.0 # Initialize sum
    if len(args) == 0: # No weight vector
        for vi in v:
            s += vi * vi
    else: # Weight vector present
        w = args[0] # Get the weight vector
        if (len(w) != len(v)): # Check lengths of lists
            raise ValueError("Length of list of weights must match length of target list.")
        for i, vi in enumerate(v):
            s += w[i] * w[i] * vi * vi
    return np.sqrt(s)


