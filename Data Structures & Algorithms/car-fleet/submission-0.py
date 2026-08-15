class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car=[]
        fleets=[]
        time=[0]*len(position)
        for i in range(len(position)):
            time = (target-position[i])/speed[i]
            car.append([position[i],time])
        car.sort(reverse = True)
        for i in range(len(position)):
            cur_t=car[i][1]
            if len(fleets) == 0 or cur_t> fleets[-1]:
                fleets.append(cur_t)
        return len(fleets)