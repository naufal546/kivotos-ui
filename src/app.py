import streamlit as st

homepage = st.Page("./homepage.py", title="Home", default=True)

about = st.Page("./about.py", title="About dev")

abydos = st.Page("./abydos.py", title="Abydos High School")

gehenna = st.Page("./gehenna.py", title="Gehenna Academy")

pg = st.navigation({
    "Homepage": [homepage, about],
    "School": [abydos, gehenna]
})

pg.run()
