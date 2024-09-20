from flask import Flask
import requests
from bs4 import BeautifulSoup



def get_table_values():
    


    response = requests.get("https://www.bankier.pl/waluty/kursy-walut/nbp")

    document = BeautifulSoup(response.text, "html.parser")

    boxes = document.find(id="boxCurrency")

    tables = boxes.find(class_="boxContent boxTable")

    table = tables.find(class_="sortTableMixedData floatingHeaderTable")

    values = table.find_all("tr")
    vals = ""

    for i in values:
        if i.get("class"):
            continue
        vals+=str(i)

    

    return vals


app = Flask(__name__)


@app.route("/one_currency_table")
def currency():
    return f"<table>{get_table_values()}</table"




if __name__ == "__main__":
    app.run(host="0.0.0.0")




