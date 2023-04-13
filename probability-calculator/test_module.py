import copy
import random

# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = [k for k, v in kwargs.items() for i in range(v)]

  def draw(self, number):
    try:
      # return a number of random balls
      self.result = random.sample(self.contents, k=number)
    except:
      # If more balls are drawn than available, return all the balls.
      self.result = self.contents
    return self.result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  expected_balls = [k for k, v in expected_balls.items() for i in range(v)]
  success = 0

  # perform experiment for a specific number of times
  for i in range(num_experiments):
    # return instance of draw method
    balls_drawn = hat.draw(num_balls_drawn)
    balls_left = copy.copy(balls_drawn)

    # check if all expected balls are drawn
    for i in range(len(expected_balls)):
      if expected_balls[i] not in balls_left:
        continue
      elif expected_balls[i] in balls_left:
        balls_left.remove(expected_balls[i])

    # if all expected balls are found in balls drawn, add increase success by 1
    if (len(balls_drawn) - len(expected_balls)) == len(balls_left):
      success += 1

  probability = success / num_experiments

  return probability
