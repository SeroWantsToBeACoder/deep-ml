import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    norm_types = ["l1", "l2", "linf", "frobenius"]

    if norm_type == "frobenius" and arr.ndim != 2:
        raise ValueError("Frobenius norm requires a 2D array.")
    
    
    arr = arr.flat
    
    
    if norm_type == "l1":
        out = 0
        for el in arr:
            out += abs(el)
        return float(out)
    elif norm_type == "l2" or norm_type == "frobenius":
        out = 0
        for el in arr:
            out += pow(el, 2)
        return float(np.sqrt(out))
    elif norm_type == "linf":
        out = abs(arr[0])
        for el in arr:
            if abs(el) > out:
                out = abs(el)
        return float(out)
    else:
        raise ValueError(...)



