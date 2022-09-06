



#Como? criar uma planilha cripto com python.

import openpyxl
from cripto import cotacao

workbook = openpyxl.Workbook()
worksheet = workbook.active

dicinario_cripto_cotacao = cotacao()

linha = 1

worksheet["A1"] ="Simbolo"
worksheet["B1"] = "Valor"

for simbolo in dicinario_cripto_cotacao:
    linha += 1 

    worksheet[f"A{linha}"] = simbolo
    worksheet[f"B{linha}"] = dicinario_cripto_cotacao[simbolo]

estilo_da_tabela = openpyxl.worksheet.table.TableStyleInfo(name = "TableStyleMedium2",
                                            showRowStripes = True)

tabela_cripto = openpyxl.worksheet.table.Table(ref="A1:B101",
                                                displayName = "Criptos",
                                                tableStyleInfo = estilo_da_tabela)

worksheet.add_table(tabela_cripto)

workbook.save("planilha_cripto.xlsx")
    