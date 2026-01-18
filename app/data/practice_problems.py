PRACTICE_PROBLEMS = {
    "Very Easy": {
        "Loops": [ {
            "id": "print_numbers_1_to_n",
            "title": "Print Numbers 1 to N",
            "topic": "Loops",
            "description": "Print numbers from 1 to N.",
            "description_full": "Given an integer N, print numbers from 1 to N separated by spaces.",
            "input": "Integer N",
            "output": "Numbers from 1 to N",
            "example": "Input:\n5\nOutput:\n1 2 3 4 5",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5", "output": "1 2 3 4 5"},
                {"input": "1", "output": "1"},
                {"input": "3", "output": "1 2 3"}
            ]
        },
        {
            "id": "print_reverse_n_to_1",
            "title": "Print N to 1",
            "topic": "Loops",
            "description": "Print numbers from N to 1.",
            "description_full": "Given N, print numbers from N down to 1 separated by spaces.",
            "input": "Integer N",
            "output": "Numbers from N to 1",
            "example": "Input:\n4\nOutput:\n4 3 2 1",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "4", "output": "4 3 2 1"},
                {"input": "1", "output": "1"},
                {"input": "3", "output": "3 2 1"}
            ]
        },
        {
            "id": "sum_first_n_numbers",
            "title": "Sum of First N Numbers",
            "topic": "Loops",
            "description": "Sum numbers from 1 to N.",
            "description_full": "Given N, compute the sum 1+2+...+N.",
            "input": "Integer N",
            "output": "Sum",
            "example": "Input:\n5\nOutput:\n15",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5", "output": "15"},
                {"input": "1", "output": "1"},
                {"input": "3", "output": "6"}
            ]
        },
        {
            "id": "count_even_1_to_n",
            "title": "Count Even Numbers 1..N",
            "topic": "Loops",
            "description": "Count evens between 1 and N.",
            "description_full": "Given N, count numbers in [1,N] that are even.",
            "input": "Integer N",
            "output": "Count",
            "example": "Input:\n10\nOutput:\n5",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "10", "output": "5"},
                {"input": "1", "output": "0"},
                {"input": "6", "output": "3"}
            ]
        },
        {
            "id": "print_even_numbers",
            "title": "Print Even Numbers Up to N",
            "topic": "Loops",
            "description": "Print even numbers ≤ N.",
            "description_full": "Given N, print all even numbers from 1 to N separated by spaces. If none, print an empty line.",
            "input": "Integer N",
            "output": "Even numbers",
            "example": "Input:\n6\nOutput:\n2 4 6",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "6", "output": "2 4 6"},
                {"input": "2", "output": "2"},
                {"input": "1", "output": ""}
            ]
        },
        {
            "id": "count_odd_1_to_n",
            "title": "Count Odd Numbers 1..N",
            "topic": "Loops",
            "description": "Count odd numbers between 1 and N.",
            "description_full": "Given N, count numbers in [1,N] that are odd.",
            "input": "Integer N",
            "output": "Count",
            "example": "Input:\n7\nOutput:\n4",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "7", "output": "4"},
                {"input": "1", "output": "1"},
                {"input": "8", "output": "4"}
            ]
        },
        {
            "id": "print_odd_numbers",
            "title": "Print Odd Numbers Up to N",
            "topic": "Loops",
            "description": "Print odd numbers ≤ N.",
            "description_full": "Given N, print all odd numbers from 1 to N separated by spaces. If none, print an empty line.",
            "input": "Integer N",
            "output": "Odd numbers",
            "example": "Input:\n7\nOutput:\n1 3 5 7",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "7", "output": "1 3 5 7"},
                {"input": "1", "output": "1"},
                {"input": "2", "output": "1"}
            ]
        },
        {
            "id": "multiplication_table_1_to_10",
            "title": "Multiplication Table 1..10",
            "topic": "Loops",
            "description": "Print multiplication table of N from 1 to 10.",
            "description_full": "Given N, print N*1 N*2 ... N*10 separated by spaces.",
            "input": "Integer N",
            "output": "10 space-separated numbers",
            "example": "Input:\n2\nOutput:\n2 4 6 8 10 12 14 16 18 20",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "2", "output": "2 4 6 8 10 12 14 16 18 20"},
                {"input": "1", "output": "1 2 3 4 5 6 7 8 9 10"},
                {"input": "5", "output": "5 10 15 20 25 30 35 40 45 50"}
            ]
        },
        {
            "id": "sum_of_digits_loop",
            "title": "Sum of Digits (Loop)",
            "topic": "Loops",
            "description": "Sum digits of a non-negative integer.",
            "description_full": "Given N, compute sum of its decimal digits using loops.",
            "input": "Integer N",
            "output": "Sum of digits",
            "example": "Input:\n1234\nOutput:\n10",
            "constraints": "N >= 0",
            "explanation": "",
            "tests": [
                {"input": "1234", "output": "10"},
                {"input": "9", "output": "9"},
                {"input": "1001", "output": "2"}
            ]
        },
        {
            "id": "count_digits_loop",
            "title": "Count Digits (Loop)",
            "topic": "Loops",
            "description": "Count number of digits of N.",
            "description_full": "Given N ≥ 0, print the number of decimal digits in N.",
            "input": "Integer N",
            "output": "Digit count",
            "example": "Input:\n12345\nOutput:\n5",
            "constraints": "N >= 0",
            "explanation": "",
            "tests": [
                {"input": "12345", "output": "5"},
                {"input": "9", "output": "1"},
                {"input": "1000", "output": "4"}
            ]
        }],
        "Conditionals": [{
            "id": "max_of_two",
            "title": "Maximum of Two Numbers",
            "topic": "Conditionals",
            "description": "Print the larger of two integers.",
            "description_full": "Given two integers A and B, print the maximum of A and B. If equal, print either.",
            "input": "Two integers A B",
            "output": "Maximum value",
            "example": "Input:\n3 5\nOutput:\n5",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "3 5", "output": "5"},
                {"input": "7 2", "output": "7"},
                {"input": "4 4", "output": "4"}
            ]
        },
        {
            "id": "is_even",
            "title": "Check Even",
            "topic": "Conditionals",
            "description": "Check if integer is even.",
            "description_full": "Given N, print YES if N is even, otherwise NO.",
            "input": "Integer N",
            "output": "YES or NO",
            "example": "Input:\n4\nOutput:\nYES",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "4", "output": "YES"},
                {"input": "7", "output": "NO"},
                {"input": "0", "output": "YES"}
            ]
        },
        {
            "id": "sign_of_number",
            "title": "Sign of Number",
            "topic": "Conditionals",
            "description": "Find sign of a number.",
            "description_full": "Given integer N, print POSITIVE, NEGATIVE, or ZERO.",
            "input": "Integer N",
            "output": "POSITIVE / NEGATIVE / ZERO",
            "example": "Input:\n0\nOutput:\nZERO",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5", "output": "POSITIVE"},
                {"input": "-3", "output": "NEGATIVE"},
                {"input": "0", "output": "ZERO"}
            ]
        },
        {
            "id": "is_vowel",
            "title": "Check Vowel",
            "topic": "Conditionals",
            "description": "Check if a character is a vowel.",
            "description_full": "Given single letter C, print YES if vowel (a,e,i,o,u case-insensitive) else NO.",
            "input": "Single character C",
            "output": "YES or NO",
            "example": "Input:\na\nOutput:\nYES",
            "constraints": "C is alphabetic",
            "explanation": "",
            "tests": [
                {"input": "a", "output": "YES"},
                {"input": "B", "output": "NO"},
                {"input": "U", "output": "YES"}
            ]
        },
        {
            "id": "is_palindrome_number",
            "title": "Is Palindrome Number",
            "topic": "Conditionals",
            "description": "Check if number reads same backwards.",
            "description_full": "Given non-negative integer N, print YES if its decimal representation is palindrome else NO.",
            "input": "Integer N",
            "output": "YES or NO",
            "example": "Input:\n121\nOutput:\nYES",
            "constraints": "N >= 0",
            "explanation": "",
            "tests": [
                {"input": "121", "output": "YES"},
                {"input": "123", "output": "NO"},
                {"input": "7", "output": "YES"}
            ]
        },
        {
            "id": "leap_year",
            "title": "Leap Year Check",
            "topic": "Conditionals",
            "description": "Check if year is leap year.",
            "description_full": "Given year Y, print YES if leap year (Gregorian rules) else NO.",
            "input": "Integer Y",
            "output": "YES or NO",
            "example": "Input:\n2000\nOutput:\nYES",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "2000", "output": "YES"},
                {"input": "1900", "output": "NO"},
                {"input": "2024", "output": "YES"}
            ]
        },
        {
            "id": "grade_from_marks",
            "title": "Grade from Marks",
            "topic": "Conditionals",
            "description": "Map marks to grade.",
            "description_full": "Given integer marks 0-100, print grade: A (>=90), B (>=75), C (>=60), D (>=50), F otherwise.",
            "input": "Integer marks",
            "output": "Grade letter",
            "example": "Input:\n82\nOutput:\nB",
            "constraints": "0 <= marks <= 100",
            "explanation": "",
            "tests": [
                {"input": "95", "output": "A"},
                {"input": "60", "output": "C"},
                {"input": "49", "output": "F"}
            ]
        },
        {
            "id": "is_three_digit",
            "title": "Is Three Digit Number",
            "topic": "Conditionals",
            "description": "Check if absolute value has 3 digits.",
            "description_full": "Given integer N, print YES if |N| has exactly 3 digits else NO.",
            "input": "Integer N",
            "output": "YES or NO",
            "example": "Input:\n-123\nOutput:\nYES",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "123", "output": "YES"},
                {"input": "99", "output": "NO"},
                {"input": "-100", "output": "YES"}
            ]
        },
        {
            "id": "max_of_three",
            "title": "Maximum of Three Numbers",
            "topic": "Conditionals",
            "description": "Find maximum among three integers.",
            "description_full": "Given three integers A B C, print the maximum.",
            "input": "Three integers A B C",
            "output": "Maximum",
            "example": "Input:\n3 7 5\nOutput:\n7",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "3 7 5", "output": "7"},
                {"input": "9 9 2", "output": "9"},
                {"input": "-1 -5 -2", "output": "-1"}
            ]
        }],
        "Basic Math": [ {
            "id": "gcd_two_numbers",
            "title": "GCD of Two Numbers",
            "topic": "Basic Math",
            "description": "Compute GCD of A and B.",
            "description_full": "Given two positive integers A and B, print gcd(A,B).",
            "input": "Two integers A B",
            "output": "GCD value",
            "example": "Input:\n12 8\nOutput:\n4",
            "constraints": "A,B >= 0",
            "explanation": "",
            "tests": [
                {"input": "12 8", "output": "4"},
                {"input": "100 25", "output": "25"},
                {"input": "7 13", "output": "1"}
            ]
        },
        {
            "id": "lcm_two_numbers",
            "title": "LCM of Two Numbers",
            "topic": "Basic Math",
            "description": "Compute LCM of A and B.",
            "description_full": "Given positive integers A and B, print lcm(A,B).",
            "input": "Two integers A B",
            "output": "LCM value",
            "example": "Input:\n4 6\nOutput:\n12",
            "constraints": "A,B > 0",
            "explanation": "",
            "tests": [
                {"input": "4 6", "output": "12"},
                {"input": "5 5", "output": "5"},
                {"input": "3 7", "output": "21"}
            ]
        },
        {
            "id": "is_power_of_two",
            "title": "Is Power of Two",
            "topic": "Basic Math",
            "description": "Check whether N is a power of two.",
            "description_full": "Given N>0, print YES if N is power of two else NO.",
            "input": "Integer N",
            "output": "YES or NO",
            "example": "Input:\n8\nOutput:\nYES",
            "constraints": "N > 0",
            "explanation": "",
            "tests": [
                {"input": "8", "output": "YES"},
                {"input": "6", "output": "NO"},
                {"input": "1", "output": "YES"}
            ]
        },
        {
            "id": "sum_of_digits",
            "title": "Sum of Digits",
            "topic": "Basic Math",
            "description": "Compute sum of digits of N.",
            "description_full": "Given non-negative integer N, print sum of its digits.",
            "input": "Integer N",
            "output": "Sum",
            "example": "Input:\n305\nOutput:\n8",
            "constraints": "N >= 0",
            "explanation": "",
            "tests": [
                {"input": "305", "output": "8"},
                {"input": "0", "output": "0"},
                {"input": "999", "output": "27"}
            ]
        },
        {
            "id": "count_set_bits",
            "title": "Count Set Bits",
            "topic": "Basic Math",
            "description": "Count number of 1-bits in binary representation.",
            "description_full": "Given non-negative integer N, print count of 1s in its binary form.",
            "input": "Integer N",
            "output": "Count",
            "example": "Input:\n5\nOutput:\n2",
            "constraints": "N >= 0",
            "explanation": "",
            "tests": [
                {"input": "5", "output": "2"},
                {"input": "0", "output": "0"},
                {"input": "1023", "output": "10"}
            ]
        },
        {
            "id": "is_prime_small",
            "title": "Is Prime (Small N)",
            "topic": "Basic Math",
            "description": "Check primality of N (small).",
            "description_full": "Given N (<=10^6), print YES if prime else NO.",
            "input": "Integer N",
            "output": "YES or NO",
            "example": "Input:\n7\nOutput:\nYES",
            "constraints": "N <= 1e6",
            "explanation": "",
            "tests": [
                {"input": "7", "output": "YES"},
                {"input": "1", "output": "NO"},
                {"input": "12", "output": "NO"}
            ]
        },
        {
            "id": "sum_of_proper_divisors",
            "title": "Sum of Proper Divisors",
            "topic": "Basic Math",
            "description": "Sum all proper divisors of N (excluding N).",
            "description_full": "Given N, print sum of its proper divisors.",
            "input": "Integer N",
            "output": "Sum",
            "example": "Input:\n6\nOutput:\n6",
            "constraints": "N >= 1",
            "explanation": "",
            "tests": [
                {"input": "6", "output": "6"},
                {"input": "5", "output": "1"},
                {"input": "1", "output": "0"}
            ]
        },
        {
            "id": "reverse_integer_digits",
            "title": "Reverse Integer Digits",
            "topic": "Basic Math",
            "description": "Reverse decimal digits of N.",
            "description_full": "Given integer N (non-negative), print the integer formed by reversing its digits (no leading zeros).",
            "input": "Integer N",
            "output": "Reversed integer",
            "example": "Input:\n1200\nOutput:\n21",
            "constraints": "N >= 0",
            "explanation": "",
            "tests": [
                {"input": "1200", "output": "21"},
                {"input": "987", "output": "789"},
                {"input": "0", "output": "0"}
            ]
        },
        {
            "id": "sum_of_odd_numbers_1_to_n",
            "title": "Sum of Odd Numbers up to N",
            "topic": "Basic Math",
            "description": "Sum odd integers ≤ N.",
            "description_full": "Given N, compute sum of all odd integers from 1 to N.",
            "input": "Integer N",
            "output": "Sum",
            "example": "Input:\n6\nOutput:\n9",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "6", "output": "9"},
                {"input": "1", "output": "1"},
                {"input": "10", "output": "25"}
            ]
        }],
        "Strings": [{
            "id": "count_vowels",
            "title": "Count Vowels",
            "topic": "Strings",
            "description": "Count vowels in a string.",
            "description_full": "Given a string S, count vowels (a,e,i,o,u) case-insensitive.",
            "input": "String S",
            "output": "Number of vowels",
            "example": "Input:\napple\nOutput:\n2",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "apple", "output": "2"},
                {"input": "AEIOU", "output": "5"},
                {"input": "xyz", "output": "0"}
            ]
        },
        {
            "id": "reverse_string",
            "title": "Reverse String",
            "topic": "Strings",
            "description": "Reverse the input string.",
            "description_full": "Given string S, print S reversed.",
            "input": "String S",
            "output": "Reversed string",
            "example": "Input:\nhello\nOutput:\nolleh",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "hello", "output": "olleh"},
                {"input": "a", "output": "a"},
                {"input": "abc", "output": "cba"}
            ]
        },
        {
            "id": "swap_case_string",
            "title": "Swap Case",
            "topic": "Strings",
            "description": "Swap uppercase/lowercase letters.",
            "description_full": "Given S, swap case of all alphabetic characters.",
            "input": "String S",
            "output": "Case-swapped string",
            "example": "Input:\nHello\nOutput:\nhELLO",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "Hello", "output": "hELLO"},
                {"input": "aBc123", "output": "AbC123"},
                {"input": "ABC", "output": "abc"}
            ]
        },
        {
            "id": "remove_vowels",
            "title": "Remove Vowels",
            "topic": "Strings",
            "description": "Remove vowels from string.",
            "description_full": "Given S, remove all vowels (a,e,i,o,u both cases) and print rest.",
            "input": "String S",
            "output": "String without vowels",
            "example": "Input:\napple\nOutput:\nppl",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "apple", "output": "ppl"},
                {"input": "AEIOU", "output": ""},
                {"input": "Banana", "output": "Bnn"}
            ]
        },
        {
            "id": "count_words_in_sentence",
            "title": "Count Words",
            "topic": "Strings",
            "description": "Count words separated by spaces.",
            "description_full": "Given a sentence S, count words separated by single spaces (trim edges).",
            "input": "String S",
            "output": "Word count",
            "example": "Input:\nI love coding\nOutput:\n3",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "I love coding", "output": "3"},
                {"input": "Hello World", "output": "2"},
                {"input": "one", "output": "1"}
            ]
        },
        {
            "id": "string_palindrome_check",
            "title": "String Palindrome",
            "topic": "Strings",
            "description": "Check if a string is palindrome.",
            "description_full": "Given S, print YES if S reads same backwards else NO (case-sensitive).",
            "input": "String S",
            "output": "YES or NO",
            "example": "Input:\nlevel\nOutput:\nYES",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "level", "output": "YES"},
                {"input": "Hello", "output": "NO"},
                {"input": "a", "output": "YES"}
            ]
        },
        {
            "id": "first_char_frequency",
            "title": "First Character Frequency",
            "topic": "Strings",
            "description": "Count occurrences of first character in string.",
            "description_full": "Given S (non-empty), print how many times S[0] appears in S.",
            "input": "String S",
            "output": "Count",
            "example": "Input:\nbanana\nOutput:\n3",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "banana", "output": "3"},
                {"input": "abc", "output": "1"},
                {"input": "aaaa", "output": "4"}
            ]
        },
        {
            "id": "remove_spaces",
            "title": "Remove Spaces",
            "topic": "Strings",
            "description": "Remove all spaces from string.",
            "description_full": "Given S, remove all space characters and print result.",
            "input": "String S",
            "output": "String without spaces",
            "example": "Input:\nHello World\nOutput:\nHelloWorld",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "Hello World", "output": "HelloWorld"},
                {"input": " a b ", "output": "ab"},
                {"input": "x", "output": "x"}
            ]
        },
        {
            "id": "concat_two_strings",
            "title": "Concatenate Two Strings",
            "topic": "Strings",
            "description": "Concatenate A and B with a space.",
            "description_full": "Given two strings A and B, print A + ' ' + B.",
            "input": "Two strings A B (space separated)",
            "output": "Concatenated string",
            "example": "Input:\nhello world\nOutput:\nhello world",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "hello world", "output": "hello world"},
                {"input": "a b", "output": "a b"},
                {"input": "foo bar", "output": "foo bar"}
            ]
        }],
        "Arrays": [{
            "id": "sum_of_array",
            "title": "Sum of Array",
            "topic": "Arrays",
            "description": "Sum N integers.",
            "description_full": "Given N and N integers, print their sum.",
            "input": "N then N integers",
            "output": "Sum",
            "example": "Input:\n5\n1 2 3 4 5\nOutput:\n15",
            "constraints": "1 <= N <= 1e5",
            "explanation": "",
            "tests": [
                {"input": "5\n1 2 3 4 5", "output": "15"},
                {"input": "3\n1 1 1", "output": "3"},
                {"input": "1\n99", "output": "99"}
            ]
        },
        {
            "id": "max_element",
            "title": "Maximum Element",
            "topic": "Arrays",
            "description": "Find maximum in the array.",
            "description_full": "Given N and array A, print maximum element.",
            "input": "N then N integers",
            "output": "Maximum value",
            "example": "Input:\n4\n1 3 2 5\nOutput:\n5",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "4\n1 3 2 5", "output": "5"},
                {"input": "3\n-1 -2 -3", "output": "-1"},
                {"input": "1\n100", "output": "100"}
            ]
        },
        {
            "id": "min_element",
            "title": "Minimum Element",
            "topic": "Arrays",
            "description": "Find minimum in the array.",
            "description_full": "Given N and array A, print minimum element.",
            "input": "N then N integers",
            "output": "Minimum value",
            "example": "Input:\n4\n1 3 2 5\nOutput:\n1",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "4\n1 3 2 5", "output": "1"},
                {"input": "3\n-1 -2 -3", "output": "-3"},
                {"input": "1\n100", "output": "100"}
            ]
        },
        {
            "id": "second_largest_element",
            "title": "Second Largest Element",
            "topic": "Arrays",
            "description": "Find 2nd largest distinct element.",
            "description_full": "Given N and array A, print second largest distinct integer or -1 if none.",
            "input": "N then N integers",
            "output": "Second largest or -1",
            "example": "Input:\n5\n1 2 3 4 5\nOutput:\n4",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5\n1 2 3 4 5", "output": "4"},
                {"input": "3\n10 10 10", "output": "-1"},
                {"input": "4\n5 1 5 3", "output": "3"}
            ]
        },
        {
            "id": "count_occurrences",
            "title": "Count Occurrences",
            "topic": "Arrays",
            "description": "Count occurrences of X in array.",
            "description_full": "Given N, array A and X, print frequency of X in A.",
            "input": "N then N integers then X",
            "output": "Frequency",
            "example": "Input:\n5\n1 2 2 3 2\n2\nOutput:\n3",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5\n1 2 2 3 2\n2", "output": "3"},
                {"input": "3\n1 1 1\n2", "output": "0"},
                {"input": "1\n5\n5", "output": "1"}
            ]
        },
        {
            "id": "reverse_array",
            "title": "Reverse Array",
            "topic": "Arrays",
            "description": "Reverse order of elements.",
            "description_full": "Given N and array A, print elements in reverse order.",
            "input": "N then N integers",
            "output": "Reversed array",
            "example": "Input:\n4\n1 2 3 4\nOutput:\n4 3 2 1",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "4\n1 2 3 4", "output": "4 3 2 1"},
                {"input": "1\n7", "output": "7"},
                {"input": "3\n5 5 5", "output": "5 5 5"}
            ]
        },
        {
            "id": "sum_prefixes",
            "title": "Sum of Prefixes",
            "topic": "Arrays",
            "description": "Print cumulative prefix sums.",
            "description_full": "Given N and array A, print prefix sums for each i.",
            "input": "N then N integers",
            "output": "N numbers (prefix sums)",
            "example": "Input:\n4\n1 2 3 4\nOutput:\n1 3 6 10",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "4\n1 2 3 4", "output": "1 3 6 10"},
                {"input": "3\n5 -1 2", "output": "5 4 6"},
                {"input": "1\n7", "output": "7"}
            ]
        },
        {
            "id": "rotate_array_left_once",
            "title": "Rotate Array Left by 1",
            "topic": "Arrays",
            "description": "Rotate array left by one position.",
            "description_full": "Given N and array A, rotate left by 1 and print result.",
            "input": "N then N integers",
            "output": "Rotated array",
            "example": "Input:\n5\n1 2 3 4 5\nOutput:\n2 3 4 5 1",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5\n1 2 3 4 5", "output": "2 3 4 5 1"},
                {"input": "3\n10 20 30", "output": "20 30 10"},
                {"input": "1\n7", "output": "7"}
            ]
        },
        {
            "id": "find_first_negative",
            "title": "Find First Negative",
            "topic": "Arrays",
            "description": "Return index of first negative number or -1.",
            "description_full": "Given N and array A, print 0-based index of first negative element or -1 if none.",
            "input": "N then N integers",
            "output": "Index or -1",
            "example": "Input:\n4\n1 -2 3 -4\nOutput:\n1",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "4\n1 -2 3 -4", "output": "1"},
                {"input": "3\n1 2 3", "output": "-1"},
                {"input": "1\n-5", "output": "0"}
            ]}],
        "Patterns": [{
            "id": "print_square_star_n",
            "title": "Square of Stars",
            "topic": "Patterns",
            "description": "Print NxN square of '*' characters.",
            "description_full": "Given N, print N lines each with N asterisks separated by no space.",
            "input": "Integer N",
            "output": "N lines",
            "example": "Input:\n3\nOutput:\n***\n***\n***",
            "constraints": "N>0",
            "explanation": "",
            "tests": [
                {"input": "3", "output": "***\n***\n***"},
                {"input": "1", "output": "*"},
                {"input": "2", "output": "**\n**"}
            ]
        },
        {
            "id": "print_right_triangle",
            "title": "Right Triangle Stars",
            "topic": "Patterns",
            "description": "Print right-angled triangle of stars.",
            "description_full": "Given N, print 1..N stars per line forming a right triangle.",
            "input": "Integer N",
            "output": "N lines",
            "example": "Input:\n3\nOutput:\n*\n**\n***",
            "constraints": "N>0",
            "explanation": "",
            "tests": [
                {"input": "3", "output": "*\n**\n***"},
                {"input": "1", "output": "*"},
                {"input": "2", "output": "*\n**"}
            ]
        },
        {
            "id": "print_number_triangle",
            "title": "Number Triangle",
            "topic": "Patterns",
            "description": "Print increasing numbers per line.",
            "description_full": "Given N, print line i containing numbers 1..i separated by spaces.",
            "input": "Integer N",
            "output": "N lines",
            "example": "Input:\n3\nOutput:\n1\n1 2\n1 2 3",
            "constraints": "N>0",
            "explanation": "",
            "tests": [
                {"input": "3", "output": "1\n1 2\n1 2 3"},
                {"input": "1", "output": "1"},
                {"input": "2", "output": "1\n1 2"}
            ]
        },
        {
            "id": "print_pyramid_numbers",
            "title": "Pyramid Numbers",
            "topic": "Patterns",
            "description": "Print centered pyramid of numbers (simple).",
            "description_full": "Given N, print N rows with increasing odd counts (formatting minimal: left-aligned allowed).",
            "input": "Integer N",
            "output": "N rows",
            "example": "Input:\n2\nOutput:\n1\n1 2 1",
            "constraints": "small N",
            "explanation": "",
            "tests": [
                {"input": "2", "output": "1\n1 2 1"},
                {"input": "1", "output": "1"},
                {"input": "3", "output": "1\n1 2 1\n1 2 3 2 1"}
            ]
        },
        {
            "id": "print_alphabet_triangle",
            "title": "Alphabet Triangle",
            "topic": "Patterns",
            "description": "Print letters A.. per row.",
            "description_full": "Given N, print first N lines with letters A.. increasing per line.",
            "input": "Integer N",
            "output": "N lines",
            "example": "Input:\n3\nOutput:\nA\nA B\nA B C",
            "constraints": "N <= 26",
            "explanation": "",
            "tests": [
                {"input": "3", "output": "A\nA B\nA B C"},
                {"input": "1", "output": "A"},
                {"input": "2", "output": "A\nA B"}
            ]
        },
        {
            "id": "hollow_square",
            "title": "Hollow Square",
            "topic": "Patterns",
            "description": "Print hollow square of size N.",
            "description_full": "Given N>=2, print N lines forming a hollow square using '*'.",
            "input": "Integer N",
            "output": "N lines",
            "example": "Input:\n4\nOutput:\n****\n*  *\n*  *\n****",
            "constraints": "N>=2",
            "explanation": "",
            "tests": [
                {"input": "4", "output": "****\n*  *\n*  *\n****"},
                {"input": "2", "output": "**\n**"},
                {"input": "3", "output": "***\n* *\n***"}
            ]
        },
        {
            "id": "diagonal_star",
            "title": "Diagonal Star",
            "topic": "Patterns",
            "description": "Print stars on diagonal positions.",
            "description_full": "Given N, print N lines with star at i-th position on i-th row (1-indexed).",
            "input": "Integer N",
            "output": "N lines",
            "example": "Input:\n3\nOutput:\n*  \n * \n  *",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "3", "output": "*  \n * \n  *"},
                {"input": "1", "output": "*"},
                {"input": "2", "output": "* \n *"}
            ]
        },
        {
            "id": "print_repeat_char_n",
            "title": "Repeat Character N times",
            "topic": "Patterns",
            "description": "Print character C repeated N times.",
            "description_full": "Given character C and integer N, print C repeated N times on one line.",
            "input": "C N",
            "output": "Single line with C repeated N times",
            "example": "Input:\na 3\nOutput:\naaa",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "a 3", "output": "aaa"},
                {"input": "* 1", "output": "*"},
                {"input": "x 5", "output": "xxxxx"}
            ]
        },
        {
            "id": "numeric_pattern_triangle",
            "title": "Numeric Pattern Triangle",
            "topic": "Patterns",
            "description": "Print triangle where row i contains i repeated i times.",
            "description_full": "Given N, print rows: 1; 22; 333; ... up to N.",
            "input": "Integer N",
            "output": "N lines",
            "example": "Input:\n3\nOutput:\n1\n22\n333",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "3", "output": "1\n22\n333"},
                {"input": "1", "output": "1"},
                {"input": "2", "output": "1\n22"}
            ]
        }],
        "Functions": [ {
            "id": "factorial_small",
            "title": "Factorial (Small N)",
            "topic": "Functions",
            "description": "Compute factorial of small N.",
            "description_full": "Given N (<=20), print N! using iterative method.",
            "input": "Integer N",
            "output": "N!",
            "example": "Input:\n5\nOutput:\n120",
            "constraints": "0 <= N <= 20",
            "explanation": "",
            "tests": [
                {"input": "5", "output": "120"},
                {"input": "0", "output": "1"},
                {"input": "7", "output": "5040"}
            ]
        },
        {
            "id": "is_prime_function",
            "title": "Is Prime (Function)",
            "topic": "Functions",
            "description": "Use a function to test primality.",
            "description_full": "Given N, print YES if prime else NO. Encourage using helper function.",
            "input": "Integer N",
            "output": "YES or NO",
            "example": "Input:\n11\nOutput:\nYES",
            "constraints": "N small",
            "explanation": "",
            "tests": [
                {"input": "11", "output": "YES"},
                {"input": "12", "output": "NO"},
                {"input": "2", "output": "YES"}
            ]
        },
        {
            "id": "gcd_function",
            "title": "GCD Function",
            "topic": "Functions",
            "description": "Implement gcd as a function and use it.",
            "description_full": "Given A B, compute gcd via helper function and print result.",
            "input": "Two integers A B",
            "output": "GCD",
            "example": "Input:\n9 6\nOutput:\n3",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "9 6", "output": "3"},
                {"input": "10 5", "output": "5"},
                {"input": "7 13", "output": "1"}
            ]
        },
        {
            "id": "is_palindrome_function",
            "title": "String Palindrome (Function)",
            "topic": "Functions",
            "description": "Write helper to check palindrome.",
            "description_full": "Given S, use function is_palindrome to print YES/NO.",
            "input": "String S",
            "output": "YES or NO",
            "example": "Input:\nmadam\nOutput:\nYES",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "madam", "output": "YES"},
                {"input": "hello", "output": "NO"},
                {"input": "a", "output": "YES"}
            ]
        },
        {
            "id": "power_function",
            "title": "Power Using Loop",
            "topic": "Functions",
            "description": "Compute A^B for non-negative B without built-in pow.",
            "description_full": "Given A and non-negative integer B, compute A^B using loop.",
            "input": "Two integers A B",
            "output": "A^B",
            "example": "Input:\n2 3\nOutput:\n8",
            "constraints": "B >= 0",
            "explanation": "",
            "tests": [
                {"input": "2 3", "output": "8"},
                {"input": "5 0", "output": "1"},
                {"input": "3 2", "output": "9"}
            ]
        },
        {
            "id": "is_perfect_square_function",
            "title": "Is Perfect Square",
            "topic": "Functions",
            "description": "Check if N is perfect square using helper.",
            "description_full": "Given N, print YES if exists integer x s.t. x*x = N else NO.",
            "input": "Integer N",
            "output": "YES or NO",
            "example": "Input:\n16\nOutput:\nYES",
            "constraints": "N >= 0",
            "explanation": "",
            "tests": [
                {"input": "16", "output": "YES"},
                {"input": "14", "output": "NO"},
                {"input": "0", "output": "YES"}
            ]
        },
        {
            "id": "swap_two_numbers_function",
            "title": "Swap Two Numbers",
            "topic": "Functions",
            "description": "Swap two numbers and print result.",
            "description_full": "Given A and B, print B A (swapped). Use helper function if desired.",
            "input": "Two integers A B",
            "output": "B A",
            "example": "Input:\n3 5\nOutput:\n5 3",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "3 5", "output": "5 3"},
                {"input": "1 1", "output": "1 1"},
                {"input": "-1 2", "output": "2 -1"}
            ]
        },
        {
            "id": "fahrenheit_to_celsius_function",
            "title": "F to C Conversion",
            "topic": "Functions",
            "description": "Convert Fahrenheit to Celsius (integer rounding).",
            "description_full": "Given integer F, print Celsius as integer using formula C = (F-32)*5/9 (floor/trunc).",
            "input": "Integer F",
            "output": "Integer C",
            "example": "Input:\n32\nOutput:\n0",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "32", "output": "0"},
                {"input": "212", "output": "100"},
                {"input": "68", "output": "20"}
            ]
        },
        {
            "id": "is_armstrong_small",
            "title": "Armstrong Number (Small)",
            "topic": "Functions",
            "description": "Check Armstrong number for 3-digit N.",
            "description_full": "Given N (0..999), print YES if sum of cubes of digits equals N, else NO.",
            "input": "Integer N",
            "output": "YES or NO",
            "example": "Input:\n153\nOutput:\nYES",
            "constraints": "0 <= N <= 999",
            "explanation": "",
            "tests": [
                {"input": "153", "output": "YES"},
                {"input": "370", "output": "YES"},
                {"input": "100", "output": "NO"}
            ]
        }],
        "Searching": [{
            "id": "linear_search_index",
            "title": "Linear Search Index",
            "topic": "Searching",
            "description": "Find index of X using linear search.",
            "description_full": "Given N and array A and X, print 0-based index of first occurrence of X or -1.",
            "input": "N then N integers then X",
            "output": "Index or -1",
            "example": "Input:\n5\n1 3 5 7 9\n7\nOutput:\n3",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5\n1 3 5 7 9\n7", "output": "3"},
                {"input": "3\n1 2 3\n4", "output": "-1"},
                {"input": "4\n2 2 2 2\n2", "output": "0"}
            ]
        },
        {
            "id": "find_min_index",
            "title": "Index of Minimum Element",
            "topic": "Searching",
            "description": "Find index of first minimum element.",
            "description_full": "Given N and array A, print 0-based index of smallest element (first occurrence).",
            "input": "N then N integers",
            "output": "Index",
            "example": "Input:\n3\n2 1 3\nOutput:\n1",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "3\n2 1 3", "output": "1"},
                {"input": "4\n5 5 1 5", "output": "2"},
                {"input": "1\n7", "output": "0"}
            ]
        },
        {
            "id": "contains_duplicate",
            "title": "Contains Duplicate",
            "topic": "Searching",
            "description": "Check if array contains duplicates.",
            "description_full": "Given N and array A, print YES if any element repeats else NO.",
            "input": "N then N integers",
            "output": "YES or NO",
            "example": "Input:\n4\n1 2 3 1\nOutput:\nYES",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "4\n1 2 3 1", "output": "YES"},
                {"input": "3\n1 2 3", "output": "NO"},
                {"input": "1\n5", "output": "NO"}
            ]
        },
        {
            "id": "count_greater_than_x",
            "title": "Count Greater Than X",
            "topic": "Searching",
            "description": "Count elements greater than X.",
            "description_full": "Given N, array A and X, print how many Ai > X.",
            "input": "N then N integers then X",
            "output": "Count",
            "example": "Input:\n5\n1 3 5 7 9\n4\nOutput:\n3",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5\n1 3 5 7 9\n4", "output": "3"},
                {"input": "3\n1 2 3\n10", "output": "0"},
                {"input": "4\n5 6 7 8\n6", "output": "2"}
            ]
        },
        {
            "id": "find_last_occurrence",
            "title": "Find Last Occurrence",
            "topic": "Searching",
            "description": "Return last index of X or -1.",
            "description_full": "Given N, array A and X, print last 0-based index of X or -1.",
            "input": "N then N integers then X",
            "output": "Index or -1",
            "example": "Input:\n5\n1 2 3 2 1\n2\nOutput:\n3",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5\n1 2 3 2 1\n2", "output": "3"},
                {"input": "3\n1 1 1\n1", "output": "2"},
                {"input": "2\n5 6\n7", "output": "-1"}
            ]
        },
        {
            "id": "find_element_count",
            "title": "Count Specific Element",
            "topic": "Searching",
            "description": "Count how many times X appears.",
            "description_full": "Given N, array A and X, print frequency of X.",
            "input": "N then N integers then X",
            "output": "Frequency",
            "example": "Input:\n5\n2 2 3 2 2\n2\nOutput:\n4",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5\n2 2 3 2 2\n2", "output": "4"},
                {"input": "3\n1 2 3\n4", "output": "0"},
                {"input": "1\n0\n0", "output": "1"}
            ]
        },
        {
            "id": "find_first_even_index",
            "title": "Find First Even Index",
            "topic": "Searching",
            "description": "Find index of first even element.",
            "description_full": "Given N and array A, print 0-based index of first even element or -1.",
            "input": "N then N integers",
            "output": "Index or -1",
            "example": "Input:\n4\n1 3 4 5\nOutput:\n2",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "4\n1 3 4 5", "output": "2"},
                {"input": "3\n1 3 5", "output": "-1"},
                {"input": "1\n2", "output": "0"}
            ]
        },
        {
            "id": "find_index_sum_target",
            "title": "Find Pair Sum (Brute)",
            "topic": "Searching",
            "description": "Find indices i<j where Ai+Aj = X and print any pair or -1 -1.",
            "description_full": "Given N, array A and X, print indices i j (0-based) of any pair summing to X or -1 -1.",
            "input": "N then N integers then X",
            "output": "i j or -1 -1",
            "example": "Input:\n5\n1 2 3 4 5\n9\nOutput:\n3 4",
            "constraints": "N small",
            "explanation": "",
            "tests": [
                {"input": "5\n1 2 3 4 5\n9", "output": "3 4"},
                {"input": "3\n1 1 1\n4", "output": "-1 -1"},
                {"input": "4\n2 7 11 15\n9", "output": "0 1"}
            ]
        }],
        "Sorting": [{
            "id": "sort_ascending",
            "title": "Sort Array Ascending",
            "topic": "Sorting",
            "description": "Sort array in non-decreasing order.",
            "description_full": "Given N and array A, sort and print elements ascending.",
            "input": "N then N integers",
            "output": "Sorted array",
            "example": "Input:\n5\n3 1 4 2 5\nOutput:\n1 2 3 4 5",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5\n3 1 4 2 5", "output": "1 2 3 4 5"},
                {"input": "3\n2 2 1", "output": "1 2 2"},
                {"input": "1\n7", "output": "7"}
            ]
        },
        {
            "id": "is_sorted",
            "title": "Is Array Sorted",
            "topic": "Sorting",
            "description": "Check if array is sorted non-decreasingly.",
            "description_full": "Given N and array A, print YES if sorted else NO.",
            "input": "N then N integers",
            "output": "YES or NO",
            "example": "Input:\n3\n1 2 3\nOutput:\nYES",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "3\n1 2 3", "output": "YES"},
                {"input": "3\n2 1 3", "output": "NO"},
                {"input": "1\n5", "output": "YES"}
            ]
        },
        {
            "id": "sort_descending",
            "title": "Sort Array Descending",
            "topic": "Sorting",
            "description": "Sort array in non-increasing order.",
            "description_full": "Given N and array A, sort descending and print.",
            "input": "N then N integers",
            "output": "Sorted array (desc)",
            "example": "Input:\n4\n1 3 2 4\nOutput:\n4 3 2 1",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "4\n1 3 2 4", "output": "4 3 2 1"},
                {"input": "3\n2 2 1", "output": "2 2 1"},
                {"input": "1\n9", "output": "9"}
            ]
        },
        {
            "id": "find_median_sorted",
            "title": "Median of Sorted Array",
            "topic": "Sorting",
            "description": "Find median of odd-length sorted array.",
            "description_full": "Given N odd and sorted array, print middle element.",
            "input": "N then N integers (sorted)",
            "output": "Median value",
            "example": "Input:\n5\n1 2 3 4 5\nOutput:\n3",
            "constraints": "N odd",
            "explanation": "",
            "tests": [
                {"input": "5\n1 2 3 4 5", "output": "3"},
                {"input": "1\n7", "output": "7"},
                {"input": "3\n2 4 6", "output": "4"}
            ]
        },
        {
            "id": "kth_smallest",
            "title": "Kth Smallest Element",
            "topic": "Sorting",
            "description": "Find k-th smallest element (1-based).",
            "description_full": "Given N and array A and k, print k-th smallest element.",
            "input": "N then N integers then k",
            "output": "kth smallest",
            "example": "Input:\n5\n5 3 1 2 4\n2\nOutput:\n2",
            "constraints": "1 <= k <= N",
            "explanation": "",
            "tests": [
                {"input": "5\n5 3 1 2 4\n2", "output": "2"},
                {"input": "3\n1 2 3\n1", "output": "1"},
                {"input": "4\n2 2 3 1\n3", "output": "2"}
            ]
        },
        {
            "id": "count_inversions_bruteforce",
            "title": "Count Inversions (Brute)",
            "topic": "Sorting",
            "description": "Count pairs i<j with Ai>Aj (brute force).",
            "description_full": "Given N and array A, print inversion count (N small).",
            "input": "N then N integers",
            "output": "Inversion count",
            "example": "Input:\n3\n3 1 2\nOutput:\n2",
            "constraints": "N small",
            "explanation": "",
            "tests": [
                {"input": "3\n3 1 2", "output": "2"},
                {"input": "3\n1 2 3", "output": "0"},
                {"input": "4\n4 3 2 1", "output": "6"}
            ]
        },
        {
            "id": "sort_unique",
            "title": "Sort Unique Elements",
            "topic": "Sorting",
            "description": "Print unique elements sorted ascending.",
            "description_full": "Given N and array A, output distinct elements sorted.",
            "input": "N then N integers",
            "output": "Sorted distinct elements",
            "example": "Input:\n6\n1 2 1 3 2 4\nOutput:\n1 2 3 4",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "6\n1 2 1 3 2 4", "output": "1 2 3 4"},
                {"input": "3\n2 2 2", "output": "2"},
                {"input": "1\n5", "output": "5"}
            ]
        },
        {
            "id": "sort_by_absolute_value",
            "title": "Sort by Absolute Value",
            "topic": "Sorting",
            "description": "Sort array by absolute values ascending.",
            "description_full": "Given N and array A, sort by |Ai| and print values in that order.",
            "input": "N then N integers",
            "output": "Sorted by absolute",
            "example": "Input:\n5\n-2 3 -1 4 0\nOutput:\n0 -1 -2 3 4",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5\n-2 3 -1 4 0", "output": "0 -1 -2 3 4"},
                {"input": "3\n2 -2 1", "output": "1 2 -2"},
                {"input": "1\n-5", "output": "-5"}
            ]
        }],
        "Matrices": [ {
            "id": "matrix_diagonal_sum",
            "title": "Sum of Primary Diagonal",
            "topic": "Matrices",
            "description": "Sum primary diagonal of NxN matrix.",
            "description_full": "Given N and NxN matrix, print sum of elements where row==col.",
            "input": "N then N lines of N integers",
            "output": "Diagonal sum",
            "example": "Input:\n2\n1 2\n3 4\nOutput:\n5",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "2\n1 2\n3 4", "output": "5"},
                {"input": "1\n9", "output": "9"},
                {"input": "3\n1 0 0\n0 1 0\n0 0 1", "output": "3"}
            ]
        },
        {
            "id": "matrix_row_sum",
            "title": "Row with Maximum Sum",
            "topic": "Matrices",
            "description": "Find row index with maximum sum (0-based).",
            "description_full": "Given N and NxN matrix, print the 0-based index of the row with max sum (smallest index on tie).",
            "input": "N then NxN integers",
            "output": "Row index",
            "example": "Input:\n3\n1 2 3\n4 5 6\n1 1 1\nOutput:\n1",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "3\n1 2 3\n4 5 6\n1 1 1", "output": "1"},
                {"input": "2\n1 1\n1 1", "output": "0"},
                {"input": "1\n5", "output": "0"}
            ]
        },
        {
            "id": "transpose_matrix",
            "title": "Transpose Matrix",
            "topic": "Matrices",
            "description": "Compute transpose of NxN matrix.",
            "description_full": "Given N and NxN matrix, print its transpose (rows become columns).",
            "input": "N then NxN integers",
            "output": "Transposed matrix",
            "example": "Input:\n2\n1 2\n3 4\nOutput:\n1 3\n2 4",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "2\n1 2\n3 4", "output": "1 3\n2 4"},
                {"input": "1\n9", "output": "9"},
                {"input": "3\n1 2 3\n4 5 6\n7 8 9", "output": "1 4 7\n2 5 8\n3 6 9"}
            ]
        },
        {
            "id": "sum_of_matrix",
            "title": "Sum of All Matrix Elements",
            "topic": "Matrices",
            "description": "Sum all elements of the matrix.",
            "description_full": "Given N and NxN matrix, print sum of all entries.",
            "input": "N then NxN integers",
            "output": "Sum",
            "example": "Input:\n2\n1 2\n3 4\nOutput:\n10",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "2\n1 2\n3 4", "output": "10"},
                {"input": "1\n0", "output": "0"},
                {"input": "3\n1 1 1\n1 1 1\n1 1 1", "output": "9"}
            ]
        },
        {
            "id": "matrix_border_sum",
            "title": "Sum of Border Elements",
            "topic": "Matrices",
            "description": "Sum elements on matrix border.",
            "description_full": "Given N and NxN matrix, sum elements in first and last rows and columns (avoid double counting).",
            "input": "N then NxN integers",
            "output": "Sum",
            "example": "Input:\n3\n1 2 3\n4 5 6\n7 8 9\nOutput:\n40",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "3\n1 2 3\n4 5 6\n7 8 9", "output": "40"},
                {"input": "1\n5", "output": "5"},
                {"input": "2\n1 2\n3 4", "output": "10"}
            ]
        },
        {
            "id": "matrix_count_zero",
            "title": "Count Zeros in Matrix",
            "topic": "Matrices",
            "description": "Count zero entries in matrix.",
            "description_full": "Given N and NxN matrix, print number of entries equal to 0.",
            "input": "N then NxN integers",
            "output": "Count of zeros",
            "example": "Input:\n2\n0 1\n2 0\nOutput:\n2",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "2\n0 1\n2 0", "output": "2"},
                {"input": "1\n5", "output": "0"},
                {"input": "3\n0 0 0\n0 0 0\n0 0 0", "output": "9"}
            ]
        },
        {
            "id": "matrix_find_value",
            "title": "Find Value in Matrix",
            "topic": "Matrices",
            "description": "Find if value exists in matrix.",
            "description_full": "Given N,matrix and X, print YES if X present else NO.",
            "input": "N then NxN integers then X",
            "output": "YES or NO",
            "example": "Input:\n2\n1 2\n3 4\n3\nOutput:\nYES",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "2\n1 2\n3 4\n3", "output": "YES"},
                {"input": "1\n5\n6", "output": "NO"},
                {"input": "3\n1 2 3\n4 5 6\n7 8 9\n8", "output": "YES"}
            ]
        },
        {
            "id": "matrix_row_reverse",
            "title": "Reverse Each Row",
            "topic": "Matrices",
            "description": "Reverse elements in each row.",
            "description_full": "Given N and NxN matrix, print matrix where each row's elements are reversed.",
            "input": "N then NxN integers",
            "output": "Transformed matrix",
            "example": "Input:\n2\n1 2\n3 4\nOutput:\n2 1\n4 3",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "2\n1 2\n3 4", "output": "2 1\n4 3"},
                {"input": "1\n9", "output": "9"},
                {"input": "3\n1 2 3\n4 5 6\n7 8 9", "output": "3 2 1\n6 5 4\n9 8 7"}
            ]
        },
        {
            "id": "matrix_column_sum",
            "title": "Sum of Each Column",
            "topic": "Matrices",
            "description": "Compute sum for each column.",
            "description_full": "Given N and NxN matrix, print N numbers where i-th is sum of column i.",
            "input": "N then NxN integers",
            "output": "N column sums",
            "example": "Input:\n2\n1 2\n3 4\nOutput:\n4 6",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "2\n1 2\n3 4", "output": "4 6"},
                {"input": "1\n5", "output": "5"},
                {"input": "3\n1 1 1\n1 1 1\n1 1 1", "output": "3 3 3"}
            ]
        }]
    },

    "Easy": {
        "Loops": [{
            "id": "sum_of_first_n_even_numbers",
            "title": "Sum of First N Even Numbers",
            "topic": "Loops",
            "description": "Sum first N even natural numbers.",
            "description_full": "Given N, compute the sum of the first N even natural numbers (2 + 4 + ...).",
            "input": "Integer N",
            "output": "Sum",
            "example": "Input:\n3\nOutput:\n12",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "3", "output": "12"},
                {"input": "1", "output": "2"},
                {"input": "5", "output": "30"}
            ]
        },
        {
            "id": "sum_of_first_n_odd_numbers",
            "title": "Sum of First N Odd Numbers",
            "topic": "Loops",
            "description": "Sum the first N odd numbers.",
            "description_full": "Given N, compute the sum of first N odd numbers (1+3+5+...).",
            "input": "Integer N",
            "output": "Sum",
            "example": "Input:\n4\nOutput:\n16",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "4", "output": "16"},
                {"input": "1", "output": "1"},
                {"input": "5", "output": "25"}
            ]
        },
        {
            "id": "count_multiples_of_k",
            "title": "Count Multiples of K Up to N",
            "topic": "Loops",
            "description": "Count numbers ≤ N divisible by K.",
            "description_full": "Given N and K, count how many integers in [1, N] are divisible by K.",
            "input": "Two integers N K",
            "output": "Count",
            "example": "Input:\n10 3\nOutput:\n3",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "10 3", "output": "3"},
                {"input": "1 1", "output": "1"},
                {"input": "15 5", "output": "3"}
            ]
        },
        {
            "id": "sum_of_squares_1_to_n",
            "title": "Sum of Squares 1..N",
            "topic": "Loops",
            "description": "Compute sum of squares from 1 to N.",
            "description_full": "Given N, compute 1^2 + 2^2 + ... + N^2.",
            "input": "Integer N",
            "output": "Sum",
            "example": "Input:\n3\nOutput:\n14",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "3", "output": "14"},
                {"input": "1", "output": "1"},
                {"input": "5", "output": "55"}
            ]
        },
        {
            "id": "count_digits_greater_than_d",
            "title": "Count Digits Greater Than D",
            "topic": "Loops",
            "description": "In a number, count digits greater than D.",
            "description_full": "Given N and digit D (0-9), count digits in N that are strictly greater than D.",
            "input": "Two space-separated values: N D",
            "output": "Count",
            "example": "Input:\n57234 4\nOutput:\n2",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "57234 4", "output": "2"},
                {"input": "1000 0", "output": "1"},
                {"input": "98765 5", "output": "4"}
            ]
        },
        {
            "id": "sum_even_index_elements",
            "title": "Sum Elements at Even Indices",
            "topic": "Loops",
            "description": "Sum array elements at even indices (0-based).",
            "description_full": "Given N and array A, compute sum of elements at indices 0,2,4,...",
            "input": "N then N integers",
            "output": "Sum",
            "example": "Input:\n5\n1 2 3 4 5\nOutput:\n9",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5\n1 2 3 4 5", "output": "9"},
                {"input": "1\n10", "output": "10"},
                {"input": "4\n1 1 1 1", "output": "2"}
            ]
        },
        {
            "id": "product_of_first_n_numbers_mod",
            "title": "Product of First N Numbers Mod M",
            "topic": "Loops",
            "description": "Compute product 1*2*...*N modulo M.",
            "description_full": "Given N and M, compute (1*2*...*N) % M.",
            "input": "Two integers N M",
            "output": "Value",
            "example": "Input:\n5 100\nOutput:\n20",
            "constraints": "N small enough (<=20) to avoid overflow without mod",
            "explanation": "",
            "tests": [
                {"input": "5 100", "output": "20"},
                {"input": "1 7", "output": "1"},
                {"input": "6 13", "output": "12"}
            ]
        },
        {
            "id": "repeat_string_n_times",
            "title": "Repeat String N Times",
            "topic": "Loops",
            "description": "Repeat given string N times separated by spaces.",
            "description_full": "Given string S and integer N, output S repeated N times separated by a single space.",
            "input": "S N",
            "output": "Concatenated string",
            "example": "Input:\nhi 3\nOutput:\nhi hi hi",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "hi 3", "output": "hi hi hi"},
                {"input": "a 1", "output": "a"},
                {"input": "ok 2", "output": "ok ok"}
            ]
        },
        {
            "id": "sum_digits_until_single_digit",
            "title": "Digit Sum Until Single Digit",
            "topic": "Loops",
            "description": "Repeatedly sum digits until single digit remains.",
            "description_full": "Given non-negative N, repeatedly replace N with sum of its digits until N < 10; print the resulting single digit.",
            "input": "Integer N",
            "output": "Single digit",
            "example": "Input:\n9875\nOutput:\n2",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "9875", "output": "2"},
                {"input": "9", "output": "9"},
                {"input": "199", "output": "1"}
            ]
        }],
        "Conditionals": [{
            "id": "is_leap_year_verbose",
            "title": "Leap Year (Detailed)",
            "topic": "Conditionals",
            "description": "Check leap year with messages.",
            "description_full": "Given year Y, print 'YES' if leap year, otherwise 'NO'. Use Gregorian rules (divisible by 400 or divisible by 4 and not 100).",
            "input": "Integer Y",
            "output": "YES or NO",
            "example": "Input:\n2004\nOutput:\nYES",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "2004", "output": "YES"},
                {"input": "1900", "output": "NO"},
                {"input": "2000", "output": "YES"}
            ]
        },
        {
            "id": "classify_triangle",
            "title": "Classify Triangle",
            "topic": "Conditionals",
            "description": "Given sides, determine triangle type or invalid.",
            "description_full": "Given three positive integers a, b, c, determine if they form a valid triangle. If valid, print 'Equilateral', 'Isosceles', or 'Scalene'. If not valid, print 'Invalid'.",
            "input": "Three integers a b c",
            "output": "One of Equilateral/Isosceles/Scalene/Invalid",
            "example": "Input:\n3 4 5\nOutput:\nScalene",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "3 4 5", "output": "Scalene"},
                {"input": "2 2 2", "output": "Equilateral"},
                {"input": "1 2 3", "output": "Invalid"}
            ]
        },
        {
            "id": "compare_three_numbers",
            "title": "Compare Three Numbers",
            "topic": "Conditionals",
            "description": "Check ordering among three numbers.",
            "description_full": "Given A B C, print 'ASC' if strictly increasing, 'DESC' if strictly decreasing, else 'NONE'.",
            "input": "Three integers A B C",
            "output": "ASC / DESC / NONE",
            "example": "Input:\n1 2 3\nOutput:\nASC",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "1 2 3", "output": "ASC"},
                {"input": "3 2 1", "output": "DESC"},
                {"input": "1 1 2", "output": "NONE"}
            ]
        },
        {
            "id": "classify_angle",
            "title": "Classify Angle",
            "topic": "Conditionals",
            "description": "Determine acute/obtuse/right angle type.",
            "description_full": "Given integer angle A (0<A<180), print 'Acute' (<90), 'Right' (=90), or 'Obtuse' (>90).",
            "input": "Integer A",
            "output": "Acute / Right / Obtuse",
            "example": "Input:\n90\nOutput:\nRight",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "60", "output": "Acute"},
                {"input": "90", "output": "Right"},
                {"input": "120", "output": "Obtuse"}
            ]
        },
        {
            "id": "quadratic_roots_real",
            "title": "Quadratic Real Roots Check",
            "topic": "Conditionals",
            "description": "Check discriminant for real roots.",
            "description_full": "Given coefficients a b c, compute discriminant D=b^2-4ac. If D<0 print 'NO', else print 'YES'.",
            "input": "Three integers a b c",
            "output": "YES or NO",
            "example": "Input:\n1 0 -1\nOutput:\nYES",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "1 0 -1", "output": "YES"},
                {"input": "1 0 1", "output": "NO"},
                {"input": "1 -2 1", "output": "YES"}
            ]
        },
        {
            "id": "digit_sum_even_or_odd",
            "title": "Digit Sum Even/Odd",
            "topic": "Conditionals",
            "description": "Print if sum of digits is even or odd.",
            "description_full": "Given non-negative integer N, compute sum of digits and print 'EVEN' or 'ODD'.",
            "input": "Integer N",
            "output": "EVEN or ODD",
            "example": "Input:\n123\nOutput:\nEVEN",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "123", "output": "EVEN"},
                {"input": "5", "output": "ODD"},
                {"input": "0", "output": "EVEN"}
            ]
        },
        {
            "id": "intersecting_intervals_check",
            "title": "Do Intervals Intersect",
            "topic": "Conditionals",
            "description": "Check if two closed intervals intersect.",
            "description_full": "Given intervals [a,b] and [c,d], print 'YES' if they intersect (non-empty), else 'NO'.",
            "input": "Four integers a b c d",
            "output": "YES or NO",
            "example": "Input:\n1 3 2 4\nOutput:\nYES",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "1 3 2 4", "output": "YES"},
                {"input": "1 2 3 4", "output": "NO"},
                {"input": "0 5 5 7", "output": "YES"}
            ]
        },
        {
            "id": "is_perfect_number",
            "title": "Perfect Number Check",
            "topic": "Conditionals",
            "description": "Check perfect number property.",
            "description_full": "Given N, check if sum of proper divisors equals N; print YES or NO.",
            "input": "Integer N",
            "output": "YES or NO",
            "example": "Input:\n6\nOutput:\nYES",
            "constraints": "N small",
            "explanation": "",
            "tests": [
                {"input": "6", "output": "YES"},
                {"input": "28", "output": "YES"},
                {"input": "12", "output": "NO"}
            ]
        },
        {
            "id": "is_armstrong_number",
            "title": "Armstrong Number Check",
            "topic": "Conditionals",
            "description": "Check Armstrong for any digit length.",
            "description_full": "Given N, check if sum of each digit^count_digits equals N; print YES/NO.",
            "input": "Integer N",
            "output": "YES or NO",
            "example": "Input:\n153\nOutput:\nYES",
            "constraints": "N reasonable small",
            "explanation": "",
            "tests": [
                {"input": "153", "output": "YES"},
                {"input": "9474", "output": "YES"},
                {"input": "100", "output": "NO"}
            ]
        }],
        "Basic Math": [{
            "id": "sum_of_arithmetic_progression",
            "title": "Sum of AP",
            "topic": "Basic Math",
            "description": "Sum of first N terms of AP with first term a and difference d.",
            "description_full": "Given a, d, N, compute sum of AP: N/2 * (2a + (N-1)d).",
            "input": "Three integers a d N",
            "output": "Sum",
            "example": "Input:\n1 1 5\nOutput:\n15",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "1 1 5", "output": "15"},
                {"input": "2 2 3", "output": "12"},
                {"input": "0 5 4", "output": "30"}
            ]
        },
        {
            "id": "sum_of_geometric_progression_integer",
            "title": "Sum of GP (Integer)",
            "topic": "Basic Math",
            "description": "Sum of geometric series with integer ratio r.",
            "description_full": "Given a, r, n, compute sum a*(r^n -1)/(r-1) if r !=1, else a*n. All integers small.",
            "input": "Three integers a r n",
            "output": "Sum",
            "example": "Input:\n2 2 3\nOutput:\n14",
            "constraints": "r!=1 or handle accordingly",
            "explanation": "",
            "tests": [
                {"input": "2 2 3", "output": "14"},
                {"input": "3 1 4", "output": "12"},
                {"input": "1 3 2", "output": "4"}
            ]
        },
        {
            "id": "count_divisors",
            "title": "Count Divisors",
            "topic": "Basic Math",
            "description": "Count positive divisors of N.",
            "description_full": "Given N, print number of positive integer divisors of N.",
            "input": "Integer N",
            "output": "Count",
            "example": "Input:\n6\nOutput:\n4",
            "constraints": "N small (<=1e6)",
            "explanation": "",
            "tests": [
                {"input": "6", "output": "4"},
                {"input": "1", "output": "1"},
                {"input": "12", "output": "6"}
            ]
        },
        {
            "id": "sum_of_digits_power_k",
            "title": "Sum of Digits^k",
            "topic": "Basic Math",
            "description": "Compute sum of each digit raised to k.",
            "description_full": "Given N and k, compute sum of (digit^k) for each decimal digit of N.",
            "input": "N k",
            "output": "Sum",
            "example": "Input:\n23 3\nOutput:\n35",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "23 3", "output": "35"},
                {"input": "5 2", "output": "25"},
                {"input": "10 1", "output": "1"}
            ]
        },
        {
            "id": "count_trailing_zeros_factorial",
            "title": "Trailing Zeros in Factorial",
            "topic": "Basic Math",
            "description": "Number of trailing zeros in N!.",
            "description_full": "Given N, compute number of trailing zeros in N! (count of factors of 10).",
            "input": "Integer N",
            "output": "Count of zeros",
            "example": "Input:\n5\nOutput:\n1",
            "constraints": "N up to 1e9 (use division by powers of 5)",
            "explanation": "",
            "tests": [
                {"input": "5", "output": "1"},
                {"input": "100", "output": "24"},
                {"input": "25", "output": "6"}
            ]
        },
        {
            "id": "sum_digits_in_range",
            "title": "Sum of digits for numbers 1..N",
            "topic": "Basic Math",
            "description": "Compute sum of digits of all integers from 1 to N (N small).",
            "description_full": "Given small N, compute total sum of digits for each integer 1..N.",
            "input": "Integer N",
            "output": "Sum",
            "example": "Input:\n11\nOutput:\n4",
            "constraints": "N small <= 10000",
            "explanation": "",
            "tests": [
                {"input": "11", "output": "4"},
                {"input": "1", "output": "1"},
                {"input": "20", "output": "102"}
            ]
        },
        {
            "id": "decimal_to_binary",
            "title": "Decimal to Binary",
            "topic": "Basic Math",
            "description": "Convert decimal to binary string.",
            "description_full": "Given non-negative N, print its binary representation without leading zeros (0 for 0).",
            "input": "Integer N",
            "output": "Binary string",
            "example": "Input:\n5\nOutput:\n101",
            "constraints": "N >= 0",
            "explanation": "",
            "tests": [
                {"input": "5", "output": "101"},
                {"input": "0", "output": "0"},
                {"input": "8", "output": "1000"}
            ]
        },
        {
            "id": "binary_to_decimal",
            "title": "Binary to Decimal",
            "topic": "Basic Math",
            "description": "Convert binary string to decimal.",
            "description_full": "Given binary string S, print decimal integer value.",
            "input": "Binary string S",
            "output": "Decimal integer",
            "example": "Input:\n101\nOutput:\n5",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "101", "output": "5"},
                {"input": "0", "output": "0"},
                {"input": "1000", "output": "8"}
            ]
        },
        {
            "id": "greatest_power_less_than_n",
            "title": "Greatest Power of 2 ≤ N",
            "topic": "Basic Math",
            "description": "Find greatest power of 2 not exceeding N.",
            "description_full": "Given N, print largest 2^k such that 2^k ≤ N.",
            "input": "Integer N",
            "output": "Value",
            "example": "Input:\n10\nOutput:\n8",
            "constraints": "N >= 1",
            "explanation": "",
            "tests": [
                {"input": "10", "output": "8"},
                {"input": "1", "output": "1"},
                {"input": "16", "output": "16"}
            ]
        }],
        "Strings": [{
            "id": "remove_consecutive_duplicates",
            "title": "Remove Consecutive Duplicates",
            "topic": "Strings",
            "description": "Compress by removing consecutive duplicate chars.",
            "description_full": "Given string S, remove characters that repeat consecutively so that only one of each run remains.",
            "input": "String S",
            "output": "Processed string",
            "example": "Input:\naaabbc\nOutput:\nabc",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "aaabbc", "output": "abc"},
                {"input": "a", "output": "a"},
                {"input": "aabbcca", "output": "abca"}
            ]
        },
        {
            "id": "count_substring_occurrences",
            "title": "Count Substring Occurrences",
            "topic": "Strings",
            "description": "Count non-overlapping occurrences of substring P in S.",
            "description_full": "Given strings S and P, count how many times P occurs in S (non-overlapping).",
            "input": "Two strings S P (space separated; P has no spaces)",
            "output": "Count",
            "example": "Input:\nabababa aba\nOutput:\n2",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "abababa aba", "output": "2"},
                {"input": "aaaa a", "output": "4"},
                {"input": "hello ll", "output": "1"}
            ]
        },
        {
            "id": "most_frequent_word",
            "title": "Most Frequent Word",
            "topic": "Strings",
            "description": "Find most frequent word in sentence.",
            "description_full": "Given sentence S (words separated by spaces), print the most frequent word; if tie print lexicographically smallest.",
            "input": "String S",
            "output": "Word",
            "example": "Input:\napple banana apple\nOutput:\napple",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "apple banana apple", "output": "apple"},
                {"input": "b a b a", "output": "a"},
                {"input": "one", "output": "one"}
            ]
        },
        {
            "id": "capitalize_first_letters",
            "title": "Capitalize First Letters",
            "topic": "Strings",
            "description": "Capitalize first character of each word.",
            "description_full": "Given sentence S, capitalize first letter of each word; other letters unchanged.",
            "input": "String S",
            "output": "Processed sentence",
            "example": "Input:\nhello world\nOutput:\nHello World",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "hello world", "output": "Hello World"},
                {"input": "a", "output": "A"},
                {"input": "multiple words here", "output": "Multiple Words Here"}
            ]
        },
        {
            "id": "is_anagram",
            "title": "Anagram Check",
            "topic": "Strings",
            "description": "Check if two strings are anagrams.",
            "description_full": "Given strings A and B (no spaces), print YES if A is an anagram of B else NO.",
            "input": "Two strings A B",
            "output": "YES or NO",
            "example": "Input:\nlisten silent\nOutput:\nYES",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "listen silent", "output": "YES"},
                {"input": "aab aba", "output": "YES"},
                {"input": "ab c", "output": "NO"}
            ]
        },
        {
            "id": "left_rotate_string_k",
            "title": "Left Rotate String by K",
            "topic": "Strings",
            "description": "Rotate string left by k positions.",
            "description_full": "Given string S and integer k, perform left rotation and print result.",
            "input": "S k",
            "output": "Rotated string",
            "example": "Input:\nabcdef 2\nOutput:\ncdefab",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "abcdef 2", "output": "cdefab"},
                {"input": "a 3", "output": "a"},
                {"input": "hello 0", "output": "hello"}
            ]
        },
        {
            "id": "longest_common_prefix",
            "title": "Longest Common Prefix",
            "topic": "Strings",
            "description": "Find longest common prefix of list of words.",
            "description_full": "Given N and N words, print longest common prefix among them (empty string if none).",
            "input": "N then N words",
            "output": "Prefix",
            "example": "Input:\n3\nflower flow flight\nOutput:\nfl",
            "constraints": "words separated by spaces",
            "explanation": "",
            "tests": [
                {"input": "3\nflower flow flight", "output": "fl"},
                {"input": "2\na b", "output": ""},
                {"input": "1\nhello", "output": "hello"}
            ]
        },
        {
            "id": "replace_spaces_with_dash",
            "title": "Replace Spaces with Dash",
            "topic": "Strings",
            "description": "Replace spaces by '-' in a string.",
            "description_full": "Given line S, replace each space by a hyphen '-' and print result.",
            "input": "String S",
            "output": "Processed string",
            "example": "Input:\nHello World\nOutput:\nHello-World",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "Hello World", "output": "Hello-World"},
                {"input": " a b ", "output": "-a-b-"},
                {"input": "x", "output": "x"}
            ]
        },
        {
            "id": "remove_substring_all",
            "title": "Remove All Occurrences of Substring",
            "topic": "Strings",
            "description": "Remove every non-overlapping occurrence of P from S.",
            "description_full": "Given S and P, remove all non-overlapping occurrences of P and print resultant string (if empty print empty line).",
            "input": "S P",
            "output": "Processed string",
            "example": "Input:\nababab ab\nOutput:\n",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "ababab ab", "output": ""},
                {"input": "hello l", "output": "heo"},
                {"input": "aaaa aa", "output": ""}
            ]
        }],
        "Arrays": [ {
            "id": "remove_element_and_shift",
            "title": "Remove Element and Shift",
            "topic": "Arrays",
            "description": "Remove first occurrence of X and shift remaining.",
            "description_full": "Given N, array A and X, remove the first occurrence of X and print resulting array; if X not present print original.",
            "input": "N then N integers then X",
            "output": "Array after removal",
            "example": "Input:\n5\n1 2 3 4 5\n3\nOutput:\n1 2 4 5",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5\n1 2 3 4 5\n3", "output": "1 2 4 5"},
                {"input": "3\n1 2 3\n4", "output": "1 2 3"},
                {"input": "1\n5\n5", "output": ""}
            ]
        },
        {
            "id": "rotate_array_right_k",
            "title": "Rotate Array Right by K",
            "topic": "Arrays",
            "description": "Right-rotate array by K positions.",
            "description_full": "Given N, array A and integer K, rotate array right by K (K may be > N) and print result.",
            "input": "N then N integers then K",
            "output": "Rotated array",
            "example": "Input:\n5\n1 2 3 4 5\n2\nOutput:\n4 5 1 2 3",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5\n1 2 3 4 5\n2", "output": "4 5 1 2 3"},
                {"input": "3\n1 2 3\n3", "output": "1 2 3"},
                {"input": "1\n9\n10", "output": "9"}
            ]
        },
        {
            "id": "merge_two_sorted_arrays",
            "title": "Merge Two Sorted Arrays",
            "topic": "Arrays",
            "description": "Merge two sorted arrays into one sorted array.",
            "description_full": "Given N, sorted A, M, sorted B, print merged sorted array of size N+M.",
            "input": "N then N integers then M then M integers",
            "output": "Merged sorted array",
            "example": "Input:\n3\n1 3 5\n2\n2 4\nOutput:\n1 2 3 4 5",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "3\n1 3 5\n2\n2 4", "output": "1 2 3 4 5"},
                {"input": "1\n1\n1\n2", "output": "1 2"},
                {"input": "0\n\n1\n5", "output": "5"}
            ]
        },
        {
            "id": "remove_duplicates_sorted_array",
            "title": "Remove Duplicates From Sorted Array",
            "topic": "Arrays",
            "description": "Given sorted array, remove duplicates and print unique elements.",
            "description_full": "Given N and sorted A, print distinct elements in order.",
            "input": "N then N integers",
            "output": "Unique elements",
            "example": "Input:\n6\n1 1 2 2 3 3\nOutput:\n1 2 3",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "6\n1 1 2 2 3 3", "output": "1 2 3"},
                {"input": "3\n5 5 5", "output": "5"},
                {"input": "1\n7", "output": "7"}
            ]
        },
        {
            "id": "product_of_array_except_self_small",
            "title": "Product of Array Except Self (small)",
            "topic": "Arrays",
            "description": "For each index produce product of all elements except at index (no division).",
            "description_full": "Given N small and array A, print N numbers where i-th is product of all Aj for j!=i.",
            "input": "N then N integers",
            "output": "N numbers",
            "example": "Input:\n3\n1 2 3\nOutput:\n6 3 2",
            "constraints": "N small, values small",
            "explanation": "",
            "tests": [
                {"input": "3\n1 2 3", "output": "6 3 2"},
                {"input": "2\n3 4", "output": "4 3"},
                {"input": "1\n5", "output": "1"}
            ]
        },
        {
            "id": "separate_even_odd",
            "title": "Separate Even and Odd Elements",
            "topic": "Arrays",
            "description": "Reorder array so evens precede odds (keep relative order).",
            "description_full": "Given N and array A, print array with all even elements first in original relative order followed by all odd elements in original order.",
            "input": "N then N integers",
            "output": "Reordered array",
            "example": "Input:\n6\n1 2 3 4 5 6\nOutput:\n2 4 6 1 3 5",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "6\n1 2 3 4 5 6", "output": "2 4 6 1 3 5"},
                {"input": "3\n2 4 6", "output": "2 4 6"},
                {"input": "3\n1 3 5", "output": "1 3 5"}
            ]
        },
        {
            "id": "largest_sum_contiguous_subarray_k",
            "title": "Max Sum of Subarray of Size K",
            "topic": "Arrays",
            "description": "Find maximum sum among all contiguous subarrays of length K.",
            "description_full": "Given N and array A and K (K<=N), print maximum sum of any contiguous subarray of length K.",
            "input": "N then N integers then K",
            "output": "Maximum sum",
            "example": "Input:\n5\n1 2 3 4 5\n2\nOutput:\n9",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5\n1 2 3 4 5\n2", "output": "9"},
                {"input": "3\n-1 -2 -3\n1", "output": "-1"},
                {"input": "4\n2 1 5 2\n3", "output": "8"}
            ]
        },
        {
            "id": "rotate_matrix_clockwise_once",
            "title": "Rotate Matrix 90° Clockwise (small)",
            "topic": "Arrays",
            "description": "Rotate NxN matrix 90 degrees clockwise.",
            "description_full": "Given N and NxN matrix, output matrix rotated 90 degrees clockwise. N small.",
            "input": "N then NxN integers",
            "output": "Rotated matrix",
            "example": "Input:\n2\n1 2\n3 4\nOutput:\n3 1\n4 2",
            "constraints": "N small",
            "explanation": "",
            "tests": [
                {"input": "2\n1 2\n3 4", "output": "3 1\n4 2"},
                {"input": "1\n9", "output": "9"},
                {"input": "3\n1 2 3\n4 5 6\n7 8 9", "output": "7 4 1\n8 5 2\n9 6 3"}
            ]
        }],
        "Patterns": [ {
            "id": "hollow_triangle",
            "title": "Hollow Right Triangle",
            "topic": "Patterns",
            "description": "Print hollow right-angled triangle of height N.",
            "description_full": "Given N>=2, print a right triangle with stars on border and spaces inside.",
            "input": "Integer N",
            "output": "N lines",
            "example": "Input:\n4\nOutput:\n*\n**\n* *\n****",
            "constraints": "N>=2",
            "explanation": "",
            "tests": [
                {"input": "4", "output": "*\n**\n* *\n****"},
                {"input": "2", "output": "*\n**"},
                {"input": "3", "output": "*\n**\n***"}
            ]
        },
        {
            "id": "number_pyramid_centered",
            "title": "Centered Number Pyramid",
            "topic": "Patterns",
            "description": "Print centered pyramid with numbers increasing then decreasing each row.",
            "description_full": "Given N, for i from 1..N print numbers 1..i..1 separated by spaces; approximate centered formatting ok.",
            "input": "Integer N",
            "output": "N rows",
            "example": "Input:\n3\nOutput:\n1\n1 2 1\n1 2 3 2 1",
            "constraints": "N small",
            "explanation": "",
            "tests": [
                {"input": "3", "output": "1\n1 2 1\n1 2 3 2 1"},
                {"input": "1", "output": "1"},
                {"input": "2", "output": "1\n1 2 1"}
            ]
        },
        {
            "id": "zigzag_numbers",
            "title": "Zigzag Numbers Pattern",
            "topic": "Patterns",
            "description": "Print zigzag number pattern for N rows.",
            "description_full": "Given N, print rows where odd rows increase 1..i and even rows decrease i..1 (space separated).",
            "input": "Integer N",
            "output": "N rows",
            "example": "Input:\n4\nOutput:\n1\n2 1\n1 2 3\n4 3 2 1",
            "constraints": "N small",
            "explanation": "",
            "tests": [
                {"input": "4", "output": "1\n2 1\n1 2 3\n4 3 2 1"},
                {"input": "1", "output": "1"},
                {"input": "2", "output": "1\n2 1"}
            ]
        },
        {
            "id": "diamond_pattern_stars",
            "title": "Diamond Pattern of Stars",
            "topic": "Patterns",
            "description": "Print diamond shape of stars for odd N.",
            "description_full": "Given odd N (height), print diamond pattern of stars (simplified formatting allowed).",
            "input": "Odd integer N",
            "output": "N rows",
            "example": "Input:\n3\nOutput:\n *\n***\n *",
            "constraints": "N odd and small",
            "explanation": "",
            "tests": [
                {"input": "3", "output": " *\n***\n *"},
                {"input": "1", "output": "*"},
                {"input": "5", "output": "  *\n ***\n*****\n ***\n  *"}
            ]
        },
        {
            "id": "checkerboard_pattern",
            "title": "Checkerboard Pattern",
            "topic": "Patterns",
            "description": "Print N x M checkerboard of '*' and ' '.",
            "description_full": "Given N and M, print an N by M grid where positions with (i+j) even contain '*' else space or '.' (choose a space).",
            "input": "N M",
            "output": "N lines",
            "example": "Input:\n2 3\nOutput:\n* *\n * ",
            "constraints": "N,M small",
            "explanation": "",
            "tests": [
                {"input": "2 3", "output": "* *\n * "},
                {"input": "1 1", "output": "*"},
                {"input": "3 3", "output": "* *\n * \n* *"}
            ]
        },
        {
            "id": "numeric_diamond",
            "title": "Numeric Diamond",
            "topic": "Patterns",
            "description": "Print numeric diamond shape for small N.",
            "description_full": "Given odd N, print diamond with increasing numbers up to center then mirror (formatting minimal).",
            "input": "Odd integer N",
            "output": "N rows",
            "example": "Input:\n3\nOutput:\n 1\n121\n 1",
            "constraints": "N small odd",
            "explanation": "",
            "tests": [
                {"input": "3", "output": " 1\n121\n 1"},
                {"input": "1", "output": "1"},
                {"input": "5", "output": "  1\n 121\n12321\n 121\n  1"}
            ]
        },
        {
            "id": "mirror_triangle",
            "title": "Mirror Right Triangle",
            "topic": "Patterns",
            "description": "Print mirrored right triangle (right aligned).",
            "description_full": "Given N, print N rows where row i has N-i spaces then i stars.",
            "input": "Integer N",
            "output": "N rows",
            "example": "Input:\n3\nOutput:\n  *\n **\n***",
            "constraints": "N>0",
            "explanation": "",
            "tests": [
                {"input": "3", "output": "  *\n **\n***"},
                {"input": "1", "output": "*"},
                {"input": "2", "output": " *\n**"}
            ]
        },
        {
            "id": "pascals_triangle_rows",
            "title": "Print First K Rows of Pascal's Triangle",
            "topic": "Patterns",
            "description": "Print first K rows (space-separated) of Pascal's Triangle.",
            "description_full": "Given K, print rows 0..K-1 of Pascal's triangle, each row numbers separated by spaces.",
            "input": "Integer K",
            "output": "K lines",
            "example": "Input:\n3\nOutput:\n1\n1 1\n1 2 1",
            "constraints": "K small",
            "explanation": "",
            "tests": [
                {"input": "3", "output": "1\n1 1\n1 2 1"},
                {"input": "1", "output": "1"},
                {"input": "4", "output": "1\n1 1\n1 2 1\n1 3 3 1"}
            ]
        }],
        "Functions": [{
            "id": "gcd_multiple_numbers",
            "title": "GCD of Multiple Numbers",
            "topic": "Functions",
            "description": "Compute gcd of N numbers using function.",
            "description_full": "Given N and N integers, compute gcd of all numbers using a helper function.",
            "input": "N then N integers",
            "output": "GCD",
            "example": "Input:\n3\n12 18 30\nOutput:\n6",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "3\n12 18 30", "output": "6"},
                {"input": "2\n7 13", "output": "1"},
                {"input": "1\n9", "output": "9"}
            ]
        },
        {
            "id": "power_mod_function",
            "title": "Modular Exponentiation (Function)",
            "topic": "Functions",
            "description": "Compute (a^b) % m using fast exponentiation function.",
            "description_full": "Given a b m, compute a^b mod m using a helper fast power function.",
            "input": "a b m",
            "output": "Value",
            "example": "Input:\n2 10 1000\nOutput:\n24",
            "constraints": "b >= 0",
            "explanation": "",
            "tests": [
                {"input": "2 10 1000", "output": "24"},
                {"input": "3 0 5", "output": "1"},
                {"input": "10 1 7", "output": "3"}
            ]
        },
        {
            "id": "is_palindrome_ignoring_nonalpha",
            "title": "String Palindrome Ignore Non-alpha",
            "topic": "Functions",
            "description": "Check palindrome ignoring non-letter characters and case.",
            "description_full": "Given string S, consider only alphabetic characters and ignore case; print YES if palindrome else NO. Use helper to normalize string.",
            "input": "String S",
            "output": "YES or NO",
            "example": "Input:\nA man, a plan, a canal: Panama\nOutput:\nYES",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "A man, a plan, a canal: Panama", "output": "YES"},
                {"input": "Hello, olleH", "output": "YES"},
                {"input": "abc", "output": "NO"}
            ]
        },
        {
            "id": "is_sorted_function",
            "title": "Is Sorted Using Function",
            "topic": "Functions",
            "description": "Encapsulate sorted check into a function.",
            "description_full": "Given N and array A, use helper function to return YES if A is non-decreasing else NO.",
            "input": "N then N integers",
            "output": "YES or NO",
            "example": "Input:\n3\n1 2 3\nOutput:\nYES",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "3\n1 2 3", "output": "YES"},
                {"input": "3\n2 1 3", "output": "NO"},
                {"input": "1\n5", "output": "YES"}
            ]
        },
        {
            "id": "count_set_bits_function",
            "title": "Count Set Bits Using Function",
            "topic": "Functions",
            "description": "Use helper to count set bits in integer.",
            "description_full": "Given integer N, print number of ones in binary representation using a helper function.",
            "input": "Integer N",
            "output": "Count",
            "example": "Input:\n13\nOutput:\n3",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "13", "output": "3"},
                {"input": "0", "output": "0"},
                {"input": "1023", "output": "10"}
            ]
        },
        {
            "id": "is_armstrong_using_function",
            "title": "Armstrong Using Function",
            "topic": "Functions",
            "description": "Use helper to test Armstrong property.",
            "description_full": "Given N, use helper to test if N equals sum of its digits^k where k is number of digits.",
            "input": "Integer N",
            "output": "YES or NO",
            "example": "Input:\n9474\nOutput:\nYES",
            "constraints": "N small",
            "explanation": "",
            "tests": [
                {"input": "9474", "output": "YES"},
                {"input": "153", "output": "YES"},
                {"input": "100", "output": "NO"}
            ]
        },
        {
            "id": "euclid_lcm_function",
            "title": "LCM Using GCD Function",
            "topic": "Functions",
            "description": "Compute LCM using gcd helper function.",
            "description_full": "Given A and B, compute LCM = A / gcd(A,B) * B, using helper gcd function.",
            "input": "Two integers A B",
            "output": "LCM",
            "example": "Input:\n4 6\nOutput:\n12",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "4 6", "output": "12"},
                {"input": "5 5", "output": "5"},
                {"input": "3 7", "output": "21"}
            ]
        },
        {
            "id": "is_perfect_square_function",
            "title": "Check Perfect Square Using Function",
            "topic": "Functions",
            "description": "Use helper to detect perfect squares efficiently.",
            "description_full": "Given N, print YES if perfect square else NO. Use helper that checks integer sqrt.",
            "input": "Integer N",
            "output": "YES or NO",
            "example": "Input:\n49\nOutput:\nYES",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "49", "output": "YES"},
                {"input": "50", "output": "NO"},
                {"input": "0", "output": "YES"}
            ]
        },
        {
            "id": "fibonacci_nth_using_function",
            "title": "Nth Fibonacci Using Function (iterative)",
            "topic": "Functions",
            "description": "Return nth Fibonacci number (0-indexed) using helper iterative function.",
            "description_full": "Given n (small), print nth Fibonacci number (F0=0,F1=1).",
            "input": "Integer n",
            "output": "Fibonacci number",
            "example": "Input:\n5\nOutput:\n5",
            "constraints": "n small (<=40)",
            "explanation": "",
            "tests": [
                {"input": "5", "output": "5"},
                {"input": "0", "output": "0"},
                {"input": "1", "output": "1"}
            ]
        }],
        "Searching": [{
            "id": "binary_search_sorted_array",
            "title": "Binary Search Index",
            "topic": "Searching",
            "description": "Find index of X in sorted array using binary search.",
            "description_full": "Given N and sorted A and X, print 0-based index of X or -1 if not found (use binary search).",
            "input": "N then N integers then X",
            "output": "Index or -1",
            "example": "Input:\n5\n1 2 3 4 5\n3\nOutput:\n2",
            "constraints": "Array sorted",
            "explanation": "",
            "tests": [
                {"input": "5\n1 2 3 4 5\n3", "output": "2"},
                {"input": "3\n1 2 3\n4", "output": "-1"},
                {"input": "1\n7\n7", "output": "0"}
            ]
        },
        {
            "id": "first_pair_with_sum_two_pointer",
            "title": "First Pair Sum (Two-pointer)",
            "topic": "Searching",
            "description": "On sorted array, find any pair with sum X using two-pointer.",
            "description_full": "Given sorted array A and X, print indices i j (0-based) of pair with Ai+Aj=X else -1 -1.",
            "input": "N then sorted N integers then X",
            "output": "i j or -1 -1",
            "example": "Input:\n5\n1 2 3 4 5\n9\nOutput:\n3 4",
            "constraints": "Array sorted",
            "explanation": "",
            "tests": [
                {"input": "5\n1 2 3 4 5\n9", "output": "3 4"},
                {"input": "3\n1 1 1\n2", "output": "0 1"},
                {"input": "4\n2 7 11 15\n9", "output": "0 1"}
            ]
        },
        {
            "id": "first_missing_positive_small",
            "title": "First Missing Positive (small N)",
            "topic": "Searching",
            "description": "Find smallest positive integer missing from array (N small).",
            "description_full": "Given N and A, find smallest positive integer not present; constraints small so brute force okay.",
            "input": "N then N integers",
            "output": "Smallest missing positive int",
            "example": "Input:\n3\n1 2 4\nOutput:\n3",
            "constraints": "N small",
            "explanation": "",
            "tests": [
                {"input": "3\n1 2 4", "output": "3"},
                {"input": "2\n2 3", "output": "1"},
                {"input": "1\n1", "output": "2"}
            ]
        },
        {
            "id": "find_peak_element",
            "title": "Find Peak Element",
            "topic": "Searching",
            "description": "Find any index i which is a peak (A[i] >= neighbors).",
            "description_full": "Given N and array A, print index of any peak element (0-based). For endpoints, only one neighbor considered.",
            "input": "N then N integers",
            "output": "Index",
            "example": "Input:\n5\n1 3 2 1 4\nOutput:\n1",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5\n1 3 2 1 4", "output": "1"},
                {"input": "1\n10", "output": "0"},
                {"input": "2\n2 1", "output": "0"}
            ]
        },
        {
            "id": "count_elements_less_than_x_sorted",
            "title": "Count Elements < X in Sorted Array",
            "topic": "Searching",
            "description": "On sorted array, count elements < X using binary search.",
            "description_full": "Given sorted array A and X, print count of elements strictly less than X.",
            "input": "N then N integers then X",
            "output": "Count",
            "example": "Input:\n5\n1 2 3 4 5\n4\nOutput:\n3",
            "constraints": "Array sorted",
            "explanation": "",
            "tests": [
                {"input": "5\n1 2 3 4 5\n4", "output": "3"},
                {"input": "3\n1 1 2\n1", "output": "0"},
                {"input": "4\n-2 0 1 3\n2", "output": "3"}
            ]
        },
        {
            "id": "find_rotation_point_sorted_rotated",
            "title": "Find Rotation Index in Rotated Sorted Array",
            "topic": "Searching",
            "description": "Find smallest element index in rotated sorted array.",
            "description_full": "Given N and rotated sorted array A (originally increasing), find index of the smallest element (rotation point) using binary search.",
            "input": "N then N integers",
            "output": "Index",
            "example": "Input:\n5\n4 5 1 2 3\nOutput:\n2",
            "constraints": "N >=1",
            "explanation": "",
            "tests": [
                {"input": "5\n4 5 1 2 3", "output": "2"},
                {"input": "3\n1 2 3", "output": "0"},
                {"input": "4\n2 3 4 1", "output": "3"}
            ]
        },
        {
            "id": "find_smallest_missing_in_sorted_range",
            "title": "Smallest Missing in Sorted 1..N Array",
            "topic": "Searching",
            "description": "Given sorted distinct positives, find smallest missing positive number starting from 1.",
            "description_full": "Given N and sorted distinct array of positives, find smallest missing positive starting from 1.",
            "input": "N then N integers",
            "output": "Smallest missing positive",
            "example": "Input:\n3\n1 2 4\nOutput:\n3",
            "constraints": "Array sorted distinct positive",
            "explanation": "",
            "tests": [
                {"input": "3\n1 2 4", "output": "3"},
                {"input": "2\n2 3", "output": "1"},
                {"input": "3\n1 2 3", "output": "4"}
            ]
        },
        {
            "id": "find_shortest_distance_to_target",
            "title": "Shortest Distance to Target Value",
            "topic": "Searching",
            "description": "Find minimum absolute difference between target and any array element.",
            "description_full": "Given N, array A and X, print minimal |Ai - X|.",
            "input": "N then N integers then X",
            "output": "Minimum absolute difference",
            "example": "Input:\n5\n1 3 6 9 12\n8\nOutput:\n2",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5\n1 3 6 9 12\n8", "output": "2"},
                {"input": "3\n1 2 3\n5", "output": "2"},
                {"input": "1\n10\n10", "output": "0"}
            ]
        }],
        "Sorting": [{
            "id": "count_pairs_with_diff_k",
            "title": "Count Pairs with Difference K",
            "topic": "Sorting",
            "description": "Count number of pairs (i<j) with |Ai-Aj| = K.",
            "description_full": "Given N and array A and integer K, count number of unordered pairs whose absolute difference equals K. For Easy constraints N small enough for n log n or n^2.",
            "input": "N then N integers then K",
            "output": "Count",
            "example": "Input:\n5\n1 5 3 4 2\n2\nOutput:\n3",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5\n1 5 3 4 2\n2", "output": "3"},
                {"input": "3\n1 1 1\n0", "output": "3"},
                {"input": "4\n1 2 3 4\n5", "output": "0"}
            ]
        },
        {
            "id": "sort_by_frequency_then_value",
            "title": "Sort by Frequency Then Value",
            "topic": "Sorting",
            "description": "Sort elements by frequency descending, ties by value ascending.",
            "description_full": "Given N and array A, print elements sorted primarily by decreasing frequency then increasing value.",
            "input": "N then N integers",
            "output": "Sorted list",
            "example": "Input:\n6\n4 5 6 5 4 3\nOutput:\n4 4 5 5 3 6",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "6\n4 5 6 5 4 3", "output": "4 4 5 5 3 6"},
                {"input": "3\n1 1 2", "output": "1 1 2"},
                {"input": "4\n2 3 2 3", "output": "2 2 3 3"}
            ]
        },
        {
            "id": "k_closest_elements_sorted",
            "title": "K Closest Elements to X",
            "topic": "Sorting",
            "description": "From sorted array, print k elements closest to X (by absolute difference) in ascending order.",
            "description_full": "Given sorted A, X and k, choose k elements with minimal |Ai-X|; if tie choose smaller Ai. Print chosen elements sorted ascending.",
            "input": "N then N integers then X then k",
            "output": "k elements",
            "example": "Input:\n5\n1 2 3 4 5\n3 2\nOutput:\n2 3",
            "constraints": "Array sorted",
            "explanation": "",
            "tests": [
                {"input": "5\n1 2 3 4 5\n3 2", "output": "2 3"},
                {"input": "4\n1 2 3 4\n2 1", "output": "2"},
                {"input": "3\n10 20 30\n25 1", "output": "20"}
            ]
        },
        {
            "id": "find_mode_value",
            "title": "Find Mode (Most Frequent)",
            "topic": "Sorting",
            "description": "Determine most frequent value; tie -> smallest value.",
            "description_full": "Given N and array A, print the value that appears most frequently; ties resolved to smallest value.",
            "input": "N then N integers",
            "output": "Mode value",
            "example": "Input:\n6\n1 2 2 3 3 3\nOutput:\n3",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "6\n1 2 2 3 3 3", "output": "3"},
                {"input": "3\n2 2 1", "output": "2"},
                {"input": "4\n1 1 2 2", "output": "1"}
            ]
        },
        {
            "id": "sort_by_digit_sum",
            "title": "Sort by Digit Sum",
            "topic": "Sorting",
            "description": "Sort numbers by sum of digits ascending; tie by value.",
            "description_full": "Given N and array A, sort by (digit sum, value) and print.",
            "input": "N then N integers",
            "output": "Sorted array",
            "example": "Input:\n4\n10 2 11 20\nOutput:\n2 10 11 20",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "4\n10 2 11 20", "output": "2 10 11 20"},
                {"input": "3\n1 10 100", "output": "1 10 100"},
                {"input": "3\n12 21 3", "output": "3 12 21"}
            ]
        },
        {
            "id": "sort_by_absolute_difference",
            "title": "Sort by Absolute Difference from X",
            "topic": "Sorting",
            "description": "Sort array by |Ai - X| asc; tie by Ai asc.",
            "description_full": "Given N array A and integer X, sort A by absolute difference from X; ties by Ai.",
            "input": "N then N integers then X",
            "output": "Sorted array",
            "example": "Input:\n5\n1 4 2 5 3\n3\nOutput:\n3 2 4 1 5",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "5\n1 4 2 5 3\n3", "output": "3 2 4 1 5"},
                {"input": "3\n2 2 2\n1", "output": "2 2 2"},
                {"input": "1\n7\n5", "output": "7"}
            ]
        },
        {
            "id": "sort_pairs_by_second",
            "title": "Sort Pairs by Second Value",
            "topic": "Sorting",
            "description": "Given pairs, sort by second element ascending, tie by first.",
            "description_full": "Given N pairs (a,b), print pairs sorted by b, then a.",
            "input": "N then N pairs (a b each line)",
            "output": "Sorted pairs lines",
            "example": "Input:\n3\n1 3\n2 1\n3 2\nOutput:\n2 1\n3 2\n1 3",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "3\n1 3\n2 1\n3 2", "output": "2 1\n3 2\n1 3"},
                {"input": "1\n5 5", "output": "5 5"},
                {"input": "2\n1 1\n1 2", "output": "1 1\n1 2"}
            ]
        },
        {
            "id": "sort_strings_by_length",
            "title": "Sort Strings by Length",
            "topic": "Sorting",
            "description": "Sort list of words by length ascending, ties lexicographically.",
            "description_full": "Given N and N words, print them ordered by (length, lexicographic).",
            "input": "N then N words",
            "output": "Sorted words",
            "example": "Input:\n3\napple a abc\nOutput:\na abc apple",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "3\napple a abc", "output": "a abc apple"},
                {"input": "2\naa a", "output": "a aa"},
                {"input": "1\nhello", "output": "hello"}
            ]
        }],
        "Matrices": [{
            "id": "matrix_row_col_transpose",
            "title": "Transpose Non-square Matrix",
            "topic": "Matrices",
            "description": "Transpose an R x C matrix to C x R.",
            "description_full": "Given R C and R rows with C integers each, print the transposed matrix (C rows, each with R integers).",
            "input": "R C then matrix R rows",
            "output": "Transposed matrix",
            "example": "Input:\n2 3\n1 2 3\n4 5 6\nOutput:\n1 4\n2 5\n3 6",
            "constraints": "R,C small",
            "explanation": "",
            "tests": [
                {"input": "2 3\n1 2 3\n4 5 6", "output": "1 4\n2 5\n3 6"},
                {"input": "1 1\n9", "output": "9"},
                {"input": "3 1\n1\n2\n3", "output": "1 2 3"}
            ]
        },
        {
            "id": "matrix_addition",
            "title": "Add Two Matrices",
            "topic": "Matrices",
            "description": "Add two R x C matrices element-wise.",
            "description_full": "Given R C then first matrix then second matrix, print their sum matrix.",
            "input": "R C then matrix A then matrix B",
            "output": "Sum matrix",
            "example": "Input:\n2 2\n1 2\n3 4\n5 6\n7 8\nOutput:\n6 8\n10 12",
            "constraints": "R,C small",
            "explanation": "",
            "tests": [
                {"input": "2 2\n1 2\n3 4\n5 6\n7 8", "output": "6 8\n10 12"},
                {"input": "1 1\n1\n2\nOutput: 3", "output": "3"},
                {"input": "2 1\n1\n2\n3\n4", "output": "4\n6"}
            ]
        },
        {
            "id": "matrix_scalar_multiplication",
            "title": "Scalar Multiply Matrix",
            "topic": "Matrices",
            "description": "Multiply every element of matrix by scalar K.",
            "description_full": "Given R C then matrix then K, print matrix where each element multiplied by K.",
            "input": "R C then matrix then K",
            "output": "Scaled matrix",
            "example": "Input:\n2 2\n1 2\n3 4\n2\nOutput:\n2 4\n6 8",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "2 2\n1 2\n3 4\n2", "output": "2 4\n6 8"},
                {"input": "1 1\n5\n3", "output": "15"},
                {"input": "2 3\n1 0 2\n3 4 5\n0", "output": "0 0 0\n0 0 0"}
            ]
        },
        {
            "id": "matrix_trace",
            "title": "Trace of Square Matrix",
            "topic": "Matrices",
            "description": "Sum of diagonal elements of NxN matrix.",
            "description_full": "Given N and NxN matrix, print sum of main diagonal elements.",
            "input": "N then NxN integers",
            "output": "Trace",
            "example": "Input:\n3\n1 2 3\n4 5 6\n7 8 9\nOutput:\n15",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "3\n1 2 3\n4 5 6\n7 8 9", "output": "15"},
                {"input": "1\n9", "output": "9"},
                {"input": "2\n1 2\n3 4", "output": "5"}
            ]
        },
        {
            "id": "matrix_saddle_point",
            "title": "Find Saddle Point",
            "topic": "Matrices",
            "description": "Find any element that is min in its row and max in its column.",
            "description_full": "Given R C matrix, find any saddle point (min in row and max in col) and print its value; if none print 'NONE'.",
            "input": "R C then matrix",
            "output": "Value or NONE",
            "example": "Input:\n3 3\n1 2 3\n4 5 6\n7 8 9\nOutput:\nNONE",
            "constraints": "R,C small",
            "explanation": "",
            "tests": [
                {"input": "2 2\n1 2\n3 4", "output": "NONE"},
                {"input": "3 3\n3 1 3\n2 4 2\n5 6 5", "output": "4"},
                {"input": "1 1\n7", "output": "7"}
            ]
        },
        {
            "id": "matrix_rotate_180",
            "title": "Rotate Matrix 180 Degrees",
            "topic": "Matrices",
            "description": "Rotate matrix 180 degrees (flip both axes).",
            "description_full": "Given R C then matrix, output matrix rotated by 180 degrees.",
            "input": "R C then matrix",
            "output": "Rotated matrix",
            "example": "Input:\n2 2\n1 2\n3 4\nOutput:\n4 3\n2 1",
            "constraints": "R,C small",
            "explanation": "",
            "tests": [
                {"input": "2 2\n1 2\n3 4", "output": "4 3\n2 1"},
                {"input": "1 3\n1 2 3", "output": "3 2 1"},
                {"input": "3 1\n1\n2\n3", "output": "3\n2\n1"}
            ]
        },
        {
            "id": "matrix_is_symmetric",
            "title": "Matrix Symmetric Check",
            "topic": "Matrices",
            "description": "Check if NxN matrix is symmetric (A^T == A).",
            "description_full": "Given N and NxN matrix, print YES if matrix equals its transpose else NO.",
            "input": "N then NxN integers",
            "output": "YES or NO",
            "example": "Input:\n2\n1 2\n2 1\nOutput:\nYES",
            "constraints": "",
            "explanation": "",
            "tests": [
                {"input": "2\n1 2\n2 1", "output": "YES"},
                {"input": "2\n1 0\n1 1", "output": "NO"},
                {"input": "1\n5", "output": "YES"}
            ]
        },
        {
            "id": "matrix_spiral_order_small",
            "title": "Print Matrix in Spiral Order (small)",
            "topic": "Matrices",
            "description": "Output elements of NxM matrix in clockwise spiral order.",
            "description_full": "Given R C and matrix R x C (small), print its elements in spiral order separated by spaces.",
            "input": "R C then matrix",
            "output": "Single line with elements in spiral order",
            "example": "Input:\n2 2\n1 2\n3 4\nOutput:\n1 2 4 3",
            "constraints": "R,C small",
            "explanation": "",
            "tests": [
                {"input": "2 2\n1 2\n3 4", "output": "1 2 4 3"},
                {"input": "1 3\n1 2 3", "output": "1 2 3"},
                {"input": "3 3\n1 2 3\n4 5 6\n7 8 9", "output": "1 2 3 6 9 8 7 4 5"}
            ]
        },
        {
            "id": "matrix_max_2x2_submatrix_sum",
            "title": "Max Sum 2x2 Submatrix",
            "topic": "Matrices",
            "description": "Find maximum sum among all 2x2 submatrices.",
            "description_full": "Given R C and matrix, compute maximum sum over all contiguous 2x2 submatrices (R,C >=2).",
            "input": "R C then matrix",
            "output": "Max sum",
            "example": "Input:\n3 3\n1 2 3\n4 5 6\n7 8 9\nOutput:\n28",
            "constraints": "R,C >=2",
            "explanation": "",
            "tests": [
                {"input": "3 3\n1 2 3\n4 5 6\n7 8 9", "output": "28"},
                {"input": "2 2\n1 1\n1 1", "output": "4"},
                {"input": "2 3\n1 2 3\n4 5 6", "output": "18"}
            ]
        }

    ]
    },

    "Medium": {
        "Loops": [

    {
        "id": "loop_sum_first_n",
        "title": "Sum of First N Numbers",
        "topic": "Loops",
        "description": "Calculate sum from 1 to N.",
        "description_full": "Given an integer N, calculate the sum of numbers from 1 to N using a loop.",
        "input": "Integer N",
        "output": "Sum",
        "example": "Input:\n5\nOutput:\n15",
        "constraints": "N >= 1",
        "explanation": "",
        "tests": [
            {"input": "5", "output": "15"},
            {"input": "1", "output": "1"},
            {"input": "10", "output": "55"}
        ]
    },

    {
        "id": "loop_factorial",
        "title": "Factorial Using Loop",
        "topic": "Loops",
        "description": "Compute factorial of a number.",
        "description_full": "Given integer N, compute N factorial using a loop.",
        "input": "Integer N",
        "output": "Factorial",
        "example": "Input:\n5\nOutput:\n120",
        "constraints": "0 <= N <= 20",
        "explanation": "",
        "tests": [
            {"input": "5", "output": "120"},
            {"input": "0", "output": "1"},
            {"input": "7", "output": "5040"}
        ]
    },

    {
        "id": "loop_reverse_number",
        "title": "Reverse a Number",
        "topic": "Loops",
        "description": "Reverse digits of a number.",
        "description_full": "Given a non-negative integer N, reverse its digits using a loop.",
        "input": "Integer N",
        "output": "Reversed number",
        "example": "Input:\n120\nOutput:\n21",
        "constraints": "N >= 0",
        "explanation": "",
        "tests": [
            {"input": "120", "output": "21"},
            {"input": "0", "output": "0"},
            {"input": "987", "output": "789"}
        ]
    },

    {
        "id": "loop_count_digits",
        "title": "Count Digits",
        "topic": "Loops",
        "description": "Count number of digits.",
        "description_full": "Given integer N, count how many digits it has using loops.",
        "input": "Integer N",
        "output": "Digit count",
        "example": "Input:\n12345\nOutput:\n5",
        "constraints": "N >= 0",
        "explanation": "",
        "tests": [
            {"input": "12345", "output": "5"},
            {"input": "9", "output": "1"},
            {"input": "1000", "output": "4"}
        ]
    },

    {
        "id": "loop_sum_digits",
        "title": "Sum of Digits",
        "topic": "Loops",
        "description": "Calculate sum of digits.",
        "description_full": "Given integer N, calculate sum of its digits using loops.",
        "input": "Integer N",
        "output": "Sum",
        "example": "Input:\n305\nOutput:\n8",
        "constraints": "N >= 0",
        "explanation": "",
        "tests": [
            {"input": "305", "output": "8"},
            {"input": "0", "output": "0"},
            {"input": "999", "output": "27"}
        ]
    },

    {
        "id": "loop_fibonacci_series",
        "title": "Fibonacci Series",
        "topic": "Loops",
        "description": "Print Fibonacci numbers.",
        "description_full": "Given integer N, print first N Fibonacci numbers using a loop.",
        "input": "Integer N",
        "output": "Fibonacci series",
        "example": "Input:\n5\nOutput:\n0 1 1 2 3",
        "constraints": "N >= 1",
        "explanation": "",
        "tests": [
            {"input": "1", "output": "0"},
            {"input": "2", "output": "0 1"},
            {"input": "5", "output": "0 1 1 2 3"}
        ]
    },

    {
        "id": "loop_check_prime",
        "title": "Check Prime Number",
        "topic": "Loops",
        "description": "Check if number is prime.",
        "description_full": "Given integer N, check whether it is a prime number using loops.",
        "input": "Integer N",
        "output": "YES or NO",
        "example": "Input:\n7\nOutput:\nYES",
        "constraints": "N >= 1",
        "explanation": "",
        "tests": [
            {"input": "7", "output": "YES"},
            {"input": "1", "output": "NO"},
            {"input": "12", "output": "NO"}
        ]
    },

    {
        "id": "loop_multiplication_table",
        "title": "Multiplication Table",
        "topic": "Loops",
        "description": "Print multiplication table.",
        "description_full": "Given integer N, print multiplication table from 1 to 10.",
        "input": "Integer N",
        "output": "10 space-separated numbers",
        "example": "Input:\n2\nOutput:\n2 4 6 8 10 12 14 16 18 20",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "2", "output": "2 4 6 8 10 12 14 16 18 20"},
            {"input": "1", "output": "1 2 3 4 5 6 7 8 9 10"},
            {"input": "5", "output": "5 10 15 20 25 30 35 40 45 50"}
        ]
    },

    {
        "id": "loop_count_even",
        "title": "Count Even Numbers",
        "topic": "Loops",
        "description": "Count even numbers from 1 to N.",
        "description_full": "Given integer N, count how many even numbers exist between 1 and N.",
        "input": "Integer N",
        "output": "Count",
        "example": "Input:\n10\nOutput:\n5",
        "constraints": "N >= 1",
        "explanation": "",
        "tests": [
            {"input": "10", "output": "5"},
            {"input": "1", "output": "0"},
            {"input": "6", "output": "3"}
        ]
    },

    {
        "id": "loop_count_odd",
        "title": "Count Odd Numbers",
        "topic": "Loops",
        "description": "Count odd numbers from 1 to N.",
        "description_full": "Given integer N, count how many odd numbers exist between 1 and N.",
        "input": "Integer N",
        "output": "Count",
        "example": "Input:\n7\nOutput:\n4",
        "constraints": "N >= 1",
        "explanation": "",
        "tests": [
            {"input": "7", "output": "4"},
            {"input": "1", "output": "1"},
            {"input": "8", "output": "4"}
        ]
    }

],
        "Conditionals": [

    {
        "id": "cond_triangle_validity",
        "title": "Triangle Validity",
        "topic": "Conditionals",
        "description": "Check whether three sides form a triangle.",
        "description_full": "Given three integers A, B, and C representing sides, check if they can form a valid triangle.",
        "input": "Three integers A B C",
        "output": "YES or NO",
        "example": "Input:\n3 4 5\nOutput:\nYES",
        "constraints": "A, B, C > 0",
        "explanation": "",
        "tests": [
            {"input": "3 4 5", "output": "YES"},
            {"input": "1 2 3", "output": "NO"},
            {"input": "5 5 5", "output": "YES"}
        ]
    },

    {
        "id": "cond_triangle_type",
        "title": "Triangle Type",
        "topic": "Conditionals",
        "description": "Determine type of triangle.",
        "description_full": "Given sides of a triangle, determine whether it is Equilateral, Isosceles, or Scalene.",
        "input": "Three integers A B C",
        "output": "Equilateral / Isosceles / Scalene",
        "example": "Input:\n5 5 5\nOutput:\nEquilateral",
        "constraints": "Valid triangle",
        "explanation": "",
        "tests": [
            {"input": "5 5 5", "output": "Equilateral"},
            {"input": "5 5 3", "output": "Isosceles"},
            {"input": "3 4 5", "output": "Scalene"}
        ]
    },

    {
        "id": "cond_leap_year",
        "title": "Leap Year Check",
        "topic": "Conditionals",
        "description": "Check if year is leap year.",
        "description_full": "Given a year Y, check whether it is a leap year according to Gregorian calendar rules.",
        "input": "Integer Y",
        "output": "YES or NO",
        "example": "Input:\n2024\nOutput:\nYES",
        "constraints": "Y >= 1",
        "explanation": "",
        "tests": [
            {"input": "2024", "output": "YES"},
            {"input": "1900", "output": "NO"},
            {"input": "2000", "output": "YES"}
        ]
    },

    {
        "id": "cond_quadratic_roots",
        "title": "Nature of Quadratic Roots",
        "topic": "Conditionals",
        "description": "Determine nature of roots.",
        "description_full": "Given coefficients a, b, c of a quadratic equation, determine the nature of its roots.",
        "input": "Three integers a b c",
        "output": "Real and Distinct / Real and Equal / Imaginary",
        "example": "Input:\n1 -5 6\nOutput:\nReal and Distinct",
        "constraints": "a != 0",
        "explanation": "",
        "tests": [
            {"input": "1 -5 6", "output": "Real and Distinct"},
            {"input": "1 -2 1", "output": "Real and Equal"},
            {"input": "1 2 5", "output": "Imaginary"}
        ]
    },

    {
        "id": "cond_grade_calculation",
        "title": "Grade Calculation",
        "topic": "Conditionals",
        "description": "Assign grade based on marks.",
        "description_full": "Given marks (0–100), assign grade A, B, C, D, or F based on conditions.",
        "input": "Integer marks",
        "output": "Grade",
        "example": "Input:\n85\nOutput:\nB",
        "constraints": "0 <= marks <= 100",
        "explanation": "",
        "tests": [
            {"input": "95", "output": "A"},
            {"input": "70", "output": "C"},
            {"input": "45", "output": "F"}
        ]
    },

    {
        "id": "cond_sign_of_number",
        "title": "Sign of Number",
        "topic": "Conditionals",
        "description": "Determine sign of a number.",
        "description_full": "Given integer N, determine whether it is Positive, Negative, or Zero.",
        "input": "Integer N",
        "output": "POSITIVE / NEGATIVE / ZERO",
        "example": "Input:\n-5\nOutput:\nNEGATIVE",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "-5", "output": "NEGATIVE"},
            {"input": "0", "output": "ZERO"},
            {"input": "10", "output": "POSITIVE"}
        ]
    },

    {
        "id": "cond_even_odd",
        "title": "Even or Odd",
        "topic": "Conditionals",
        "description": "Check if number is even or odd.",
        "description_full": "Given integer N, check whether it is even or odd.",
        "input": "Integer N",
        "output": "EVEN or ODD",
        "example": "Input:\n4\nOutput:\nEVEN",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "4", "output": "EVEN"},
            {"input": "7", "output": "ODD"},
            {"input": "0", "output": "EVEN"}
        ]
    },

    {
        "id": "cond_vowel_consonant",
        "title": "Vowel or Consonant",
        "topic": "Conditionals",
        "description": "Check vowel or consonant.",
        "description_full": "Given a single alphabet character, check whether it is a vowel or a consonant.",
        "input": "Single character",
        "output": "VOWEL or CONSONANT",
        "example": "Input:\na\nOutput:\nVOWEL",
        "constraints": "Alphabetic character",
        "explanation": "",
        "tests": [
            {"input": "a", "output": "VOWEL"},
            {"input": "B", "output": "CONSONANT"},
            {"input": "U", "output": "VOWEL"}
        ]
    },

    {
        "id": "cond_max_of_three",
        "title": "Maximum of Three Numbers",
        "topic": "Conditionals",
        "description": "Find maximum among three numbers.",
        "description_full": "Given three integers, determine the maximum using conditional statements.",
        "input": "Three integers A B C",
        "output": "Maximum value",
        "example": "Input:\n3 7 5\nOutput:\n7",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "3 7 5", "output": "7"},
            {"input": "9 2 4", "output": "9"},
            {"input": "-1 -5 -2", "output": "-1"}
        ]
    },

    {
        "id": "cond_age_category",
        "title": "Age Category",
        "topic": "Conditionals",
        "description": "Determine age category.",
        "description_full": "Given age, determine whether the person is Child, Teen, Adult, or Senior.",
        "input": "Integer age",
        "output": "Category",
        "example": "Input:\n25\nOutput:\nAdult",
        "constraints": "Age >= 0",
        "explanation": "",
        "tests": [
            {"input": "10", "output": "Child"},
            {"input": "16", "output": "Teen"},
            {"input": "65", "output": "Senior"}
        ]
    }

],
        "Strings": [

    {
        "id": "str_longest_word",
        "title": "Longest Word in Sentence",
        "topic": "Strings",
        "description": "Find the longest word in a sentence.",
        "description_full": "Given a sentence S, find and print the longest word. If multiple words have the same maximum length, print the first one.",
        "input": "String S",
        "output": "Longest word",
        "example": "Input:\nI love competitive coding\nOutput:\ncompetitive",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "I love competitive coding", "output": "competitive"},
            {"input": "hello world", "output": "hello"},
            {"input": "a bb ccc", "output": "ccc"}
        ]
    },

    {
        "id": "str_word_count",
        "title": "Word Count",
        "topic": "Strings",
        "description": "Count words in a sentence.",
        "description_full": "Given a sentence S, count the number of words separated by spaces.",
        "input": "String S",
        "output": "Word count",
        "example": "Input:\nI love coding\nOutput:\n3",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "I love coding", "output": "3"},
            {"input": "Hello World", "output": "2"},
            {"input": "one", "output": "1"}
        ]
    },

    {
        "id": "str_character_frequency",
        "title": "Character Frequency",
        "topic": "Strings",
        "description": "Count frequency of each character.",
        "description_full": "Given string S, count frequency of each character (case-sensitive).",
        "input": "String S",
        "output": "Character frequencies",
        "example": "Input:\nbanana\nOutput:\nb:1 a:3 n:2",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "banana", "output": "b:1 a:3 n:2"},
            {"input": "aab", "output": "a:2 b:1"},
            {"input": "x", "output": "x:1"}
        ]
    },

    {
        "id": "str_remove_duplicates",
        "title": "Remove Duplicate Characters",
        "topic": "Strings",
        "description": "Remove duplicate characters from string.",
        "description_full": "Given string S, remove duplicate characters while keeping first occurrences.",
        "input": "String S",
        "output": "Modified string",
        "example": "Input:\nbanana\nOutput:\nban",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "banana", "output": "ban"},
            {"input": "aaaa", "output": "a"},
            {"input": "abc", "output": "abc"}
        ]
    },

    {
        "id": "str_most_frequent_char",
        "title": "Most Frequent Character",
        "topic": "Strings",
        "description": "Find most frequent character.",
        "description_full": "Given string S, find the character with the highest frequency. If tie, return first.",
        "input": "String S",
        "output": "Character",
        "example": "Input:\nmississippi\nOutput:\ni",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "mississippi", "output": "i"},
            {"input": "aabb", "output": "a"},
            {"input": "x", "output": "x"}
        ]
    },

    {
        "id": "str_anagram_check",
        "title": "Anagram Check",
        "topic": "Strings",
        "description": "Check if two strings are anagrams.",
        "description_full": "Given two strings S1 and S2, check whether they are anagrams of each other.",
        "input": "Two strings S1 S2",
        "output": "YES or NO",
        "example": "Input:\nlisten silent\nOutput:\nYES",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "listen silent", "output": "YES"},
            {"input": "hello world", "output": "NO"},
            {"input": "a a", "output": "YES"}
        ]
    },

    {
        "id": "str_reverse_words",
        "title": "Reverse Words in Sentence",
        "topic": "Strings",
        "description": "Reverse each word in a sentence.",
        "description_full": "Given a sentence S, reverse each word while keeping word order same.",
        "input": "String S",
        "output": "Modified sentence",
        "example": "Input:\nI love coding\nOutput:\nI evol gnidoc",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "I love coding", "output": "I evol gnidoc"},
            {"input": "hello", "output": "olleh"},
            {"input": "a bc", "output": "a cb"}
        ]
    },

    {
        "id": "str_string_rotation",
        "title": "String Rotation Check",
        "topic": "Strings",
        "description": "Check if one string is rotation of another.",
        "description_full": "Given strings S1 and S2, check if S2 is a rotation of S1.",
        "input": "Two strings S1 S2",
        "output": "YES or NO",
        "example": "Input:\nabcd cdab\nOutput:\nYES",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "abcd cdab", "output": "YES"},
            {"input": "abcd acbd", "output": "NO"},
            {"input": "a a", "output": "YES"}
        ]
    },

    {
        "id": "str_count_palindromic_words",
        "title": "Count Palindromic Words",
        "topic": "Strings",
        "description": "Count palindromic words in sentence.",
        "description_full": "Given a sentence S, count how many words are palindromes.",
        "input": "String S",
        "output": "Count",
        "example": "Input:\nmadam level hello\nOutput:\n2",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "madam level hello", "output": "2"},
            {"input": "abc def", "output": "0"},
            {"input": "a aa aaa", "output": "3"}
        ]
    },

    {
        "id": "str_remove_extra_spaces",
        "title": "Remove Extra Spaces",
        "topic": "Strings",
        "description": "Remove extra spaces from sentence.",
        "description_full": "Given sentence S, remove leading, trailing, and multiple intermediate spaces.",
        "input": "String S",
        "output": "Cleaned sentence",
        "example": "Input:\n  I   love   coding  \nOutput:\nI love coding",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "  I   love   coding  ", "output": "I love coding"},
            {"input": "hello   world", "output": "hello world"},
            {"input": "a", "output": "a"}
        ]
    }

],
        "Arrays": [

    {
        "id": "arr_second_largest",
        "title": "Second Largest Element",
        "topic": "Arrays",
        "description": "Find the second largest element in array.",
        "description_full": "Given an array of integers, find the second largest distinct element. If it does not exist, print -1.",
        "input": "N followed by N integers",
        "output": "Second largest element or -1",
        "example": "Input:\n5\n1 2 3 4 5\nOutput:\n4",
        "constraints": "N >= 1",
        "explanation": "",
        "tests": [
            {"input": "5\n1 2 3 4 5", "output": "4"},
            {"input": "3\n10 10 10", "output": "-1"},
            {"input": "4\n5 1 5 3", "output": "3"}
        ]
    },

    {
        "id": "arr_two_sum_indices",
        "title": "Two Sum Indices",
        "topic": "Arrays",
        "description": "Find indices of two numbers whose sum equals target.",
        "description_full": "Given an array and integer X, find indices i and j such that A[i] + A[j] = X.",
        "input": "N followed by N integers then X",
        "output": "i j or -1 -1",
        "example": "Input:\n4\n2 7 11 15\n9\nOutput:\n0 1",
        "constraints": "Exactly one solution or none",
        "explanation": "",
        "tests": [
            {"input": "4\n2 7 11 15\n9", "output": "0 1"},
            {"input": "3\n1 2 3\n7", "output": "-1 -1"},
            {"input": "4\n3 3 4 5\n6", "output": "0 1"}
        ]
    },

    {
        "id": "arr_rotate_k",
        "title": "Rotate Array K Times",
        "topic": "Arrays",
        "description": "Rotate array to the right by K steps.",
        "description_full": "Given an array, rotate it to the right by K positions.",
        "input": "N followed by N integers then K",
        "output": "Rotated array",
        "example": "Input:\n5\n1 2 3 4 5\n2\nOutput:\n4 5 1 2 3",
        "constraints": "K >= 0",
        "explanation": "",
        "tests": [
            {"input": "5\n1 2 3 4 5\n2", "output": "4 5 1 2 3"},
            {"input": "3\n10 20 30\n1", "output": "30 10 20"},
            {"input": "1\n7\n3", "output": "7"}
        ]
    },

    {
        "id": "arr_max_subarray_sum",
        "title": "Maximum Subarray Sum",
        "topic": "Arrays",
        "description": "Find maximum subarray sum.",
        "description_full": "Given an array, find the maximum possible sum of a contiguous subarray.",
        "input": "N followed by N integers",
        "output": "Maximum sum",
        "example": "Input:\n5\n-2 1 -3 4 -1\nOutput:\n4",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "5\n-2 1 -3 4 -1", "output": "4"},
            {"input": "3\n1 2 3", "output": "6"},
            {"input": "3\n-5 -1 -8", "output": "-1"}
        ]
    },

    {
        "id": "arr_move_zeros",
        "title": "Move Zeros to End",
        "topic": "Arrays",
        "description": "Move all zeros to the end.",
        "description_full": "Given an array, move all zeros to the end while maintaining order of non-zero elements.",
        "input": "N followed by N integers",
        "output": "Modified array",
        "example": "Input:\n5\n0 1 0 3 12\nOutput:\n1 3 12 0 0",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "5\n0 1 0 3 12", "output": "1 3 12 0 0"},
            {"input": "3\n0 0 0", "output": "0 0 0"},
            {"input": "4\n1 2 3 4", "output": "1 2 3 4"}
        ]
    },

    {
        "id": "arr_remove_duplicates_sorted",
        "title": "Remove Duplicates from Sorted Array",
        "topic": "Arrays",
        "description": "Remove duplicates from sorted array.",
        "description_full": "Given a sorted array, remove duplicate elements and print unique elements.",
        "input": "N followed by N sorted integers",
        "output": "Array without duplicates",
        "example": "Input:\n6\n1 1 2 2 3 3\nOutput:\n1 2 3",
        "constraints": "Array sorted",
        "explanation": "",
        "tests": [
            {"input": "6\n1 1 2 2 3 3", "output": "1 2 3"},
            {"input": "3\n1 1 1", "output": "1"},
            {"input": "4\n1 2 3 4", "output": "1 2 3 4"}
        ]
    },

    {
        "id": "arr_prefix_sum",
        "title": "Prefix Sum Array",
        "topic": "Arrays",
        "description": "Generate prefix sum array.",
        "description_full": "Given an array, generate its prefix sum array.",
        "input": "N followed by N integers",
        "output": "Prefix sums",
        "example": "Input:\n4\n1 2 3 4\nOutput:\n1 3 6 10",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "4\n1 2 3 4", "output": "1 3 6 10"},
            {"input": "3\n5 -1 2", "output": "5 4 6"},
            {"input": "1\n7", "output": "7"}
        ]
    },

    {
        "id": "arr_majority_element",
        "title": "Majority Element",
        "topic": "Arrays",
        "description": "Find majority element.",
        "description_full": "Given an array, find the element that appears more than N/2 times, or -1 if none.",
        "input": "N followed by N integers",
        "output": "Majority element or -1",
        "example": "Input:\n5\n2 2 1 2 3\nOutput:\n2",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "5\n2 2 1 2 3", "output": "2"},
            {"input": "3\n1 2 3", "output": "-1"},
            {"input": "1\n7", "output": "7"}
        ]
    },

    {
        "id": "arr_longest_increasing_subarray",
        "title": "Longest Increasing Subarray",
        "topic": "Arrays",
        "description": "Find length of longest increasing subarray.",
        "description_full": "Given an array, find the length of the longest contiguous increasing subarray.",
        "input": "N followed by N integers",
        "output": "Length",
        "example": "Input:\n6\n1 2 3 1 2 3\nOutput:\n3",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "6\n1 2 3 1 2 3", "output": "3"},
            {"input": "5\n5 4 3 2 1", "output": "1"},
            {"input": "4\n1 2 2 3", "output": "2"}
        ]
    }

],
        "Patterns": [

    {
        "id": "pattern_hollow_square",
        "title": "Hollow Square Pattern",
        "topic": "Patterns",
        "description": "Print hollow square using stars.",
        "description_full": "Given integer N, print a hollow square of size N using '*' characters.",
        "input": "Integer N",
        "output": "Pattern of stars",
        "example": "Input:\n4\nOutput:\n****\n*  *\n*  *\n****",
        "constraints": "N >= 2",
        "explanation": "",
        "tests": [
            {"input": "4", "output": "****\n*  *\n*  *\n****"},
            {"input": "2", "output": "**\n**"},
            {"input": "3", "output": "***\n* *\n***"}
        ]
    },

    {
        "id": "pattern_inverted_triangle",
        "title": "Inverted Right Triangle",
        "topic": "Patterns",
        "description": "Print inverted right triangle.",
        "description_full": "Given N, print an inverted right triangle using '*' characters.",
        "input": "Integer N",
        "output": "Pattern",
        "example": "Input:\n3\nOutput:\n***\n**\n*",
        "constraints": "N > 0",
        "explanation": "",
        "tests": [
            {"input": "3", "output": "***\n**\n*"},
            {"input": "1", "output": "*"},
            {"input": "2", "output": "**\n*"}
        ]
    },

    {
        "id": "pattern_number_pyramid",
        "title": "Number Pyramid",
        "topic": "Patterns",
        "description": "Print pyramid of numbers.",
        "description_full": "Given N, print pyramid where i-th row contains numbers from 1 to i.",
        "input": "Integer N",
        "output": "Number pyramid",
        "example": "Input:\n4\nOutput:\n1\n1 2\n1 2 3\n1 2 3 4",
        "constraints": "N > 0",
        "explanation": "",
        "tests": [
            {"input": "4", "output": "1\n1 2\n1 2 3\n1 2 3 4"},
            {"input": "1", "output": "1"},
            {"input": "2", "output": "1\n1 2"}
        ]
    },

    {
        "id": "pattern_full_pyramid_stars",
        "title": "Full Star Pyramid",
        "topic": "Patterns",
        "description": "Print centered star pyramid.",
        "description_full": "Given N, print a centered pyramid of stars with N rows.",
        "input": "Integer N",
        "output": "Star pyramid",
        "example": "Input:\n3\nOutput:\n  *\n ***\n*****",
        "constraints": "N > 0",
        "explanation": "",
        "tests": [
            {"input": "3", "output": "  *\n ***\n*****"},
            {"input": "1", "output": "*"},
            {"input": "2", "output": " *\n***"}
        ]
    },

    {
        "id": "pattern_diamond",
        "title": "Diamond Pattern",
        "topic": "Patterns",
        "description": "Print diamond star pattern.",
        "description_full": "Given N, print a diamond pattern using stars.",
        "input": "Integer N",
        "output": "Diamond pattern",
        "example": "Input:\n3\nOutput:\n  *\n ***\n*****\n ***\n  *",
        "constraints": "N > 0",
        "explanation": "",
        "tests": [
            {"input": "3", "output": "  *\n ***\n*****\n ***\n  *"},
            {"input": "1", "output": "*"},
            {"input": "2", "output": " *\n***\n *"}
        ]
    },

    {
        "id": "pattern_floyd_triangle",
        "title": "Floyd's Triangle",
        "topic": "Patterns",
        "description": "Print Floyd's number triangle.",
        "description_full": "Given N, print Floyd's triangle with consecutive numbers.",
        "input": "Integer N",
        "output": "Floyd triangle",
        "example": "Input:\n3\nOutput:\n1\n2 3\n4 5 6",
        "constraints": "N > 0",
        "explanation": "",
        "tests": [
            {"input": "3", "output": "1\n2 3\n4 5 6"},
            {"input": "1", "output": "1"},
            {"input": "2", "output": "1\n2 3"}
        ]
    },

    {
        "id": "pattern_pascal_triangle",
        "title": "Pascal's Triangle",
        "topic": "Patterns",
        "description": "Print Pascal's triangle.",
        "description_full": "Given N, print first N rows of Pascal's triangle.",
        "input": "Integer N",
        "output": "Pascal triangle",
        "example": "Input:\n4\nOutput:\n1\n1 1\n1 2 1\n1 3 3 1",
        "constraints": "N > 0",
        "explanation": "",
        "tests": [
            {"input": "4", "output": "1\n1 1\n1 2 1\n1 3 3 1"},
            {"input": "1", "output": "1"},
            {"input": "2", "output": "1\n1 1"}
        ]
    },

    {
        "id": "pattern_alphabet_triangle",
        "title": "Alphabet Triangle",
        "topic": "Patterns",
        "description": "Print alphabet triangle.",
        "description_full": "Given N, print letters from A increasing row-wise.",
        "input": "Integer N",
        "output": "Alphabet pattern",
        "example": "Input:\n3\nOutput:\nA\nA B\nA B C",
        "constraints": "N <= 26",
        "explanation": "",
        "tests": [
            {"input": "3", "output": "A\nA B\nA B C"},
            {"input": "1", "output": "A"},
            {"input": "2", "output": "A\nA B"}
        ]
    },

    {
        "id": "pattern_binary_triangle",
        "title": "Binary Triangle",
        "topic": "Patterns",
        "description": "Print binary pattern.",
        "description_full": "Given N, print triangle with alternating 0s and 1s.",
        "input": "Integer N",
        "output": "Binary pattern",
        "example": "Input:\n3\nOutput:\n1\n0 1\n1 0 1",
        "constraints": "N > 0",
        "explanation": "",
        "tests": [
            {"input": "3", "output": "1\n0 1\n1 0 1"},
            {"input": "1", "output": "1"},
            {"input": "2", "output": "1\n0 1"}
        ]
    },

    {
        "id": "pattern_cross",
        "title": "Cross Star Pattern",
        "topic": "Patterns",
        "description": "Print cross using stars.",
        "description_full": "Given odd integer N, print a cross pattern using '*' characters.",
        "input": "Odd integer N",
        "output": "Cross pattern",
        "example": "Input:\n5\nOutput:\n*   *\n * * \n  *  \n * * \n*   *",
        "constraints": "N is odd",
        "explanation": "",
        "tests": [
            {"input": "5", "output": "*   *\n * * \n  *  \n * * \n*   *"},
            {"input": "1", "output": "*"},
            {"input": "3", "output": "* *\n * \n* *"}
        ]
    }

],
        "Functions": [

    {
        "id": "func_factorial",
        "title": "Factorial Using Function",
        "topic": "Functions",
        "description": "Compute factorial using function.",
        "description_full": "Given integer N, compute N! using a user-defined function.",
        "input": "Integer N",
        "output": "Factorial of N",
        "example": "Input:\n5\nOutput:\n120",
        "constraints": "0 <= N <= 20",
        "explanation": "",
        "tests": [
            {"input": "5", "output": "120"},
            {"input": "0", "output": "1"},
            {"input": "7", "output": "5040"}
        ]
    },

    {
        "id": "func_is_prime",
        "title": "Prime Check Using Function",
        "topic": "Functions",
        "description": "Check prime number using function.",
        "description_full": "Given integer N, determine whether it is prime using a helper function.",
        "input": "Integer N",
        "output": "YES or NO",
        "example": "Input:\n11\nOutput:\nYES",
        "constraints": "N >= 1",
        "explanation": "",
        "tests": [
            {"input": "11", "output": "YES"},
            {"input": "12", "output": "NO"},
            {"input": "2", "output": "YES"}
        ]
    },

    {
        "id": "func_gcd",
        "title": "GCD Using Function",
        "topic": "Functions",
        "description": "Compute GCD using function.",
        "description_full": "Given two integers A and B, compute their GCD using a function.",
        "input": "Two integers A B",
        "output": "GCD",
        "example": "Input:\n12 18\nOutput:\n6",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "12 18", "output": "6"},
            {"input": "7 13", "output": "1"},
            {"input": "10 5", "output": "5"}
        ]
    },

    {
        "id": "func_lcm",
        "title": "LCM Using Function",
        "topic": "Functions",
        "description": "Compute LCM using function.",
        "description_full": "Given two integers A and B, compute their LCM using a function.",
        "input": "Two integers A B",
        "output": "LCM",
        "example": "Input:\n4 6\nOutput:\n12",
        "constraints": "A,B > 0",
        "explanation": "",
        "tests": [
            {"input": "4 6", "output": "12"},
            {"input": "5 5", "output": "5"},
            {"input": "3 7", "output": "21"}
        ]
    },

    {
        "id": "func_reverse_number",
        "title": "Reverse Number Using Function",
        "topic": "Functions",
        "description": "Reverse digits using function.",
        "description_full": "Given integer N, reverse its digits using a function.",
        "input": "Integer N",
        "output": "Reversed number",
        "example": "Input:\n123\nOutput:\n321",
        "constraints": "N >= 0",
        "explanation": "",
        "tests": [
            {"input": "123", "output": "321"},
            {"input": "1200", "output": "21"},
            {"input": "0", "output": "0"}
        ]
    },

    {
        "id": "func_palindrome_string",
        "title": "String Palindrome Using Function",
        "topic": "Functions",
        "description": "Check string palindrome.",
        "description_full": "Given string S, check whether it is palindrome using a function.",
        "input": "String S",
        "output": "YES or NO",
        "example": "Input:\nmadam\nOutput:\nYES",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "madam", "output": "YES"},
            {"input": "hello", "output": "NO"},
            {"input": "a", "output": "YES"}
        ]
    },

    {
        "id": "func_power",
        "title": "Power Using Function",
        "topic": "Functions",
        "description": "Compute power using function.",
        "description_full": "Given integers A and B, compute A raised to power B using a function.",
        "input": "Two integers A B",
        "output": "A^B",
        "example": "Input:\n2 3\nOutput:\n8",
        "constraints": "B >= 0",
        "explanation": "",
        "tests": [
            {"input": "2 3", "output": "8"},
            {"input": "5 0", "output": "1"},
            {"input": "3 4", "output": "81"}
        ]
    },

    {
        "id": "func_is_perfect_square",
        "title": "Perfect Square Check",
        "topic": "Functions",
        "description": "Check perfect square using function.",
        "description_full": "Given integer N, check whether it is a perfect square using a function.",
        "input": "Integer N",
        "output": "YES or NO",
        "example": "Input:\n16\nOutput:\nYES",
        "constraints": "N >= 0",
        "explanation": "",
        "tests": [
            {"input": "16", "output": "YES"},
            {"input": "14", "output": "NO"},
            {"input": "0", "output": "YES"}
        ]
    },

    {
        "id": "func_swap_numbers",
        "title": "Swap Two Numbers",
        "topic": "Functions",
        "description": "Swap two numbers using function.",
        "description_full": "Given two integers A and B, swap them using a function and print result.",
        "input": "Two integers A B",
        "output": "Swapped values",
        "example": "Input:\n3 5\nOutput:\n5 3",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "3 5", "output": "5 3"},
            {"input": "1 1", "output": "1 1"},
            {"input": "-1 2", "output": "2 -1"}
        ]
    },

    {
        "id": "func_armstrong",
        "title": "Armstrong Number Using Function",
        "topic": "Functions",
        "description": "Check Armstrong number.",
        "description_full": "Given integer N (0–999), check whether it is an Armstrong number using a function.",
        "input": "Integer N",
        "output": "YES or NO",
        "example": "Input:\n153\nOutput:\nYES",
        "constraints": "0 <= N <= 999",
        "explanation": "",
        "tests": [
            {"input": "153", "output": "YES"},
            {"input": "370", "output": "YES"},
            {"input": "100", "output": "NO"}
        ]
    }

],
        "Searching": [

    {
        "id": "search_linear_index",
        "title": "Linear Search Index",
        "topic": "Searching",
        "description": "Find index using linear search.",
        "description_full": "Given an array and a value X, find the 0-based index of the first occurrence of X using linear search.",
        "input": "N followed by N integers then X",
        "output": "Index or -1",
        "example": "Input:\n5\n1 3 5 7 9\n7\nOutput:\n3",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "5\n1 3 5 7 9\n7", "output": "3"},
            {"input": "3\n1 2 3\n4", "output": "-1"},
            {"input": "4\n2 2 2 2\n2", "output": "0"}
        ]
    },

    {
        "id": "search_binary_index",
        "title": "Binary Search Index",
        "topic": "Searching",
        "description": "Find element using binary search.",
        "description_full": "Given a sorted array and a value X, find its index using binary search.",
        "input": "N followed by N sorted integers then X",
        "output": "Index or -1",
        "example": "Input:\n5\n1 3 5 7 9\n5\nOutput:\n2",
        "constraints": "Array sorted",
        "explanation": "",
        "tests": [
            {"input": "5\n1 3 5 7 9\n5", "output": "2"},
            {"input": "3\n10 20 30\n25", "output": "-1"},
            {"input": "1\n7\n7", "output": "0"}
        ]
    },

    {
        "id": "search_first_occurrence",
        "title": "First Occurrence",
        "topic": "Searching",
        "description": "Find first occurrence of element.",
        "description_full": "Given an array and value X, find the index of the first occurrence of X.",
        "input": "N followed by N integers then X",
        "output": "Index or -1",
        "example": "Input:\n5\n1 2 3 2 2\n2\nOutput:\n1",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "5\n1 2 3 2 2\n2", "output": "1"},
            {"input": "3\n1 1 1\n1", "output": "0"},
            {"input": "4\n1 2 3 4\n5", "output": "-1"}
        ]
    },

    {
        "id": "search_last_occurrence",
        "title": "Last Occurrence",
        "topic": "Searching",
        "description": "Find last occurrence of element.",
        "description_full": "Given an array and value X, find the index of the last occurrence of X.",
        "input": "N followed by N integers then X",
        "output": "Index or -1",
        "example": "Input:\n5\n1 2 3 2 2\n2\nOutput:\n4",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "5\n1 2 3 2 2\n2", "output": "4"},
            {"input": "3\n1 1 1\n1", "output": "2"},
            {"input": "4\n1 2 3 4\n5", "output": "-1"}
        ]
    },

    {
        "id": "search_count_occurrences",
        "title": "Count Occurrences",
        "topic": "Searching",
        "description": "Count occurrences of element.",
        "description_full": "Given an array and value X, count how many times X appears in the array.",
        "input": "N followed by N integers then X",
        "output": "Count",
        "example": "Input:\n5\n2 2 3 2 4\n2\nOutput:\n3",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "5\n2 2 3 2 4\n2", "output": "3"},
            {"input": "3\n1 1 1\n2", "output": "0"},
            {"input": "1\n7\n7", "output": "1"}
        ]
    },

    {
        "id": "search_lower_bound",
        "title": "Lower Bound",
        "topic": "Searching",
        "description": "Find lower bound index.",
        "description_full": "Given a sorted array and X, find the index of the first element >= X.",
        "input": "N followed by N sorted integers then X",
        "output": "Index or N",
        "example": "Input:\n5\n1 3 5 7 9\n6\nOutput:\n3",
        "constraints": "Array sorted",
        "explanation": "",
        "tests": [
            {"input": "5\n1 3 5 7 9\n6", "output": "3"},
            {"input": "3\n1 2 3\n0", "output": "0"},
            {"input": "3\n1 2 3\n5", "output": "3"}
        ]
    },

    {
        "id": "search_upper_bound",
        "title": "Upper Bound",
        "topic": "Searching",
        "description": "Find upper bound index.",
        "description_full": "Given a sorted array and X, find the index of the first element > X.",
        "input": "N followed by N sorted integers then X",
        "output": "Index or N",
        "example": "Input:\n5\n1 3 5 7 9\n5\nOutput:\n3",
        "constraints": "Array sorted",
        "explanation": "",
        "tests": [
            {"input": "5\n1 3 5 7 9\n5", "output": "3"},
            {"input": "3\n1 2 3\n3", "output": "3"},
            {"input": "3\n1 2 3\n0", "output": "0"}
        ]
    },

    {
        "id": "search_min_element_index",
        "title": "Index of Minimum Element",
        "topic": "Searching",
        "description": "Find index of minimum element.",
        "description_full": "Given an array, find the index of the minimum element (first if tie).",
        "input": "N followed by N integers",
        "output": "Index",
        "example": "Input:\n4\n3 1 2 1\nOutput:\n1",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "4\n3 1 2 1", "output": "1"},
            {"input": "1\n5", "output": "0"},
            {"input": "3\n2 3 4", "output": "0"}
        ]
    },

    {
        "id": "search_first_even_index",
        "title": "First Even Element Index",
        "topic": "Searching",
        "description": "Find index of first even element.",
        "description_full": "Given an array, find the index of the first even element or -1 if none.",
        "input": "N followed by N integers",
        "output": "Index or -1",
        "example": "Input:\n5\n1 3 5 4 2\nOutput:\n3",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "5\n1 3 5 4 2", "output": "3"},
            {"input": "3\n1 3 5", "output": "-1"},
            {"input": "1\n2", "output": "0"}
        ]
    },

    {
        "id": "search_pair_sum",
        "title": "Find Pair with Given Sum",
        "topic": "Searching",
        "description": "Find any pair whose sum equals target.",
        "description_full": "Given an array and target X, find indices of any pair whose sum is X.",
        "input": "N followed by N integers then X",
        "output": "i j or -1 -1",
        "example": "Input:\n5\n1 4 5 6 8\n9\nOutput:\n0 3",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "5\n1 4 5 6 8\n9", "output": "0 3"},
            {"input": "3\n1 2 3\n7", "output": "-1 -1"},
            {"input": "4\n2 7 11 15\n9", "output": "0 1"}
        ]
    }

],
        "Sorting": [

    {
        "id": "sort_ascending",
        "title": "Sort Array Ascending",
        "topic": "Sorting",
        "description": "Sort array in ascending order.",
        "description_full": "Given an array of integers, sort the array in non-decreasing (ascending) order.",
        "input": "N followed by N integers",
        "output": "Sorted array",
        "example": "Input:\n5\n3 1 4 2 5\nOutput:\n1 2 3 4 5",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "5\n3 1 4 2 5", "output": "1 2 3 4 5"},
            {"input": "3\n2 2 1", "output": "1 2 2"},
            {"input": "1\n7", "output": "7"}
        ]
    },

    {
        "id": "sort_descending",
        "title": "Sort Array Descending",
        "topic": "Sorting",
        "description": "Sort array in descending order.",
        "description_full": "Given an array of integers, sort the array in non-increasing (descending) order.",
        "input": "N followed by N integers",
        "output": "Sorted array",
        "example": "Input:\n4\n1 3 2 4\nOutput:\n4 3 2 1",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "4\n1 3 2 4", "output": "4 3 2 1"},
            {"input": "3\n2 2 1", "output": "2 2 1"},
            {"input": "1\n9", "output": "9"}
        ]
    },

    {
        "id": "sort_check_sorted",
        "title": "Check If Array Is Sorted",
        "topic": "Sorting",
        "description": "Check whether array is sorted.",
        "description_full": "Given an array, check if it is sorted in non-decreasing order.",
        "input": "N followed by N integers",
        "output": "YES or NO",
        "example": "Input:\n3\n1 2 3\nOutput:\nYES",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "3\n1 2 3", "output": "YES"},
            {"input": "3\n2 1 3", "output": "NO"},
            {"input": "1\n5", "output": "YES"}
        ]
    },

    {
        "id": "sort_kth_smallest",
        "title": "Kth Smallest Element",
        "topic": "Sorting",
        "description": "Find kth smallest element.",
        "description_full": "Given an array and integer K, find the Kth smallest element after sorting.",
        "input": "N followed by N integers then K",
        "output": "Kth smallest element",
        "example": "Input:\n5\n5 3 1 2 4\n2\nOutput:\n2",
        "constraints": "1 <= K <= N",
        "explanation": "",
        "tests": [
            {"input": "5\n5 3 1 2 4\n2", "output": "2"},
            {"input": "3\n1 2 3\n1", "output": "1"},
            {"input": "4\n2 2 3 1\n3", "output": "2"}
        ]
    },

    {
        "id": "sort_unique_elements",
        "title": "Sort Unique Elements",
        "topic": "Sorting",
        "description": "Sort only unique elements.",
        "description_full": "Given an array, remove duplicates and print unique elements in sorted order.",
        "input": "N followed by N integers",
        "output": "Sorted unique elements",
        "example": "Input:\n6\n1 2 1 3 2 4\nOutput:\n1 2 3 4",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "6\n1 2 1 3 2 4", "output": "1 2 3 4"},
            {"input": "3\n2 2 2", "output": "2"},
            {"input": "1\n5", "output": "5"}
        ]
    },

    {
        "id": "sort_by_absolute",
        "title": "Sort by Absolute Value",
        "topic": "Sorting",
        "description": "Sort elements by absolute value.",
        "description_full": "Given an array, sort elements based on absolute value in ascending order.",
        "input": "N followed by N integers",
        "output": "Sorted array",
        "example": "Input:\n5\n-2 3 -1 4 0\nOutput:\n0 -1 -2 3 4",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "5\n-2 3 -1 4 0", "output": "0 -1 -2 3 4"},
            {"input": "3\n2 -2 1", "output": "1 2 -2"},
            {"input": "1\n-5", "output": "-5"}
        ]
    },

    {
        "id": "sort_even_odd",
        "title": "Sort Evens Then Odds",
        "topic": "Sorting",
        "description": "Sort evens first then odds.",
        "description_full": "Given an array, place even numbers first (sorted), followed by odd numbers (sorted).",
        "input": "N followed by N integers",
        "output": "Modified array",
        "example": "Input:\n6\n1 2 3 4 5 6\nOutput:\n2 4 6 1 3 5",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "6\n1 2 3 4 5 6", "output": "2 4 6 1 3 5"},
            {"input": "3\n3 1 5", "output": "1 3 5"},
            {"input": "4\n2 4 6 8", "output": "2 4 6 8"}
        ]
    },

    {
        "id": "sort_frequency",
        "title": "Sort by Frequency",
        "topic": "Sorting",
        "description": "Sort elements by frequency.",
        "description_full": "Given an array, sort elements by increasing frequency. If tie, sort by value.",
        "input": "N followed by N integers",
        "output": "Sorted array",
        "example": "Input:\n6\n4 4 1 2 2 2\nOutput:\n1 4 4 2 2 2",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "6\n4 4 1 2 2 2", "output": "1 4 4 2 2 2"},
            {"input": "3\n3 3 3", "output": "3 3 3"},
            {"input": "4\n1 2 3 4", "output": "1 2 3 4"}
        ]
    },

    {
        "id": "sort_merge_sorted_arrays",
        "title": "Merge Two Sorted Arrays",
        "topic": "Sorting",
        "description": "Merge two sorted arrays.",
        "description_full": "Given two sorted arrays, merge them into a single sorted array.",
        "input": "N M followed by two sorted arrays",
        "output": "Merged sorted array",
        "example": "Input:\n3 3\n1 3 5\n2 4 6\nOutput:\n1 2 3 4 5 6",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "3 3\n1 3 5\n2 4 6", "output": "1 2 3 4 5 6"},
            {"input": "1 1\n5\n3", "output": "3 5"},
            {"input": "2 1\n1 2\n3", "output": "1 2 3"}
        ]
    },

    {
        "id": "sort_count_inversions",
        "title": "Count Inversions",
        "topic": "Sorting",
        "description": "Count inversion pairs.",
        "description_full": "Given an array, count pairs (i, j) such that i < j and A[i] > A[j].",
        "input": "N followed by N integers",
        "output": "Inversion count",
        "example": "Input:\n3\n3 1 2\nOutput:\n2",
        "constraints": "N small",
        "explanation": "",
        "tests": [
            {"input": "3\n3 1 2", "output": "2"},
            {"input": "3\n1 2 3", "output": "0"},
            {"input": "4\n4 3 2 1", "output": "6"}
        ]
    }

],
        "Matrices": [

    {
        "id": "matrix_count_zero",
        "title": "Count Zeros in Matrix",
        "topic": "Matrices",
        "description": "Count zero entries in matrix.",
        "description_full": "Given N and an NxN matrix, print the number of elements equal to 0.",
        "input": "Integer N followed by NxN integers",
        "output": "Count of zeros",
        "example": "Input:\n2\n0 1\n2 0\nOutput:\n2",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "2\n0 1\n2 0", "output": "2"},
            {"input": "1\n5", "output": "0"},
            {"input": "3\n0 0 0\n0 0 0\n0 0 0", "output": "9"}
        ]
    },

    {
        "id": "matrix_sum_all",
        "title": "Sum of All Elements",
        "topic": "Matrices",
        "description": "Find sum of all matrix elements.",
        "description_full": "Given N and an NxN matrix, compute the sum of all elements.",
        "input": "Integer N followed by NxN integers",
        "output": "Sum",
        "example": "Input:\n2\n1 2\n3 4\nOutput:\n10",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "2\n1 2\n3 4", "output": "10"},
            {"input": "1\n0", "output": "0"},
            {"input": "3\n1 1 1\n1 1 1\n1 1 1", "output": "9"}
        ]
    },

    {
        "id": "matrix_diagonal_sum",
        "title": "Primary Diagonal Sum",
        "topic": "Matrices",
        "description": "Sum of primary diagonal elements.",
        "description_full": "Given N and an NxN matrix, compute the sum of elements where row index equals column index.",
        "input": "Integer N followed by NxN integers",
        "output": "Diagonal sum",
        "example": "Input:\n2\n1 2\n3 4\nOutput:\n5",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "2\n1 2\n3 4", "output": "5"},
            {"input": "1\n9", "output": "9"},
            {"input": "3\n1 0 0\n0 1 0\n0 0 1", "output": "3"}
        ]
    },

    {
        "id": "matrix_secondary_diagonal_sum",
        "title": "Secondary Diagonal Sum",
        "topic": "Matrices",
        "description": "Sum of secondary diagonal elements.",
        "description_full": "Given N and an NxN matrix, compute the sum of elements where row + column = N - 1.",
        "input": "Integer N followed by NxN integers",
        "output": "Diagonal sum",
        "example": "Input:\n3\n1 2 3\n4 5 6\n7 8 9\nOutput:\n15",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "3\n1 2 3\n4 5 6\n7 8 9", "output": "15"},
            {"input": "1\n7", "output": "7"},
            {"input": "2\n1 2\n3 4", "output": "5"}
        ]
    },

    {
        "id": "matrix_row_max_sum",
        "title": "Row with Maximum Sum",
        "topic": "Matrices",
        "description": "Find row index having maximum sum.",
        "description_full": "Given N and an NxN matrix, find the 0-based index of the row with the maximum sum.",
        "input": "Integer N followed by NxN integers",
        "output": "Row index",
        "example": "Input:\n3\n1 2 3\n4 5 6\n1 1 1\nOutput:\n1",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "3\n1 2 3\n4 5 6\n1 1 1", "output": "1"},
            {"input": "2\n1 1\n1 1", "output": "0"},
            {"input": "1\n5", "output": "0"}
        ]
    },

    {
        "id": "matrix_column_sum",
        "title": "Column-wise Sum",
        "topic": "Matrices",
        "description": "Compute sum of each column.",
        "description_full": "Given N and an NxN matrix, print the sum of elements in each column.",
        "input": "Integer N followed by NxN integers",
        "output": "N space-separated integers",
        "example": "Input:\n2\n1 2\n3 4\nOutput:\n4 6",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "2\n1 2\n3 4", "output": "4 6"},
            {"input": "1\n5", "output": "5"},
            {"input": "3\n1 1 1\n1 1 1\n1 1 1", "output": "3 3 3"}
        ]
    },

    {
        "id": "matrix_transpose",
        "title": "Transpose of Matrix",
        "topic": "Matrices",
        "description": "Compute transpose of matrix.",
        "description_full": "Given N and an NxN matrix, print its transpose.",
        "input": "Integer N followed by NxN integers",
        "output": "Transposed matrix",
        "example": "Input:\n2\n1 2\n3 4\nOutput:\n1 3\n2 4",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "2\n1 2\n3 4", "output": "1 3\n2 4"},
            {"input": "1\n9", "output": "9"},
            {"input": "3\n1 2 3\n4 5 6\n7 8 9", "output": "1 4 7\n2 5 8\n3 6 9"}
        ]
    },

    {
        "id": "matrix_border_sum",
        "title": "Sum of Border Elements",
        "topic": "Matrices",
        "description": "Find sum of boundary elements.",
        "description_full": "Given N and an NxN matrix, compute the sum of boundary (border) elements.",
        "input": "Integer N followed by NxN integers",
        "output": "Sum",
        "example": "Input:\n3\n1 2 3\n4 5 6\n7 8 9\nOutput:\n40",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "3\n1 2 3\n4 5 6\n7 8 9", "output": "40"},
            {"input": "1\n5", "output": "5"},
            {"input": "2\n1 2\n3 4", "output": "10"}
        ]
    },

    {
        "id": "matrix_find_element",
        "title": "Search Element in Matrix",
        "topic": "Matrices",
        "description": "Check if element exists in matrix.",
        "description_full": "Given N, an NxN matrix, and integer X, check whether X exists in the matrix.",
        "input": "Integer N, NxN integers, then X",
        "output": "YES or NO",
        "example": "Input:\n2\n1 2\n3 4\n3\nOutput:\nYES",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "2\n1 2\n3 4\n3", "output": "YES"},
            {"input": "1\n5\n6", "output": "NO"},
            {"input": "3\n1 2 3\n4 5 6\n7 8 9\n8", "output": "YES"}
        ]
    },

    {
        "id": "matrix_reverse_rows",
        "title": "Reverse Each Row",
        "topic": "Matrices",
        "description": "Reverse elements of each row.",
        "description_full": "Given N and an NxN matrix, reverse the elements of each row.",
        "input": "Integer N followed by NxN integers",
        "output": "Modified matrix",
        "example": "Input:\n2\n1 2\n3 4\nOutput:\n2 1\n4 3",
        "constraints": "",
        "explanation": "",
        "tests": [
            {"input": "2\n1 2\n3 4", "output": "2 1\n4 3"},
            {"input": "1\n9", "output": "9"},
            {"input": "3\n1 2 3\n4 5 6\n7 8 9", "output": "3 2 1\n6 5 4\n9 8 7"}
        ]
    }

]
    }
}
