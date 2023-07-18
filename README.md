# Identify-the-Index
Identify the index of the mismatch string

1 - Two strings are defined:
text1 = "dhayajune2345678"
text2 = "dhayajune2945678"

2 - The zip function is used to combine the corresponding elements of text1 and text2. It creates pairs of characters from both strings. However, zip returns an iterator, so the zip_texts variable doesn't store the actual result yet.

3 - The enumerate function is applied to zip_texts. It adds an index to each pair of characters, creating a new iterator called enum_texts.

4 - A for loop is used to iterate over the pairs in enum_texts. Each pair is unpacked into variables i (index) and (a, b) (characters from text1 and text2).

5 - Inside the loop, it checks if a is not equal to b (i.e., if the characters at the corresponding positions in text1 and text2 are different).

6 - If the characters are different, it prints the index i where the characters mismatched.

Note: The loop won't actually print anything because the zip_texts iterator is already exhausted when the enumerate function is called. As a result, the loop doesn't have any items to iterate over, and nothing will be printed. If you want to see the output, you should remove the enumerate line and print directly from the zip function.
