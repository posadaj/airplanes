from turtle import Turtle


class Airplane:

	def __init__(self):
		self.turtle = Turtle()
		self.screen = self.turtle.screen
		self.setup_window()
		self.setup_cursor()
		self.setup_listeners()

	def setup_window(self):
		self.screen.title('Airplane Control')
		# t.screen.bgcolor("orange")

	def setup_cursor(self):
		self.turtle.speed(1)
		self.turtle.shapesize(2, 2, 1)

	def setup_listeners(self):
		self.screen.onkey(self.increase_speed, "Up")
		self.screen.onkey(self.decrease_speed, "Down")
		self.screen.onkey(self.yaw_lef, "Left")
		self.screen.onkey(self.yaw_right, "Right")
		self.screen.listen()

	def increase_speed(self):
		print("Current speed: " + str(self.turtle.speed()))
		self.turtle.speed(self.turtle.speed() + 1)

	def decrease_speed(self):
		print("Current speed: " + str(self.turtle.speed()))
		self.turtle.speed(self.turtle.speed() - 1)


	def fly(self):
		for _ in range(10):
			self.turtle.forward(100)
			self.turtle.left(90)
			self.turtle.forward(50)
			self.turtle.left(10)
			self.turtle.forward(50)
			self.turtle.home()


def main():
	airplane = Airplane()

	airplane.fly()


if __name__ == '__main__':
	main()