#
def lex_sort(words, order, index = 0):
    '''
        lex_sort is a recursive algorithm.
        :param words => list of words to sort
        :param order =>  string of chars representing the lexographic order to sort the words into
        :param index => the index on each word to start sorting from. Used internally for recursion
    '''
    # if our words to sort is 1 or less, we can just return the list
    # this is our base case.
    if len(words) <= 1:
        return words

    # we create a dictionary of char to int. The int is the bucket index used in our list of buckets
    # that way we can easily reference which bucket to store a word in later
    order_map = {char:index for index,char in enumerate(order)}
    # create the empty buckets. I'm pretty sure there is a way to do the next block of lines in a single list comprehensions... maybe two.
    # that would be a bad idea for anyone who wants to read it.
    buckets = [ [] for char in order]
    to_return = []
    for word in words:
        # if the word is smaller than the index we are currently lookig at, we know it will come before anything that will be in our buckets.
        # Therefore we can add it to our return list.
        # We are also assuming here that words is correctly ordered for any word that doesn't make it into our buckets.
        # This is only true if lex_sort was started with index of 0

        if index >= len(word):
            to_return.append(word)

        # Otherwise we divide up our words into the buckets we created earlier, based on the current sort index
        else:
            sort_char = word[index]
            buckets[order_map[sort_char]].append(word)

    # once we have our words sorted into buckets. We can sort those buckets using lex_sort on the next index.
    # we can then append them together and return
    for bucket in buckets:
        to_return += lex_sort(bucket, order, index +1)
    return to_return
