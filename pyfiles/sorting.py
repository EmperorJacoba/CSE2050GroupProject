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

def get_algorithm_method(algorithm_type: str):
    """
    Takes algorithm type and returns the corresponding sorting algorithm
    :param algorithm_type: "bubble" or "insertion"
    :return: Sorting algorithm function. Call with <algorithm>(list[EnrollmentRecord], <property>),
    where property is an EnrollmentRecord property ("name", "id", "date")

    Created by Jacob Russell
    """
    match algorithm_type:
        case "insertion":
            return insertion
        case "bubble":
            return bubble
        case _:
            raise ValueError("Invalid sorting algorithm type")