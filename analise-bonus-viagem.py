import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""
client = Client(account_sid, auth_token)



lista_meses = ['janeiro','fevereiro', 'março', 'março', 'abril', 'maio','junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mes {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="",
            from_="",
            body=f'No mes {mes} alguem bateu a meta. Vendedor:{vendedor}, Vendas: {vendas}')
        print(message.sid)





# verificar se algum valor na coluluna vendas daquele arquivo é maior que 55.000


# se for maior que 55.000 -> enviar um sms com o nome, mes e as vendas do vendedor


# caso não seja maior que 55.000 não quero fazer nada
