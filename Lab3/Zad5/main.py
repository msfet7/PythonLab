#https://www.geeksforgeeks.org/mealy-and-moore-machines-in-toc/
states = {
    0 : {"out" : 0, "next":[1, 2] }, 
    1 : {"out" : 0, "next": [1, 3] },
    2 : {"out" : 0, "next":[4, 2] },
    3 : {"out" : 1, "next":[4, 2] },
    4 : {"out" : 1, "next":[1, 3] }
}
# state: {output, [next state if 0, next state if 1]}

class mooreMachine :
    def __init__(self):
        self.currState = 0
    def input(self, input):
        nextState = states[self.currState]["next"][input]
        self.currState = nextState
    def currentState(self):
        return self.currState
    def output(self):
        return states[self.currState]["out"]


machineUnderTest = mooreMachine()
inputs = [1, 1, 0, 0, 1, 0, 1]

print("Start state {} with output {}".format(machineUnderTest.currentState(), machineUnderTest.output()))

for oneInput in inputs :
    machineUnderTest.input(oneInput)
    print(str(oneInput))
    print("Current state {} with output {}".format(machineUnderTest.currentState(), machineUnderTest.output()))
    print('\n')