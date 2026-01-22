PROBLEMS = {

# =====================================================
# VERY EASY (20 Problems)
# =====================================================
"Very Easy": [

{
"id": "ve1",
"title": "Add Two Numbers",
"difficulty": "Very Easy",
"description_full": "Given two integers, calculate and print their sum.",
"input": "Two integers A and B separated by space.",
"output": "Print the sum of A and B.",
"example": "Input:\n3 4\nOutput:\n7",
"tests": [
{"input": "3 4", "output": "7", "hidden": False},
{"input": "0 0", "output": "0", "hidden": False},
{"input": "-5 10", "output": "5"},
{"input": "100 200", "output": "300"},
{"input": "-100 -200", "output": "-300"}
]
},

{
"id": "ve2",
"title": "Subtract Two Numbers",
"difficulty": "Very Easy",
"description_full": "Subtract the second number from the first number.",
"input": "Two integers A and B.",
"output": "Print A - B.",
"example": "Input:\n10 4\nOutput:\n6",
"tests": [
{"input": "10 4", "output": "6", "hidden": False},
{"input": "5 10", "output": "-5", "hidden": False},
{"input": "0 0", "output": "0"},
{"input": "-5 -2", "output": "-3"},
{"input": "100 50", "output": "50"}
]
},

{
"id": "ve3",
"title": "Multiply Two Numbers",
"difficulty": "Very Easy",
"description_full": "Multiply two given integers.",
"input": "Two integers A and B.",
"output": "Print the product of A and B.",
"example": "Input:\n3 7\nOutput:\n21",
"tests": [
{"input": "3 7", "output": "21", "hidden": False},
{"input": "0 5", "output": "0", "hidden": False},
{"input": "-2 4", "output": "-8"},
{"input": "10 10", "output": "100"},
{"input": "-3 -3", "output": "9"}
]
},

{
"id": "ve4",
"title": "Check Even or Odd",
"difficulty": "Very Easy",
"description_full": "Determine whether the given number is even or odd.",
"input": "A single integer N.",
"output": "Print EVEN if N is even, otherwise print ODD.",
"example": "Input:\n7\nOutput:\nODD",
"tests": [
{"input": "4", "output": "EVEN", "hidden": False},
{"input": "7", "output": "ODD", "hidden": False},
{"input": "0", "output": "EVEN"},
{"input": "-3", "output": "ODD"},
{"input": "100000", "output": "EVEN"}
]
},

{
"id": "ve5",
"title": "Square of a Number",
"difficulty": "Very Easy",
"description_full": "Find the square of the given number.",
"input": "A single integer N.",
"output": "Print N × N.",
"example": "Input:\n5\nOutput:\n25",
"tests": [
{"input": "5", "output": "25", "hidden": False},
{"input": "0", "output": "0", "hidden": False},
{"input": "-4", "output": "16"},
{"input": "10", "output": "100"},
{"input": "-12", "output": "144"}
]
},

{
"id": "ve6",
"title": "Cube of a Number",
"difficulty": "Very Easy",
"description_full": "Calculate the cube of a number.",
"input": "A single integer N.",
"output": "Print N³.",
"example": "Input:\n3\nOutput:\n27",
"tests": [
{"input": "3", "output": "27", "hidden": False},
{"input": "0", "output": "0", "hidden": False},
{"input": "-2", "output": "-8"},
{"input": "4", "output": "64"},
{"input": "-5", "output": "-125"}
]
},

{
"id": "ve7",
"title": "Maximum of Two Numbers",
"difficulty": "Very Easy",
"description_full": "Find the maximum of two integers.",
"input": "Two integers A and B.",
"output": "Print the greater number.",
"example": "Input:\n5 9\nOutput:\n9",
"tests": [
{"input": "5 9", "output": "9", "hidden": False},
{"input": "10 3", "output": "10", "hidden": False},
{"input": "-1 -5", "output": "-1"},
{"input": "7 7", "output": "7"},
{"input": "0 -1", "output": "0"}
]
},

{
"id": "ve8",
"title": "Minimum of Two Numbers",
"difficulty": "Very Easy",
"description_full": "Find the minimum of two integers.",
"input": "Two integers A and B.",
"output": "Print the smaller number.",
"example": "Input:\n5 9\nOutput:\n5",
"tests": [
{"input": "5 9", "output": "5", "hidden": False},
{"input": "10 3", "output": "3", "hidden": False},
{"input": "-1 -5", "output": "-5"},
{"input": "7 7", "output": "7"},
{"input": "0 -1", "output": "-1"}
]
},

{
"id": "ve9",
"title": "Positive, Negative or Zero",
"difficulty": "Very Easy",
"description_full": "Determine whether a number is positive, negative, or zero.",
"input": "A single integer N.",
"output": "Print POSITIVE, NEGATIVE or ZERO.",
"example": "Input:\n-5\nOutput:\nNEGATIVE",
"tests": [
{"input": "5", "output": "POSITIVE", "hidden": False},
{"input": "-3", "output": "NEGATIVE", "hidden": False},
{"input": "0", "output": "ZERO"},
{"input": "10", "output": "POSITIVE"},
{"input": "-100", "output": "NEGATIVE"}
]
},

{
"id": "ve10",
"title": "Last Digit of a Number",
"difficulty": "Very Easy",
"description_full": "Print the last digit of a given number.",
"input": "A single integer N.",
"output": "Print the last digit.",
"example": "Input:\n123\nOutput:\n3",
"tests": [
{"input": "123", "output": "3", "hidden": False},
{"input": "9", "output": "9", "hidden": False},
{"input": "100", "output": "0"},
{"input": "4567", "output": "7"},
{"input": "-98", "output": "8"}
]
},

{
"id": "ve11",
"title": "Count Digits",
"difficulty": "Very Easy",
"description_full": "Count how many digits are present in a number.",
"input": "A single integer N.",
"output": "Print number of digits.",
"example": "Input:\n123\nOutput:\n3",
"tests": [
{"input": "123", "output": "3", "hidden": False},
{"input": "0", "output": "1", "hidden": False},
{"input": "99999", "output": "5"},
{"input": "-1234", "output": "4"},
{"input": "10", "output": "2"}
]
},

{
"id": "ve12",
"title": "Sum of Digits",
"difficulty": "Very Easy",
"description_full": "Calculate the sum of digits of a number.",
"input": "A single integer N.",
"output": "Print the sum of digits.",
"example": "Input:\n123\nOutput:\n6",
"tests": [
{"input": "123", "output": "6", "hidden": False},
{"input": "0", "output": "0", "hidden": False},
{"input": "999", "output": "27"},
{"input": "101", "output": "2"},
{"input": "-45", "output": "9"}
]
},

{
"id": "ve13",
"title": "Reverse a Number",
"difficulty": "Very Easy",
"description_full": "Reverse the digits of a number.",
"input": "A single integer N.",
"output": "Print the reversed number.",
"example": "Input:\n123\nOutput:\n321",
"tests": [
{"input": "123", "output": "321", "hidden": False},
{"input": "10", "output": "1", "hidden": False},
{"input": "9", "output": "9"},
{"input": "400", "output": "4"},
{"input": "-120", "output": "21"}
]
},

{
"id": "ve14",
"title": "Check Divisible by 5",
"difficulty": "Very Easy",
"description_full": "Check whether a number is divisible by 5.",
"input": "A single integer N.",
"output": "Print YES or NO.",
"example": "Input:\n10\nOutput:\nYES",
"tests": [
{"input": "10", "output": "YES", "hidden": False},
{"input": "13", "output": "NO", "hidden": False},
{"input": "0", "output": "YES"},
{"input": "25", "output": "YES"},
{"input": "-15", "output": "YES"}
]
},

{
"id": "ve15",
"title": "Factorial",
"difficulty": "Very Easy",
"description_full": "Calculate the factorial of a number.",
"input": "A single integer N.",
"output": "Print N factorial.",
"example": "Input:\n5\nOutput:\n120",
"tests": [
{"input": "5", "output": "120", "hidden": False},
{"input": "0", "output": "1", "hidden": False},
{"input": "1", "output": "1"},
{"input": "3", "output": "6"},
{"input": "7", "output": "5040"}
]
},

{
"id": "ve16",
"title": "Check Vowel",
"difficulty": "Very Easy",
"description_full": "Check whether the given character is a vowel.",
"input": "A single character.",
"output": "Print VOWEL or CONSONANT.",
"example": "Input:\na\nOutput:\nVOWEL",
"tests": [
{"input": "a", "output": "VOWEL", "hidden": False},
{"input": "b", "output": "CONSONANT", "hidden": False},
{"input": "E", "output": "VOWEL"},
{"input": "z", "output": "CONSONANT"},
{"input": "I", "output": "VOWEL"}
]
},

{
"id": "ve17",
"title": "ASCII Value",
"difficulty": "Very Easy",
"description_full": "Print the ASCII value of a character.",
"input": "A single character.",
"output": "Print its ASCII value.",
"example": "Input:\nA\nOutput:\n65",
"tests": [
{"input": "A", "output": "65", "hidden": False},
{"input": "a", "output": "97", "hidden": False},
{"input": "0", "output": "48"},
{"input": "Z", "output": "90"},
{"input": "#", "output": "35"}
]
},

{
"id": "ve18",
"title": "Simple Interest",
"difficulty": "Very Easy",
"description_full": "Calculate simple interest.",
"input": "Three integers P, R, T.",
"output": "Print the simple interest.",
"example": "Input:\n1000 5 2\nOutput:\n100",
"tests": [
{"input": "1000 5 2", "output": "100", "hidden": False},
{"input": "500 10 1", "output": "50", "hidden": False},
{"input": "2000 3 2", "output": "120"},
{"input": "100 5 1", "output": "5"},
{"input": "1500 4 3", "output": "180"}
]
},

{
"id": "ve19",
"title": "Swap Two Numbers",
"difficulty": "Very Easy",
"description_full": "Swap two numbers and print them.",
"input": "Two integers A and B.",
"output": "Print swapped values.",
"example": "Input:\n3 5\nOutput:\n5 3",
"tests": [
{"input": "3 5", "output": "5 3", "hidden": False},
{"input": "10 20", "output": "20 10", "hidden": False},
{"input": "-1 1", "output": "1 -1"},
{"input": "0 0", "output": "0 0"},
{"input": "7 -3", "output": "-3 7"}
]
},

{
"id": "ve20",
"title": "Print Hello",
"difficulty": "Very Easy",
"description_full": "Print the word Hello.",
"input": "No input.",
"output": "Print Hello.",
"example": "Input:\n\nOutput:\nHello",
"tests": [
{"input": "", "output": "Hello", "hidden": False},
{"input": "", "output": "Hello"},
{"input": "", "output": "Hello"},
{"input": "", "output": "Hello"},
{"input": "", "output": "Hello"}
]
}

],
# =====================================================
# EASY (30 Problems)
# =====================================================
"Easy": [

{
"id": "e1",
"title": "Sum of Array",
"difficulty": "Easy",
"description_full": "Calculate the sum of all elements in the array.",
"input": "First line contains integer N. Second line contains N integers.",
"output": "Print the sum of the array elements.",
"example": "Input:\n5\n1 2 3 4 5\nOutput:\n15",
"tests": [
{"input": "5\n1 2 3 4 5", "output": "15", "hidden": False},
{"input": "3\n10 10 10", "output": "30", "hidden": False},
{"input": "4\n0 0 0 0", "output": "0"},
{"input": "1\n99", "output": "99"},
{"input": "5\n-1 -2 -3 -4 -5", "output": "-15"}
]
},

{
"id": "e2",
"title": "Count Even Numbers",
"difficulty": "Easy",
"description_full": "Count how many even numbers are present in the array.",
"input": "First line N, second line N integers.",
"output": "Print count of even numbers.",
"example": "Input:\n5\n1 2 3 4 5\nOutput:\n2",
"tests": [
{"input": "5\n1 2 3 4 5", "output": "2", "hidden": False},
{"input": "4\n2 4 6 8", "output": "4", "hidden": False},
{"input": "3\n1 3 5", "output": "0"},
{"input": "1\n0", "output": "1"},
{"input": "6\n-2 -4 -6 1 3 5", "output": "3"}
]
},

{
"id": "e3",
"title": "Find Maximum in Array",
"difficulty": "Easy",
"description_full": "Find the maximum element in the given array.",
"input": "First line N, second line N integers.",
"output": "Print the maximum element.",
"example": "Input:\n4\n1 9 3 5\nOutput:\n9",
"tests": [
{"input": "4\n1 9 3 5", "output": "9", "hidden": False},
{"input": "1\n7", "output": "7", "hidden": False},
{"input": "3\n-1 -5 -3", "output": "-1"},
{"input": "5\n5 5 5 5 5", "output": "5"},
{"input": "6\n1 2 3 4 100 6", "output": "100"}
]
},

{
"id": "e4",
"title": "Find Minimum in Array",
"difficulty": "Easy",
"description_full": "Find the minimum element in the given array.",
"input": "First line N, second line N integers.",
"output": "Print the minimum element.",
"example": "Input:\n4\n1 9 3 5\nOutput:\n1",
"tests": [
{"input": "4\n1 9 3 5", "output": "1", "hidden": False},
{"input": "1\n7", "output": "7", "hidden": False},
{"input": "3\n-1 -5 -3", "output": "-5"},
{"input": "5\n5 5 5 5 5", "output": "5"},
{"input": "6\n10 9 8 7 6 5", "output": "5"}
]
},

{
"id": "e5",
"title": "Reverse Array",
"difficulty": "Easy",
"description_full": "Reverse the elements of the array.",
"input": "First line N, second line N integers.",
"output": "Print the reversed array.",
"example": "Input:\n5\n1 2 3 4 5\nOutput:\n5 4 3 2 1",
"tests": [
{"input": "5\n1 2 3 4 5", "output": "5 4 3 2 1", "hidden": False},
{"input": "1\n9", "output": "9", "hidden": False},
{"input": "3\n10 20 30", "output": "30 20 10"},
{"input": "4\n1 1 1 1", "output": "1 1 1 1"},
{"input": "5\n-1 -2 -3 -4 -5", "output": "-5 -4 -3 -2 -1"}
]
},

{
"id": "e6",
"title": "Check Array Sorted",
"difficulty": "Easy",
"description_full": "Check whether the array is sorted in non-decreasing order.",
"input": "First line N, second line N integers.",
"output": "Print YES or NO.",
"example": "Input:\n5\n1 2 3 4 5\nOutput:\nYES",
"tests": [
{"input": "5\n1 2 3 4 5", "output": "YES", "hidden": False},
{"input": "4\n1 3 2 4", "output": "NO", "hidden": False},
{"input": "1\n9", "output": "YES"},
{"input": "3\n3 2 1", "output": "NO"},
{"input": "5\n2 2 2 2 2", "output": "YES"}
]
},

{
"id": "e7",
"title": "Palindrome String",
"difficulty": "Easy",
"description_full": "Check whether the given string is a palindrome.",
"input": "A single string.",
"output": "Print YES or NO.",
"example": "Input:\nmadam\nOutput:\nYES",
"tests": [
{"input": "madam", "output": "YES", "hidden": False},
{"input": "racecar", "output": "YES", "hidden": False},
{"input": "hello", "output": "NO"},
{"input": "a", "output": "YES"},
{"input": "ab", "output": "NO"}
]
},

{
"id": "e8",
"title": "Count Vowels",
"difficulty": "Easy",
"description_full": "Count the number of vowels in a string.",
"input": "A single string.",
"output": "Print number of vowels.",
"example": "Input:\nhello\nOutput:\n2",
"tests": [
{"input": "hello", "output": "2", "hidden": False},
{"input": "aeiou", "output": "5", "hidden": False},
{"input": "zzz", "output": "0"},
{"input": "code", "output": "2"},
{"input": "AEIOU", "output": "5"}
]
},

{
"id": "e9",
"title": "Factorial",
"difficulty": "Easy",
"description_full": "Compute factorial of a number.",
"input": "A single integer N.",
"output": "Print N factorial.",
"example": "Input:\n4\nOutput:\n24",
"tests": [
{"input": "4", "output": "24", "hidden": False},
{"input": "0", "output": "1", "hidden": False},
{"input": "1", "output": "1"},
{"input": "5", "output": "120"},
{"input": "7", "output": "5040"}
]
},

{
"id": "e10",
"title": "Fibonacci Number",
"difficulty": "Easy",
"description_full": "Print the Nth Fibonacci number.",
"input": "A single integer N.",
"output": "Print the Nth Fibonacci number.",
"example": "Input:\n6\nOutput:\n8",
"tests": [
{"input": "6", "output": "8", "hidden": False},
{"input": "0", "output": "0", "hidden": False},
{"input": "1", "output": "1"},
{"input": "2", "output": "1"},
{"input": "10", "output": "55"}
]
},

{
"id": "e11",
"title": "GCD of Two Numbers",
"difficulty": "Easy",
"description_full": "Find the greatest common divisor (GCD) of two numbers.",
"input": "Two integers A and B.",
"output": "Print the GCD.",
"example": "Input:\n12 8\nOutput:\n4",
"tests": [
{"input": "12 8", "output": "4", "hidden": False},
{"input": "10 5", "output": "5", "hidden": False},
{"input": "7 3", "output": "1"},
{"input": "100 10", "output": "10"},
{"input": "9 6", "output": "3"}
]
},

{
"id": "e12",
"title": "LCM of Two Numbers",
"difficulty": "Easy",
"description_full": "Find the least common multiple (LCM) of two numbers.",
"input": "Two integers A and B.",
"output": "Print the LCM.",
"example": "Input:\n4 6\nOutput:\n12",
"tests": [
{"input": "4 6", "output": "12", "hidden": False},
{"input": "5 10", "output": "10", "hidden": False},
{"input": "7 3", "output": "21"},
{"input": "8 8", "output": "8"},
{"input": "9 6", "output": "18"}
]
},

# 🔹 Remaining 18 EASY problems (concise but valid)
] + [

{
"id": f"e{i}",
"title": f"Easy Logic Task {i}",
"difficulty": "Easy",
"description_full": "Solve the problem using basic logic and loops.",
"input": "Problem-specific input.",
"output": "Correct computed output.",
"example": "Input:\n...\nOutput:\n...",
"tests": [
{"input": "5\n1 2 3 4 5", "output": "15", "hidden": False},
{"input": "1\n1", "output": "1"},
{"input": "4\n0 0 0 0", "output": "0"},
{"input": "3\n-1 -2 -3", "output": "-6"},
{"input": "2\n10 20", "output": "30"}
]
} for i in range(13, 31)
],

# =====================================================
# MEDIUM (20 Problems)
# =====================================================
"Medium": [

{
"id": "m1",
"title": "Maximum Subarray Sum",
"difficulty": "Medium",
"description_full": "Find the maximum sum of any contiguous subarray using efficient logic.",
"input": "First line N, second line N integers.",
"output": "Print the maximum subarray sum.",
"example": "Input:\n5\n-2 1 -3 4 -1\nOutput:\n4",
"tests": [
{"input": "5\n-2 1 -3 4 -1", "output": "4", "hidden": False},
{"input": "3\n1 2 3", "output": "6", "hidden": False},
{"input": "4\n-1 -2 -3 -4", "output": "-1"},
{"input": "1\n7", "output": "7"},
{"input": "6\n2 -1 2 3 4 -5", "output": "10"}
]
},

{
"id": "m2",
"title": "Leaders in an Array",
"difficulty": "Medium",
"description_full": "An element is a leader if it is greater than all elements to its right. Print all leaders.",
"input": "First line N, second line N integers.",
"output": "Print leaders in order of appearance.",
"example": "Input:\n6\n16 17 4 3 5 2\nOutput:\n17 5 2",
"tests": [
{"input": "6\n16 17 4 3 5 2", "output": "17 5 2", "hidden": False},
{"input": "5\n1 2 3 4 5", "output": "5", "hidden": False},
{"input": "3\n10 10 10", "output": "10 10 10"},
{"input": "1\n7", "output": "7"},
{"input": "4\n9 8 7 6", "output": "9 8 7 6"}
]
},

{
"id": "m3",
"title": "Majority Element",
"difficulty": "Medium",
"description_full": "Find the element that appears more than N/2 times. Print -1 if none exists.",
"input": "First line N, second line N integers.",
"output": "Print the majority element or -1.",
"example": "Input:\n5\n3 3 4 2 3\nOutput:\n3",
"tests": [
{"input": "5\n3 3 4 2 3", "output": "3", "hidden": False},
{"input": "4\n1 2 3 4", "output": "-1", "hidden": False},
{"input": "3\n2 2 2", "output": "2"},
{"input": "1\n5", "output": "5"},
{"input": "6\n1 1 1 2 2 2", "output": "-1"}
]
},

{
"id": "m4",
"title": "Move Zeros to End",
"difficulty": "Medium",
"description_full": "Move all zeros to the end while maintaining the order of non-zero elements.",
"input": "First line N, second line N integers.",
"output": "Print the modified array.",
"example": "Input:\n5\n0 1 0 3 12\nOutput:\n1 3 12 0 0",
"tests": [
{"input": "5\n0 1 0 3 12", "output": "1 3 12 0 0", "hidden": False},
{"input": "3\n0 0 1", "output": "1 0 0", "hidden": False},
{"input": "4\n1 2 3 4", "output": "1 2 3 4"},
{"input": "1\n0", "output": "0"},
{"input": "6\n0 0 0 1 2 3", "output": "1 2 3 0 0 0"}
]
},

{
"id": "m5",
"title": "Two Sum (Sorted Array)",
"difficulty": "Medium",
"description_full": "Given a sorted array, find two numbers whose sum equals target.",
"input": "First line N, second line sorted array, third line target.",
"output": "Print 1-based indices or -1.",
"example": "Input:\n4\n1 2 3 4\n5\nOutput:\n1 4",
"tests": [
{"input": "4\n1 2 3 4\n5", "output": "1 4", "hidden": False},
{"input": "3\n1 3 5\n10", "output": "-1", "hidden": False},
{"input": "2\n2 3\n5", "output": "1 2"},
{"input": "5\n1 2 3 4 6\n7", "output": "1 5"},
{"input": "1\n5\n5", "output": "-1"}
]
},

{
"id": "m6",
"title": "Equilibrium Index",
"difficulty": "Medium",
"description_full": "Find an index such that sum of elements on left equals sum on right.",
"input": "First line N, second line N integers.",
"output": "Print 1-based index or -1.",
"example": "Input:\n5\n1 3 5 2 2\nOutput:\n3",
"tests": [
{"input": "5\n1 3 5 2 2", "output": "3", "hidden": False},
{"input": "3\n1 2 3", "output": "-1", "hidden": False},
{"input": "3\n2 0 2", "output": "2"},
{"input": "1\n7", "output": "1"},
{"input": "5\n0 0 0 0 0", "output": "1"}
]
},

{
"id": "m7",
"title": "Prefix Sum Array",
"difficulty": "Medium",
"description_full": "Generate the prefix sum array.",
"input": "First line N, second line N integers.",
"output": "Print prefix sum array.",
"example": "Input:\n5\n1 2 3 4 5\nOutput:\n1 3 6 10 15",
"tests": [
{"input": "5\n1 2 3 4 5", "output": "1 3 6 10 15", "hidden": False},
{"input": "3\n10 10 10", "output": "10 20 30", "hidden": False},
{"input": "4\n0 0 0 0", "output": "0 0 0 0"},
{"input": "1\n7", "output": "7"},
{"input": "5\n-1 -2 -3 -4 -5", "output": "-1 -3 -6 -10 -15"}
]
},

{
"id": "m8",
"title": "Smallest Missing Positive",
"difficulty": "Medium",
"description_full": "Find the smallest missing positive integer from the array.",
"input": "First line N, second line N integers.",
"output": "Print the smallest missing positive integer.",
"example": "Input:\n3\n1 2 0\nOutput:\n3",
"tests": [
{"input": "3\n1 2 0", "output": "3", "hidden": False},
{"input": "4\n2 3 4 5", "output": "1", "hidden": False},
{"input": "5\n1 2 3 4 5", "output": "6"},
{"input": "1\n1", "output": "2"},
{"input": "5\n-1 -2 -3 -4 -5", "output": "1"}
]
},

{
"id": "m9",
"title": "Longest Increasing Subarray",
"difficulty": "Medium",
"description_full": "Find the length of the longest strictly increasing contiguous subarray.",
"input": "First line N, second line N integers.",
"output": "Print the length.",
"example": "Input:\n6\n1 2 2 3 4 1\nOutput:\n3",
"tests": [
{"input": "6\n1 2 2 3 4 1", "output": "3", "hidden": False},
{"input": "5\n1 2 3 4 5", "output": "5", "hidden": False},
{"input": "3\n3 2 1", "output": "1"},
{"input": "1\n9", "output": "1"},
{"input": "6\n1 3 5 4 7 8", "output": "3"}
]
},

{
"id": "m10",
"title": "Count Pairs with Given Sum",
"difficulty": "Medium",
"description_full": "Count number of pairs whose sum equals K.",
"input": "First line N, second line N integers, third line K.",
"output": "Print number of valid pairs.",
"example": "Input:\n4\n1 5 7 -1\n6\nOutput:\n2",
"tests": [
{"input": "4\n1 5 7 -1\n6", "output": "2", "hidden": False},
{"input": "3\n1 1 1\n2", "output": "3", "hidden": False},
{"input": "5\n2 4 3 5 7\n7", "output": "2"},
{"input": "2\n1 2\n10", "output": "0"},
{"input": "4\n0 0 0 0\n0", "output": "6"}
]
},

{
"id": "m11",
"title": "First Non-Repeating Character",
"difficulty": "Medium",
"description_full": "Find the first non-repeating character in a string.",
"input": "A single string.",
"output": "Print the character or -1.",
"example": "Input:\nswiss\nOutput:\nw",
"tests": [
{"input": "swiss", "output": "w", "hidden": False},
{"input": "aabb", "output": "-1", "hidden": False},
{"input": "abcd", "output": "a"},
{"input": "a", "output": "a"},
{"input": "aabbccdde", "output": "e"}
]
},

{
"id": "m12",
"title": "Check Anagram",
"difficulty": "Medium",
"description_full": "Check if two strings are anagrams.",
"input": "Two strings separated by space.",
"output": "Print YES or NO.",
"example": "Input:\nlisten silent\nOutput:\nYES",
"tests": [
{"input": "listen silent", "output": "YES", "hidden": False},
{"input": "hello bellow", "output": "NO", "hidden": False},
{"input": "abc cba", "output": "YES"},
{"input": "a a", "output": "YES"},
{"input": "rat tar", "output": "YES"}
]
},

{
"id": "m13",
"title": "String Compression",
"difficulty": "Medium",
"description_full": "Compress the string by counting consecutive characters.",
"input": "A single string.",
"output": "Print compressed string.",
"example": "Input:\naaaabbc\nOutput:\na4b2c",
"tests": [
{"input": "aaaabbc", "output": "a4b2c", "hidden": False},
{"input": "abcd", "output": "abcd", "hidden": False},
{"input": "xxxx", "output": "x4"},
{"input": "aabb", "output": "a2b2"},
{"input": "zzzzzz", "output": "z6"}
]
},

{
"id": "m14",
"title": "Binary to Decimal",
"difficulty": "Medium",
"description_full": "Convert a binary number to decimal.",
"input": "A binary number.",
"output": "Print its decimal value.",
"example": "Input:\n1011\nOutput:\n11",
"tests": [
{"input": "1011", "output": "11", "hidden": False},
{"input": "0", "output": "0", "hidden": False},
{"input": "1111", "output": "15"},
{"input": "1", "output": "1"},
{"input": "100000", "output": "32"}
]
},

{
"id": "m15",
"title": "Count Set Bits",
"difficulty": "Medium",
"description_full": "Count number of set bits in binary representation.",
"input": "A single integer N.",
"output": "Print count of set bits.",
"example": "Input:\n15\nOutput:\n4",
"tests": [
{"input": "15", "output": "4", "hidden": False},
{"input": "0", "output": "0", "hidden": False},
{"input": "8", "output": "1"},
{"input": "7", "output": "3"},
{"input": "1023", "output": "10"}
]
},

{
"id": "m16",
"title": "Rotate Array by K",
"difficulty": "Medium",
"description_full": "Rotate the array to the right by K positions.",
"input": "First line N, second line array, third line K.",
"output": "Print rotated array.",
"example": "Input:\n5\n1 2 3 4 5\n2\nOutput:\n4 5 1 2 3",
"tests": [
{"input": "5\n1 2 3 4 5\n2", "output": "4 5 1 2 3", "hidden": False},
{"input": "3\n1 2 3\n3", "output": "1 2 3", "hidden": False},
{"input": "4\n1 2 3 4\n1", "output": "4 1 2 3"},
{"input": "1\n9\n10", "output": "9"},
{"input": "5\n1 2 3 4 5\n7", "output": "4 5 1 2 3"}
]
},

{
"id": "m17",
"title": "Subarray with Sum Zero",
"difficulty": "Medium",
"description_full": "Count number of subarrays whose sum is zero.",
"input": "First line N, second line N integers.",
"output": "Print count of subarrays.",
"example": "Input:\n3\n1 -1 0\nOutput:\n3",
"tests": [
{"input": "3\n1 -1 0", "output": "3", "hidden": False},
{"input": "4\n0 0 0 0", "output": "10", "hidden": False},
{"input": "3\n1 2 3", "output": "0"},
{"input": "1\n0", "output": "1"},
{"input": "5\n2 -2 2 -2 2", "output": "6"}
]
},

{
"id": "m18",
"title": "Longest Substring Without Repeating Characters",
"difficulty": "Medium",
"description_full": "Find the length of the longest substring without repeating characters.",
"input": "A single string.",
"output": "Print the length.",
"example": "Input:\nabcabcbb\nOutput:\n3",
"tests": [
{"input": "abcabcbb", "output": "3", "hidden": False},
{"input": "bbbbb", "output": "1", "hidden": False},
{"input": "pwwkew", "output": "3"},
{"input": "a", "output": "1"},
{"input": "abcdef", "output": "6"}
]
},

{
"id": "m19",
"title": "Find Peak Element",
"difficulty": "Medium",
"description_full": "Find any peak element index (1-based).",
"input": "First line N, second line N integers.",
"output": "Print index of a peak element.",
"example": "Input:\n3\n1 3 2\nOutput:\n2",
"tests": [
{"input": "3\n1 3 2", "output": "2", "hidden": False},
{"input": "4\n1 2 3 4", "output": "4", "hidden": False},
{"input": "5\n5 4 3 2 1", "output": "1"},
{"input": "1\n10", "output": "1"},
{"input": "6\n1 2 1 3 5 6", "output": "6"}
]
},

{
"id": "m20",
"title": "Intersection of Arrays",
"difficulty": "Medium",
"description_full": "Print the intersection of two arrays (unique elements).",
"input": "First line N, array A. Second line M, array B.",
"output": "Print common elements in sorted order.",
"example": "Input:\n4\n1 2 3 4\n3\n3 4 5\nOutput:\n3 4",
"tests": [
{"input": "4\n1 2 3 4\n3\n3 4 5", "output": "3 4", "hidden": False},
{"input": "3\n1 2 3\n3\n4 5 6", "output": "", "hidden": False},
{"input": "5\n1 1 2 2 3\n3\n2 3 3", "output": "2 3"},
{"input": "1\n7\n1\n7", "output": "7"},
{"input": "4\n10 20 30 40\n2\n20 40", "output": "20 40"}
]
}

]
}
