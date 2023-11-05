import random
# number of region compare-exchange repetiotion
C = 1

# swap elements 
def compare_exchange(dataset, i, j):
    if ((i < j) and (dataset[i] > dataset[j])) or ((i > j) and (dataset[i] < dataset[j])):
        temp = dataset[i]
        dataset[i] = dataset[j]
        dataset[j] = temp

def permute_random(dataset):
    for i in range(len(dataset)):
        rand = random.randint(0, len(dataset)-i)+i-1
        temp = dataset[i]
        dataset[i] = dataset[rand]
        dataset[rand] = temp

def region_compare_exchange(dataset, s, t, offset):
    mate = list(range(offset))
    for _ in range(0, C):
        for i in range(offset):
            mate[i] = i
        permute_random(mate)
        for i in range(offset):
            compare_exchange(dataset, s+i, t+mate[i])

def randomized_shellsort(dataset):
    n = len(dataset)
    offset = n
    while offset > 1:
        offset = int(offset/2)
        for i in range(0, n-offset, offset):  # compare-exchange Up
            region_compare_exchange(dataset, i, i+offset, offset)
        for i in range(n-offset, 0, -offset): # compare-exchange down
            region_compare_exchange(dataset, i-offset, i, offset)
        for i in range(0, n-3*offset, offset): # compare 3 hops up
            region_compare_exchange(dataset, i, i+3*offset, offset)
        for i in range(0, n-2*offset, offset): # compare 2 hops up
            region_compare_exchange(dataset, i, i+2*offset, offset)
        for i in range(0, n, 2*offset):        # compare odd-even regions
            region_compare_exchange(dataset, i, i+offset, offset)
        for i in range(offset, n-offset, 2*offset): # compare even-odd regions
            region_compare_exchange(dataset, i, i+offset, offset)

# def main():
#     dataset = [8,3,2,9,0,1,5,16]
#     randomized_shellsort(dataset)

# if __name__ == '__main__':
#     main()