import random, time, tracemalloc
from randomized_shellsort import randomized_shellsort
from max_heapsort import heap_sort

# generate Datasets according to size and types
def generate_dataset(ds_size, ds_type):
    dataset_sorted = list(range(ds_size))
    if ds_type == 'sorted':
        return dataset_sorted
    elif ds_type == 'reversed':
        return dataset_sorted[::-1]
    elif ds_type == 'random':
        random.shuffle(dataset_sorted)
        return dataset_sorted

# calculate Running Time & Memory Usage for each sorting
def count_time_memory(dataset, algorithm):
    tracemalloc.start()
    start = time.time()
    
    if algorithm == 'shellsort':
        randomized_shellsort(dataset)
    elif algorithm == 'heapsort':
        heap_sort(dataset)
    end = time.time()
    memory_usage =  tracemalloc.get_traced_memory()[1]

    tracemalloc.stop()
    running_time = (end-start)*1000
    return running_time, memory_usage


def main():
    sizes = [512, 8192, 65536]
    types = ['sorted', 'reversed', 'random']
    algorithms = ['shellsort', 'heapsort']
    
    for ds_size in range(3):
        for ds_type in range(3):
            file_name = str(sizes[ds_size]) + '_' + types[ds_type] + '.txt'
            result = open(file_name, "w")
            dataset = generate_dataset(sizes[ds_size], types[ds_type])
            result.write(f"Created {types[ds_type]} dataset with size of {sizes[ds_size]}\n")
            result.write(f"{dataset}\n\n")
            
            for algo in range(2): 
                time, memory = count_time_memory(dataset, algorithms[algo])
                if algo == 0:
                    result.write(f"Sorting with Randomized Shellsort Algorithm\n")
                else:
                    result.write(f"Sorting with Max-Heapsort Algorithm\n")
                print(f"Sorting Dataset {types[ds_type]} with a size of {sizes[ds_size]} using {algorithms[algo]}")
                print(f"Running Time: {time} , Memory Usage: {memory}\n")
                result.write(f"Sorted {types[ds_type]} dataset with size of {sizes[ds_size]}\n")
                result.write(f"{dataset}\n")
                result.write(f"Running Time: {time} , Memory Usage: {memory}\n")
            result.close()
   

if __name__ == '__main__':
    main()
