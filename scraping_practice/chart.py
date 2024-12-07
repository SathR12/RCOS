from matplotlib import pyplot as plt
import numpy as np


class Diagram:
    
    X, Y, LEGEND, TITLE, LENGTH, WIDTH = None, None, None, None, None, None
    
    def __init__(self, *args):
        if len(args) == 1 and type(args[0]) == dict :
            self.data_set = args[0] 
            self.keys = list(self.data_set.keys())
            self.values = list(self.data_set.values())
        
        elif len(args) == 2:
            self.keys, self.values = args[0], args[1]
            self.data_set = dict(zip(args[0], args[1]))
            #print(self.data_set)
        
        assert len(args) == 1 or len(args) == 2, "Invalid number of parameters"
        
    #must set graph title 
    def set_title(self, title):
        Diagram.TITLE = title
    
    #must set graph dimensions
    def set_dimensions(self, length, width):
        Diagram.LENGTH, Diagram.WIDTH = length, width
        
    def set_legend(self, legend):
        Diagram.LEGEND = legend
    
    def set_x_increment(self, increment):
        Diagram.X = increment
        
    def set_y_increment(self, increment):
        Diagram.Y = increment
        
    def initialize_graph(self, labelx = "x-axis", labely = "y-axis"):
        figure = plt.figure(figsize = (Diagram.LENGTH, Diagram.WIDTH))
        plt.plot(self.keys, self.values)
        plt.xlabel(labelx)
        plt.ylabel(labely)
        plt.xticks(np.arange(min(self.keys), max(self.keys) + 1, Diagram.X))
        #plt.yticks(np.arange(min(self.values), max(self.values) + 1, Diagram.Y))
        plt.title(Diagram.TITLE)
        plt.legend(Diagram.LEGEND)
    
    def show_graph(self):
        plt.gcf().canvas.set_window_title("Graph")
        plt.show()
        
        

