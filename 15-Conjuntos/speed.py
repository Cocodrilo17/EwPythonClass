# Speed Comparison, sets and lists
from timeit import timeit

my_list = list(range(1_000_000))
my_set = set(range(1_000_000))

list_time = timeit("999999 in my_list", globals=globals(), number=1000)
set_time = timeit("999999 in my_set", globals=globals(), number=1000)

print(f"List: {list_time:.6f}")
print(f"Set: {set_time:.6f}")
