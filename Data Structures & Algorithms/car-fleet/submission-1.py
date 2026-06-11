class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i],speed[i]) for i in range(len(position))]
        cars.sort(reverse = True)
        slowest = []
        for i,c in enumerate(cars):
            time = (target - c[0])/c[1]
            if i==0:
                slowest.append(time)
            if slowest[-1] < time:
                slowest.append(time)
        return len(slowest)