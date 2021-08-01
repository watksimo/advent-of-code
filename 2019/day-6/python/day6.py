import networkx as nx

def load_input(input_filename):
  f = open(input_filename, "r")
  conn_array = [_.strip().split(")") for _ in f.readlines()]
  graph = nx.Graph()
  graph.add_edges_from(conn_array)
  return graph

def solve_part1(input_graph):
  total_dist = 0
  shortest_path_lengths = nx.all_pairs_shortest_path_length(input_graph)
  for node in shortest_path_lengths:
    if node[0] == "COM": return sum(node[1].values())

def solve_part2(input_graph):
  you_orbit = list(input_graph.edges("YOU"))[0][1]
  san_orbit = list(input_graph.edges("SAN"))[0][1]
  return len(nx.shortest_path(input_graph, source=you_orbit, target=san_orbit)) - 1

if __name__ == '__main__':
  input_graph = load_input("../input.txt")
  total_orbits = solve_part1(input_graph)
  you_to_santa = solve_part2(input_graph)

  # Solutions
  print("Part 1: {}".format(total_orbits))
  print("Part 2: {}".format(you_to_santa))
  
