import json
from requests import Session
from decouple import (
    AutoConfig
)
from requests.exceptions import (
    ConnectionError,
    Timeout,
    TooManyRedirects
)


class CoinMarketCap():
    """
    Acessar a API do CoinMarketCap.
    """
    def __init__(self, env_path=r"../core/.env", env_variable="SECRET_KEY"):
        config = AutoConfig(env_path)
        self.SECRET_KEY = config(env_variable)

    def crypto_quote(self, limit="100", convert="USD"):
        """
        Retorna o simbolo é o valor da criptocoin.
        """

        url = """
        https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"""

        parameters = {
            "start": "1",
            "limit": limit,
            "convert": convert
        }

        headers = {
            "Accepts": "application/json",
            "X-CMC_PRO_API_KEY": self.SECRET_KEY
        }

        session = Session()
        session.headers.update(headers)
        try:
            response = session.get(url, params=parameters)
            data_full = json.loads(response.text)["data"]
            dicionario_de_criptos = {}

            for data in data_full:
                simbolo_da_criptomoeda = data["symbol"]
                preco_da_criptomoeda = data["quote"]["USD"]["price"]

                dicionario_de_criptos[simbolo_da_criptomoeda] = (
                    preco_da_criptomoeda
                )

            print(dicionario_de_criptos)
            return dicionario_de_criptos

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)


if __name__ == "__main__":
    CoinMarketCap().crypto_quote()
