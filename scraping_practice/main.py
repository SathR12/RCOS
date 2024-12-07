from chart import *
from parser import dates, cases


if __name__ == "__main__":
    #covid_graph = Diagram({2018: 10, 2019: 50, 2020: 30})
    print(dates, cases)
    covid_graph = Diagram(dates, cases)
    covid_graph.set_title("COVID-19 Cases")
    covid_graph.set_dimensions(10, 4)
    covid_graph.set_legend("Cases")
    covid_graph.set_x_increment(1)
    covid_graph.initialize_graph(labelx = "Years", labely = "Cases in Millions")
    covid_graph.show_graph()
