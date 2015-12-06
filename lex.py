def lex_sort(words, order, index = 0):
    if len(words) <= 1:
        return words
    order_map = {char:index for index,char in enumerate(order)}
    buckets = [ [] for char in order]
    to_return = []
    for word in words:
        if index >= len(word):
            to_return.append(word)
        else:
            sort_char = word[index]
            buckets[order_map[sort_char]].append(word)

    for bucket in buckets:
        to_return += lex_sort(bucket, order, index +1)
    return to_return
