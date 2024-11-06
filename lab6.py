import pandas as pd

datos = pd.read_csv('sales_data.csv', encoding='latin1')
datos = datos[datos.STATE.notnull()]
datos.to_xml('output/result.xml')
