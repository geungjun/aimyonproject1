import streamlit as st
import pandas as pd

st.title('야르 처음 만드는 스트림릿')
st.write('안녕 반가워')
st.write('야르야르')
data = pd.DataFrame({
    '숫자': [1, 2, 3, 4],
    '제곱': [1, 4, 9, 16]
})
