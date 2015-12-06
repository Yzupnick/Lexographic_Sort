# Lexographic Sort
Summary: Write a function to sort an array of strings based on an arbitrary lexicographic ordering. The function will take two parameters: an array of strings to sort and a string specifying the lexicographic order.
 
Example input #1: ( ["acb", "abc", "bca"], "abc")
Example output #1: ["abc","acb","bca"]
 
Example input #2: ( ["acb", "abc", "bca"], "cba")
Example output #2: ["bca", "acb", "abc"]
 
Example input #3: (["aaa","aa",""], "a")
Example output #3: ["", "aa", "aaa"]
 
You may assume that the strings to be sorted consist only of characters from the specified lexicographical ordering. You may also assume that the characters in the strings to sort consist only of lowercase a-z.

# Run Time Analysis 
The inner loop of the lex_sort function loops through each (unsorted) word in our input list. The function itself has to be called at least as many times as the number of charachters in the second shortest word. In the worst case, the algorithm is O(ln). Where l is the length of the second to longest word (could be the same as the longest) and n is the length of our list of words to sort.  

