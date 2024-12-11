#https://www.geeksforgeeks.org/mealy-and-moore-machines-in-toc/
states = {
    0 : {"out" : 0, "next":{1, 2} }, 
    1 : {"out" : 0, "next": {1, 3} },
    2 : {"out" : 0, "next":{4, 2} },
    3 : {"out" : 1, "next":{4, 2} },
    4 : {"out" : 1, "next":{1, 3} }
}


class mooreMachine :
    def __init__(self):
        pass
    def input(self):
        pass
    def currentState(self):
        pass
    def output(self):
        pass

print(states[1]["out"])