
class PreferenceError(Exception) :
    def __init__(self, error) :
        self.error = error
    def __str__(self) :
        return repr(self.error)

def pref_input(pref_matrix, other_matrix_N) :
    if type(pref_matrix) != list :
        raise PreferenceError("Preferences must be lists.")
    if len(pref_matrix) == 0 | other_matrix_N == 0 :
        raise PreferenceError("Preferences must be non-empty lists.")
    for pref in pref_matrix :
        if type(pref) != list :
            raise PreferenceError("Individual preferences must be lists.")
        if len(pref) != other_matrix_N+1 :
            raise PreferenceError("Individual preferences lenght must be equal to the other group number of agents plus one.")
        for elem in pref :
            if type(elem) != int :
                raise PreferenceError("Individual preferences elements must be non-negative integers.")
        if sorted(pref) != list(range(other_matrix_N+1)) :
            raise PreferenceError("Individual preferences elements out of index.")
            
def pref_copy(pref) :
    copy = []
    for i in range(len(pref)) :
        copy.append(pref[i][:])
    return copy

def DA(matrix_M,matrix_W) :
    #
    # Inputs
    #     pref_M - Preferences of proposing agents
    #     pref_W - Preferences of proposed agents
    #     
    # The preferences must be inputed as a matrix (i.e. a list of lists of the same length).
    #
    # Example: [[2,1,0],
    #           [1,0,2],
    #           [0,1,2]]
    #
    # Agent 1 prefers 2nd over 1st, and being alone as its last choice.
    # Agent 2 prefers 1st over being alone, and 2nd as its last choice.
    # Agent 3 prefers being alone than 1st, and 2nd as its last choice.
    # (this means that are 2 counterpart agents)
    #
    # Outputs
    #     matchs - Three-element dict. The first is the list with the matchs for proposing agents. The second is the list with the matchs for proposed agents. The third is the number of steps that algorithm took.
    #
    pref_M = pref_copy(matrix_M)
    pref_W = pref_copy(matrix_W)
    M = len(pref_M)
    W = len(pref_W)
    pref_input(pref_M,W)
    pref_input(pref_W,M)
    W_status = []
    for w in range(0,W) :
        W_status.append([0])
    M_active = []
    for m in range(0,M) :
        M_active.append(1)
    step = 0
    while 1 in M_active :
        for m in range(0,M) :
            if M_active[m] == 1 and pref_M[m][0] == 0 :
                M_active[m] = 0
            elif M_active[m] == 1 :
                W_status[pref_M[m][0]-1].append(m+1)
                del pref_M[m][0]
                M_active[m] = 0
        for w in range(0,W) :
            if len(W_status[w]) > 1 :
                while len(W_status[w]) > 1 :
                    if pref_W[w].index(W_status[w][0]) < pref_W[w].index(W_status[w][1]) :
                        if W_status[w][1] != 0 :
                            M_active[W_status[w][1]-1] = 1
                        del W_status[w][1]
                    else :
                        if W_status[w][0] != 0 :
                            M_active[W_status[w][0]-1] = 1
                        del W_status[w][0]
        step = step+1
    match_M = []
    match_W = []
    for m in range(0,M) :
        if [m+1] in W_status :
            match_M.append(W_status.index([m+1])+1)
        else :
            match_M.append(0)
    for w in range(0,W) :
        match_W.append(W_status[w][0])
    return {"M" : match_M , "W" : match_W , "steps" : step}    







