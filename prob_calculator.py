import random

class Hat:

    def __name__(self):
        return "hat"
    def __init__(self, **args):
        self.args = args
        self.contents = []
        self.drawn_balls = []
        if len(args) >= 1:
            for i, j in self.args.items():
                for k in range(j):
                    self.contents.append(i)
        else:
            print("Error: You must introduce at least 1 argument")

    def draw(self, ball_number):

        choice_balls = []
        if len(self.contents) < ball_number:
            #print("Not enough balls in the hat. Returning all the balls...")
            for i in range(len(self.drawn_balls)):
                self.contents.append(self.drawn_balls[i])
            self.drawn_balls = []
        for i in range(ball_number):
          #print(self.contents)
          choice = random.choice(self.contents)
          choice_balls.append(choice)
          self.drawn_balls.append(choice_balls[i])
          popindex = self.contents.index(choice)
          self.contents.pop(popindex)
        return choice_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    expected_balls_list = []
    if len(expected_balls) >= 1:
      if num_balls_drawn <= len(expected_balls):
        for i, j in expected_balls.items():
            for k in range(j):
                expected_balls_list.append(i)
        for exp in range (num_experiments):
            expected_balls_list.sort()
            drawn_balls_list = hat.draw(num_balls_drawn)
            #print("Drawn balls: ",drawn_balls_list)
            #print("Expected balls: ",expected_balls_list)
            ok = 0
            for i in expected_balls_list:
                if i in drawn_balls_list:
                    ok+=1
                    index_element_to_delete = drawn_balls_list.index(i)
                    drawn_balls_list.pop(index_element_to_delete)
                else:
                    ok+=0
            #print(ok)
            #print("exp",len(expected_balls_list))
            if ok == len(expected_balls_list):
                success +=1
                #print(success)
            exp += 1
            #print("Experiment number: ",exp)
            #print("________________")
        #print("The experiment has concluded.")
        #print("________________")
        return success/num_experiments
      else:
        return 1.0
    else:
        return("Error: You must introduce at least 1 argument for the expected balls")
