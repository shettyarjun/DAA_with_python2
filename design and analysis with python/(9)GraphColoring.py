class Graph:
    def __init__(self):
        self.edges = {}
        
    def add_edge(self, s1, s2):
        self.edges.setdefault(s1, []).append(s2)
        self.edges.setdefault(s2, []).append(s1)
        
    def schedule(self):
        colors = {}
        for subject, neighbors in self.edges.items():
            used_colors = {colors.get(n, 0) for n in neighbors if n in colors}
            colors[subject] = min(set(range(1, len(self.edges) + 1)) - used_colors, default=len(self.edges) + 1)
        return colors
    
    def min_time_slots(self):
        return max(self.schedule().values())

def main():
    graph = Graph()
    
    n = int(input("Enter number of subjects: "))
    for _ in range(n):
      subjects = [input("Enter subject: ")]
      m = int(input("Enter number of students: "))
      for i in range(m):
        input(f"Enter student {i+1} : ")
    
    num_edges = int(input("Enter number of edges: "))
    for _ in range(num_edges):
        s1, s2 = input("Enter edge (subject1 subject2): ").split()
        graph.add_edge(s1, s2)
    
    print("Minimum time slots needed:", graph.min_time_slots())

if __name__ == "__main__":
    main()
