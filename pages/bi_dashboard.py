import streamlit as st

import streamlit as st

def bi_dashboard_page():
    st.subheader("BI- Dashboard")
    st.write("Insights on Cab Fare Trends.")

    # 
    
    power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiZTU2MjUzOWMtYWFjNC00OGFkLTljMjctNjdkMTAzMGI0Y2VjIiwidCI6IjNjYjkxMTI3LTkyNDMtNGQ1Yy04NWJiLTM2Zjc4YTIwMDA2MiJ9"

    # Embed Power BI report using iframe
    st.components.v1.iframe(power_bi_url, width=900, height=600)

if __name__ == "__main__":
    bi_dashboard_page()
