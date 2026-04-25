# Week 7 Homework: Moonlight Festival Control Booth

## Summary

This homework uses Python’s `heapq` module to manage festival alerts based on priority. Instead of processing alerts in arrival order, the system processes the most urgent alerts first. I implemented functions to order all alerts, handle ties stably, return the top k alerts, and peek at the next alert without modifying the original data.

---

## Approach

### `order_festival_alerts`

I used a min-heap where each item is a tuple `(priority, title)`.
Since Python’s heap is a min-heap, smaller priority numbers come out first.
I pushed all alerts into the heap and repeatedly popped from it to build the result list in correct order.

---

### `order_festival_alerts_stable`

To handle ties, I added the index of each alert: `(priority, index, title)`.
This ensures that if two alerts have the same priority, the one that appeared earlier is processed first.
Input order matters because the problem requires stable ordering for equal priorities.

---

### `top_k_festival_alerts`

I built a heap using `(priority, index, title)` and then popped only `k` elements.
I used `min(k, len(alerts))` to safely handle cases where `k` is larger than the number of alerts.
If `k <= 0`, I returned an empty list.

---

### `peek_next_festival_alert`

I created a heap from the input but did not remove any elements.
I simply returned the top element of the heap (`heap[0]`).
This ensures the original input list is not modified.

---

## Complexity

### `order_festival_alerts`

* **Time:** O(n log n)
* **Space:** O(n)
* **Why:** Inserting n items into the heap and removing n items both take O(log n) per operation.

---

### `order_festival_alerts_stable`

* **Time:** O(n log n)
* **Space:** O(n)
* **Why:** Same as above, with a slightly larger tuple but same complexity.

---

### `top_k_festival_alerts`

* **Time:** O(n log n)
* **Space:** O(n)
* **Why:** Building the heap takes O(n log n), and extracting k elements takes O(k log n).

---

### `peek_next_festival_alert`

* **Time:** O(n log n)
* **Space:** O(n)
* **Why:** Building the heap takes O(n log n), and peeking is O(1).

---

## Edge-case checklist

### `order_festival_alerts`

* [x] empty input
* [x] one alert
* [x] multiple different priorities

### `order_festival_alerts_stable`

* [x] same-priority tie
* [x] all same priority
* [x] empty input

### `top_k_festival_alerts`

* [x] `k = 0`
* [x] `k > len(alerts)`
* [x] duplicate priorities
* [x] empty input

### `peek_next_festival_alert`

* [x] empty input
* [x] normal case

---

## Test notes

* All required edge cases were tested using pytest
* Tests confirm correct ordering and stability
* All tests passed successfully (`16 passed`)

---

## Assistance & Sources

### AI used?

* [x] Yes

If yes, what did it help with?

* Helped understand heap usage and debugging errors
* Assisted in verifying correctness of implementation

### Other sources

* Python documentation for `heapq`
* Class notes and lecture examples

---

## Reflection

What was hardest?

* Understanding how to handle stable ordering using index
* Fixing GitHub push and repository issues

What do you understand better now?

* How heaps work and why they are useful for priority queues
* How to manage edge cases and test code properly
* How to use Git and GitHub for submission
