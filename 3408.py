class TaskManager:

    def __init__(self, tasks: List[List[int]]):
       self.di = {}
       self.sl = SortedList()
       for t in tasks:
           self.add(*t)
                                                                   
    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.di[taskId] = (userId, priority)
        self.sl.add((-priority, -taskId))
                                                          
    def edit(self, taskId: int, newPriority: int) -> None:
        userId, priority = self.di[taskId]
        self.sl.remove((-priority, -taskId))
        self.di.[taskId] = (userId, newPriority)
        self.sl.add((-newPriority, -taskId))
                                       
    def rmv(self, taskId: int) -> None:
       userID, priority = self.di[taskId]
       del self.di[taskId]
       self.sl.remove((-priority, -taskId))
                             
    def execTop(self) -> int:
        if not self.sl:
            return -1
        priority, taskId = self.sl.pop(0)
        taskId = -taskId
        userId, _ = self.di[taskId]
        del self.di[taskId]
        return userId
        


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()
