import streamlit as st
from io import BytesIO
import requests
from streamlit_option_menu import option_menu
from PIL import Image, ImageOps


col1, col2, col3 = st.columns([1, 2, 1])
with col2:
  st.image("https://static.miraheze.org/bluearchivewiki/d/d1/Miyu_%28Swimsuit%29.png", use_column_width=True)