import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="About Software",
                   page_icon="image1.png", layout="wide")

with open("style.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)


st.markdown("# Campaign Type Database Reports",
            unsafe_allow_html=True)


with st.sidebar:
    st.markdown("### :blue[Select Campaign Type]")
    campaign_select = st.radio(
        label="campaigntype", options=["### :red[Leads]", "### :blue[Traffic]"], key='campaigntype')

try:
    master_df = st.session_state.cleaned_database
    if campaign_select == "### :red[Leads]":
        condition = master_df.Campaign_type == "Leads"
        leads_db = master_df.loc[condition]
        leads_df = leads_db
        st.markdown("## :red[Leads Database]")
        st.dataframe(leads_df)
        st.markdown("## Key Summary Report")
        st.markdown("---")
        st.write(round(leads_df.describe(), 2))
        conversion_sum = round(leads_df.Results.sum())
        spend_sum = round(leads_df.Amount_spent.sum())
        impressions_sum = round(leads_df.Impressions.sum())
        linkclicks_sum = round(leads_df.Link_clicks.sum())
        st.markdown("## Key Indicators")
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.text_input(label="Conversions", value="Total Conversions")
            st.text_input(label="Spends", value="Total Spends")
            st.text_input(label="Impressions", value="Total Impressions")
            st.text_input(label="Link Clicks", value="Total Link_Clicks")

        with col2:
            st.text_input(label="Total Conversions", value=conversion_sum)
            st.text_input(label="Total Spends", value=spend_sum)
            st.text_input(label="Total Impressions", value=impressions_sum)
            st.text_input(label="Total Link Clicks", value=linkclicks_sum)

        if leads_df not in st.session_state:
            st.session_state["leads_df"] = leads_df

    else:
        condition = master_df.Campaign_type == "Traffic"
        traffic_db = master_df.loc[condition]
        traffic_df = traffic_db
        st.markdown("## :blue[Traffic Database]")
        st.dataframe(traffic_df)
        st.markdown("## Key Summary Report")
        st.markdown("---")
        st.write(round(traffic_df.describe(), 2))
        conversion_sum = round(traffic_df.Results.sum())
        spend_sum = round(traffic_df.Amount_spent.sum())
        impressions_sum = round(traffic_df.Impressions.sum())
        linkclicks_sum = round(traffic_df.Link_clicks.sum())
        st.markdown("## Key Indicators")
        st.markdown("---")
        col1, col2 = st.columns(2)
        with col1:
            st.text_input(label="Conversions", value="Total Conversions")
            st.text_input(label="Spends", value="Total Spends")
            st.text_input(label="Impressions", value="Total Impressions")
            st.text_input(label="Link_Clicks", value="Total Link_Clicks")

        with col2:
            st.text_input(label="Total Conversions", value=conversion_sum)
            st.text_input(label="Total Spends", value=spend_sum)
            st.text_input(label="Total Impressions", value=impressions_sum)
            st.text_input(label="Total LinkClicks", value=linkclicks_sum)

        if traffic_df not in st.session_state:
            st.session_state["traffic_df"] = traffic_df
except:
    if AttributeError:
        st.warning("The file is not loaded. No Database found")
    elif ValueError:
        st.warning("Use Right Values of selection")
    else:
        pass
