from dataset import Dataset
import matplotlib.pyplot as plt
import sys
import math


def main() -> None:
    try:
        dataset = Dataset(sys.argv[1])
        features_name = dataset.clean_data_describe().columns
        test = dataset.get_dataset()

        color_map = {'Ravenclaw':'Green', 'Slytherin':'Orange', 'Gryffindor':'Red', 'Hufflepuff':'Blue'}
        all_house = test['Hogwarts House'].unique()
        plt.figure(figsize=(29, 18))
        for x in range((len(features_name))):
            plt.subplot(3, 5, x + 1)
            for house in all_house:
                data_by_house = test.loc[test['Hogwarts House'] == house]
                plt.xlabel(features_name[x])
                if x == len(features_name) - 1:
                    plt.ylabel(features_name[0])
                    y_feature = data_by_house[features_name[0]]
                else:
                    plt.ylabel(features_name[x + 1])
                    y_feature = data_by_house[features_name[x + 1]]
                x_feature = data_by_house[features_name[x]]
                plt.scatter(x_feature, y_feature, color=color_map[house], alpha=0.5)
        plt.show()
    except KeyboardInterrupt as msg:
        print(msg)


if __name__ == '__main__':
    main()