import streamlit as st
import pandas as pd
import numpy as np
import time


st.set_page_config(page_title="About Software",
                   page_icon="image1.png", layout="wide")

with open("style.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)


st.markdown("# Custom Performance Analysis Reports",
            unsafe_allow_html=True)


with st.sidebar:
    st.markdown("### :blue[Select Campaign Type]")
    campaign_select = st.radio(
        label="campaigntype", options=["### :red[Leads]", "### :blue[Traffic]"], key='campaigntype')
    st.markdown("---")

    st.markdown("### :blue[Select Custom Performance Standards]")
    slider1 = st.select_slider(label="Mean_Impression_Ratio_score - Minimum", options=[
        0.4, 0.5, 0.6, 0.75, 0.9, 1, 1.1, 1.25, 1.5, 1.75, 2, 2.25, 2.5])

    slider2 = st.select_slider(label="Mean_Impression_Ratio_score - Maximum", options=[
        0.4, 0.5, 0.6, 0.75, 0.9, 1, 1.1, 1.25, 1.5, 1.75, 2, 2.25, 2.5])

    slider3 = st.select_slider(label="Mean_ResultLink_Ratio_score - Minimum", options=[
        0.4, 0.5, 0.6, 0.75, 0.9, 1, 1.1, 1.25, 1.5, 1.75, 2, 2.25, 2.5])

    slider4 = st.select_slider(label="Mean_ResultLink_Ratio_score - Maximum", options=[
        0.4, 0.5, 0.6, 0.75, 0.9, 1, 1.1, 1.25, 1.5, 1.75, 2, 2.25, 2.5])


try:
    leads_df_custom = st.session_state.leads_df
    traffic_df_custom = st.session_state.traffic_df
    if campaign_select == "### :red[Leads]":
        summary_databse = leads_df_custom.groupby(by=['Campaign_name', 'Adset_name', 'Ad_name', 'Result_indicator'])[
            ['Impressions', 'Link_clicks', 'Results', 'Amount_spent']].sum()
        summary_databse["impression_link_ratio"] = round(
            (summary_databse.Link_clicks / summary_databse.Impressions) * 100, 2)
        summary_databse["result_link_ratio"] = round(
            (summary_databse.Results / summary_databse.Link_clicks) * 100, 2)
        summary_databse["mean_imp_link_ratio"] = round(summary_databse.groupby(
            by=['Ad_name'])[['impression_link_ratio']].transform('mean'), 2)
        summary_databse["mean_result_link_ratio"] = round(summary_databse.groupby(
            by=['Ad_name'])[['result_link_ratio']].transform('mean'), 2)
        st.dataframe(summary_databse)
        if summary_databse not in st.session_state:
            st.session_state["summary_database"] = summary_databse

        st.markdown("## :blue[Custom Lead Data Analysis]")
        st.markdown("---")
        criteria_a = np.logical_and(summary_databse.impression_link_ratio >= float(slider1) * summary_databse.mean_imp_link_ratio,
                                    summary_databse.impression_link_ratio <= float(slider2) * summary_databse.mean_imp_link_ratio)
        criteria_b = np.logical_and(summary_databse.result_link_ratio >= float(slider3) * summary_databse.mean_result_link_ratio,
                                    summary_databse.result_link_ratio <= float(slider4) * summary_databse.mean_result_link_ratio)
        performing_df = (summary_databse[criteria_a & criteria_b])
        st.dataframe(performing_df)

        if performing_df not in st.session_state:
            st.session_state["performing_df"] = performing_df
    else:
        summary_databse = traffic_df_custom.groupby(by=['Campaign_name', 'Adset_name', 'Ad_name', 'Result_indicator'])[
            ['Impressions', 'Link_clicks', 'Results', 'Amount_spent']].sum()
        summary_databse["impression_link_ratio"] = round(
            (summary_databse.Link_clicks / summary_databse.Impressions) * 100, 2)
        summary_databse["result_link_ratio"] = round(
            (summary_databse.Results / summary_databse.Link_clicks) * 100, 2)
        summary_databse["mean_imp_link_ratio"] = round(summary_databse.groupby(
            by=['Ad_name'])[['impression_link_ratio']].transform('mean'), 2)
        summary_databse["mean_result_link_ratio"] = round(summary_databse.groupby(
            by=['Ad_name'])[['result_link_ratio']].transform('mean'), 2)
        st.dataframe(summary_databse)
        if summary_databse not in st.session_state:
            st.session_state["summary_database"] = summary_databse

        st.markdown("## :blue[Custom Traffic Data Analysis]")
        st.markdown("---")
        criteria_a = np.logical_and(summary_databse.impression_link_ratio >= float(slider1) * summary_databse.mean_imp_link_ratio,
                                    summary_databse.impression_link_ratio <= float(slider2) * summary_databse.mean_imp_link_ratio)
        criteria_b = np.logical_and(summary_databse.result_link_ratio >= float(slider3) * summary_databse.mean_result_link_ratio,
                                    summary_databse.result_link_ratio <= float(slider4) * summary_databse.mean_result_link_ratio)
        performing_df = (summary_databse[criteria_a & criteria_b])
        st.dataframe(performing_df)

        if performing_df not in st.session_state:
            st.session_state["performing_df"] = performing_df
except:
    if AttributeError:
        st.warning("The file is not loaded. No Database found")
    elif ValueError:
        st.warning("Use Right Values of selection")
    else:
        pass
