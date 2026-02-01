import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    norm = np.linalg.norm(v, axis=-1, keepdims=True)
    return v / (norm + 1e-8)  
