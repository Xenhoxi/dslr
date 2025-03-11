from dataset import Dataset
import matplotlib.pyplot as plt
import pandas as pd
from scatter_plot import scatter_plot
from histogram import histogram_plot
import sys
import math


def main() -> None:
    try:
        dataset = Dataset(sys.argv[1])
        features = dataset.clean_data_describe().columns
        print(features)
        data_set = dataset.get_dataset()
        print(data_set)
        subplot_place = 1
        plt.figure(figsize=(29, 18))
        # setdata = pd.plotting.scatter_matrix(data_set)

        for x in range(len(features)):
            for y in range(len(features)):
                plt.subplot(13, 13, subplot_place)
                if (features[x] == features[y]):
                    histogram_plot(features[x], data_set)
                else:
                    scatter_plot(features[x], features[y], data_set)
                subplot_place += 1
                plt.xticks([])
                plt.yticks([])
                plt.tight_layout()
        plt.legend(data_set['Hogwarts House'].unique(), bbox_to_anchor=(0.9, 0.25), fontsize=24)
        plt.savefig("mixed_test.png")
        plt.show()
    except (KeyboardInterrupt) as msg:
        print(msg)


if __name__ == '__main__':
    main()
