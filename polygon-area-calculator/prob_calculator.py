import copy
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = [k for k, v in kwargs.items() for i in range(v)]

    def draw(self, number):
        self.number = number
        try:
            # return a number of random balls
            draw = random.sample(self.contents, k=self.number)
        except:
            # If more balls are drawn than available, return all the balls.
            draw = self.contents
        return draw

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    expected_balls = [k for k, v in expected_balls.items() for i in range(v)]
    success = 0

    # perform experiment for a specific number of times
    for i in range(num_experiments):
        # return instance of draw method
        draw = hat.draw(num_balls_drawn)

        # check if all expected balls are drawn
        for i in range(len(expected_balls)):
            if expected_balls[i] not in draw:
                continue
            elif expected_balls[i] in draw:
                draw.remove(expected_balls[i])

        if (num_balls_drawn - len(expected_balls)) == len(draw):
            success += 1

    probability = success / num_experiments

    return probability