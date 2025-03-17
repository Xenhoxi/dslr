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
        # print(data_set)
        subplot_place = 1
        plt.figure(figsize=(29, 18))
        for x in range(len(features)):
            for y in range(len(features)):
                plt.subplot(13, 13, subplot_place)
                if (features[x] == features[y]):
                    histogram_plot(features[x], data_set)
                else:
                    scatter_plot(features[y], features[x], data_set)
                if x != 12:
                    plt.xticks([])
                else:
                    plt.xlabel(f"{features[y]}")
                if y != 0:
                    plt.yticks([])
                else:
                    plt.ylabel(f"{features[x]}")
                subplot_place += 1
        plt.tight_layout()
        plt.subplots_adjust(wspace=0, hspace=0)
        plt.legend(data_set['Hogwarts House'].unique(), bbox_to_anchor=(0.9, 0.25), fontsize=10)
        plt.show()
        plt.savefig("pair_plot.png")
    except (KeyboardInterrupt) as msg:
        print(msg)


if __name__ == '__main__':
    main()
