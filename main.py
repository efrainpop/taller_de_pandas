import pandas as pd

data_1 = [1, 2, 3, 4, 5]
etiquetas = ['a', 'b', 'c', 'd', 'e']

serie = pd.Series(data_1, index=etiquetas)
print(serie)

datos = {'Nombre':['Alice', 'Bob', 'Charlie'],
         'Edad': [25, 30, 35],
         'Ciudad': ['A', 'B', 'C']}
df = pd.DataFrame(datos, index=['a', 'b', 'c'])
print(df)
#Seleccionar datos con loc[]
seleccion_loc = df.loc['b', 'Edad']
print(seleccion_loc) #Resultado 30

#Seleccionar datos con iloc[]
seleccion_iloc = df.iloc[1, 1]
print(seleccion_iloc) #Resultado 30

#Selccionar datos con at[]
seleccion_at = df.at['b', 'Edad']
print(seleccion_at) #Resultado 30

#Seleccionar datos con iat[]
seleccion_iat = df.iat[1, 1]
print(seleccion_iat) #Resultado 30

data = {'state':['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year':[2000, 2001, 2002, 2001, 2002, 2003],
        'pop':[1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)

frame_reordenado = pd.DataFrame(data, columns=['year', 'state', 'pop'])
print(frame_reordenado)

frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four', 'five', 'six'])
print(frame2)
print(frame2.columns)
print(frame2['state'])
print(frame2.year)