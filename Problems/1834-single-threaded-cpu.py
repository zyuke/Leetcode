class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        N = len(tasks)

        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort()

        res = []
        import heapq
        taskQ = []
        heapq.heapify(taskQ)
        curTime = 0

        while True:
            if len(res) == N:
                break

            # add due tasks
            while tasks and tasks[0][0] <= curTime:
                item = tasks.pop(0)
                heapq.heappush(taskQ, (item[1], item[2]))

            # check cur pending task
            if taskQ:
                curItem = heapq.heappop(taskQ)
                res.append(curItem[1])
                curTime += curItem[0] 
            # add more tasks if queue is empty
            else:
                if tasks:
                    # idle
                    if tasks[0][0] > curTime:
                        item = tasks.pop(0)
                        heapq.heappush(taskQ, (item[1], item[2]))
                        curTime = item[0]

        return res
