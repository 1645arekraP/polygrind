"""import os
import sys
import django
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pg_site.settings")
django.setup()

from pg_app.utils.LeetcodeWrapper import LeetcodeWrapper
from pg_app.models import Question

def slugify(s:str):
    return s.lower().replace(" ", "-")

neetcode250 = [
    "Concatenation of Array",
    "Contains Duplicate",
    "Valid Anagram",
    "Two Sum",
    "Longest Common Prefix",
    "Group Anagrams",
    "Remove Element",
    "Majority Element",
    "Design HashSet",
    "Design HashMap",
    "Sort an Array",
    "Sort Colors",
    "Top K Frequent Elements",
    "Encode and Decode Strings",
    "Range Sum Query 2D Immutable",
    "Product of Array Except Self",
    "Valid Sudoku",
    "Longest Consecutive Sequence",
    "Best Time to Buy And Sell Stock II",
    "Majority Element II",
    "Subarray Sum Equals K",
    "First Missing Positive",
    "Reverse String",
    "Valid Palindrome",
    "Valid Palindrome II",
    "Merge Strings Alternately",
    "Merge Sorted Array",
    "Remove Duplicates From Sorted Array",
    "Two Sum II Input Array Is Sorted",
    "3Sum",
    "4Sum",
    "Rotate Array",
    "Container With Most Water",
    "Boats to Save People",
    "Trapping Rain Water",
    "Contains Duplicate II",
    "Best Time to Buy And Sell Stock",
    "Longest Substring Without Repeating Characters",
    "Longest Repeating Character Replacement",
    "Permutation In String",
    "Minimum Size Subarray Sum",
    "Find K Closest Elements",
    "Minimum Window Substring",
    "Sliding Window Maximum",
    "Baseball Game",
    "Valid Parentheses",
    "Implement Stack Using Queues",
    "Implement Queue using Stacks",
    "Min Stack",
    "Evaluate Reverse Polish Notation",
    "Generate Parentheses",
    "Asteroid Collision",
    "Daily Temperatures",
    "Online Stock Span",
    "Car Fleet",
    "Simplify Path",
    "Decode String",
    "Maximum Frequency Stack",
    "Largest Rectangle In Histogram",
    "Binary Search",
    "Search Insert Position",
    "Guess Number Higher Or Lower",
    "sqrtx",
    "Search a 2D Matrix",
    "Koko Eating Bananas",
    "capacity-to-ship-packages-within-d-days",
    "Find Minimum In Rotated Sorted Array",
    "Search In Rotated Sorted Array",
    "Search In Rotated Sorted Array II",
    "Time Based Key Value Store",
    "Split Array Largest Sum",
    "Median of Two Sorted Arrays",
    "Find in Mountain Array",
    "Reverse Linked List",
    "Merge Two Sorted Lists",
    "Linked List Cycle",
    "Reorder List",
    "Remove Nth Node From End of List",
    "Copy List With Random Pointer",
    "Add Two Numbers",
    "Find The Duplicate Number",
    "Reverse Linked List II",
    "Design Circular Queue",
    "LRU Cache",
    "LFU Cache",
    "Merge K Sorted Lists",
    "Reverse Nodes In K Group",
    "Binary Tree Inorder Traversal",
    "Binary Tree Preorder Traversal",
    "Binary Tree Postorder Traversal",
    "Invert Binary Tree",
    "Maximum Depth of Binary Tree",
    "Diameter of Binary Tree",
    "Balanced Binary Tree",
    "Same Tree",
    "Subtree of Another Tree",
    "Lowest Common Ancestor of a Binary Search Tree",
    "Insert into a Binary Search Tree",
    "Delete Node in a BST",
    "Binary Tree Level Order Traversal",
    "Binary Tree Right Side View",
    "Construct Quad Tree",
    "Count Good Nodes In Binary Tree",
    "Validate Binary Search Tree",
    "Kth Smallest Element In a Bst",
    "Construct Binary Tree From Preorder And Inorder Traversal",
    "House Robber III",
    "Delete Leaves With a Given Value",
    "Binary Tree Maximum Path Sum",
    "Serialize And Deserialize Binary Tree",
    "Kth Largest Element In a Stream",
    "Last Stone Weight",
    "K Closest Points to Origin",
    "Kth Largest Element In An Array",
    "Task Scheduler",
    "Design Twitter",
    "Single Threaded CPU",
    "Reorganize String",
    "Longest Happy String",
    "Car Pooling",
    "Find Median From Data Stream",
    "IPO",
    "sum-of-all-subset-xor-totals",
    "Subsets",
    "Combination Sum",
    "Combination Sum II",
    "Combinations",
    "Permutations",
    "Subsets II",
    "Permutations II",
    "Word Search",
    "Palindrome Partitioning",
    "Letter Combinations of a Phone Number",
    "Matchsticks to Square",
    "Partition to K Equal Sum Subsets",
    "N Queens",
    "N Queens II",
    "Word Break II",
    "Implement Trie Prefix Tree",
    "Design Add And Search Words Data Structure",
    "Extra Characters in a String",
    "Word Search II",
    "Island Perimeter",
    "Verifying An Alien Dictionary",
    "Find the Town Judge",
    "Number of Islands",
    "Max Area of Island",
    "Clone Graph",
    "Walls And Gates",
    "Rotting Oranges",
    "Pacific Atlantic Water Flow",
    "Surrounded Regions",
    "Open The Lock",
    "Course Schedule",
    "Course Schedule II",
    "Graph Valid Tree",
    "Course Schedule IV",
    "Number of Connected Components In An Undirected Graph",
    "Redundant Connection",
    "Accounts Merge",
    "Evaluate Division",
    "Minimum Height Trees",
    "Word Ladder",
    "Path with Minimum Effort",
    "Network Delay Time",
    "Reconstruct Itinerary",
    "Min Cost to Connect All Points",
    "Swim In Rising Water",
    "Alien Dictionary",
    "Cheapest Flights Within K Stops",
    "Find Critical and Pseudo Critical Edges in Minimum Spanning Tree",
    "Build a Matrix With Conditions",
    "Greatest Common Divisor Traversal",
    "Climbing Stairs",
    "Min Cost Climbing Stairs",
    "N-th Tribonacci Number",
    "House Robber",
    "House Robber II",
    "Longest Palindromic Substring",
    "Palindromic Substrings",
    "Decode Ways",
    "Coin Change",
    "Maximum Product Subarray",
    "Word Break",
    "Longest Increasing Subsequence",
    "Partition Equal Subset Sum",
    "Combination Sum IV",
    "Perfect Squares",
    "Integer Break",
    "Stone Game III",
    "Unique Paths",
    "Unique Paths II",
    "Minimum Path Sum",
    "Longest Common Subsequence",
    "Last Stone Weight II",
    "Best Time to Buy And Sell Stock With Cooldown",
    "Coin Change II",
    "Target Sum",
    "Interleaving String",
    "Stone Game",
    "Stone Game II",
    "Longest Increasing Path In a Matrix",
    "Distinct Subsequences",
    "Edit Distance",
    "Burst Balloons",
    "Regular Expression Matching",
    "Lemonade Change",
    "Maximum Subarray",
    "Maximum Sum Circular Subarray",
    "longest-turbulent-subarray",
    "Jump Game",
    "Jump Game II",
    "Jump Game VII",
    "Gas Station",
    "Hand of Straights",
    "Dota2 Senate",
    "Merge Triplets to Form Target Triplet",
    "Partition Labels",
    "Valid Parenthesis String",
    "Candy",
    "Insert Interval",
    "Merge Intervals",
    "Non Overlapping Intervals",
    "Meeting Rooms",
    "Meeting Rooms II",
    "Meeting Rooms III",
    "Minimum Interval to Include Each Query",
    "Excel Sheet Column Title",
    "Greatest Common Divisor of Strings",
    "Insert Greatest Common Divisors in Linked List",
    "Transpose Matrix",
    "Rotate Image",
    "Spiral Matrix",
    "set-matrix-zeroes",
    "Happy Number",
    "Plus One",
    "Roman to Integer",
    "powx-n",
    "Multiply Strings",
    "Detect Squares",
    "Single Number",
    "Number of 1 Bits",
    "Counting Bits",
    "Add Binary",
    "Reverse Bits",
    "Missing Number",
    "Sum of Two Integers",
    "Reverse Integer",
    "Bitwise AND of Numbers Range",
    "Minimum Array End"
]

neetcode150 = [
    "Contains Duplicate",
    "Valid Anagram",
    "Two Sum",
    "Group Anagrams",
    "Top K Frequent Elements",
    "Encode and Decode Strings",
    "Product of Array Except Self",
    "Valid Sudoku",
    "Longest Consecutive Sequence",
    "Valid Palindrome",
    "Two Sum II Input Array Is Sorted",
    "3Sum",
    "Container With Most Water",
    "Trapping Rain Water",
    "Best Time to Buy And Sell Stock",
    "Longest Substring Without Repeating Characters",
    "Longest Repeating Character Replacement",
    "Permutation In String",
    "Minimum Window Substring",
    "Sliding Window Maximum",
    "Valid Parentheses",
    "Min Stack",
    "Evaluate Reverse Polish Notation",
    "Generate Parentheses",
    "Daily Temperatures",
    "Car Fleet",
    "Largest Rectangle In Histogram",
    "Binary Search",
    "Search a 2D Matrix",
    "Koko Eating Bananas",
    "Find Minimum In Rotated Sorted Array",
    "Search In Rotated Sorted Array",
    "Time Based Key Value Store",
    "Median of Two Sorted Arrays",
    "Reverse Linked List",
    "Merge Two Sorted Lists",
    "Linked List Cycle",
    "Reorder List",
    "Remove Nth Node From End of List",
    "Copy List With Random Pointer",
    "Add Two Numbers",
    "Find The Duplicate Number",
    "LRU Cache",
    "Merge K Sorted Lists",
    "Reverse Nodes In K Group",
    "Invert Binary Tree",
    "Maximum Depth of Binary Tree",
    "Diameter of Binary Tree",
    "Balanced Binary Tree",
    "Same Tree",
    "Subtree of Another Tree",
    "Lowest Common Ancestor of a Binary Search Tree",
    "Binary Tree Level Order Traversal",
    "Binary Tree Right Side View",
    "Count Good Nodes In Binary Tree",
    "Validate Binary Search Tree",
    "Kth Smallest Element In a Bst",
    "Construct Binary Tree From Preorder And Inorder Traversal",
    "Binary Tree Maximum Path Sum",
    "Serialize And Deserialize Binary Tree",
    "Kth Largest Element In a Stream",
    "Last Stone Weight",
    "K Closest Points to Origin",
    "Kth Largest Element In An Array",
    "Task Scheduler",
    "Design Twitter",
    "Find Median From Data Stream",
    "Subsets",
    "Combination Sum",
    "Combination Sum II",
    "Permutations",
    "Subsets II",
    "Word Search",
    "Palindrome Partitioning",
    "Letter Combinations of a Phone Number",
    "N Queens",
    "Implement Trie Prefix Tree",
    "Design Add And Search Words Data Structure",
    "Word Search II",
    "Number of Islands",
    "Max Area of Island",
    "Clone Graph",
    "Walls And Gates",
    "Rotting Oranges",
    "Pacific Atlantic Water Flow",
    "Surrounded Regions",
    "Course Schedule",
    "Course Schedule II",
    "Graph Valid Tree",
    "Number of Connected Components In An Undirected Graph",
    "Redundant Connection",
    "Word Ladder",
    "Network Delay Time",
    "Reconstruct Itinerary",
    "Min Cost to Connect All Points",
    "Swim In Rising Water",
    "Alien Dictionary",
    "Cheapest Flights Within K Stops",
    "Climbing Stairs",
    "Min Cost Climbing Stairs",
    "House Robber",
    "House Robber II",
    "Longest Palindromic Substring",
    "Palindromic Substrings",
    "Decode Ways",
    "Coin Change",
    "Maximum Product Subarray",
    "Word Break",
    "Longest Increasing Subsequence",
    "Partition Equal Subset Sum",
    "Unique Paths",
    "Longest Common Subsequence",
    "Best Time to Buy And Sell Stock With Cooldown",
    "Coin Change II",
    "Target Sum",
    "Interleaving String",
    "Longest Increasing Path In a Matrix",
    "Distinct Subsequences",
    "Edit Distance",
    "Burst Balloons",
    "Regular Expression Matching",
    "Maximum Subarray",
    "Jump Game",
    "Jump Game II",
    "Gas Station",
    "Hand of Straights",
    "Merge Triplets to Form Target Triplet",
    "Partition Labels",
    "Valid Parenthesis String",
    "Insert Interval",
    "Merge Intervals",
    "Non Overlapping Intervals",
    "Meeting Rooms",
    "Meeting Rooms II",
    "Minimum Interval to Include Each Query",
    "Rotate Image",
    "Spiral Matrix",
    "set-matrix-zeroes",
    "Happy Number",
    "Plus One",
    "powx-n",
    "Multiply Strings",
    "Detect Squares",
    "Single Number",
    "Number of 1 Bits",
    "Counting Bits",
    "Reverse Bits",
    "Missing Number",
    "Sum of Two Integers",
    "Reverse Integer"
]

blind75 = [
    "Contains Duplicate",
    "Valid Anagram",
    "Two Sum",
    "Group Anagrams",
    "Top K Frequent Elements",
    "Encode and Decode Strings",
    "Product of Array Except Self",
    "Longest Consecutive Sequence",
    "Valid Palindrome",
    "3Sum",
    "Container With Most Water",
    "Best Time to Buy And Sell Stock",
    "Longest Substring Without Repeating Characters",
    "Longest Repeating Character Replacement",
    "Minimum Window Substring",
    "Valid Parentheses",
    "Find Minimum In Rotated Sorted Array",
    "Search In Rotated Sorted Array",
    "Reverse Linked List",
    "Merge Two Sorted Lists",
    "Linked List Cycle",
    "Reorder List",
    "Remove Nth Node From End of List",
    "Merge K Sorted Lists",
    "Invert Binary Tree",
    "Maximum Depth of Binary Tree",
    "Same Tree",
    "Subtree of Another Tree",
    "Lowest Common Ancestor of a Binary Search Tree",
    "Binary Tree Level Order Traversal",
    "Validate Binary Search Tree",
    "Kth Smallest Element In a Bst",
    "Construct Binary Tree From Preorder And Inorder Traversal",
    "Binary Tree Maximum Path Sum",
    "Serialize And Deserialize Binary Tree",
    "Find Median From Data Stream",
    "Combination Sum",
    "Word Search",
    "Implement Trie Prefix Tree",
    "Design Add And Search Words Data Structure",
    "Word Search II",
    "Number of Islands",
    "Clone Graph",
    "Pacific Atlantic Water Flow",
    "Course Schedule",
    "Graph Valid Tree",
    "Number of Connected Components In An Undirected Graph",
    "Alien Dictionary",
    "Climbing Stairs",
    "House Robber",
    "House Robber II",
    "Longest Palindromic Substring",
    "Palindromic Substrings",
    "Decode Ways",
    "Coin Change",
    "Maximum Product Subarray",
    "Word Break",
    "Longest Increasing Subsequence",
    "Unique Paths",
    "Longest Common Subsequence",
    "Maximum Subarray",
    "Jump Game",
    "Insert Interval",
    "Merge Intervals",
    "Non Overlapping Intervals",
    "Meeting Rooms",
    "Meeting Rooms II",
    "Rotate Image",
    "Spiral Matrix",
    "set-matrix-zeroes",
    "Number of 1 Bits",
    "Counting Bits",
    "Reverse Bits",
    "Missing Number",
    "Sum of Two Integers"
]

sb75 = []
for s in blind75:
    sb75.append(slugify(s))
nc150 = []
for s in neetcode150:
    nc150.append(slugify(s))
nc250 = []
for s in neetcode250:
    nc250.append(slugify(s))

print(sb75)
lcw = LeetcodeWrapper()
questions = lcw.getProblems(3416)
for i, q in enumerate(questions):
    question_pools = ['LC_ALL']
    if q.title_slug in sb75:
        question_pools.append("BLIND_75")
        #sb75.remove(q.title_slug)
    if q.title_slug in nc150:
        question_pools.append("NEETCODE_150")
        #nc150.remove(q.title_slug)
    if q.title_slug in nc250:
        question_pools.append("NEETCODE_250")
        #nc250.remove(q.title_slug)
    #q.pool_tag = question_pools
    try:
        Question.objects.create(
            ac_rate = q.ac_rate,
            content = q.content,
            difficulty = q.difficulty,
            is_paid = q.is_paid,
            link = q.link,
            title = q.title,
            title_slug = q.title_slug,
            topic_tags = q.topic_tags,
            pool_tag=question_pools
        )
        print(f"{i + 1}/{Question.objects.count()}")
    except Exception as e:
        print(e)
print(sb75)
print("-"*64)
print(nc150)
print("-"*64)
print(nc250)
print("-"*64)"""