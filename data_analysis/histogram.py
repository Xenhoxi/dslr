from dataset import Dataset
import matplotlib.pyplot as plt
import numpy as np
import sys
import math


def main() -> None:
    try:
        dataset = Dataset(sys.argv[1])
        set = dataset.get_dataset()

        plt.figure(figsize=(29, 18))
        features_name = dataset.clean_data_describe().columns
        # ncols = round(math.sqrt(len(features_name)))
        # fig, ax = plt.subplots(ncols=ncols, nrows=ncols, figsize=(29, 18))

        # for a in ax.ravel():
        #     a.axis("off")

        for x in range(len(features_name)):
            plt.subplot(3, 5, x + 1)
            histogram_plot(features_name[x], set)
            plt.title(features_name[x])
        #     x = math.floor(i / ncols)
        #     y = math.floor(i % ncols)
        #     for house in all_house:
        #         data_by_house = set.loc[set['Hogwarts House'] == house]
        #         feature = data_by_house[features_name[i]]
        #         ax[x, y].hist(feature, color=color_map[house], alpha=0.5, edgecolor='black', label=house)
        #         ax[x, y].title.set_text(features_name[i])
        #         ax[x, y].axis("on")
        plt.legend(set['Hogwarts House'].unique(), bbox_to_anchor=(0.9, 0.25), fontsize=24)

        # fig.savefig("histogram.png")
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
