import TreeNode as TN
import Problem as P
import Problem_State as PS
import time

if __name__ == '__main__':

    # inizializzazione matrice
    r = [[5, 1, 2],
         [4, 6, 3],
         [0, 7, 8]]
    start = PS.State(r)
    depth_limit = 20
    problem = P.Problem(start)

    TN.Print_Path(TN.Tree_Search(problem, depth_limit), time.process_time())  #run dell'algoritmo di searching




