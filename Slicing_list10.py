def main(list1,n):
    """
    A list of several elements is given. Return all elements in reverse order except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    a=n
    b=list1[-a::]
    c=b[::-1]
    return (c)
print (main(list1=['a', 'b', 'c', 'd', 'e', 'f'], n = 3))