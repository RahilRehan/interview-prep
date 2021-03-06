# TODO list

### general
- python exception handling
- python testing
- python oops programming
- implement comparision on python user defined types => __lt__
- properties in python classes
ex: 
```python
# example from closest star problem in heaps section, this is representation of a star
class Star:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z

    @property
    def distance(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __lt__(self, rhs: 'Star') -> bool:
        return self.distance < rhs.distance

    def __repr__(self):
        return str(self.distance)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, rhs):
        return math.isclose(self.distance, rhs.distance)
```
- explore namedtuples

- variant problems after each questoin in epi

### revision
- linked list problems
- stack and queue problems

### primitives
- learn more about xor
- masks in python
- clear and set lowermost bits
- signedness in integers and bits
- shifting
- caching bits for faster processing
- commutativity and associativity  for parallel and reorder operations
- remove lowest set bit => x&(x-1)
- get lowest set bit => x & ~ (x-1)
- create a alternating flag in each iteration=> x^=1
- todo: precomputation(using cache) problems. 0.1 and 0.3

### stack problems
- expression evaluation problems, rpn, polish
- 7.4 dir path normalization, didnt understand well

### tree problems
- iscomplete bt, isfull bt, isperfect bt
- tree orders without recursion
- morris traversal for inorder and preorder
- euler path
- postorder (a lil trickier) - https://www.techiedelight.com/postorder-tree-traversal-iterative-recursive/

### searching 
- partition algorithm (look at 11.7 problem - searching)
- 11.9 find missing ip address

### bit manipulation
- learn about bases and conversions
- conversion between bits, kb, bytes, mb, gb etc

### hash tables
- ordereddict and lru cache problem
- smallest subarray covering keywords in order (12.7)
