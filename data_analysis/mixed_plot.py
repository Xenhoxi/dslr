from dataset import Dataset
import matplotlib.pyplot as plt
from scatter_plot import scatter_plot
from histogram import histogram_plot
import sys
import math


def main() -> None:
	try:
		dataset = Dataset(sys.argv[1])
		x_plots = ['Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Ancient Runes']
		y_plots = ['Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Ancient Runes']
		data_set = dataset.get_dataset()
		subplot_place = 0
		plt.figure(figsize=(29, 18))
		for x in range(len(x_plots)):
			for y in range(len(y_plots)):
				print(subplot_place + 1)
				plt.subplot(4, 4, subplot_place + 1)
				if (x_plots[x] == y_plots[y]):
					histogram_plot(x_plots[x], data_set)
				else:
					scatter_plot(x_plots[x], y_plots[y], data_set)
				print("passage: ", x)
				subplot_place += 1
		plt.savefig("mixed_test.png")
		plt.show()
	except (KeyboardInterrupt) as msg:
		print(msg)

if __name__ == '__main__':
	main()