import streamlit as st


def footer_home():
    logo_url = "Black and White Simple Minimalist Modern Line Beauty Salon Logo"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> AIMLnext </p>  
        
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "Black and White Simple Minimalist Modern Line Beauty Salon Logo"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;"> Created by deepak</p>  
       
        </div>
                
                """, unsafe_allow_html=True)
