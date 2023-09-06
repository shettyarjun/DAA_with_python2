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
    num_jobs = int(input("Enter number of jobs: "))
    jobs = [Job(*map(int, input(f"Task ID, Deadline, Profit for Job {i + 1}: ").split())) for i in range(num_jobs)]
    deadline_limit = int(input("Enter Deadline Limit: "))
    schedule_jobs(jobs, deadline_limit)
