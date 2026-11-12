import pandas as pd
from pathlib import Path 
from matrx_operations import prepare_matrix

PROJECT_PATH= Path(__file__).resolve().parent.parent
DIR_DATA=PROJECT_PATH/"data"



def load_and_combine_wine_data():
    red=pd.read_csv(DIR_DATA/"winequality-red.csv",sep=";")
    white=pd.read_csv(DIR_DATA/"winequality-white.csv",sep=";")
    print("red==>",red.shape)
    print("white==>",white.shape)

    data_win=pd.concat([red,white],ignore_index=True)
    print("win_data==>",data_win.shape)
    print(data_win.head(5))
    data_win.to_csv(DIR_DATA/"wine_quality.csv",index=False)

def load_wine_data():
    data_win=pd.read_csv(DIR_DATA/"wine_quality.csv")
    print("win_data==>",data_win.shape)
    print(data_win.head(5))
    print(data_win.isna().sum())
    print(data_win.duplicated().sum())
    print(data_win.shape)
    return data_win




if __name__ == "__main__":
    print("jjj")
    data = load_wine_data()
    x=prepare_matrix(data)
    print(x.shape)
    # load_and_combine_wine_data()