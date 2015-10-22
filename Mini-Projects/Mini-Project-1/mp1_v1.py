# Mini Project 1 - Zombie Apocalypse
# Principles of Computing, Part 2
# Jordan Hall
# 10/21/2015

"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        poc_grid.Grid.clear(self)
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)       
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        boundary = poc_queue.Queue()        
        
        if entity_type == ZOMBIE:
            for zombie in self._zombie_list: 
                boundary.enqueue(zombie)
            opposite = self._human_list
        else:
            for human in self._human_list: 
                boundary.enqueue(human)
            opposite = self._zombie_list
                    
        visited = poc_grid.Grid(self.get_grid_height(), self.get_grid_width())
        area_of_grid = self.get_grid_height()*self.get_grid_width()
        distance_field = [[area_of_grid for dummy_col in range(self.get_grid_width())] for dummy_row in range(self.get_grid_height())]
        
        for cell in self._cells:
            if not self.is_empty(cell[0], cell[1]) and cell not in opposite:
                visited.set_full(cell[0], cell[1])
        
        for cell in boundary:
            distance_field[cell[0]][cell[1]] = 0
        
        
        while len(boundary) > 0:
            current_cell = boundary.dequeue()
            for neighbor_cell in visited.four_neighbors(current_cell[0], current_cell[1]):
                if visited.is_empty(neighbor_cell[0], neighbor_cell[1]):
                    boundary.enqueue(neighbor_cell)
                    visited.set_full(neighbor_cell[0], neighbor_cell[1])
                    distance_field[neighbor_cell[0]][neighbor_cell[1]] = distance_field[current_cell[0]][current_cell[1]] + 1
        
        return distance_field
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        for h_index, human in enumerate(self._human_list):
            moves = self.eight_neighbors(human[0], human[1])
            
            # Remove moves that are the location of an obstacle
            #for move in moves:
            #   if self._cells[move[0]][move[1]] == OBSTACLE:
            #        moves.remove(move)
            
            # Skip if there are no possible moves
            if len(moves) == 0:
                pass
            else:
                # Create a dictionary of distances for each of the potential moves
                distance_dict = {}
                for move in moves:
                    distance_dict[move] = zombie_distance_field[move[0]][move[1]]

                # Determine the best move(s) based on maximum distance from the zombies
                best_moves = []
                max_distance = max(distance_dict.values())
                print max_distance
                print moves
                print distance_dict
                for move in moves:
                    if distance_dict[move] == max_distance:
                        best_moves.append(move)

                print best_moves
                # If more than one best move, choose one at random
                if len(best_moves) == 1:
                    best_move = best_moves[0]
                else:                
                    best_move = best_moves[random.randint(0,len(best_moves)-1)]
                self._human_list[h_index] = best_move
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        for z_index, zombie in enumerate(self._zombie_list):
            moves = self.four_neighbors(zombie[0], zombie[1])
            
            # Remove moves that are the location of an obstacle
            #for move in moves:
            #   if self._cells[move[0]][move[1]] == OBSTACLE:
            #        moves.remove(move)
            
            # Skip if there are no possible moves
            if len(moves) == 0:
                pass
            else:
                # Create a dictionary of distances for each of the potential moves
                distance_dict = {}
                for move in moves:
                    distance_dict[move] = human_distance_field[move[0]][move[1]]

                # Determine the best move(s) based on maximum distance from the zombies
                best_moves = []
                min_distance = min(distance_dict.values())
                for move in moves:
                    if distance_dict[move] == min_distance:
                        best_moves.append(move)

                # If more than one best move, choose one at random
                if len(best_moves) == 1:
                    best_move = best_moves[0]
                else:                
                    best_move = best_moves[random.randint(0,len(best_moves)-1)]
                self._zombie_list[z_index] = best_move

# Start up gui for simulation - You will need to write some code above
# before this will work without errors

poc_zombie_gui.run_gui(Apocalypse(30, 40))
