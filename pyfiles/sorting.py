from enrollment_record import EnrollmentRecord

def bubble(L: list[EnrollmentRecord], property: str) -> list[EnrollmentRecord]:
    """
    Takes a list of EnrollmentRecords and sorts it by the given property with bubble sort algorithm.
    :param L: list[EnrollmentRecord]
    :param property: EnrollmentRecord property to sort by ("name", "id", "date")
    :return: Sorted L

    Created by Justin Elak
    """
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
    """
    Takes a list of EnrollmentRecords and sorts it by the given property with insertion sort algorithm.
    :param L: list[EnrollmentRecord]
    :param property: EnrollmentRecord property to sort by ("name", "id", "date")
    :return: Sorted L

    Created by Justin Elak
    """
    for i in range(len(L)):
        for j in range(len(L) - i, len(L)):
            if L[j - 1].get_property(property) > L[j].get_property(property):
                L[j - 1], L[j] = L[j], L[j - 1]
            else: break

    return L

def _merge(L: list[EnrollmentRecord], L1: list[EnrollmentRecord], L2: list[EnrollmentRecord], property: str):
    """
    Internal merge function for merge sort.

    Created by Jacob Russell
    """
    i = 0
    j = 0

    while len(L1) > i and len(L2) > j:
        if L1[i].get_property(property) < L2[j].get_property(property):
            L[i+j] = L1[i]
            i += 1
        else:
            L[i+j] = L2[j]
            j += 1

    L[i+j:] = L1[i:] + L2[j:]

def merge_sort(L: list[EnrollmentRecord], property: str) -> list[EnrollmentRecord]:
    """
    Takes a list of EnrollmentRecords and sorts it by the given property with merge sort algorithm.
    :param L: list[EnrollmentRecord]
    :param property: EnrollmentRecord property to sort by ("name", "id", "date")
    :return: Sorted L

    Created by Jacob Russell
    """
    if len(L) < 2:
        return L

    mid = len(L) // 2
    left = L[:mid]
    right = L[mid:]

    merge_sort(left, property)
    merge_sort(right, property)

    _merge(L, left, right, property)

    return L

def quick_sort(L: list[EnrollmentRecord], property: str) -> list[EnrollmentRecord]:
    """
    Takes a list of EnrollmentRecords and sorts it by the given property with quick sort algorithm.
    :param L: list[EnrollmentRecord]
    :param property: EnrollmentRecord property to sort by ("name", "id", "date")
    :return: Sorted L

    Created by Jacob Russell
    """
    return _quicksort(L, 0, len(L), property)

def _quicksort(L: list[EnrollmentRecord], left, right, property):
    """
    Internal quicksort logic for the quicksort algorithm.

    Created by Jacob Russell
    """
    if right - left <= 1:
        return L

    pivot = _partition(L, left, right, property)

    _quicksort(L, left, pivot, property)
    _quicksort(L, pivot+1, right, property)

    return L

def _partition(L: list[EnrollmentRecord], left, right, property):
    """
    Internal partition algorithm for the quicksort algorithm.

    Created by Jacob Russell
    """
    pivot = right - 1
    right = pivot - 1

    while left < right:
        while L[left].get_property(property) < L[pivot].get_property(property):
            left += 1
        while left < right and L[right].get_property(property) >= L[pivot].get_property(property):
            right -= 1
        if left < right:
            L[left], L[right] = L[right], L[left]

    if L[left].get_property(property) >= L[pivot].get_property(property):
        L[left], L[pivot] = L[pivot], L[left]

    return left

def get_algorithm_method(algorithm_type: str):
    """
    Takes algorithm type and returns the corresponding sorting algorithm
    :param algorithm_type: "merge" or "quick"
    :return: Sorting algorithm function. Call with <algorithm>(list[EnrollmentRecord], <property>),
    where property is an EnrollmentRecord property ("name", "id", "date")
    :except DeprecationWarning: Pass in insertion/bubble (deprecated algorithms)
    Created by Jacob Russell
    """
    match algorithm_type:
        case "insertion":
            raise DeprecationWarning("Insertion sort is no longer supported for course sorting.")
            # return insertion
        case "bubble":
            raise DeprecationWarning("Bubble sort is no longer supported for course sorting.")
            # return bubble
        case "merge":
            return merge_sort
        case "quick":
            return quick_sort
        case _:
            raise ValueError("Invalid sorting algorithm type")