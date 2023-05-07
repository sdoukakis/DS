
# Εργασία03 - Δραστηριότητα μαθητών από το μάθημα ειδικά θέματα διδακτικής της πληροφορικής

with open('sorting_runtimes.txt', 'r') as file:
    data = file.read().splitlines()

runtimes = {}

for i in range(0, len(data), 8):
    algorithm = data[i].split(' - ')[0]
    runtime = float(data[i+1].split(' - ')[1].split(' ')[0])
    runtimes[algorithm] = runtimes.get(algorithm, 0) + runtime

for algorithm, runtime in runtimes.items():
    avg_runtime = runtime / 10

fastest_algorithm = min(runtimes.items(), key=lambda x: x[1])
print(f"The fastest sorting algorithm is {fastest_algorithm[0]} with an average runtime of {fastest_algorithm[1]/10:.6f} seconds.")
