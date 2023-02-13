import time
import datetime

motors = 0
wheels = 0
tank = 0


class my_task():
    name = ""
    period = -1
    execution_time = -1
    max_period = -1

#################################################################################
    def __init__(self, name, period, execution_time, max_period):

        self.name = name
        self.period = period
        self.execution_time = execution_time
        self.max_period = max_period

#################################################################################
    def run(self):
        print("Oil stocked: {}".format(tank))
        print("Motors produced: {}".format(motors))
        print("Wheels produced: {}".format(wheels))
        print("\tRunning task {}".format(self.name))
        time.sleep(self.execution_time)
        print("\tEnding task {}".format(self.name))
        updatePeriods(self.execution_time)


#################################################################################
if __name__ == '__main__':
    last_execution = datetime.datetime.now()

    # Instanciation of task objects
    task_list = []
    task_list.append(my_task(name="Pump 1", period=5,
                     execution_time=2, max_period=5))
    task_list.append(my_task(name="Pump 2", period=15,
                     execution_time=3, max_period=15))
    task_list.append(my_task(name="Machine 1", period=5,
                     execution_time=5, max_period=5))
    task_list.append(my_task(name="Machine 2", period=5,
                     execution_time=3, max_period=5))

    def updatePeriods(executionTime: int):
        for current_task in task_list:
            current_task.period -= executionTime
            if current_task.period <= 0:
                current_task.period += current_task.max_period

    while(True):
        for i in task_list:
            if (i.period >= i.execution_time):
                if i.name == "Pump 1" and (tank + 10) <= 50:
                    i.run()
                    tank += 10
                elif i.name == "Pump 2" and (tank + 20) <= 50:
                    i.run()
                    tank += 20
                elif i.name == "Machine 1" and tank >= 25 and (motors == 0 or wheels/motors >= 4):
                    i.run()
                    motors += 1
                    tank -= 25
                elif i.name == "Machine 2" and tank >= 5 and (motors == 0 or wheels/motors < 4):
                    for j in range(0, 4):
                        if (tank > 0 and wheels / 4 != 0):
                            i.run()
                            wheels += 1
                            tank -= 5
