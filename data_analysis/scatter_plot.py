from dataset import Dataset
import matplotlib.pyplot as plt
import sys


def main() -> None:
    try:
        dataset = Dataset(sys.argv[1])
        features_name = dataset.clean_data_describe().columns
        test = dataset.get_dataset()

        plt.figure(figsize=(29, 18))
        for x in range((len(features_name))):
            plt.subplot(3, 5, x + 1)
            if x == len(features_name) - 1:
                scatter_plot(features_name[x], features_name[0], test)
                plt.xlabel(features_name[x])
                plt.ylabel(features_name[0])
            else:
                scatter_plot(features_name[x], features_name[x + 1], test)
                plt.xlabel(features_name[x])
                plt.ylabel(features_name[0 + 1])
        plt.legend(test['Hogwarts House'].unique(), bbox_to_anchor=(0.9, 0.25), fontsize=24)
        plt.savefig("scatter_plot.png")
        plt.show()
    except KeyboardInterrupt as msg:
        print(msg)


def scatter_plot(feature_1, feature_2, test):
    color_map = {'Ravenclaw': 'Green', 'Slytherin': 'Orange', 'Gryffindor': 'Red', 'Hufflepuff': 'Blue'}
    all_house = test['Hogwarts House'].unique()
    for house in all_house:
        data_by_house = test.loc[test['Hogwarts House'] == house]
        x_feature = data_by_house[feature_1]
        y_feature = data_by_house[feature_2]
        plt.scatter(x_feature, y_feature, color=color_map[house], alpha=0.5)

if __name__ == '__main__':
    main()