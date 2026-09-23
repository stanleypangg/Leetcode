Task = namedtuple('Task', ['taskId', 'userId', 'description', 'dueDate', 'tags'])

class TodoList:

    def __init__(self):
        self.serial = 0
        self.tasks = {}
        self.users = defaultdict(set)

    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: list[str]) -> int:
        self.serial += 1
        taskId = self.serial

        task = Task(taskId, userId, taskDescription, dueDate, set(tags))
        self.tasks[taskId] = task
        self.users[userId].add(taskId)

        return taskId

    def getAllTasks(self, userId: int) -> list[str]:
        taskIds = list(self.users[userId])
        taskIds.sort(key=lambda t: self.tasks[t].dueDate)
        return [self.tasks[t].description for t in taskIds]

    def getTasksForTag(self, userId: int, tag: str) -> list[str]:
        taskIds = [t for t in self.users[userId] if tag in self.tasks[t].tags]
        taskIds.sort(key=lambda t: self.tasks[t].dueDate)
        return [self.tasks[t].description for t in taskIds]

    def completeTask(self, userId: int, taskId: int) -> None:
        task = self.tasks.get(taskId)
        if task is None or task.userId != userId:
            return
        
        del self.tasks[taskId]
        self.users[userId].remove(taskId)

# Your TodoList object will be instantiated and called as such:
# obj = TodoList()
# param_1 = obj.addTask(userId,taskDescription,dueDate,tags)
# param_2 = obj.getAllTasks(userId)
# param_3 = obj.getTasksForTag(userId,tag)
# obj.completeTask(userId,taskId)