import streamlit as st
import pandas as pd

#제목 쓰는 것
st.title('야르 처음 만드는 스트림릿')
#내용 쓰는 것
st.write('안녕 반가워')
st.write('야르야르')

#표
data = pd.DataFrame({
    '숫자': [1, 2, 3, 4],
    '제곱': [1, 4, 9, 16]
})
st.dataframe(data)

#입력받기
n=st.text_input('이름이나 써보거라')
if n==True:
    st.write(f'반갑구나 {n}님.')
