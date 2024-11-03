import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="About Software",
                   page_icon="image1.png", layout="wide")

with open("style.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)

st.markdown("# About Software",
            unsafe_allow_html=True)

st.markdown('---')

st.write('''
The app helps optimize meta paid campaigns to the optimal levels. Since the analysis goes from campaign levels to ad groups, adsets to different versions of creatives it helps optimize the campaign across the lowest denominator that affects the campaign. 

The optmizer is built in such a way that campaign analysis of Traffic campaigns and Lead campaigns can be ascertained seperately so that one can build a strong awareness and conversion funnel.

The comparisions of performance are done with group level mean, both for awareness and lead conversions and hence the accuracy of prediction is at its highest. 

The app is built on a simple UI and needs just minimalistic operations to derive results.

Analysis of Meta campaigns have neven been so easy.. Switch on to ppc optimizer and say good bye to multiple complex excel sheet data.

 ''')

st.markdown(
    "## Required Columns for Meta Data output from Meta console")
st.markdown('---')
st.write(''' 
1. Reporting starts
2. Reporting ends
3. Campaign name
4. Ad set name
5. Ad name
6. Ad delivery
7. Attribution setting
8. Results
9. Result indicator
10. Reach
11. Frequency
12. Cost per results
13. Ad set budget
14. Ad set budget type
15. Amount spent (INR)
16. Ends
17. Quality ranking
18. Engagement rate ranking
19. Conversion rate ranking
20. Impressions
21. CPM (cost per 1,000 impressions) (INR)
22. Link clicks
23. CPC (cost per link click) (INR)
24. CTR (link click-through rate)
25. Clicks (all)
26. CTR (all)
27. CPC (all) (INR)
''')

st.write('''Apart from the above format of reporting required from meta console, other two important aspect to note are
1. sheet_name
2. header

### sheet_name is the name of the excel sheet which has the data from meta console.

### header is basically the row which the column headers as per the excel sheet which has the data from meta console.
''')

st.markdown(
    "## Custom Data Adjustments")

st.write('''
To get only those campaign that meets the custom settings of the user, the user can use the custom setting sliders to use the minimum and maximum values of the category listed. Based on the setting chosen, all data that falls within the ambit of range will be exhibited as custom database.
''')

st.write('''
All database can be exported as CSV file or taken printout or enlarged directly with the button provided above the dataframes for appropriate user actions.

###  So Try the app. Get your optimizations in razor speed and keep ahead of the world on your meta campaigns

''')
