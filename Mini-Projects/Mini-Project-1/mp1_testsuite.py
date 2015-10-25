# Test Suite for Mini Project 1
# Principles of Computing, Part 2
# Jordan Hall
# 10/24/2015

import poc_simpletest as pst
import mp1_vf as mp1

## Apocalypse Class Function Tests

# clear function test
def clear_test():    
    print "Commencing clear function test..."
    tests = [(mp1.Apocalypse(grid_height=4, grid_width=4, obstacle_list=[(1,0)]), [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
             (mp1.Apocalypse(grid_height=4, grid_width=4, zombie_list=[(2,0)]), [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
             (mp1.Apocalypse(grid_height=4, grid_width=4, human_list=[(0,0)]), [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
             (mp1.Apocalypse(grid_height=4, grid_width=4, obstacle_list=[(0,0),(1,1),(2,2)], zombie_list=[(2,0),(0,2)], human_list=[(1,0),(0,1)]), [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
             (mp1.Apocalypse(grid_height=5, grid_width=10, obstacle_list=[(0,0),(1,6),(2,5)], zombie_list=[(2,0),(0,2)], human_list=[(4,7),(0,1)]), [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]),
    ]
    
    clear_ts = pst.TestSuite()
    
    for test in tests:
        test[0].clear()
        computed = test[0]._cells
        expected = test[1]
        clear_ts.run_test(computed, expected)
        
    clear_ts.report_results()
    print

# add_zombie function test
def add_zombie_test():    
    print "Commencing add_zombie function test..."
    tests = [(mp1.Apocalypse(grid_height=4, grid_width=4, obstacle_list=[(1,0)]), (1,2), [(1,2)]),
             (mp1.Apocalypse(grid_height=4, grid_width=4, zombie_list=[(2,0)]), (1,2), [(2,0), (1,2)]),
             (mp1.Apocalypse(grid_height=4, grid_width=4, human_list=[(0,0)]), (0,1), [(0,1)]),
             (mp1.Apocalypse(grid_height=4, grid_width=4, obstacle_list=[(0,0),(1,1)], zombie_list=[(2,0),(0,2)], human_list=[(1,0),(0,1)]), (2,2), [(2,0),(0,2),(2,2)]),
             (mp1.Apocalypse(grid_height=5, grid_width=10, obstacle_list=[(0,0),(1,6),(2,5)], zombie_list=[(2,0),(0,2)], human_list=[(4,7),(0,1)]), (4,1), [(2,0),(0,2),(4,1)]),
    ]
    
    add_zombie_ts = pst.TestSuite()
    
    for test in tests:
        test[0].add_zombie(row=test[1][0], col=test[1][1])
        computed = test[0]._zombie_list
        expected = test[2]
        add_zombie_ts.run_test(computed, expected)
        
    add_zombie_ts.report_results()
    print

# num_zombie function test
def num_zombies_test():    
    print "Commencing add_zombie function test..."
    tests = [(mp1.Apocalypse(grid_height=4, grid_width=4, obstacle_list=[(1,0)]), 0),
             (mp1.Apocalypse(grid_height=4, grid_width=4, zombie_list=[(2,0)]), 1),
             (mp1.Apocalypse(grid_height=4, grid_width=4, zombie_list=[(0,1)], human_list=[(0,0)]), 1),
             (mp1.Apocalypse(grid_height=4, grid_width=4, obstacle_list=[(0,0),(1,1)], zombie_list=[(2,0),(0,2),(2,2)], human_list=[(1,0),(0,1)]), 3),
             (mp1.Apocalypse(grid_height=5, grid_width=10, obstacle_list=[(0,0),(1,6),(2,5)], zombie_list=[(2,0),(0,2),(4,1),(1,4)], human_list=[(4,7),(0,1)]), 4),
    ]
    
    num_zombies_ts = pst.TestSuite()
    
    for test in tests:
        computed = test[0].num_zombies()
        expected = test[1]
        num_zombies_ts.run_test(computed, expected)
        
    num_zombies_ts.report_results()
    print



# Run the test functions
clear_test()
add_zombie_test()
num_zombies_test()

