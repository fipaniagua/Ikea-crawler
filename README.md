# Ikea-crawler

Web Scrapper to get all categories of Ikea catalog from https://www.ikea.com/es/es/cat/productos-products/ and get all products from the same catalog.
Then write a .xlsx file with all the products information.

## Set Up

1. Install [Python](https://phoenixnap.com/kb/how-to-install-python-3-windows)
2. Install [PIP](https://phoenixnap.com/kb/install-pip-windows)
3. Install requirments. \
   `pip install requirementes -r requirementes.txt`
4. download ChromeDriver from https://chromedriver.storage.googleapis.com/index.html?path=88.0.4324.96/   
5. move ChromeDriver from downloads folder to the program folder

## Usage

1. Run categories program to get all the categories in a .xlsx file. \
   `python categories.py`

2. Run main.py to get all  product from the categories.xlsx file. \
  `python main.py`
