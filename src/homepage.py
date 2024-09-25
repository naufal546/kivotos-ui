import streamlit as st

with st.container():
    st.markdown('''
    <h1 style="text-align: center;">&nbsp&nbsp&nbspWelcome to Kivotos</h1>
    ''', unsafe_allow_html=True)

    st.write("")

    homeImage = "https://static.miraheze.org/bluearchivewiki/b/b4/Arisu_%28Maid%29.png"

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(homeImage)

    st.write("")

    st.markdown('''
    <h2 style="text-align: center;">&nbsp&nbsp&nbspThis is Our Happy Memories, Sensei!</h2>
    ''', unsafe_allow_html=True)
