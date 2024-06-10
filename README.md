# Queue - Python Implementation

This project consists of a simple queue implementation in Python. A queue is a data structure that follows the "First In, First Out" (FIFO) principle, where the first element added is the first one to be removed.

## Features

- **Push:** Adds an item to the end of the queue.
- **Pop:** Removes the first item from the queue, if any.
- **Top:** Returns the first item in the queue without removing it.
- **Empty:** Checks if the queue is empty.

## How to Use

1. Instantiate an object of the `Queue` class.
2. Add elements to the queue using the `push(item)` method.
3. Remove elements from the queue using the `pop()` method.
4. Peek at the first element of the queue without removing it using the `top()` method.
5. Check if the queue is empty using the `empty()` method.

## Usage Example

```python
queue = Queue()

for i in range(100+1):
    queue.push(i)
    print(f"List: {queue.list}\n")
    t.sleep(0.2)

print(f"Filled list: {queue.list}\n")
print("Please wait...\n")
t.sleep(3)

while not queue.empty():
    queue_first_item = queue.top()
    queue.pop()
    print(f"Item successfully removed from the list: {queue_first_item}\n")
    print(f"List: {queue.list}\n")
    t.sleep(0.2)
```
This example demonstrates how to fill a queue with numbers from 0 to 100, print the queue, wait for a few seconds, and then remove each element from the queue while printing the resulting queue.

## Installation Requirements

- Python 3.x

## Author

This code was developed by Ageu Felipe Nunes Moraes (myself) as part of a personal project dedicated to strengthening and maturing coding skills. For any questions or suggestions, please contact me at [ageumoraes67@gmail.com](mailto:ageumoraes67@gmail.com).

## Disclaimer

This is a software project developed by an individual and is not affiliated with any other entity.
