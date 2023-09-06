class Job:
    def __init__(self, taskid, deadline, profit):
        self.taskid = taskid
        self.deadline = deadline
        self.profit = profit

def schedule_jobs(jobs, T):
    jobs.sort(key=lambda x: x.profit, reverse=True)
    slot = [0] * T
    profit = 0

    for j in jobs:
        for i in range(min(j.deadline - 1, T - 1), -1, -1):
            if not slot[i]:
                slot[i] = j.taskid
                profit += j.profit
                break

    print("Scheduled Jobs:", [x for x in slot if x != 0])
    print("Total Profit:", profit)

if __name__ == "__main__":
    jobs = []
    num_jobs = int(input("Enter the number of jobs: "))

    for i in range(num_jobs):
        task_id, deadline, profit = map(int, input(f"Enter Task ID, Deadline, Profit for Job {i + 1}: ").split())
        jobs.append((task_id, deadline, profit))

    deadline_limit = int(input("Enter Deadline Limit: "))
    schedule_jobs(jobs, deadline_limit)
