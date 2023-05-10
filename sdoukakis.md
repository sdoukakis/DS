
# Αποθετήριο του μαθήματος: Ανάλυση Δεδομένων

## Ονοματεπώνυμο
## [Προφίλ Github: aggelos2000430](https://github.com/aggelos2000430)

| Εβδομάδα | Παραδοτέα | Ολοκλήρωση Παραδοτέου :heavy_check_mark: |
| --- | --- | --- |
| 1 | Δημιουργία προφίλ στην πλατφόρμα + Fork του αποθετηρίου του μαθήματος|  |
| 2 | Δημιουργία του αρχείου .md στο προφίλ σας και αντιγραφή του πίνακα παραδοτέων στο προσωπικό σας αρχείο με τίτλο το ονοματεπώνυμο σας με λατινικούς χαρακτήρες που αποτελεί και την τελική αναφορά του μαθήματος|  |
| 3 | Συγγραφή μιας σύντομης περιγραφής για την σημασία της ανάλυσης δεδομένων στον σύγχρονο κόσμο |  |
| 4 | Εκτέλεση του κώδικα στο σύστημά σας |  |
| 5 | Αντιγραφή του python κώδικα και λεπτομερής σχολιασμός του, εντός της αναφοράς σας |  |
| 6 | Προφορική υποστήριξη της αναφοράς σας |  |
## Παραδοτέο 3
Η ανάλυση δεδομένων είναι η διαδικασία αξιολόγησης δεδομένων χρησιμοποιώντας αναλυτικά και στατιστικά εργαλεία για να ανακαλύψετε χρήσιμες πληροφορίες και να βοηθήσετε στη λήψη επιχειρηματικών αποφάσεων. Υπάρχουν διάφορες μέθοδοι ανάλυσης δεδομένων, όπως η εξόρυξη δεδομένων, η ανάλυση των κειμένων, η επιχειρηματική ευφυΐα και η απεικόνιση δεδομένων.
## Παραδοτέο 5
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

This code reads data from a file named 'sorting_runtimes.txt', which contains the runtimes of various sorting algorithms. Each line of the file represents the runtime of a single sorting algorithm. The file has eight lines per algorithm, with the first line containing the name of the algorithm and the next line containing the runtime.
The code then reads the data from the file and stores it in a list called data, with each line of the file as a separate item in the list.
Next, the code initializes an empty dictionary called runtimes to store the total runtime for each sorting algorithm. The code then loops through the data list in increments of eight, as there are eight lines for each algorithm in the file. For each algorithm, the code extracts the name and runtime from the appropriate lines in the data list, converts the runtime to a float value, and adds it to the corresponding entry in the runtimes dictionary.
After calculating the total runtime for each algorithm, the code then calculates the average runtime by dividing the total runtime by the number of times the algorithm was run, which in this case is 10.
Finally, the code finds the algorithm with the fastest average runtime by using the min function to find the minimum value in the runtimes dictionary and returns its key-value pair as a tuple. The lambda function is used to specify that the key to compare in the min function is the second element of each tuple, which is the runtime value.
The code then prints a string indicating the algorithm with the fastest average runtime and its runtime in seconds, formatted to six decimal places.
