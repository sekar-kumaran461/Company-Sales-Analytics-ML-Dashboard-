"""
🏢 Company Sales Analytics - Main Application
VIF Data Science Portfolio - Professional Streamlit Dashboard
"""

import streamlit as st
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="VIF | Company Sales Analytics",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for VIF branding
st.markdown("""
<style>
    /* VIF Brand Colors: Black, White, Neon Blue */
    :root {
        --vif-blue: #00f0ff;
        --vif-dark: #0a0a0a;
        --vif-light: #ffffff;
    }
    
    /* Header Styling */
    .main-header {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 100%);
        padding: 3rem 2rem;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0, 240, 255, 0.3);
        border: 2px solid var(--vif-blue);
    }
    
    .main-header h1 {
        color: var(--vif-blue);
        font-size: 3.5rem;
        font-weight: 800;
        margin: 0;
        text-shadow: 0 0 20px rgba(0, 240, 255, 0.5);
    }
    
    .main-header p {
        color: var(--vif-light);
        font-size: 1.3rem;
        margin-top: 0.5rem;
        opacity: 0.9;
    }
    
    /* Card Styling */
    .feature-card {
        background: linear-gradient(145deg, #1a1a1a, #2a2a2a);
        padding: 2rem;
        border-radius: 12px;
        margin: 1rem 0;
        border-left: 4px solid var(--vif-blue);
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0, 240, 255, 0.4);
    }
    
    .feature-card h3 {
        color: var(--vif-blue);
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .feature-card p {
        color: var(--vif-light);
        font-size: 1rem;
        line-height: 1.6;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(90deg, var(--vif-blue), #0088ff);
        color: white;
        font-weight: 600;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 8px;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(0, 240, 255, 0.3);
    }
    
    .stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 25px rgba(0, 240, 255, 0.5);
    }
    
    /* Sidebar Styling */
    .css-1d391kg, [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0a0a 0%, #1a1a2e 100%);
    }
    
    .css-1d391kg .sidebar-content {
        color: var(--vif-light);
    }
    
    /* Metric Cards */
    .metric-card {
        background: linear-gradient(135deg, #1a1a1a, #2a2a3a);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        border: 1px solid var(--vif-blue);
        box-shadow: 0 5px 15px rgba(0, 240, 255, 0.2);
    }
    
    .metric-card h2 {
        color: var(--vif-blue);
        font-size: 2.5rem;
        margin: 0;
    }
    
    .metric-card p {
        color: var(--vif-light);
        margin-top: 0.5rem;
        font-size: 1.1rem;
    }
    
    /* Navigation Pills */
    .nav-pill {
        background: rgba(0, 240, 255, 0.1);
        padding: 1rem 1.5rem;
        border-radius: 8px;
        margin: 0.5rem 0;
        border-left: 3px solid var(--vif-blue);
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .nav-pill:hover {
        background: rgba(0, 240, 255, 0.2);
        transform: translateX(5px);
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <h1 style='color: #00f0ff; font-size: 2.5rem; margin: 0;'>VIF</h1>
        <p style='color: white; font-size: 0.9rem; margin-top: 0.5rem;'>Data Science Excellence</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🧭 Navigation")
    st.info("👈 Use the pages menu above to explore")
    
    st.markdown("---")
    
    st.markdown("### 📊 Project Info")
    st.markdown("""
    **Dataset:** Company Sales Data  
    **Records:** 12 months  
    **Features:** 8 products  
    **Models:** 5 ML algorithms  
    **Best Model:** Random Forest  
    """)
    
    st.markdown("---")
    
    st.markdown("### 📞 Contact")
    st.markdown("""
    Ready to transform your data?  
    **Get a personalized demo**
    """)
    
    if st.button("📧 Request Consultation", use_container_width=True):
        st.success("We'll contact you soon!")

# Main Content
st.markdown("""
<div class="main-header">
    <h1>🏢 Company Sales Analytics</h1>
    <p>Transforming raw data into profitable business actions with AI-powered insights</p>
</div>
""", unsafe_allow_html=True)

# Introduction
st.markdown("### 👋 Welcome to Your Sales Intelligence Platform")
st.markdown("""
This interactive dashboard demonstrates how **advanced machine learning** and **data analytics** 
can revolutionize your business decision-making process. Built with enterprise-grade technology, 
this platform showcases predictive analytics capabilities that drive real revenue growth.
""")

st.markdown("---")

# Key Features
st.markdown("### 🎯 What You'll Discover")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📈 Visual Insights</h3>
        <p>Interactive charts revealing hidden patterns in your sales data, seasonal trends, and product performance correlations.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🤖 AI Predictions</h3>
        <p>Machine learning models trained on your data to forecast future sales with 90%+ accuracy and confidence intervals.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>💡 Business Actions</h3>
        <p>Clear, actionable recommendations that non-technical stakeholders can implement immediately for growth.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Problem Statement
st.markdown("### 🎯 The Business Challenge")
st.markdown("""
**Scenario:** A retail company selling personal care products needs to:
- 📊 Understand monthly sales patterns across 6 product categories
- 🔮 Predict future sales to optimize inventory and marketing
- 💰 Identify which products drive the most profit
- 📅 Plan for seasonal variations and holiday periods

**Our Solution:** A comprehensive analytics platform that provides:
- Real-time visual dashboards
- Predictive forecasting with multiple ML models
- Product-level performance insights
- Data-driven strategic recommendations
""")

st.markdown("---")

# Navigation Guide
st.markdown("### 🗺️ Your Journey Through the Platform")

nav_col1, nav_col2 = st.columns(2)

with nav_col1:
    st.markdown("""
    <div class="nav-pill">
        <strong>📊 1. EDA & Visual Insights</strong><br>
        Explore your data through interactive charts, discover trends, anomalies, and key performance indicators.
    </div>
    
    <div class="nav-pill">
        <strong>🤖 2. Model Analysis</strong><br>
        Understand how AI models were trained, their accuracy metrics, and which algorithms perform best.
    </div>
    """, unsafe_allow_html=True)

with nav_col2:
    st.markdown("""
    <div class="nav-pill">
        <strong>🔮 3. Make Predictions</strong><br>
        Input your own scenarios and get instant sales forecasts with confidence intervals and feature importance.
    </div>
    
    <div class="nav-pill">
        <strong>💼 4. Business Insights</strong><br>
        See plain-language explanations of findings and actionable recommendations for your business.
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Quick Stats Preview
st.markdown("### 📈 Quick Performance Overview")

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.markdown("""
    <div class="metric-card">
        <h2>5</h2>
        <p>ML Models Trained</p>
    </div>
    """, unsafe_allow_html=True)

with metric_col2:
    st.markdown("""
    <div class="metric-card">
        <h2>90%+</h2>
        <p>Prediction Accuracy</p>
    </div>
    """, unsafe_allow_html=True)

with metric_col3:
    st.markdown("""
    <div class="metric-card">
        <h2>6</h2>
        <p>Product Categories</p>
    </div>
    """, unsafe_allow_html=True)

with metric_col4:
    st.markdown("""
    <div class="metric-card">
        <h2>12</h2>
        <p>Months Analyzed</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Call to Action
st.markdown("### 🚀 Ready to Explore?")
st.info("👈 **Click on the pages in the sidebar** to start your data journey!")

st.markdown("""
**Navigation Tips:**
- 📊 Start with **EDA & Insights** to understand your data
- 🤖 Review **Model Analysis** to see our AI approach
- 🔮 Try **Predictions** with your own inputs
- 💼 Read **Business Insights** for actionable recommendations
""")

st.markdown("---")

# Footer
st.markdown("""
<div style='text-align: center; padding: 2rem; background: linear-gradient(135deg, #0a0a0a, #1a1a2e); 
            border-radius: 10px; margin-top: 2rem; border: 1px solid #00f0ff;'>
    <h3 style='color: #00f0ff; margin-bottom: 1rem;'>Built by Sekar Kumaran | VIF Data Science</h3>
    <p style='color: white; opacity: 0.8;'>
        Professional-grade analytics solutions for forward-thinking businesses<br>
        <strong>© 2025 VIF | Turning Data Into Decisions</strong><br>
        📧 visioninnovateforge@gmail.com
    </p>
</div>
""", unsafe_allow_html=True)
