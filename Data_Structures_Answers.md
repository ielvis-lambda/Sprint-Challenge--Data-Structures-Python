Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?
    N/A

2. What is the space complexity of your `depth_first_for_each` function?
    N/A

3. What is the runtime complexity of your `breadth_first_for_each` method?
The runtime complexity of my `breadth_first_for_each` method is O(n) since we have to visit each node once the time it takes our code to run will depend on the number of nodes (n). 

4. What is the space complexity of your `breadth_first_for_each` method?
Similarly the space complexity of our code is also O(n) since we will need as much memory for our queue as there are nodes in the tree, so the limiting factor is the number of nodes(n). 

5. What is the runtime complexity of the provided code in `names.py`?
Since there is a nested for-loop in the original `names.py` the runtime complexity will be O(n^2). The code will need to loop through both lists. Since the lists are the same size n^2 is appropriate.

6. What is the space complexity of the provided code in `names.py`?
The space complexity is probably O(n) since the memory required to run this algorithm should grow in proportion to the number of inputs. 

7. What is the runtime complexity of your optimized code in `names.py`?
The runtime of my optimized code is O(n). I'm still searching through every element in list 2 but not through both lists like the unoptimized code was. 

8. What is the space complexity of your optimized code in `names.py`?
The space complexity of this is probably also O(n) as the memory requires should grow linearly with the inputs entered. 