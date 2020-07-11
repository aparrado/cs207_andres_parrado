import numpy as np

def L2(v, *args):
    """Compute the weighted L2 norm.
    
    INPUTS
    =======
    
    RETURNS
    ========

    NOTES
    =====
    PRE: 
    POST:

    EXAMPLES
    =========
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
