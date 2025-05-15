import streamlit as st
import random

st.title("数当てゲーム")

if "answer" not in st.session_state:
    st.session_state.answer = random.randint(0, 100)

guess = st.number_input("0〜100の中で予想してね", min_value=0, max_value=100, step=1)

if st.button("判定！"):
    if guess < st.session_state.answer:
        st.write("もっと大きい数字です！")
    elif guess > st.session_state.answer:
        st.write("もっと小さい数字です！")
    else:
        st.write("正解です！🎉")
        st.session_state.answer = random.randint(0, 100)
