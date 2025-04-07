import streamlit as st
import pandas as pd
import psycopg2
import plotly.express as px

# Title
st.title(" Youth Media Trends Dashboard")
st.markdown("A Streamlit dashboard analyzing Netflix-like youth media content.")

# Connect to PostgreSQL
@st.cache_data
def load_data():
    conn = psycopg2.connect(
        host="localhost",
        database="media_db",
        user="postgres",
        password="taiba2405"
    )
    df = pd.read_sql("SELECT * FROM youth_media", conn)
    conn.close()
    return df

df = load_data()

# ---------------- Charts ----------------

# Chart 1: Type Distribution
type_counts = df['type'].value_counts()
fig1 = px.bar(x=type_counts.index, y=type_counts.values, labels={'x': 'Type', 'y': 'Count'}, title="Count of Movies vs TV Shows")
st.plotly_chart(fig1)

# Chart 2: Ratings Pie
rating_counts = df['rating'].value_counts().nlargest(5)
fig2 = px.pie(values=rating_counts.values, names=rating_counts.index, title="Top 5 Ratings Distribution")
st.plotly_chart(fig2)

# Chart 3: Shows Added Over Years
df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
year_counts = df['release_year'].value_counts().sort_index()
fig3 = px.line(x=year_counts.index, y=year_counts.values, labels={'x': 'Year', 'y': 'Count'}, title="Content Added Over Years")
st.plotly_chart(fig3) 