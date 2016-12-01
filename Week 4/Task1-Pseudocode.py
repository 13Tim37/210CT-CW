list <- INPUT list
low <- INPUT lowest value in range
high <- INPUT highest value in range

FUNCTION BINARY-SEARCH(list, low, high):
    L <- LENGTH(list)
    r <- list[round(L/2)]
    IF L = 1 AND r not in range(low,high+1):
        RETURN False
    ELSEIF r in range(low,high+1):
        RETURN True
    ELSEIF low > r:
        RETURN BINARY-SEARCH(list[round(L/2)::1],low,high)
    ELSEIF high+1 < r:
        RETURN BINARY-SEARCH(list[:round(L/2):1],low,high)
    ELSE:
        RETURN False

OUTPUT BINARY-SEARCH(list,low,high)
