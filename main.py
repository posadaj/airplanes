from turtle import Turtle


YAW_CHANGE_SIZE = 10
MAX_SPEED = 10


class Airplane:

	def __init__(self):
		self.turtle = Turtle()
		self.screen = self.turtle.screen

		self.setup_window()
		self.setup_cursor()
		self.setup_listeners()

	def setup_window(self):
		self.screen.title('Airplane Control')
		self.screen.bgcolor('white')

	def setup_cursor(self):
		self.flight_speed = 0
		self.turtle.shapesize(2, 2, 1)

	def setup_listeners(self):
		self.screen.onkey(self.increase_speed, "Up")
		self.screen.onkey(self.decrease_speed, "Down")
		self.screen.onkey(self.turn_left, "Left")
		self.screen.onkey(self.turn_right, "Right")
		self.screen.onkey(self.reset, "Return")
		self.screen.listen()

	def increase_speed(self):
		self.flight_speed = min(self.flight_speed + 1, MAX_SPEED)

	def decrease_speed(self):
		self.flight_speed = max(self.flight_speed - 1, 0)

	def turn_left(self):
		self.turtle.left(YAW_CHANGE_SIZE)

	def turn_right(self):
		self.turtle.right(YAW_CHANGE_SIZE)

	def active_fly(self):
		self.turtle.forward(1 * self.flight_speed)
		self.screen.ontimer(self.active_fly, 100)

	def reset(self):
		# Navigate back to home
		self.screen.bgcolor('blue')
		self.turtle.penup()
		self.turtle.home()

		# Reset state
		self.screen.resetscreen()
		self.setup_cursor()
		self.setup_window()


	def fly(self):
		self.screen.ontimer(self.active_fly, 250)
		self.screen.mainloop()


def main():
	airplane = Airplane()

	airplane.fly()


if __name__ == '__main__':
	main()