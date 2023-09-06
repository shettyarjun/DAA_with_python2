class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, subject1, subject2):
        if subject1 not in self.graph:
            self.graph[subject1] = []
        if subject2 not in self.graph:
            self.graph[subject2] = []
        
        self.graph[subject1].append(subject2)
        self.graph[subject2].append(subject1)

    def get_minimum_time_slots(self):
        color_map = {}
        max_color = 0

        for subject in self.graph:
            used_colors = set()
            for neighbor in self.graph[subject]:
                if neighbor in color_map:
                    used_colors.add(color_map[neighbor])
            available_color = 1
            while available_color in used_colors:
                available_color += 1
            color_map[subject] = available_color
            max_color = max(max_color, available_color)

        return max_color

def main():
    graph = Graph()
    student={}
    n=int(input("enter the number of subjects:"))
    for _ in range(n):
      subjects = [input("Enter subject: ")]
      m = int(input("Enter number of students: "))
      for i in range(m):
        input(f"Enter student {i+1} : ")
        
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        subject1, subject2 = input("Enter edge (subject1 subject2): ").split()
        graph.add_edge(subject1, subject2)

    minimum_time_slots = graph.get_minimum_time_slots()
    print(f"Minimum time slots needed: {minimum_time_slots}")

if __name__ == "__main__":
    main()
