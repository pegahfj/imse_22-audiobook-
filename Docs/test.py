import pandas as pd
import csv, json
from pandas import json_normalize



# data = pd.read_csv(r'C:\Users\Ron\Desktop\products_sold.csv')   

if __name__ == "__main__":
    dic = {}
    with open(r'books.csv', 'r') as csvf:
        dic = csv.DictReader(csvf)
    # books = pd.json_normalize(dic)
    # books = pd.read_csv(r'books.csv', sep=";")
    
    # authors = pd.DataFrame(books, columns=['Author', 'Country'])
    # authors.to_csv(r'authors.csv', index=False, sep=";")
    
    json_file_path = "bestbooks.json"
    with open(json_file_path, 'w') as j:   
        j.write(json.dumps(books, indent=4))
        
    # with open(json_file_path, 'r') as j:   
    #     book_dict = json.loads(j.read())


    # df2 = json_normalize(dict['technologies']) 
    # df2 = pd.read_json(jsonStr, orient ='index')
    # bookjson = pd.DataFrame.from_dict(book_dict, orient="index")
