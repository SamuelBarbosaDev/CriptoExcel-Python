import openpyxl
from cripto import CoinMarketCap


class PlanilhaCripto():
    """
    Planilha atualizada com simbolo é preço.
    """
    def __init__(self):
        self.workbook = openpyxl.Workbook()
        self.worksheet = self.workbook.active

    def criando_planilha(self):
        """
        Criar a planilha cripto.
        """
        cripto_simbolo_e_preco = CoinMarketCap().crypto_quote()

        self.worksheet["A1"] = "Simbolo"
        self.worksheet["B1"] = "Valor"

        for linha, simbolo in enumerate(cripto_simbolo_e_preco, start=2):

            self.worksheet[f"A{linha}"] = simbolo
            self.worksheet[f"B{linha}"] = cripto_simbolo_e_preco[simbolo]

        estilo_da_tabela = openpyxl.worksheet.table.TableStyleInfo(
            name="TableStyleMedium2",
            showRowStripes=True
        )

        tabela_cripto = openpyxl.worksheet.table.Table(
            ref="A1:B101",
            displayName="Criptos",
            tableStyleInfo=estilo_da_tabela
        )

        self.worksheet.add_table(tabela_cripto)

        self.workbook.save("planilha_cripto.xlsx")


if __name__ == "__main__":
    PlanilhaCripto().criando_planilha()
