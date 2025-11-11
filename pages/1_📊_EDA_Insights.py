"""
📊 EDA & Visual Insights Page
Company Sales Data - Interactive Exploration
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Page config
st.set_page_config(page_title="EDA & Insights", page_icon="📊", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .insight-box {
        background: linear-gradient(135deg, #1a1a1a, #2a2a3a);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #00f0ff;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0, 240, 255, 0.2);
    }
    
    .insight-box h3 {
        color: #00f0ff;
        margin-bottom: 0.5rem;
    }
    
    .insight-box p {
        color: white;
        line-height: 1.6;
    }
    
    .kpi-card {
        background: linear-gradient(135deg, #0a0a0a, #1a1a2e);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #00f0ff;
        box-shadow: 0 5px 20px rgba(0, 240, 255, 0.3);
    }
    
    .kpi-value {
        font-size: 2.5rem;
        font-weight: bold;
        color: #00f0ff;
        margin: 0.5rem 0;
    }
    
    .kpi-label {
        color: white;
        font-size: 1rem;
        opacity: 0.9;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style='background: linear-gradient(135deg, #0a0a0a, #1a1a2e); padding: 2rem; border-radius: 10px; 
            margin-bottom: 2rem; border: 2px solid #00f0ff;'>
    <h1 style='color: #00f0ff; margin: 0;'>📊 Exploratory Data Analysis</h1>
    <p style='color: white; margin-top: 0.5rem; font-size: 1.2rem;'>
        Discover patterns, trends, and insights hidden in your sales data
    </p>
</div>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('company_sales_data.csv')
    
    # Add calculated columns
    df['profit_per_unit'] = df['total_profit'] / df['total_units']
    df['month'] = df['month_number']
    
    # Add season
    seasons = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring',
               6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Fall', 10: 'Fall',
               11: 'Fall', 12: 'Winter'}
    df['season'] = df['month_number'].map(seasons)
    
    # Add quarter
    df['quarter'] = ((df['month_number'] - 1) // 3) + 1
    df['quarter'] = 'Q' + df['quarter'].astype(str)
    
    return df

try:
    df = load_data()
    
    # KPI Section
    st.markdown("### 🎯 Key Performance Indicators")
    
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
    
    with kpi_col1:
        avg_units = df['total_units'].mean()
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Average Monthly Units</div>
            <div class="kpi-value">{avg_units:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with kpi_col2:
        avg_profit = df['total_profit'].mean()
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Average Monthly Profit</div>
            <div class="kpi-value">${avg_profit:,.0f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with kpi_col3:
        top_product = df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].mean().idxmax()
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Top Selling Product</div>
            <div class="kpi-value">{top_product.title()}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with kpi_col4:
        profit_efficiency = df['profit_per_unit'].mean()
        st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-label">Profit Per Unit</div>
            <div class="kpi-value">${profit_efficiency:.2f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Interactive Filters
    st.markdown("### 🎛️ Interactive Filters")
    
    filter_col1, filter_col2 = st.columns(2)
    
    with filter_col1:
        selected_products = st.multiselect(
            "Select Products to Analyze",
            ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer'],
            default=['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
        )
    
    with filter_col2:
        selected_season = st.selectbox(
            "Filter by Season",
            ['All'] + list(df['season'].unique())
        )
    
    # Filter data
    filtered_df = df.copy()
    if selected_season != 'All':
        filtered_df = filtered_df[filtered_df['season'] == selected_season]
    
    st.markdown("---")
    
    # Visualizations
    st.markdown("### 📈 Sales Trends & Patterns")
    
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Overall Trends", "🔄 Product Comparison", "📅 Seasonal Analysis", "🔗 Correlations"])
    
    with tab1:
        st.markdown("#### Total Sales & Profit Over Time")
        
        fig = make_subplots(
            rows=2, cols=1,
            subplot_titles=('Monthly Sales Volume', 'Monthly Profit'),
            vertical_spacing=0.15
        )
        
        fig.add_trace(
            go.Scatter(x=filtered_df['month_number'], y=filtered_df['total_units'],
                      mode='lines+markers', name='Total Units',
                      line=dict(color='#00f0ff', width=3),
                      marker=dict(size=10)),
            row=1, col=1
        )
        
        fig.add_trace(
            go.Scatter(x=filtered_df['month_number'], y=filtered_df['total_profit'],
                      mode='lines+markers', name='Total Profit',
                      line=dict(color='#00ff88', width=3),
                      marker=dict(size=10)),
            row=2, col=1
        )
        
        fig.update_xaxes(title_text="Month", row=2, col=1)
        fig.update_yaxes(title_text="Units Sold", row=1, col=1)
        fig.update_yaxes(title_text="Profit ($)", row=2, col=1)
        
        fig.update_layout(
            height=600,
            showlegend=True,
            template='plotly_dark',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
            <h3>💡 Key Insight</h3>
            <p>
                Sales show a <strong>cyclical pattern</strong> with peaks during certain months.
                The profit margin remains consistent at approximately <strong>$10 per unit</strong>,
                indicating stable pricing strategy across all products.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab2:
        st.markdown("#### Product Performance Comparison")
        
        # Product sales breakdown
        product_cols = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
        product_means = filtered_df[product_cols].mean().sort_values(ascending=True)
        
        fig = go.Figure(go.Bar(
            x=product_means.values,
            y=[p.replace('_', ' ').title() for p in product_means.index],
            orientation='h',
            marker=dict(
                color=product_means.values,
                colorscale='Viridis',
                showscale=True,
                colorbar=dict(title="Units")
            ),
            text=product_means.values.round(0),
            textposition='auto',
        ))
        
        fig.update_layout(
            title="Average Monthly Sales by Product",
            xaxis_title="Average Units Sold",
            yaxis_title="Product",
            template='plotly_dark',
            height=400,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Product trends over time
        st.markdown("#### Product Sales Trends Over Time")
        
        fig = go.Figure()
        colors = ['#00f0ff', '#00ff88', '#ff00ff', '#ffaa00', '#ff0088', '#00ffff']
        
        for i, product in enumerate(selected_products):
            fig.add_trace(go.Scatter(
                x=filtered_df['month_number'],
                y=filtered_df[product],
                mode='lines+markers',
                name=product.replace('_', ' ').title(),
                line=dict(color=colors[i % len(colors)], width=2),
                marker=dict(size=8)
            ))
        
        fig.update_layout(
            title="Monthly Trends by Product Category",
            xaxis_title="Month",
            yaxis_title="Units Sold",
            template='plotly_dark',
            height=500,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            hovermode='x unified'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
            <h3>💡 Key Insight</h3>
            <p>
                <strong>Bathing Soap</strong> and <strong>Toothpaste</strong> are consistent top performers,
                showing the highest sales volumes. <strong>Shampoo</strong> shows the most volatility,
                indicating either seasonal demand or supply chain variations.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("#### Seasonal Performance Analysis")
        
        # Seasonal breakdown
        seasonal_stats = df.groupby('season')[['total_units', 'total_profit']].mean().round(0)
        
        col1, col2 = st.columns(2)
        
        with col1:
            fig = go.Figure(data=[
                go.Bar(
                    x=seasonal_stats.index,
                    y=seasonal_stats['total_units'],
                    marker=dict(
                        color=['#00f0ff', '#00ff88', '#ffaa00', '#ff0088'],
                    ),
                    text=seasonal_stats['total_units'],
                    textposition='auto',
                )
            ])
            
            fig.update_layout(
                title="Average Units Sold by Season",
                xaxis_title="Season",
                yaxis_title="Units",
                template='plotly_dark',
                height=400,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            fig = go.Figure(data=[
                go.Bar(
                    x=seasonal_stats.index,
                    y=seasonal_stats['total_profit'],
                    marker=dict(
                        color=['#00f0ff', '#00ff88', '#ffaa00', '#ff0088'],
                    ),
                    text=seasonal_stats['total_profit'],
                    textposition='auto',
                )
            ])
            
            fig.update_layout(
                title="Average Profit by Season",
                xaxis_title="Season",
                yaxis_title="Profit ($)",
                template='plotly_dark',
                height=400,
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)'
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        # Quarterly performance
        st.markdown("#### Quarterly Performance")
        
        quarterly_stats = df.groupby('quarter')[['total_units', 'total_profit']].sum()
        
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=quarterly_stats.index,
            y=quarterly_stats['total_units'],
            name='Total Units',
            marker_color='#00f0ff'
        ))
        fig.add_trace(go.Bar(
            x=quarterly_stats.index,
            y=quarterly_stats['total_profit'] / 10,  # Scale for visibility
            name='Total Profit (÷10)',
            marker_color='#00ff88'
        ))
        
        fig.update_layout(
            title="Quarterly Sales Performance",
            xaxis_title="Quarter",
            yaxis_title="Value",
            template='plotly_dark',
            height=400,
            barmode='group',
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
            <h3>💡 Key Insight</h3>
            <p>
                <strong>Q2 and Q3</strong> show higher sales volumes, likely due to summer season demand.
                <strong>Winter months</strong> maintain steady performance, suggesting consistent demand
                for personal care products year-round with seasonal spikes.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab4:
        st.markdown("#### Product Correlation Analysis")
        
        # Correlation heatmap
        product_cols = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
        corr_matrix = df[product_cols].corr()
        
        fig = go.Figure(data=go.Heatmap(
            z=corr_matrix.values,
            x=[p.replace('_', ' ').title() for p in corr_matrix.columns],
            y=[p.replace('_', ' ').title() for p in corr_matrix.index],
            colorscale='RdBu',
            zmid=0,
            text=corr_matrix.values.round(2),
            texttemplate='%{text}',
            textfont={"size": 10},
            colorbar=dict(title="Correlation")
        ))
        
        fig.update_layout(
            title="Product Sales Correlation Matrix",
            template='plotly_dark',
            height=500,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Scatter plot: Units vs Profit
        st.markdown("#### Total Units vs Total Profit Relationship")
        
        fig = px.scatter(
            df,
            x='total_units',
            y='total_profit',
            size='profit_per_unit',
            color='season',
            hover_data=['month_number'],
            labels={'total_units': 'Total Units Sold', 'total_profit': 'Total Profit ($)'},
            template='plotly_dark',
            color_discrete_sequence=['#00f0ff', '#00ff88', '#ffaa00', '#ff0088']
        )
        
        # Add trendline
        z = np.polyfit(df['total_units'], df['total_profit'], 1)
        p = np.poly1d(z)
        fig.add_trace(go.Scatter(
            x=df['total_units'].sort_values(),
            y=p(df['total_units'].sort_values()),
            mode='lines',
            name='Trend',
            line=dict(color='red', width=2, dash='dash')
        ))
        
        fig.update_layout(
            height=500,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)'
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div class="insight-box">
            <h3>💡 Key Insight</h3>
            <p>
                There's a <strong>perfect linear correlation (r=1.0)</strong> between units sold and profit,
                confirming a consistent $10 profit per unit pricing strategy. This stability indicates
                excellent cost control and predictable margin management.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Summary Statistics
    st.markdown("### 📋 Summary Statistics")
    
    summary_df = df[['total_units', 'total_profit'] + product_cols].describe().round(2)
    st.dataframe(summary_df, use_container_width=True)
    
    # Anomaly Detection
    st.markdown("### 🔍 Anomaly Detection")
    
    # Simple anomaly detection using z-score
    from scipy import stats
    df['units_zscore'] = np.abs(stats.zscore(df['total_units']))
    anomalies = df[df['units_zscore'] > 1.5]
    
    if len(anomalies) > 0:
        st.warning(f"⚠️ Found {len(anomalies)} months with unusual sales patterns:")
        st.dataframe(anomalies[['month_number', 'total_units', 'total_profit', 'season']], use_container_width=True)
    else:
        st.success("✅ No significant anomalies detected in sales data")
    
except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.info("Please ensure 'company_sales_data.csv' is in the same directory as this app.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 1rem; opacity: 0.7;'>
    <p style='color: white;'>📊 Built by Sekar Kumaran | VIF Data Science | visioninnovateforge@gmail.com</p>
</div>
""", unsafe_allow_html=True)
