import streamlit as st

st.title('NEXUXCAR - ALUGUEL DE CARROS')
st.sidebar.image('NEXUXCAR.png')
st.sidebar.title('NEXUXCAR - ALUGUEL DE CARROS')

carros = ['BMW', 'HB20', 'MUSTANG', 'UNO FIAT']
carro = st.sidebar.selectbox('Selecione O Modelo Do Carro Alugado:', carros)

valor_dia = 0.25

if carro:
     st.markdown(f'## O Carro Alugado Foi: {carro}')
     st.image(f'{carro}.png')

     if carro == 'BMW':
         valor_dia = 120
     elif carro == 'HB20':
           valor_dia = 80
     elif carro == 'MUSTANG':
           valor_dia = 400
     elif carro == 'UNO FIAT':
           valor_dia = 1500

dias = st.text_input("Quantos Dias?")
km = st.text_input('Quantos Kilometros Rodados?')
if dias:
     if km:
          
          dias = int(dias)
          km = float(km)
          
          valor_dias = dias * valor_dia
          valor_km = km * 0.15


          valor_total = valor_dias +valor_km

          st.warning(f"Você Andou {km}Km Por {dias} Dias, Então O Preço A Pagar É R${valor_total:.2f}")