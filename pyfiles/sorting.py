from enrollmentrecord import EnrollmentRecord

def is_sorted(l):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            return False
    return True

def bubble(L: list[EnrollmentRecord], property: str) -> list[EnrollmentRecord]:
    for increment in range(len(L)):
        swapped = False
        for y in range(len(L) - 1 - increment):
            if L[y].get_property(property) > L[y + 1].get_property(property):
                swapped = True
                L[y], L[y + 1] = L[y + 1], L[y]
        if not swapped:
            return L

    return L

def insertion(L: list[EnrollmentRecord], property: str) -> list[EnrollmentRecord]:
    for i in range(len(L)):
        for j in range(len(L) - i, len(L)):
            if L[j - 1].get_property(property) > L[j].get_property(property):
                L[j - 1], L[j] = L[j], L[j - 1]

    return L

def get_algorithm_method(algorithm_type: str):
    match algorithm_type:
        case "insertion":
            return insertion
        case "bubble":
            return bubble
        case _:
            raise ValueError("Invalid sorting algorithm type")


if __name__ == "__main__":
    testarr = [25,67,1,6,2,3,4,5,10,125,5,6,7,7]
    insertion(testarr)
    print(testarr)
    print(is_sorted(testarr))