def is_sorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def bubble(l):
    for increment in range(len(l)):
        swapped = False
        for y in range(len(l)-1-increment):
            if l[y] > l[y+1]:
                swapped = True
                l[y], l[y+1] = l[y+1], l[y]
        if not swapped:
            return
            

def insertion(l):
    for i in range(len(l)):
        for j in range(len(l) - i, len(l)):
            if l[j-1] > l[j]:
                l[j-1], l[j] = l[j], l[j-1]

if __name__ == "__main__":
    testarr = [25,67,1,6,2,3,4,5,10,125,5,6,7,7]
    insertion(testarr)
    print(testarr)
    print(is_sorted(testarr))