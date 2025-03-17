from dataset import Dataset
import matplotlib.pyplot as plt
import numpy as np
import sys


def main() -> None:
    try:
        dataset = Dataset(sys.argv[1])
        set = dataset.get_dataset()

        plt.figure(figsize=(29, 18))
        features_name = dataset.clean_data_describe().columns
        for x in range(len(features_name)):
            plt.subplot(4, 4, x + 1)
            histogram_plot(features_name[x], set)
            plt.title(features_name[x])
        plt.subplot(4, 4, x + 1)
        plt.legend(set['Hogwarts House'].unique(), bbox_to_anchor=(1, 0.55), fontsize=20)
        plt.savefig("histogram.png")
        plt.show()
    except (KeyboardInterrupt) as err:
        print(err)


def histogram_plot(feature, data_set):
    color_map = {'Ravenclaw':'Green', 'Slytherin':'Orange', 'Gryffindor':'Red', 'Hufflepuff':'Blue'}
    all_house = data_set['Hogwarts House'].unique()
    for house in all_house:
        data_by_house = data_set.loc[data_set['Hogwarts House'] == house]
        f_feature = data_by_house[feature]
        plt.hist(f_feature, color=color_map[house], alpha=0.5, edgecolor='black', label=house)



if __name__ == '__main__':
    main()
