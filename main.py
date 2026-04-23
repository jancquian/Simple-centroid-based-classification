import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

def uploaddoc():
    doc_o = pd.read_csv("../Practica4/iris.csv")
    doc_o.drop(columns=["sepal.length", "sepal.width"], inplace=True)
    #doc_o.drop_duplicates(subset=["petal.width", "petal.length", "variety"], inplace=True)
    return doc_o

def showdoc(df_original, df_new=None):

    df_original = pd.concat([df_original, df_new], ignore_index=True)
    sns.scatterplot(
        data=df_original,
        x="petal.width",
        y="petal.length",
        hue="variety",
        s=30,
        palette="Set1"
    )

    plt.xlabel("Petal Width")
    plt.ylabel("Petal Length")
    plt.title("Iris Dataset con Nuevos Puntos Clasificados")
    plt.legend(loc="upper left")
    plt.show()

def get_parameters():
    parameters = list()
    i = int(input("Proporciona el número de puntos a evaluar: "))
    for x in range(0,i):
        parameters.append((float(input("Proporciona X{}: ".format(x))), float(input("Proporciona Y{}: ".format(x)))))
    return parameters

def compute_average(doc_o):
    aux = {"Setosa":[0,0,0], "Versicolor":[0,0,0], "Virginica":[0,0,0]}
    ave_dots = list()
    #new_dots.append({"petal.length": local_dot[1], "petal.width": local_dot[0], "variety": tag})
    for register in doc_o.itertuples():
        # register[1] length, register[2] width register[3] variety
        aux[register[3]][0] += 1
        aux[register[3]][1] += register[1]
        aux[register[3]][2] += register[2]

    for key, element in aux.items():
        element[1] = element[1] /element[0]
        element[2] = element[2] / element[0]
        ave_dots.append({"petal.length": element[1], "petal.width": element[2], "variety": key})

    return pd.DataFrame(ave_dots)

def test_average_dots():
    data = uploaddoc()
    averaged = compute_average(data)
    print(averaged)
    showdoc(data, averaged)

def compute_distance(parameters, av_dots):
    n_dots = list()
    for local_dot in parameters:
        print(local_dot)
        aux_table = av_dots.copy()
        dif_x = aux_table["petal.width"] - local_dot[0]
        dif_y = aux_table["petal.length"] - local_dot[1]
        distance = (dif_x ** 2 + dif_y ** 2).pow(0.5)
        aux_table["distance"] = distance
        aux_table.sort_values(by=["distance"], inplace=True)
        print(aux_table)
        aux_table = aux_table.head(1)
        counts = aux_table["variety"].value_counts()
        tag = counts.idxmax()
        n_dots.append({"petal.length": local_dot[1], "petal.width": local_dot[0], "variety": tag})

    return pd.DataFrame(n_dots)

if __name__ == '__main__':
    doc = uploaddoc()
    average_dots = compute_average(doc)
    paramers = get_parameters()
    new_dots = compute_distance(paramers, average_dots)
    showdoc(doc, new_dots)


