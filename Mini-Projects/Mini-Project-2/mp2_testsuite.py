# Test Suite for Mini Project 2
# Principles of Computing, Part 2
# Jordan Hall
# 10/25/2015

import poc_simpletest as pst
import mp2_v1 as mp2

# remove_duplicates function test
def remove_duplicates_test():    
    print "Commencing remove_duplicates function test..."
    tests = [([1,1,1], [1]),
             ([1,2,2], [1,2]),
             ([1], [1]),
             ([4,5], [4,5]),
             ([1,1,2,2,2,4,5,6,6,7,7,7,7,8,9,12,14,15,15], [1,2,4,5,6,7,8,9,12,14,15]),
    ]
    
    remove_duplicates_ts = pst.TestSuite()
    
    for test in tests:
        computed = mp2.remove_duplicates(test[0])
        expected = test[1]
        remove_duplicates_ts.run_test(computed, expected)
        
    remove_duplicates_ts.report_results()
    print

# intersect function test
def intersect_test():    
    print "Commencing intersect function test..."
    tests = [([1,2], [1,4], [1]),
             ([2,5,6], [1,4,6,8], [6]),
             ([1,2,4,8,9], [1,4,5,7,9], [1,4,9]),
    ]
    
    intersect_ts = pst.TestSuite()
    
    for test in tests:
        computed = mp2.intersect(test[0], test[1])
        expected = test[2]
        intersect_ts.run_test(computed, expected)
        
    intersect_ts.report_results()
    print
    
# merge function test
def merge_test():    
    print "Commencing merge function test..."
    tests = [([1,2,5], [], [1,2,5]),
             ([1,2], [1,4], [1,1,2,4]),
             ([2,5,6], [1,4,6,8], [1,2,4,5,6,6,8]),
             ([1,2,4,8,9], [1,4,5,7,9], [1,1,2,4,4,5,7,8,9,9]),
    ]
    
    merge_ts = pst.TestSuite()
    
    for test in tests:
        computed = mp2.merge(test[0], test[1])
        expected = test[2]
        merge_ts.run_test(computed, expected)
        
    merge_ts.report_results()
    print

# merge_sort function test
def merge_sort_test():    
    print "Commencing merge_sort function test..."
    tests = [([1,2,5], [1,2,5]),
             ([1,5,2], [1,2,5]),
             ([6,2,8], [2,6,8]),
             ([7,2,1,5,8], [1,2,5,7,8]),
             ([6,4,1,76,4,7,9,8,52,25], [1,4,4,6,7,8,9,25,52,76]),
    ]
    
    merge_sort_ts = pst.TestSuite()
    
    for test in tests:
        computed = mp2.merge_sort(test[0])
        expected = test[1]
        merge_sort_ts.run_test(computed, expected)
        
    merge_sort_ts.report_results()
    print

# gen_all_strings function test
def gen_all_strings_test():    
    print "Commencing gen_all_strings function test..."
    tests = [("", [""]),
             ("a", ["","a"]),
             ("aa", ["", "a", "a", "aa", "aa"]),
             ("abb", sorted(["", "a", "b", "b", "ab", "ab", "ba", "ba", "bb", "bb", "abb", "abb", "bab", "bab", "bba", "bba"])),
             ("abc", sorted(["", "c", "b", "bc", "cb", "a", "ac", "ca", "ab", "ba", "abc", "bac", "bca", "acb", "cab", "cba"])),
    ]
    
    gen_all_strings_ts = pst.TestSuite()
    
    for test in tests:
        computed = sorted(mp2.gen_all_strings(test[0]))
        expected = test[1]
        gen_all_strings_ts.run_test(computed, expected)
        
    gen_all_strings_ts.report_results()
    print


# Run the test functions
remove_duplicates_test()
intersect_test()
merge_test()
merge_sort_test()
gen_all_strings_test()