import sequential
import time

board_sizes = [2, 4, 8, 16, 32, 64, 128, 256, 343, 512]

for n in board_sizes:
    print(f"Solving {n}-Queens problem...")
    start_time = time.time()
    solution = sequential.solve_n_queens(n)
    if solution is None:
        print("UNSAT.")
    else:
        # sequential.print_solution(solution)
        print("SAT.")
    print("Run time:  %s seconds" % (time.time() - start_time))