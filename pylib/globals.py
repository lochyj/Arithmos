
# --------------|
# GLOBAL CONSTS |
# --------------|

# Graph
CONNECTION_LIST = 0
ADJACENCY_MATRIX = 1

WEIGHT = "weight"

def check_hashable_type(object: any):
    if isinstance(object, int) or isinstance(object, float) or isinstance(object, str) or isinstance(object, tuple):
        return
    else:
        print(f"ERROR: Cannot convert {object} to a hash.")
        print("It is not a hashable type and cannot be used in Arithmos.")
        print("Exiting the program.")
        exit()
