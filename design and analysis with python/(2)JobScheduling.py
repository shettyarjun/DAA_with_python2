class Job:
    def __init__(self, taskid, deadline, profit):
        self.taskid = taskid
        self.deadline = deadline
        self.profit = profit

def schedule_jobs(jobs, T):
    profit = 0
    slot = [0] * T
    
    # Sort jobs based on profit (highest profit first)
    jobs.sort(key=lambda x: x.profit, reverse=True)
    
    # Iterate through each job
    for j in jobs:
        # Try to find a suitable slot starting from nearest deadline
        for i in range(min(j.deadline - 1, T - 1), -1, -1):
            if slot[i] == 0:  # If the slot is available
                slot[i] = j.taskid
                profit += j.profit
                break  # Job scheduled, break the loop
    
    # Print scheduled jobs and total profit
    print("Scheduled Jobs:", [x for x in slot if x != 0])
    print("Total Profit:", profit)

if __name__ == "__main__":
    num_jobs = int(input("Enter number of jobs: "))
    
    # Collect job details from the user
    jobs = []
    for i in range(num_jobs):
        task_id = int(input(f"Task ID for Job {i + 1}: "))
        deadline = int(input(f"Deadline for Job {i + 1}: "))
        profit = int(input(f"Profit for Job {i + 1}: "))
        jobs.append(Job(task_id, deadline, profit))
    
    deadline_limit = int(input("Enter Deadline Limit: "))
    schedule_jobs(jobs, deadline_limit)
