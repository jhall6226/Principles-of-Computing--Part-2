"""
Student code for Word Wrangler game
"""

import urllib2
#import codeskulptor
#import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    
    unique_list = [elem for elem in list1]
    
    index = 0
    while index < len(unique_list) - 1:
        if unique_list[index] == unique_list[index+1]:
            unique_list.pop(index)
        else:
            index += 1    
    
    return unique_list

def binary_search(search_list, left, right, elem):
    """
    Searches search_list for elem and returns True if elem is in the list and False otherwise.
    """
    if left > right:
        return False
    else:
        mid = (left + right)/2
        if elem == search_list[mid]:
            return True
        elif elem < search_list[mid]:
            return binary_search(search_list,left,mid-1,elem)
        else:
            return binary_search(search_list,mid+1,right,elem)

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    
    intersect_list = []
    
    for elem in list1:
        if binary_search(list2,0,len(list2)-1,elem):
            intersect_list.append(elem)
    
    return intersect_list

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    """   
    
    if len(list1) == 0:
        return list2
    elif len(list2) == 0:
        return list1
    else:
        if list1[0] <= list2[0]:
            return [list1[0]] + merge(list1[1:], list2)
        else:
            return [list2[0]] + merge(list1, list2[1:])
                
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) <= 1:
        return list1
    else:
        list1_1 = list1[:len(list1)/2]
        list1_2 = list1[len(list1)/2:]
        
        return merge(merge_sort(list1_1), merge_sort(list1_2))

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    
    if word == "":
        return [word]
    
    elif len(word) == 1:
        return ["", word]
        
    else:
        first_char = word[0]
        rest = word[1:]
        
        rest_strings = gen_all_strings(rest)
        
        new_strings = []
        for string in rest_strings:
            for index in range(len(string)+1):
                new_strings.append(string[:index] + first_char + string[index:])
        
        return rest_strings + new_strings

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    # Desktop Variant
    
    
    # Codeskulptor Variant
    url = codeskulptor.file2url(filename)
    netfile = urllib2.urlopen(url)
    
    strings = [line for line in netfile.readlines()]
    
    return strings

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()