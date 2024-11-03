import streamlit as st
import pandas as pd
import numpy as np
import time


st.set_page_config(page_title="About Software",
                   page_icon="image1.png", layout="wide")

with open("style.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)


st.markdown("# Custom Data Segments - Filtered Data Analysis",
            unsafe_allow_html=True)


def index_name_unique(df, indexlevel):
    unique_list = (df.index.get_level_values(
        int(indexlevel))).drop_duplicates()
    return unique_list


def ad_set_selection(df, selections, indexvalue):
    selected_db = df.loc[(slice(str(selections))), :]
    ad_set_list = index_name_unique(selected_db, indexlevel=indexvalue)
    return ad_set_list


try:
    summary_df = st.session_state.summary_database
    performing_df = st.session_state.performing_df
    campaign_name_unique = index_name_unique(df=summary_df, indexlevel=0)

    s1 = st.selectbox(label="Campaign_name",
                      options=campaign_name_unique, key="c_name")
    selections_output = s1
    if selections_output not in st.session_state:
        st.session_state["selections_output"] = selections_output
    ad_set_list = ad_set_selection(
        summary_df, selections=selections_output, indexvalue=1)
    s2 = st.selectbox(label="Adset_name",
                      options=ad_set_list, key="ad_name")
    selections_output_2 = s2
    if selections_output_2 not in st.session_state:
        st.session_state["selections_output_2"] = selections_output_2
    chart_df = summary_df.loc[(s1, s2), :]
    chart_df.reset_index(inplace=True)
    if chart_df not in st.session_state:
        st.session_state["chart_df"] = chart_df
    st.dataframe(chart_df)

except:
    if AttributeError:
        st.warning("The file is not loaded. No Database found")
    elif ValueError:
        st.warning("Use Right Values of selection")
    else:
        pass
