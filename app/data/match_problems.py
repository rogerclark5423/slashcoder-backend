# match_problems.py
# 30 PROBLEMS — MIXED (NOT HARD)
# Each with exactly 3 hidden testcases

PROBLEMS = {
    "Very Easy": [

    {
        "id": "ve1",
        "title": "Add Two Numbers",
        "description": "Print sum of A and B.",
        "description_full": "Given two integers A and B, print A+B.",
        "input": "A B",
        "output": "A+B",
        "example": "Input:\n3 4\nOutput:\n7",
        "tests": [
            {"input": "3 4", "output": "7"},
            {"input": "10 5", "output": "15"},
            {"input": "1 99", "output": "100"}
        ]
    },

    {
        "id": "ve2",
        "title": "Subtract Two Numbers",
        "description": "Print difference A-B.",
        "description_full": "Given two integers A and B, print A-B.",
        "input": "A B",
        "output": "A-B",
        "example": "Input:\n10 4\nOutput:\n6",
        "tests": [
            {"input": "10 4", "output": "6"},
            {"input": "20 5", "output": "15"},
            {"input": "50 10", "output": "40"}
        ]
    },

    {
        "id": "ve3",
        "title": "Multiply Two Numbers",
        "description": "Print A*B.",
        "description_full": "Given two integers A and B, print their product.",
        "input": "A B",
        "output": "A*B",
        "example": "Input:\n3 7\nOutput:\n21",
        "tests": [
            {"input": "3 7", "output": "21"},
            {"input": "5 5", "output": "25"},
            {"input": "9 9", "output": "81"}
        ]
    },

    {
        "id": "ve4",
        "title": "Divide Two Numbers",
        "description": "Print integer division A//B.",
        "description_full": "Given A and B, print the integer division result A//B.",
        "input": "A B",
        "output": "A//B",
        "example": "Input:\n10 3\nOutput:\n3",
        "tests": [
            {"input": "10 3", "output": "3"},
            {"input": "9 2", "output": "4"},
            {"input": "100 10", "output": "10"}
        ]
    },

    {
        "id": "ve5",
        "title": "Square of a Number",
        "description": "Print N².",
        "description_full": "Given integer N, print N*N.",
        "input": "N",
        "output": "N*N",
        "example": "Input:\n5\nOutput:\n25",
        "tests": [
            {"input": "5", "output": "25"},
            {"input": "12", "output": "144"},
            {"input": "7", "output": "49"}
        ]
    },

    {
        "id": "ve6",
        "title": "Cube of a Number",
        "description": "Print N³.",
        "description_full": "Given integer N, print N*N*N.",
        "input": "N",
        "output": "N^3",
        "example": "Input:\n3\nOutput:\n27",
        "tests": [
            {"input": "3", "output": "27"},
            {"input": "4", "output": "64"},
            {"input": "5", "output": "125"}
        ]
    },

    {
        "id": "ve7",
        "title": "Check Even or Odd",
        "description": "Print EVEN or ODD.",
        "description_full": "Given N, print EVEN if divisible by 2 else ODD.",
        "input": "N",
        "output": "EVEN/ODD",
        "example": "Input:\n4\nOutput:\nEVEN",
        "tests": [
            {"input": "4", "output": "EVEN"},
            {"input": "7", "output": "ODD"},
            {"input": "10", "output": "EVEN"}
        ]
    },

    {
        "id": "ve8",
        "title": "Check Positive or Negative",
        "description": "Check sign of number.",
        "description_full": "Given N, print POSITIVE if N>0, NEGATIVE if N<0, else ZERO.",
        "input": "N",
        "output": "POSITIVE/NEGATIVE/ZERO",
        "example": "Input:\n5\nOutput:\nPOSITIVE",
        "tests": [
            {"input": "-3", "output": "NEGATIVE"},
            {"input": "0", "output": "ZERO"},
            {"input": "9", "output": "POSITIVE"}
        ]
    },

    {
        "id": "ve9",
        "title": "Last Digit",
        "description": "Print last digit of N.",
        "description_full": "Given integer N, print N % 10.",
        "input": "N",
        "output": "last digit",
        "example": "Input:\n123\nOutput:\n3",
        "tests": [
            {"input": "123", "output": "3"},
            {"input": "506", "output": "6"},
            {"input": "9", "output": "9"}
        ]
    },

    {
        "id": "ve10",
        "title": "Sum of Digits",
        "description": "Print sum of digits of N.",
        "description_full": "Given integer N, compute sum of digits.",
        "input": "N",
        "output": "sum",
        "example": "Input:\n123\nOutput:\n6",
        "tests": [
            {"input": "123", "output": "6"},
            {"input": "999", "output": "27"},
            {"input": "101", "output": "2"}
        ]
    },

    {
        "id": "ve11",
        "title": "Reverse a Number",
        "description": "Reverse digits of N.",
        "description_full": "Given integer N, print its digit-reversed value.",
        "input": "N",
        "output": "reverse",
        "example": "Input:\n123\nOutput:\n321",
        "tests": [
            {"input": "123", "output": "321"},
            {"input": "400", "output": "004"},
            {"input": "9", "output": "9"}
        ]
    },

    {
        "id": "ve12",
        "title": "Absolute Value",
        "description": "Print |N|.",
        "description_full": "Given integer N, print absolute value of N.",
        "input": "N",
        "output": "abs(N)",
        "example": "Input:\n-5\nOutput:\n5",
        "tests": [
            {"input": "-5", "output": "5"},
            {"input": "9", "output": "9"},
            {"input": "0", "output": "0"}
        ]
    },

    {
        "id": "ve13",
        "title": "Simple Interest",
        "description": "Compute simple interest.",
        "description_full": "Given P, R, T print simple interest = (P*R*T)/100.",
        "input": "P R T",
        "output": "SI",
        "example": "Input:\n1000 5 2\nOutput:\n100",
        "tests": [
            {"input": "1000 5 2", "output": "100"},
            {"input": "500 10 1", "output": "50"},
            {"input": "1500 4 3", "output": "180"}
        ]
    },

    {
        "id": "ve14",
        "title": "Convert Celsius to Fahrenheit",
        "description": "Print Fahrenheit.",
        "description_full": "Given C, print F = (C*9/5)+32.",
        "input": "C",
        "output": "F",
        "example": "Input:\n0\nOutput:\n32",
        "tests": [
            {"input": "0", "output": "32"},
            {"input": "100", "output": "212"},
            {"input": "20", "output": "68"}
        ]
    },

    {
        "id": "ve15",
        "title": "Minimum of Two Numbers",
        "description": "Find smaller value.",
        "description_full": "Print minimum of A and B.",
        "input": "A B",
        "output": "min",
        "example": "Input:\n5 9\nOutput:\n5",
        "tests": [
            {"input": "5 9", "output": "5"},
            {"input": "100 1", "output": "1"},
            {"input": "7 7", "output": "7"}
        ]
    },

    {
        "id": "ve16",
        "title": "Print Hello",
        "description": "Output Hello.",
        "description_full": "No input. Just print Hello.",
        "input": "-",
        "output": "Hello",
        "example": "Output:\nHello",
        "tests": [
            {"input": "", "output": "Hello"},
            {"input": "", "output": "Hello"},
            {"input": "", "output": "Hello"}
        ]
    },

    {
        "id": "ve17",
        "title": "Character to Uppercase",
        "description": "Convert lowercase to uppercase.",
        "description_full": "Given lowercase character, print uppercase.",
        "input": "char",
        "output": "uppercase",
        "example": "Input:\na\nOutput:\nA",
        "tests": [
            {"input": "a", "output": "A"},
            {"input": "b", "output": "B"},
            {"input": "z", "output": "Z"}
        ]
    },

    {
        "id": "ve18",
        "title": "Find Remainder",
        "description": "Print A % B.",
        "description_full": "Given A and B, print A modulo B.",
        "input": "A B",
        "output": "A%B",
        "example": "Input:\n10 3\nOutput:\n1",
        "tests": [
            {"input": "10 3", "output": "1"},
            {"input": "20 6", "output": "2"},
            {"input": "7 7", "output": "0"}
        ]
    },

    {
        "id": "ve19",
        "title": "Add Three Numbers",
        "description": "Print A+B+C.",
        "description_full": "Given three integers A, B, and C, print their sum.",
        "input": "A B C",
        "output": "A+B+C",
        "example": "Input:\n2 3 4\nOutput:\n9",
        "tests": [
            {"input": "1 1 1", "output": "3"},
            {"input": "10 20 30", "output": "60"},
            {"input": "5 5 5", "output": "15"}
        ]
    },

    {
        "id": "ve20",
        "title": "Check Divisible by 5",
        "description": "Check if N divisible by 5.",
        "description_full": "Print YES if N%5==0 else NO.",
        "input": "N",
        "output": "YES/NO",
        "example": "Input:\n10\nOutput:\nYES",
        "tests": [
            {"input": "25", "output": "YES"},
            {"input": "13", "output": "NO"},
            {"input": "0", "output": "YES"}
        ]
    }

],
    "Easy": [

    {
        "id": "e1",
        "title": "Sum of Array",
        "description": "Find the sum of N integers.",
        "description_full": "Given N and array A of N integers, print the sum of all elements.",
        "input": "N\nA1 A2 ... AN",
        "output": "sum",
        "example": "Input:\n5\n1 2 3 4 5\nOutput:\n15",
        "tests": [
            {"input": "3\n10 10 10", "output": "30"},
            {"input": "4\n5 5 5 5", "output": "20"},
            {"input": "5\n1 1 1 1 1", "output": "5"}
        ]
    },

    {
        "id": "e2",
        "title": "Count Even Numbers",
        "description": "Count even numbers in array.",
        "description_full": "Given N and array A, count how many elements are even.",
        "input": "N\nA1 A2 ... AN",
        "output": "count",
        "example": "Input:\n5\n1 2 3 4 5\nOutput:\n2",
        "tests": [
            {"input": "4\n2 4 6 8", "output": "4"},
            {"input": "4\n1 3 5 7", "output": "0"},
            {"input": "6\n1 2 3 4 5 6", "output": "3"}
        ]
    },

    {
        "id": "e3",
        "title": "Count Odd Numbers",
        "description": "Count odd numbers in array.",
        "description_full": "Given N and array A, count how many elements are odd.",
        "input": "N\nA1 A2 ... AN",
        "output": "count",
        "example": "Input:\n5\n1 2 3 4 5\nOutput:\n3",
        "tests": [
            {"input": "4\n2 4 6 8", "output": "0"},
            {"input": "4\n1 3 5 7", "output": "4"},
            {"input": "6\n1 2 3 4 5 6", "output": "3"}
        ]
    },

    {
        "id": "e4",
        "title": "Find Maximum",
        "description": "Find largest element.",
        "description_full": "Given N and array A, print maximum element.",
        "input": "N\nA1 A2 ... AN",
        "output": "max",
        "example": "Input:\n5\n1 9 3 4 5\nOutput:\n9",
        "tests": [
            {"input": "3\n1 2 3", "output": "3"},
            {"input": "4\n10 20 5 1", "output": "20"},
            {"input": "5\n9 9 9 9 9", "output": "9"}
        ]
    },

    {
        "id": "e5",
        "title": "Find Minimum",
        "description": "Find smallest element.",
        "description_full": "Given N and array A, print minimum element.",
        "input": "N\nA1 A2 ... AN",
        "output": "min",
        "example": "Input:\n5\n5 4 3 2 1\nOutput:\n1",
        "tests": [
            {"input": "3\n10 20 5", "output": "5"},
            {"input": "4\n9 9 9 9", "output": "9"},
            {"input": "5\n1 -1 2 3 4", "output": "-1"}
        ]
    },

    {
        "id": "e6",
        "title": "Count Occurrences",
        "description": "Count how many times X appears.",
        "description_full": "Given N, array A, and X, count frequency of X in A.",
        "input": "N\nA1 A2 ... AN\nX",
        "output": "count",
        "example": "Input:\n5\n1 2 3 2 2\n2\nOutput:\n3",
        "tests": [
            {"input": "4\n5 5 5 5\n5", "output": "4"},
            {"input": "3\n1 2 3\n9", "output": "0"},
            {"input": "6\n1 1 1 2 2 3\n1", "output": "3"}
        ]
    },

    {
        "id": "e7",
        "title": "Reverse Array",
        "description": "Reverse the array.",
        "description_full": "Given N and array A, print the reversed array.",
        "input": "N\nA1 A2 ... AN",
        "output": "reversed array",
        "example": "Input:\n5\n1 2 3 4 5\nOutput:\n5 4 3 2 1",
        "tests": [
            {"input": "3\n10 20 30", "output": "30 20 10"},
            {"input": "4\n1 2 3 4", "output": "4 3 2 1"},
            {"input": "1\n9", "output": "9"}
        ]
    },

    {
        "id": "e8",
        "title": "Rotate Array Right by 1",
        "description": "Move last element to front.",
        "description_full": "Rotate array right by 1 position.",
        "input": "N\nA1 A2 ... AN",
        "output": "rotated array",
        "example": "Input:\n5\n1 2 3 4 5\nOutput:\n5 1 2 3 4",
        "tests": [
            {"input": "3\n1 2 3", "output": "3 1 2"},
            {"input": "4\n10 20 30 40", "output": "40 10 20 30"},
            {"input": "1\n9", "output": "9"}
        ]
    },

    {
        "id": "e9",
        "title": "Rotate Array Left by 1",
        "description": "Move first element to end.",
        "description_full": "Rotate array left by 1 position.",
        "input": "N\nA1 A2 ... AN",
        "output": "rotated array",
        "example": "Input:\n5\n1 2 3 4 5\nOutput:\n2 3 4 5 1",
        "tests": [
            {"input": "3\n1 2 3", "output": "2 3 1"},
            {"input": "4\n10 20 30 40", "output": "20 30 40 10"},
            {"input": "1\n5", "output": "5"}
        ]
    },

    {
        "id": "e10",
        "title": "Palindrome String",
        "description": "Check if string is palindrome.",
        "description_full": "Given string S, print YES if palindrome else NO.",
        "input": "S",
        "output": "YES/NO",
        "example": "Input:\nmadam\nOutput:\nYES",
        "tests": [
            {"input": "level", "output": "YES"},
            {"input": "hello", "output": "NO"},
            {"input": "aaa", "output": "YES"}
        ]
    },

    {
        "id": "e11",
        "title": "Count Vowels",
        "description": "Count vowels in string.",
        "description_full": "Given string S, count number of vowels.",
        "input": "S",
        "output": "count",
        "example": "Input:\nhello\nOutput:\n2",
        "tests": [
            {"input": "aeiou", "output": "5"},
            {"input": "zzz", "output": "0"},
            {"input": "code", "output": "2"}
        ]
    },

    {
        "id": "e12",
        "title": "Remove Vowels",
        "description": "Delete all vowels.",
        "description_full": "Given string S, remove all vowels and print result.",
        "input": "S",
        "output": "string",
        "example": "Input:\nhello\nOutput:\nhll",
        "tests": [
            {"input": "apple", "output": "ppl"},
            {"input": "aeiou", "output": ""},
            {"input": "world", "output": "wrld"}
        ]
    },

    {
        "id": "e13",
        "title": "Count Words",
        "description": "Count the number of words.",
        "description_full": "Given a sentence S, count number of words separated by spaces.",
        "input": "S",
        "output": "count",
        "example": "Input:\nhello world\nOutput:\n2",
        "tests": [
            {"input": "one two three", "output": "3"},
            {"input": "single", "output": "1"},
            {"input": "a b c d", "output": "4"}
        ]
    },

    {
        "id": "e14",
        "title": "Factorial",
        "description": "Compute factorial.",
        "description_full": "Given N, print N! (0 ≤ N ≤ 12).",
        "input": "N",
        "output": "N!",
        "example": "Input:\n5\nOutput:\n120",
        "tests": [
            {"input": "3", "output": "6"},
            {"input": "0", "output": "1"},
            {"input": "6", "output": "720"}
        ]
    },

    {
        "id": "e15",
        "title": "Fibonacci Series Sum",
        "description": "Sum of first N Fibonacci numbers.",
        "description_full": "Given N, print sum of first N Fibonacci numbers.",
        "input": "N",
        "output": "sum",
        "example": "Input:\n3\nOutput:\n4",
        "tests": [
            {"input": "1", "output": "1"},
            {"input": "4", "output": "7"},
            {"input": "5", "output": "12"}
        ]
    },

    {
        "id": "e16",
        "title": "GCD of Two Numbers",
        "description": "Compute GCD.",
        "description_full": "Given A and B, print their greatest common divisor.",
        "input": "A B",
        "output": "GCD",
        "example": "Input:\n10 5\nOutput:\n5",
        "tests": [
            {"input": "12 8", "output": "4"},
            {"input": "7 3", "output": "1"},
            {"input": "100 10", "output": "10"}
        ]
    },

    {
        "id": "e17",
        "title": "LCM of Two Numbers",
        "description": "Compute LCM.",
        "description_full": "Given A and B, print their least common multiple.",
        "input": "A B",
        "output": "LCM",
        "example": "Input:\n4 6\nOutput:\n12",
        "tests": [
            {"input": "5 10", "output": "10"},
            {"input": "7 3", "output": "21"},
            {"input": "4 8", "output": "8"}
        ]
    },

    {
        "id": "e18",
        "title": "Prime Check",
        "description": "Check if N is prime.",
        "description_full": "Given N, print YES if prime else NO.",
        "input": "N",
        "output": "YES/NO",
        "example": "Input:\n5\nOutput:\nYES",
        "tests": [
            {"input": "11", "output": "YES"},
            {"input": "12", "output": "NO"},
            {"input": "1", "output": "NO"}
        ]
    },

    {
        "id": "e19",
        "title": "Perfect Number Check",
        "description": "Check if N is perfect.",
        "description_full": "A perfect number is one whose proper divisors sum equals N.",
        "input": "N",
        "output": "YES/NO",
        "example": "Input:\n6\nOutput:\nYES",
        "tests": [
            {"input": "28", "output": "YES"},
            {"input": "10", "output": "NO"},
            {"input": "1", "output": "NO"}
        ]
    },

    {
        "id": "e20",
        "title": "Second Largest",
        "description": "Find the second largest element.",
        "description_full": "Given N and array A, print the 2nd largest number.",
        "input": "N\nA1 A2 ... AN",
        "output": "second largest",
        "example": "Input:\n5\n5 4 3 2 1\nOutput:\n4",
        "tests": [
            {"input": "4\n10 20 30 40", "output": "30"},
            {"input": "3\n5 5 3", "output": "5"},
            {"input": "5\n1 2 3 4 5", "output": "4"}
        ]
    },

    {
        "id": "e21",
        "title": "Count Positive Numbers",
        "description": "Count positive values in array.",
        "description_full": "Given N and array A, count how many elements are > 0.",
        "input": "N\nA1 A2 ... AN",
        "output": "count",
        "example": "Input:\n5\n-1 2 -3 4 0\nOutput:\n2",
        "tests": [
            {"input": "3\n1 2 3", "output": "3"},
            {"input": "4\n-1 -2 -3 -4", "output": "0"},
            {"input": "5\n0 0 1 2 3", "output": "3"}
        ]
    },

    {
        "id": "e22",
        "title": "Array Sorted Check",
        "description": "Check if array is sorted.",
        "description_full": "Print YES if array is sorted in non-decreasing order else NO.",
        "input": "N\nA1 A2 ... AN",
        "output": "YES/NO",
        "example": "Input:\n5\n1 2 3 4 5\nOutput:\nYES",
        "tests": [
            {"input": "3\n1 2 3", "output": "YES"},
            {"input": "4\n1 3 2 4", "output": "NO"},
            {"input": "1\n7", "output": "YES"}
        ]
    },

    {
        "id": "e23",
        "title": "Average of Numbers",
        "description": "Compute integer average.",
        "description_full": "Given N and array A, compute floor(sum/N).",
        "input": "N\nA1 A2 ... AN",
        "output": "average",
        "example": "Input:\n3\n2 4 6\nOutput:\n4",
        "tests": [
            {"input": "3\n1 2 3", "output": "2"},
            {"input": "4\n10 10 10 10", "output": "10"},
            {"input": "5\n1 1 1 1 1", "output": "1"}
        ]
    },

    {
        "id": "e24",
        "title": "Replace Negatives with Zero",
        "description": "Convert all negative values to 0.",
        "description_full": "Given N and array A, replace all negative numbers with 0.",
        "input": "N\nA1 A2 ... AN",
        "output": "modified array",
        "example": "Input:\n5\n1 -2 3 -4 5\nOutput:\n1 0 3 0 5",
        "tests": [
            {"input": "4\n-1 -2 -3 -4", "output": "0 0 0 0"},
            {"input": "3\n1 2 3", "output": "1 2 3"},
            {"input": "5\n0 -1 0 -2 0", "output": "0 0 0 0 0"}
        ]
    },

    {
        "id": "e25",
        "title": "Unique Number",
        "description": "Find element that appears once.",
        "description_full": "Given N and array where all except one number occur twice, find the unique number.",
        "input": "N\nA1 A2 ... AN",
        "output": "unique",
        "example": "Input:\n5\n1 1 2 2 3\nOutput:\n3",
        "tests": [
            {"input": "3\n5 5 9", "output": "9"},
            {"input": "7\n2 3 2 4 4 5 5", "output": "3"},
            {"input": "1\n7", "output": "7"}
        ]
    },

    {
        "id": "e26",
        "title": "Count Prime Numbers",
        "description": "Count primes in array.",
        "description_full": "Given N and array A, count how many numbers are prime.",
        "input": "N\nA1 A2 ... AN",
        "output": "count",
        "example": "Input:\n5\n1 2 3 4 5\nOutput:\n3",
        "tests": [
            {"input": "4\n2 3 5 7", "output": "4"},
            {"input": "4\n4 6 8 10", "output": "0"},
            {"input": "5\n11 13 17 19 23", "output": "5"}
        ]
    },

    {
        "id": "e27",
        "title": "Intersection of Two Arrays",
        "description": "Print common values.",
        "description_full": "Given N, array A and M, array B, print common elements (unique, sorted).",
        "input": "N\nA1 A2 ... AN\nM\nB1 B2 ... BM",
        "output": "intersection",
        "example": "Input:\n4\n1 2 3 4\n3\n3 4 5\nOutput:\n3 4",
        "tests": [
            {"input": "3\n1 2 3\n3\n4 5 6", "output": ""},
            {"input": "5\n1 1 2 2 3\n4\n2 3 3 4", "output": "2 3"},
            {"input": "3\n5 6 7\n3\n7 8 9", "output": "7"}
        ]
    },

    {
        "id": "e28",
        "title": "Remove Duplicates from Array",
        "description": "Keep only unique values.",
        "description_full": "Given N and array A, print unique elements in order.",
        "input": "N\nA1 A2 ... AN",
        "output": "unique array",
        "example": "Input:\n6\n1 2 2 3 3 4\nOutput:\n1 2 3 4",
        "tests": [
            {"input": "4\n5 5 5 5", "output": "5"},
            {"input": "5\n1 2 3 4 5", "output": "1 2 3 4 5"},
            {"input": "7\n1 1 2 2 3 3 3", "output": "1 2 3"}
        ]
    },

    {
        "id": "e29",
        "title": "Merge Two Sorted Arrays",
        "description": "Merge and print sorted result.",
        "description_full": "Given sorted arrays A and B, merge them into one sorted array.",
        "input": "N\nA1 A2 ... AN\nM\nB1 B2 ... BM",
        "output": "merged sorted array",
        "example": "Input:\n3\n1 3 5\n3\n2 4 6\nOutput:\n1 2 3 4 5 6",
        "tests": [
            {"input": "2\n1 2\n2\n3 4", "output": "1 2 3 4"},
            {"input": "3\n2 4 6\n3\n1 3 5", "output": "1 2 3 4 5 6"},
            {"input": "1\n5\n1\n1", "output": "1 5"}
        ]
    },

    {
        "id": "e30",
        "title": "Check Array Palindrome",
        "description": "Check if array reads same forward/backward.",
        "description_full": "Given N and array A, print YES if array is palindrome else NO.",
        "input": "N\nA1 A2 ... AN",
        "output": "YES/NO",
        "example": "Input:\n5\n1 2 3 2 1\nOutput:\nYES",
        "tests": [
            {"input": "3\n1 2 1", "output": "YES"},
            {"input": "4\n1 2 3 4", "output": "NO"},
            {"input": "1\n7", "output": "YES"}
        ]
    }

],
    "Medium": [

    {
        "id": "m1",
        "title": "Leaders in an Array",
        "description": "Print leaders (elements greater than all to their right).",
        "description_full": "Given N and array A, print all leaders in order of appearance (space-separated). Last element is always a leader.",
        "input": "N\nA1 A2 ... AN",
        "output": "leaders",
        "example": "Input:\n6\n16 17 4 3 5 2\nOutput:\n17 5 2",
        "tests": [
            {"input": "5\n1 2 3 4 5", "output": "5"},
            {"input": "6\n16 17 4 3 5 2", "output": "17 5 2"},
            {"input": "3\n10 10 10", "output": "10 10 10"}
        ]
    },

    {
        "id": "m2",
        "title": "Count Distinct Elements",
        "description": "Count unique values in array.",
        "description_full": "Given N and array A, print number of distinct elements.",
        "input": "N\nA1 A2 ... AN",
        "output": "count",
        "example": "Input:\n5\n1 2 2 3 3\nOutput:\n3",
        "tests": [
            {"input": "5\n1 1 1 1 1", "output": "1"},
            {"input": "4\n1 2 3 4", "output": "4"},
            {"input": "6\n1 2 2 3 4 4", "output": "4"}
        ]
    },

    {
        "id": "m3",
        "title": "Prefix Sum Array",
        "description": "Compute prefix sums.",
        "description_full": "Given N and array A, print prefix sum array (space-separated).",
        "input": "N\nA1 A2 ... AN",
        "output": "prefix sums",
        "example": "Input:\n5\n1 2 3 4 5\nOutput:\n1 3 6 10 15",
        "tests": [
            {"input": "3\n1 2 3", "output": "1 3 6"},
            {"input": "4\n5 5 5 5", "output": "5 10 15 20"},
            {"input": "5\n2 0 2 0 2", "output": "2 2 4 4 6"}
        ]
    },

    {
        "id": "m4",
        "title": "Suffix Sum Array",
        "description": "Compute suffix sums.",
        "description_full": "Given N and array A, print suffix sum array (space-separated) where position i contains sum from i to N.",
        "input": "N\nA1 A2 ... AN",
        "output": "suffix sums",
        "example": "Input:\n5\n1 2 3 4 5\nOutput:\n15 14 12 9 5",
        "tests": [
            {"input": "3\n1 2 3", "output": "6 5 3"},
            {"input": "4\n0 0 0 1", "output": "1 1 1 1"},
            {"input": "5\n2 2 2 2 2", "output": "10 8 6 4 2"}
        ]
    },

    {
        "id": "m5",
        "title": "Move Zeros to End",
        "description": "Move all zeros to array end preserving order.",
        "description_full": "Given N and array A, move all zeros to the end and print resulting array.",
        "input": "N\nA1 A2 ... AN",
        "output": "modified array",
        "example": "Input:\n5\n0 1 0 3 12\nOutput:\n1 3 12 0 0",
        "tests": [
            {"input": "5\n0 1 0 3 12", "output": "1 3 12 0 0"},
            {"input": "3\n0 0 1", "output": "1 0 0"},
            {"input": "4\n1 2 3 4", "output": "1 2 3 4"}
        ]
    },

    {
        "id": "m6",
        "title": "Majority Element",
        "description": "Find element occurring more than n/2 times or print -1.",
        "description_full": "Given N and array A, print the majority element if exists, otherwise -1.",
        "input": "N\nA1 A2 ... AN",
        "output": "majority or -1",
        "example": "Input:\n5\n3 3 4 2 3\nOutput:\n3",
        "tests": [
            {"input": "3\n1 1 2", "output": "1"},
            {"input": "4\n1 2 3 4", "output": "-1"},
            {"input": "5\n2 2 2 1 2", "output": "2"}
        ]
    },

    {
        "id": "m7",
        "title": "Max Subarray Sum (Kadane Simple)",
        "description": "Maximum subarray sum.",
        "description_full": "Given N and array A, print maximum contiguous subarray sum (at least one element).",
        "input": "N\nA1 A2 ... AN",
        "output": "max sum",
        "example": "Input:\n5\n-2 1 -3 4 -1\nOutput:\n4",
        "tests": [
            {"input": "3\n1 2 3", "output": "6"},
            {"input": "4\n-1 -2 -3 -4", "output": "-1"},
            {"input": "5\n-2 1 -3 4 -1", "output": "4"}
        ]
    },

    {
        "id": "m8",
        "title": "Find Equilibrium Index",
        "description": "Index where left sum equals right sum.",
        "description_full": "Given N and array A, print smallest index (1-based) where sum of elements left equals sum of elements right, else -1.",
        "input": "N\nA1 A2 ... AN",
        "output": "index or -1",
        "example": "Input:\n3\n1 2 3\nOutput:\n-1",
        "tests": [
            {"input": "3\n1 2 3", "output": "-1"},
            {"input": "3\n2 0 2", "output": "2"},
            {"input": "5\n1 3 5 2 2", "output": "3"}
        ]
    },

    {
        "id": "m9",
        "title": "Count Pairs with Given Sum (unsorted)",
        "description": "Count unordered pairs with sum = K.",
        "description_full": "Given N, array A and integer K, print number of unordered pairs (i<j) with Ai+Aj = K.",
        "input": "N\nA1 A2 ... AN\nK",
        "output": "count",
        "example": "Input:\n4\n1 5 7 -1\n6\nOutput:\n2",
        "tests": [
            {"input": "4\n1 5 7 -1\n6", "output": "2"},
            {"input": "3\n1 1 1\n2", "output": "3"},
            {"input": "5\n2 4 3 5 7\n7", "output": "2"}
        ]
    },

    {
        "id": "m10",
        "title": "Two Sum in Sorted Array (two-pointer)",
        "description": "Return indices of two numbers summing to K (1-based, smaller index first).",
        "description_full": "Given N and sorted array A and K, print two indices i j such that Ai+Aj=K or print -1 if none.",
        "input": "N\nA1 A2 ... AN\nK",
        "output": "i j or -1",
        "example": "Input:\n4\n1 2 3 4\n5\nOutput:\n1 4",
        "tests": [
            {"input": "4\n1 2 3 4\n5", "output": "1 4"},
            {"input": "3\n1 3 5\n10", "output": "-1"},
            {"input": "5\n1 2 3 4 6\n7", "output": "1 5"}
        ]
    },

    {
        "id": "m11",
        "title": "Find Peak Element (local maxima)",
        "description": "Find any index which is a peak (greater than neighbors).",
        "description_full": "Given N and array A, print 1-based index of any peak element. If multiple, any valid index. For N=1 return 1.",
        "input": "N\nA1 A2 ... AN",
        "output": "index",
        "example": "Input:\n3\n1 3 2\nOutput:\n2",
        "tests": [
            {"input": "1\n10", "output": "1"},
            {"input": "3\n1 3 2", "output": "2"},
            {"input": "4\n1 2 3 4", "output": "4"}
        ]
    },

    {
        "id": "m12",
        "title": "Majority Element (Boyer-Moore verify)",
        "description": "Return majority element if exists else -1 (confirmation required).",
        "description_full": "Given N and array A, use linear time / constant space approach to find majority if any.",
        "input": "N\nA1 A2 ... AN",
        "output": "majority or -1",
        "example": "Input:\n5\n3 3 4 2 3\nOutput:\n3",
        "tests": [
            {"input": "5\n3 3 4 3 3", "output": "3"},
            {"input": "4\n1 2 3 4", "output": "-1"},
            {"input": "3\n2 2 2", "output": "2"}
        ]
    },

    {
        "id": "m13",
        "title": "Find Smallest Missing Positive",
        "description": "Smallest positive integer not in array.",
        "description_full": "Given N and array A, print the smallest positive integer (>0) not present in array.",
        "input": "N\nA1 A2 ... AN",
        "output": "smallest missing",
        "example": "Input:\n3\n1 2 0\nOutput:\n3",
        "tests": [
            {"input": "3\n1 2 0", "output": "3"},
            {"input": "4\n2 3 4 5", "output": "1"},
            {"input": "5\n1 2 3 4 5", "output": "6"}
        ]
    },

    {
        "id": "m14",
        "title": "Count Inversions (brute-friendly)",
        "description": "Count pairs (i<j) where Ai>Aj.",
        "description_full": "Given N and array A (N ≤ ~2000), print inversion count. (OK to use O(N^2) for medium-level).",
        "input": "N\nA1 A2 ... AN",
        "output": "inversion count",
        "example": "Input:\n3\n3 2 1\nOutput:\n3",
        "tests": [
            {"input": "3\n3 2 1", "output": "3"},
            {"input": "4\n1 2 3 4", "output": "0"},
            {"input": "5\n2 1 3 1 2", "output": "5"}
        ]
    },

    {
        "id": "m15",
        "title": "Rotate Array by K",
        "description": "Rotate array right by K positions.",
        "description_full": "Given N and array A and K, rotate array to the right by K and print result.",
        "input": "N\nA1 A2 ... AN\nK",
        "output": "rotated array",
        "example": "Input:\n5\n1 2 3 4 5\n2\nOutput:\n4 5 1 2 3",
        "tests": [
            {"input": "5\n1 2 3 4 5\n2", "output": "4 5 1 2 3"},
            {"input": "3\n1 2 3\n3", "output": "1 2 3"},
            {"input": "4\n1 2 3 4\n1", "output": "4 1 2 3"}
        ]
    },

    {
        "id": "m16",
        "title": "Pair with Given Difference",
        "description": "Check if any pair has difference K.",
        "description_full": "Given N, array A and K, print YES if exists pair (i!=j) with |Ai-Aj|=K else NO.",
        "input": "N\nA1 A2 ... AN\nK",
        "output": "YES/NO",
        "example": "Input:\n5\n1 5 3 4 2\n3\nOutput:\nYES",
        "tests": [
            {"input": "5\n1 5 3 4 2\n3", "output": "YES"},
            {"input": "3\n1 2 4\n5", "output": "NO"},
            {"input": "4\n1 2 3 4\n1", "output": "YES"}
        ]
    },

    {
        "id": "m17",
        "title": "Count Subarrays with Sum Zero (small N)",
        "description": "Count subarrays whose sum equals zero.",
        "description_full": "Given N and array A (N smaller), print number of contiguous subarrays with sum 0.",
        "input": "N\nA1 A2 ... AN",
        "output": "count",
        "example": "Input:\n5\n0 0 0 0 0\nOutput:\n15",
        "tests": [
            {"input": "3\n1 -1 0", "output": "3"},
            {"input": "4\n0 0 0 0", "output": "10"},
            {"input": "5\n1 2 -3 3 -3", "output": "4"}
        ]
    },

    {
        "id": "m18",
        "title": "Longest Increasing Subarray (contiguous)",
        "description": "Length of longest strictly increasing contiguous subarray.",
        "description_full": "Given N and array A, print length of the longest strictly increasing contiguous subarray.",
        "input": "N\nA1 A2 ... AN",
        "output": "length",
        "example": "Input:\n6\n1 2 2 3 4 1\nOutput:\n3",
        "tests": [
            {"input": "5\n1 2 3 4 5", "output": "5"},
            {"input": "6\n1 2 2 3 4 1", "output": "3"},
            {"input": "3\n3 2 1", "output": "1"}
        ]
    },

    {
        "id": "m19",
        "title": "Count Distinct Pairs with Sum K",
        "description": "Count unique unordered pairs summing to K.",
        "description_full": "Given N and array A and K, count distinct unordered pairs (values) whose sum is K.",
        "input": "N\nA1 A2 ... AN\nK",
        "output": "count",
        "example": "Input:\n5\n1 5 7 -1 5\n6\nOutput:\n2",
        "tests": [
            {"input": "4\n1 5 1 5\n6", "output": "1"},
            {"input": "5\n1 5 7 -1 5\n6", "output": "2"},
            {"input": "3\n1 2 3\n5", "output": "1"}
        ]
    },

    {
        "id": "m20",
        "title": "Rotate Matrix 90 (conceptual) — simplified",
        "description": "Transpose and reverse rows for square matrix.",
        "description_full": "Given N and N×N matrix in single-line format (rows concatenated), rotate 90 degrees clockwise and print resulting matrix rows each on single line separated by spaces. (Input arranged as N then N*N numbers).",
        "input": "N\nr11 r12 ... r1N r21 r22 ... r2N ... rN1 ... rNN",
        "output": "rotated matrix rows (each row on new line)",
        "example": "Input:\n2\n1 2 3 4\nOutput:\n3 1\n4 2",
        "tests": [
            {"input": "2\n1 2 3 4", "output": "3 1\n4 2"},
            {"input": "3\n1 2 3 4 5 6 7 8 9", "output": "7 4 1\n8 5 2\n9 6 3"},
            {"input": "1\n5", "output": "5"}
        ]
    },

    {
        "id": "m21",
        "title": "Row Sum of Matrix",
        "description": "Sum each row.",
        "description_full": "Given R C and matrix elements (R*C numbers), print row sums space-separated.",
        "input": "R C\nr11 r12 ... r1C r21 ... rRC ...",
        "output": "row sums",
        "example": "Input:\n2 2\n1 2 3 4\nOutput:\n3 7",
        "tests": [
            {"input": "2 2\n1 2 3 4", "output": "3 7"},
            {"input": "1 3\n5 5 5", "output": "15"},
            {"input": "3 1\n1 2 3", "output": "1 2 3"}
        ]
    },

    {
        "id": "m22",
        "title": "Column Sum of Matrix",
        "description": "Sum each column.",
        "description_full": "Given R C and matrix elements, print column sums space-separated.",
        "input": "R C\nelements...",
        "output": "column sums",
        "example": "Input:\n2 2\n1 2 3 4\nOutput:\n4 6",
        "tests": [
            {"input": "2 2\n1 2 3 4", "output": "4 6"},
            {"input": "3 1\n1 2 3", "output": "6"},
            {"input": "1 4\n1 2 3 4", "output": "1 2 3 4"}
        ]
    },

    {
        "id": "m23",
        "title": "Diagonal Sum (Square Matrix)",
        "description": "Sum main diagonal.",
        "description_full": "Given N and N×N matrix, print sum of main diagonal elements.",
        "input": "N\nN*N elements row-wise",
        "output": "sum",
        "example": "Input:\n3\n1 2 3 4 5 6 7 8 9\nOutput:\n15",
        "tests": [
            {"input": "3\n1 2 3 4 5 6 7 8 9", "output": "15"},
            {"input": "2\n1 2 3 4", "output": "5"},
            {"input": "1\n10", "output": "10"}
        ]
    },

    {
        "id": "m24",
        "title": "Binary to Decimal",
        "description": "Convert binary string to decimal.",
        "description_full": "Given binary string S (no spaces), print its decimal value.",
        "input": "S",
        "output": "decimal",
        "example": "Input:\n101\nOutput:\n5",
        "tests": [
            {"input": "101", "output": "5"},
            {"input": "0", "output": "0"},
            {"input": "1111", "output": "15"}
        ]
    },

    {
        "id": "m25",
        "title": "Decimal to Binary",
        "description": "Convert decimal to binary string.",
        "description_full": "Given non-negative integer N, print its binary representation without leading zeros (0 for zero).",
        "input": "N",
        "output": "binary string",
        "example": "Input:\n5\nOutput:\n101",
        "tests": [
            {"input": "5", "output": "101"},
            {"input": "0", "output": "0"},
            {"input": "10", "output": "1010"}
        ]
    },

    {
        "id": "m26",
        "title": "Count Set Bits",
        "description": "Count 1-bits in binary representation.",
        "description_full": "Given non-negative integer N, print count of set bits (1s).",
        "input": "N",
        "output": "count",
        "example": "Input:\n5\nOutput:\n2",
        "tests": [
            {"input": "5", "output": "2"},
            {"input": "0", "output": "0"},
            {"input": "15", "output": "4"}
        ]
    },

    {
        "id": "m27",
        "title": "Check Anagram",
        "description": "Determine if two strings are anagrams.",
        "description_full": "Given two strings S1 and S2 (no spaces), print YES if anagrams else NO.",
        "input": "S1 S2",
        "output": "YES/NO",
        "example": "Input:\nlisten silent\nOutput:\nYES",
        "tests": [
            {"input": "listen silent", "output": "YES"},
            {"input": "hello bellow", "output": "NO"},
            {"input": "abc cba", "output": "YES"}
        ]
    },

    {
        "id": "m28",
        "title": "First Non-Repeating Character",
        "description": "Find first character that appears once.",
        "description_full": "Given string S, print first non-repeating character or print -1 if none.",
        "input": "S",
        "output": "char or -1",
        "example": "Input:\nswiss\nOutput:\nw",
        "tests": [
            {"input": "swiss", "output": "w"},
            {"input": "aabb", "output": "-1"},
            {"input": "abcd", "output": "a"}
        ]
    },

    {
        "id": "m29",
        "title": "String Compression (counts)",
        "description": "Basic run-length encoding.",
        "description_full": "Given string S, compress consecutive repeated chars as char+count (omit count 1).",
        "input": "S",
        "output": "compressed string",
        "example": "Input:\naaaabbc\nOutput:\na4b2c",
        "tests": [
            {"input": "aaaabbc", "output": "a4b2c"},
            {"input": "abcd", "output": "abcd"},
            {"input": "xxxx", "output": "x4"}
        ]
    },

    {
        "id": "m30",
        "title": "Find All Duplicates (simple)",
        "description": "Return sorted unique values that appear more than once.",
        "description_full": "Given N and array A, print duplicates (values appearing >=2) sorted, space-separated or empty string if none.",
        "input": "N\nA1 A2 ... AN",
        "output": "duplicates sorted",
        "example": "Input:\n6\n1 2 2 3 3 4\nOutput:\n2 3",
        "tests": [
            {"input": "6\n1 2 2 3 3 4", "output": "2 3"},
            {"input": "3\n1 2 3", "output": ""},
            {"input": "5\n5 5 5 5 5", "output": "5"}
        ]
    },

    {
        "id": "m31",
        "title": "Find Missing Number (1..N)",
        "description": "Find single missing number from 1..N in array of size N-1.",
        "description_full": "Given N (the upper bound) and N-1 distinct numbers from 1..N, print the missing number.",
        "input": "N\nA1 A2 ... A{N-1}",
        "output": "missing",
        "example": "Input:\n5\n1 2 3 5\nOutput:\n4",
        "tests": [
            {"input": "5\n1 2 3 5", "output": "4"},
            {"input": "3\n1 3", "output": "2"},
            {"input": "4\n2 3 4", "output": "1"}
        ]
    },

    {
        "id": "m32",
        "title": "Find Pair with Given Product",
        "description": "Check if pair with product K exists.",
        "description_full": "Given N, array A and K, print YES if there exists i<j with Ai*Aj=K else NO.",
        "input": "N\nA1 A2 ... AN\nK",
        "output": "YES/NO",
        "example": "Input:\n4\n2 4 1 6\n8\nOutput:\nYES",
        "tests": [
            {"input": "4\n2 4 1 6\n8", "output": "YES"},
            {"input": "3\n2 3 5\n7", "output": "NO"},
            {"input": "3\n0 0 1\n0", "output": "YES"}
        ]
    },

    {
        "id": "m33",
        "title": "Count Occurrences of Substring",
        "description": "Count non-overlapping occurrences of sub in S.",
        "description_full": "Given S and substring sub, print count of non-overlapping occurrences of sub in S.",
        "input": "S sub",
        "output": "count",
        "example": "Input:\nabababa aba\nOutput:\n2",
        "tests": [
            {"input": "abababa aba", "output": "2"},
            {"input": "aaaa aa", "output": "2"},
            {"input": "hello ll", "output": "1"}
        ]
    },

    {
        "id": "m34",
        "title": "Rotate Array Left by K",
        "description": "Rotate array left by K positions.",
        "description_full": "Given N and array A and K, rotate left by K and print result.",
        "input": "N\nA1 A2 ... AN\nK",
        "output": "rotated array",
        "example": "Input:\n5\n1 2 3 4 5\n2\nOutput:\n3 4 5 1 2",
        "tests": [
            {"input": "5\n1 2 3 4 5\n2", "output": "3 4 5 1 2"},
            {"input": "3\n1 2 3\n3", "output": "1 2 3"},
            {"input": "4\n1 2 3 4\n1", "output": "2 3 4 1"}
        ]
    },

    {
        "id": "m35",
        "title": "Find Pair Sum Closest to K",
        "description": "Find pair whose sum is closest to K; print their values (smaller first).",
        "description_full": "Given N and array A and integer K, find pair Ai,Aj (i!=j) with minimal |Ai+Aj-K| and print Ai Aj (values). If multiple pairs, print any.",
        "input": "N\nA1 A2 ... AN\nK",
        "output": "Ai Aj",
        "example": "Input:\n4\n1 3 4 7\n10\nOutput:\n3 7",
        "tests": [
            {"input": "4\n1 3 4 7\n10", "output": "3 7"},
            {"input": "3\n-1 2 1\n0", "output": "-1 1"},
            {"input": "4\n1 2 3 4\n5", "output": "1 4"}
        ]
    },

    {
        "id": "m36",
        "title": "Count Pairs with Difference K (unique values)",
        "description": "Count unique pairs (a,b) with b-a = K.",
        "description_full": "Given N and array A and integer K>=0, count unique pairs of values (x,y) such that y-x=K and both present.",
        "input": "N\nA1 A2 ... AN\nK",
        "output": "count",
        "example": "Input:\n5\n1 5 3 4 2\n2\nOutput:\n3",
        "tests": [
            {"input": "5\n1 5 3 4 2\n2", "output": "3"},
            {"input": "4\n1 1 2 2\n0", "output": "2"},
            {"input": "3\n1 2 3\n10", "output": "0"}
        ]
    },

    {
        "id": "m37",
        "title": "Longest Common Prefix",
        "description": "Find LCP of an array of strings.",
        "description_full": "Given N and N strings, print the longest common prefix (or empty string if none).",
        "input": "N\nS1 S2 ... SN",
        "output": "prefix",
        "example": "Input:\n3\nflower flow flight\nOutput:\nfl",
        "tests": [
            {"input": "3\nflower flow flight", "output": "fl"},
            {"input": "2\ndog racecar", "output": ""},
            {"input": "3\nabc abc abc", "output": "abc"}
        ]
    },

    {
        "id": "m38",
        "title": "Count Subarrays with Given Sum (positive nums)",
        "description": "Count subarrays with sum K when elements non-negative.",
        "description_full": "Given N and array A (non-negative) and K, print number of contiguous subarrays summing to K.",
        "input": "N\nA1 A2 ... AN\nK",
        "output": "count",
        "example": "Input:\n5\n1 1 1 1 1\n2\nOutput:\n4",
        "tests": [
            {"input": "5\n1 1 1 1 1\n2", "output": "4"},
            {"input": "4\n0 0 0 0\n0", "output": "10"},
            {"input": "3\n1 2 3\n3", "output": "2"}
        ]
    },

    {
        "id": "m39",
        "title": "Maximum Product Subarray (small)",
        "description": "Max product of contiguous subarray (small constraints).",
        "description_full": "Given N and array A, print maximum product possible from a contiguous non-empty subarray. (Careful with negatives).",
        "input": "N\nA1 A2 ... AN",
        "output": "max product",
        "example": "Input:\n3\n-2 0 -1\nOutput:\n0",
        "tests": [
            {"input": "3\n-2 0 -1", "output": "0"},
            {"input": "4\n-2 3 -4 2", "output": "24"},
            {"input": "3\n2 3 -2", "output": "6"}
        ]
    },

    {
        "id": "m40",
        "title": "Smallest Subarray with Given Sum >= S",
        "description": "Minimum length subarray with sum at least S.",
        "description_full": "Given N and array A (positive integers) and S, print minimal length of contiguous subarray with sum >= S else 0 if none.",
        "input": "N\nA1 A2 ... AN\nS",
        "output": "length or 0",
        "example": "Input:\n6\n2 3 1 2 4 3\n7\nOutput:\n2",
        "tests": [
            {"input": "6\n2 3 1 2 4 3\n7", "output": "2"},
            {"input": "3\n1 1 1\n5", "output": "0"},
            {"input": "4\n1 4 4 2\n4", "output": "1"}
        ]
    },

    {
        "id": "m41",
        "title": "Check Rotation (string)",
        "description": "Check if s2 is rotation of s1.",
        "description_full": "Given two strings s1 and s2, print YES if s2 is rotation of s1 else NO.",
        "input": "s1 s2",
        "output": "YES/NO",
        "example": "Input:\nabcd cdab\nOutput:\nYES",
        "tests": [
            {"input": "abcd cdab", "output": "YES"},
            {"input": "abc def", "output": "NO"},
            {"input": "aa bb", "output": "NO"}
        ]
    },

    {
        "id": "m42",
        "title": "Remove Adjacent Duplicates (string)",
        "description": "Remove adjacent duplicate characters until none remain.",
        "description_full": "Given string S, iteratively remove adjacent equal characters and print the final string (or empty).",
        "input": "S",
        "output": "final string",
        "example": "Input:\nabbaca\nOutput:\nca",
        "tests": [
            {"input": "abbaca", "output": "ca"},
            {"input": "azxxzy", "output": "ay"},
            {"input": "aabb", "output": ""}
        ]
    },

    {
        "id": "m43",
        "title": "Count Unique Prime Factors (small)",
        "description": "Count distinct prime factors of N.",
        "description_full": "Given integer N (N<= 10^9 small), print count of distinct prime factors.",
        "input": "N",
        "output": "count",
        "example": "Input:\n12\nOutput:\n2",
        "tests": [
            {"input": "12", "output": "2"},
            {"input": "13", "output": "1"},
            {"input": "1", "output": "0"}
        ]
    },

    {
        "id": "m44",
        "title": "Power of Two Check",
        "description": "Check if N is power of two.",
        "description_full": "Given positive integer N, print YES if N is power of two else NO.",
        "input": "N",
        "output": "YES/NO",
        "example": "Input:\n8\nOutput:\nYES",
        "tests": [
            {"input": "8", "output": "YES"},
            {"input": "0", "output": "NO"},
            {"input": "6", "output": "NO"}
        ]
    },

    {
        "id": "m45",
        "title": "Sum of Digits Until Single Digit",
        "description": "Repeatedly sum digits until one digit remains.",
        "description_full": "Given N (non-negative), repeatedly sum its digits until result is single digit and print it.",
        "input": "N",
        "output": "single digit",
        "example": "Input:\n9875\nOutput:\n2",
        "tests": [
            {"input": "9875", "output": "2"},
            {"input": "0", "output": "0"},
            {"input": "999", "output": "9"}
        ]
    },

    {
        "id": "m46",
        "title": "Find Longest Palindromic Prefix",
        "description": "Longest prefix of S which is palindrome.",
        "description_full": "Given string S, print the longest prefix that is also a palindrome.",
        "input": "S",
        "output": "prefix",
        "example": "Input:\nababab\nOutput:\na",
        "tests": [
            {"input": "abaXYZ", "output": "aba"},
            {"input": "abcd", "output": "a"},
            {"input": "aaab", "output": "aaa"}
        ]
    },

    {
        "id": "m47",
        "title": "Find Two Missing Numbers (1..N+2)",
        "description": "Given array of size N containing distinct numbers from 1..N+2 with two missing, print the missing numbers sorted.",
        "description_full": "Given N and N numbers from the range 1..N+2, find the two missing numbers and print them in increasing order.",
        "input": "N\nA1 A2 ... AN",
        "output": "x y",
        "example": "Input:\n3\n1 4 3\nOutput:\n2 5",
        "tests": [
            {"input": "3\n1 4 3", "output": "2 5"},
            {"input": "1\n2", "output": "1 3"},
            {"input": "4\n1 2 4 5", "output": "3 6"}
        ]
    },

    {
        "id": "m48",
        "title": "Check if Array is Rotation of Another",
        "description": "Check if B is rotation of A.",
        "description_full": "Given N, array A and array B, print YES if B is rotation of A else NO.",
        "input": "N\nA1 ... AN\nB1 ... BN",
        "output": "YES/NO",
        "example": "Input:\n4\n1 2 3 4\n3 4 1 2\nOutput:\nYES",
        "tests": [
            {"input": "4\n1 2 3 4\n3 4 1 2", "output": "YES"},
            {"input": "3\n1 2 3\n2 1 3", "output": "NO"},
            {"input": "1\n5\n5", "output": "YES"}
        ]
    },

    {
        "id": "m49",
        "title": "Rearrange Array Alternating Positives and Negatives (relative order not required)",
        "description": "Arrange positives and negatives alternately if possible, otherwise print arranged sequence with remaining at end.",
        "description_full": "Given N and array A, rearrange so that positives and negatives alternate (starting with positive if exists). Order need not be preserved. Print resulting array.",
        "input": "N\nA1 A2 ... AN",
        "output": "rearranged array",
        "example": "Input:\n6\n1 2 -3 -4 5 -6\nOutput:\n1 -3 2 -4 5 -6",
        "tests": [
            {"input": "6\n1 2 -3 -4 5 -6", "output": "1 -3 2 -4 5 -6"},
            {"input": "3\n-1 -2 3", "output": "3 -1 -2"},
            {"input": "4\n1 2 3 4", "output": "1 2 3 4"}
        ]
    },

    {
        "id": "m50",
        "title": "Longest Substring Without Repeating Characters (length)",
        "description": "Length of longest substring with all distinct characters.",
        "description_full": "Given string S, print length of the longest substring without repeating characters.",
        "input": "S",
        "output": "length",
        "example": "Input:\nabcabcbb\nOutput:\n3",
        "tests": [
            {"input": "abcabcbb", "output": "3"},
            {"input": "bbbbb", "output": "1"},
            {"input": "pwwkew", "output": "3"}
        ]
    }

]
}
