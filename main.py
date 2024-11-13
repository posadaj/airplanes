from turtle import Turtle

YAW_CHANGE_SIZE = 10


class Airplane:



	def __init__(self):
		self.turtle = Turtle()
		self.screen = self.turtle.screen
		self.flight_speed = 1

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
		self.screen.onkey(self.yaw_left, "Left")
		self.screen.onkey(self.yaw_right, "Right")
		self.screen.listen()

	def increase_speed(self):
		# print("Current speed: " + str(self.turtle.speed()))
		# self.turtle.speed(self.turtle.speed() + 1)
		self.flight_speed = self.flight_speed + 1

	def decrease_speed(self):
		# print("Current speed: " + str(self.turtle.speed()))
		# self.turtle.speed(self.turtle.speed() - 1)
		self.flight_speed = self.flight_speed - 1

	def yaw_left(self):
		self.turtle.left(YAW_CHANGE_SIZE)

	def yaw_right(self):
		self.turtle.right(YAW_CHANGE_SIZE)

	def active_fly(self):
		self.turtle.forward(1 * self.flight_speed)
		self.screen.ontimer(self.active_fly, 100)


	def fly(self):
		self.screen.ontimer(self.active_fly, 250)
		self.screen.mainloop()


def main():
	airplane = Airplane()

	airplane.fly()


if __name__ == '__main__':
	main()