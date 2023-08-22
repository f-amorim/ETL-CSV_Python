#! usr/bin/env python3

import pandas as pd

df = pd.read_csv("ID.csv")

Dados = {
        "Nome":["Diana", "Cassandra", "leona", "Catarina"],
        "Saldo":[2100.98, 1000.80, 3000.00, 1200.50]  
          }


df_02 = pd.DataFrame(Dados)



df_final = pd.concat([df, df_02],axis=1)


df_final.to_csv('ID.csv', index= False)
print(df_final)