import streamlit as st
import pandas as pd
import numpy as np
import time
import re

st.set_page_config(page_title="PPC Optimizer",
                   page_icon="image.png", layout="wide")


with open("style.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)


st.markdown("# Performance Marketing Analysis Tool",
            unsafe_allow_html=True)

st.markdown('---')
st.markdown('''
<style>
.big-font {
    font-size:20px !important;
}
</style>

<span class="big-font">Fully automated performance marketing analysis tool with complete Python pandas library at the back end.</span>
''', unsafe_allow_html=True)
st.markdown('---')


def file_upload_status():
    st.success("File successfully uploaded")


file_uploaded = st.file_uploader(label="Upload only Excel file",
                                 type=[".xlsx"],
                                 key="uploadexcel", on_change=file_upload_status)

sheet_name = st.text_input("Select Sheet Name", key="sheetname",
                           type="default", placeholder="Fill Sheet Name")
st.markdown('---')

# User Defined function - 1


def database_cleanup_addfeatures(df):
    camp_name_extract = df.iloc[0:(
        len(df) + 1), 0]
    camp_name_extract = camp_name_extract.to_frame()
    camp_name_extract["campaign_type"] = camp_name_extract.Campaign_name.str.contains(
        'Lead|Leads', flags=re.IGNORECASE, regex=True)
    camp_name_extract.replace(to_replace=[True, False], value=[
        "Leads", "Traffic"], inplace=True)
    df["Campaign_type"] = camp_name_extract.campaign_type
    # Adding Progress of work
    progress_text = "Database Optimizations Update, Deletion and Updation of Requisite Columns And Additions Of Required Features...."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    return df


try:
    if file_uploaded and sheet_name:
        meta_data_firstcut = pd.read_excel(io=file_uploaded, sheet_name=sheet_name, header=0,
                                           names=['Reporting_starts', 'Reporting_ends', 'Campaign_name', 'Adset_name',
                                                  'Ad_name', 'Ad_delivery', 'Attribution_setting', 'Results',
                                                  'Result_indicator', 'Reach', 'Frequency', 'Cost_per_results',
                                                  'Adset_budget', 'Adset_budget_type', 'Amount_spent', 'Ends',
                                                  'Quality_ranking', 'Engagement_rate_ranking', 'Conversion_rate_ranking',
                                                  'Impressions', 'CPM', 'Link_clicks', 'CPC', 'CTR',
                                                  'Clicks', 'CTR_all', 'CPC_all'])
    else:
        st.warning("File not uploaded or sheet name not filled...Check")

    drop_col_list = ['Reporting_starts', 'Reporting_ends', 'Ad_delivery', 'Attribution_setting', 'Reach', 'Cost_per_results', 'Adset_budget',
                     'Adset_budget_type', 'Ends', 'Quality_ranking', 'Engagement_rate_ranking', 'Conversion_rate_ranking', 'CTR', 'CTR_all', 'CPC_all']

    meta_data_afterdrop = meta_data_firstcut.drop(columns=drop_col_list)

    if meta_data_afterdrop not in st.session_state:
        st.session_state["meta_data_afterdrop"] = meta_data_afterdrop
    cleaned_database = database_cleanup_addfeatures(meta_data_afterdrop)
    if cleaned_database not in st.session_state:
        st.session_state["cleaned_database"] = cleaned_database
except NameError:
    pass
