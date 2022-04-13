from requests import get


def currency_rates(incurrency):
    """
        get the rate of currency by code from www.cbr.ru for RUB
        :param currency:
        :return: rate
        """

    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    contents = response.content.decode(encoding=response.encoding)
    currency = {}
    for el in contents.split('<CharCode>')[1:]:
        charcode = el[:3]
        nominal = (el.split('<Nominal>')[1].split('</Nominal>')[0])
        value = (el.split('<Value>')[1].split('</Value>')[0])
        currency.setdefault(charcode, [nominal, value])
    rate = currency.get(incurrency.upper())
    if rate is None:
        print('Указанная валюта отсутствует')
    else:
        print(f'Курс RUB за {rate[0]} {incurrency.upper()}: {rate[1]}')


currency_rates(input("Ведите код валюты (ХХХ): "))
