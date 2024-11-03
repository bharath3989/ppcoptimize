import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="About Software",
                   page_icon="image1.png", layout="wide")

with open("style.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)


st.markdown("# Master Database",
            unsafe_allow_html=True)


try:
    master_df = st.session_state.cleaned_database
    st.dataframe(master_df)
    st.markdown("## Key Summary Report of the Master Data")
    st.markdown("---")
    st.write(round(master_df.describe(), 2))
    conversion_sum = round(master_df.Results.sum())
    spend_sum = round(master_df.Amount_spent.sum())
    impressions_sum = round(master_df.Impressions.sum())
    linkclicks_sum = round(master_df.Link_clicks.sum())
    st.markdown("## Key Indicators")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.text_input(label="Conversion", value="Total Conversions")
        st.text_input(label="Spends", value="Total Spends")
        st.text_input(label="Impressions", value="Total Impressions")
        st.text_input(label="Link Clicks", value="Total Link_Clicks")

    with col2:
        st.text_input(label="Total Conversions", value=conversion_sum)
        st.text_input(label="Total Spends", value=spend_sum)
        st.text_input(label="Total Impression", value=impressions_sum)
        st.text_input(label="Total Link Clicks", value=linkclicks_sum)

except AttributeError:
    st.warning("The file is not loaded. No Database found")
