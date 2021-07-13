from typing import Dict
# TUPLES
# SETS
# DICTIONARIES
# SEQUENCES Looping
# len: use with any collection to get num of elements

# TUPLES
# Tuples can be nested, tuples are immutable (unchangeable), but they can contain mutable objects
# Tuple is defined by commas
def tuples_examples():
    t1 = (1, 2, 3, 4)
    t2 = 5, 6, "six"
    t2[2]  # "six"
    t3 = ([1, 2], [3, 4])
    t4 = t2 + t3  # (5, 6, 'six', [1, 2], [3, 4])
    print(t4)
    print(t4.__getitem__(3))  # [1, 2]
    print(t4.index("six")) # 2
tuples_examples()


# SETS
# A set is an unordered, unindexed collection of unique elements. Defined by { }
# Items cannot be changed (but can be removed), new items can be added
def sets():
    s = set()  # create an empty set
    s = {"apple", "banana", "mango"}
    s2 = {"apple", "pepper", "tomato"}
    s.add("kiwi")  # added at random position
    s.remove("banana")
    s.update(s2)  # Add elements from s2 to set s
    s3 = s.union(s2)  # Unite sets, duplicated elements appear only once
    print(s3)
sets()


# DICTIONARIES
# Key : value pairs, a tuple can be used as a key
# list method returns a list of all keys from a dictionary
# Dictionaries can be nested
di = {
    "one" : 1, 
    "two" : 2, 
    "three" : 3, 
    "four" : 4
}
dines = {
    "group1" : { 
        "a" : "1",
        "b" : "2"
    },
    "group2" : di
}
#dicon = dict([(1 , "a"), (2, "b")])  # {1: 'a', 2: 'b'}
#dicon2 = dict(one=1, two=2)  # {'one': 1, 'two': 2}, does not work when key is a number

# Merge dictionaries
def merge_dicts():
    my_first_dict = {"A": 1, "B": 2}
    my_second_dict = {"C": 3, "D": 4}
    my_merged_dict = {**my_first_dict, **my_second_dict}
    print(my_merged_dict)  #{'A': 1, 'B': 2, 'C': 3, 'D': 4}

# Dictionary comprehension
# dicomprehension = {x: x + "wow" for x in ("a", "b", "c")}  # {'a': 'awow', 'b': 'bwow', 'c': 'cwow'}

def work_dict(dict:Dict):
    print("work_dict")
    dict["drei"] = 3  # + New item, there can be duplicate values
    del dict["drei"]

    dict2 = dict.copy()  # copy of the dictionary
    val = dict.get("two") # 2 (get value by key)

    dict.pop("one")  # Delete an item by key (.popitem - delete by value)
    # del dict  # delete the dict, di.clear() to clear the dict
work_dict(di)

#list(di)  # returns a list of all key values
def print_dict():
    print("print_dict")
    for k,v in di.items(): # loop through keys and values
        print(k, v)
    for v in di.values():  # can also loop through di.keys
        print(v)
print_dict()


# SEQUENCES Looping
# Iterate over many sequences using ZIP method (creates list of tuples)
list1 = [1, 2, 3, 4]
list2 = [5, 6]
list3 = [7, 8]
ziplist = list(zip(list1, list2, list3))  # [(1, 5, 7), (2, 6, 8)], ziplist[0][1] is 5
for i in zip(list1, list2, list3):
    print(i)

# To loop over a sequence in sorted order, use the sorted()
t1 = (10, 2, 30, 4)
t2 = sorted(t1)  # returns a list [2, 4, 10, 30]

relist = []
for i in reversed(range(1, 10, 2)):  # set from 1 to 10 with step 2
    relist.append(i)
print(relist)  # [9, 7, 5, 3, 1]
