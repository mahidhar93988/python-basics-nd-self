# Define the required class here...

class Flight:
    def __init__(self, upTime, downTime):
        self.upTime = upTime
        self.downTime = downTime

    def calculateFlight(self):
        # Your Code goes here
        takeoff = self.upTime.split(":")
        landing = self.downTime.split(":")
        input1 = [int(i) for i in takeoff]
        input2 = [int(i) for i in landing]
        time_1 = input1[0]*60+input1[1]
        time_2 = input2[0]*60+input2[1]
        return abs(time_1-time_2)


# DO NOT CHANGE ANYTHING BELOW THIS LINE

if __name__ == '__main__':

    t1 = input()
    t2 = input()

    f1 = Flight(t1, t2)
    print(f1.calculateFlight())
