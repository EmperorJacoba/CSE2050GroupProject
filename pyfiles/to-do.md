# To-Do
- [ ] Add an EnrollmentRecord to represent enrollment history for a student
  - [ ] Change course enrollment roster to store enrollment history instead of raw student objects
- [ ]  Create a waitlist for full courses
   - [ ] Implement a queue using a double linked list
- [ ] Create sorting method for enrolled roster
- [ ] Add the capacity and waitlist attribute to Course
- [ ] Create Recursive binary search for drop
#
- [ ] Create test cases
  - [ ] LinkedQueue (FIFO order; dequeue on empty raises; size tracking)
  - [ ] Enrollment (enroll until capacity; extra students go on waitlist; drop triggers waitlist promotion)
  - [ ] Sorting tests (roster correctly sorted by id, name, and date for each algorithm implemented)
  - [ ] Binary search (find first/middle/last; not found returns -1; and/or behavior when roster not sorted by ID)
#
- [ ] Complexity reflection
  - [ ] Give time complexity of deque and enqueue methods
  - [ ] Give time complexity for each sorting algorithm used
  - [ ] Give time complexity for the recursive binary search and explain why sorting is important for the functionality of the search
  - [ ] Compare the two sorting algorithms and explain why one might be preferred