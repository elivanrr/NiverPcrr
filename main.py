# Importaçoes das bibliotecas
import pandas as pd
from twilio.rest import Client
from datetime import date

# Your Account SID from twilio.com/console
account_sid = "ACfea07098b9a3dd029f73621e0dfe78d9"
# Your Auth Token from twilio.com/console
auth_token = "0e3e1a70839f797022e77ca32c0f89bb"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em Excel
df = pd.read_excel('PCRRNIVER.xlsx')
nsc = df['DtaStr'][:]
data_hj = date.today()
data = data_hj.strftime('%d/%m/YY')
nome = df.loc[df['DtaStr'] == data, ["Nome", "DataDia"]]
# print("Segue a relação dos aniversariantes:","\n", nome)

# Eviando o sms
message = client.messages.create(
    to="+5595981048847",
    from_="+12565107940",
    body=f'Segue a relação dos aniversariantes:" {nome}')
print(message.sid)