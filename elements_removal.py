def elements_removal(array):
    array.sort(reverse=True)
    cost=0
    for i in range(len(array)):
        cost+=array[i]*(i+1)
    return cost


array=list(map(int,input('Enter the Array Elements : ').split()))
print(elements_removal(array))