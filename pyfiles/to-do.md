# To-Do
### 6.1 Enrollment Record
- [ ] Add an EnrollmentRecord to represent enrollment history for a student
  - [ ] Change course enrollment roster to store enrollment history instead of raw student objects

### 6.2 LinkedQueue ADT / 6.3 Course capacity, waitlist logic
- [ ]  Create a waitlist for full courses
   - [ ] Implement a queue using a double linked list

### 6.4 Sorting enrollment roster
- [ ] Create sorting method for enrolled roster
- [ ] Add the capacity and waitlist attribute to Course

### 6.5 binary search
- [ ] Create Recursive binary search for drop

**Lab 3/25! All work above must be done by 3/25**

### Unittests
  - [ ] LinkedQueue (FIFO order; dequeue on empty raises; size tracking)
  - [ ] Enrollment (enroll until capacity; extra students go on waitlist; drop triggers waitlist promotion)
  - [ ] Sorting tests (roster correctly sorted by id, name, and date for each algorithm implemented)
  - [ ] Binary search (find first/middle/last; not found returns -1; and/or behavior when roster not sorted by ID)

### Complexity Reflection
  - [ ] Give time complexity of deque and enqueue methods
  - [ ] Give time complexity for each sorting algorithm used
  - [ ] Give time complexity for the recursive binary search and explain why sorting is important for the functionality of the search
  - [ ] Compare the two sorting algorithms and explain why one might be preferred