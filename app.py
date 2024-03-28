import streamlit as st
import pandas as pd
import plotly.express as px
import preprocessing,helper
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessing.preprocess(df,region_df)

st.sidebar.title('Olympics Analysis')
st.sidebar.image("https://banner2.cleanpng.com/20171216/91f/olympic-rings-png-5a3558a6bb42b4.494781141513445542767.jpg")

user_menu = st.sidebar.radio(
    'Select an option',
    ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athlete-wise Analysis')
)


if user_menu == 'Medal Tally':
    st.sidebar.header('Medal Tally')
    years, country = helper.country_year_list(df)
    selected_years = st.sidebar.selectbox('Select a Year',years)
    selected_country = st.sidebar.selectbox('Select a Country',country)
    medal_tally = helper.fetch_medal_tally(df,selected_years,selected_country)


    if selected_years == "Overall" and selected_country == "Overall":
        st.title("Olympic Medals by Country till 2016")

    if selected_years == "Overall" and selected_country != "Overall":
        st.title(selected_country +' Olympic Journey' )

    if selected_years != "Overall" and selected_country == "Overall":
        st.title(str(selected_years) +' Olympic Standing' )

    if selected_years != "Overall" and selected_country != "Overall":
        st.title(selected_country+' Olympic Medals in '+str(selected_years) )
    st.table(medal_tally)


if user_menu == 'Overall Analysis':
    editions = df['Year'].unique().shape[0]-1
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    athletes = df['Name'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    nations = df['region'].unique().shape[0]

    st.title('Top Statistics')
    col1,col2,col3 = st.columns(3, gap= "large")



    with col1 :
        st.subheader('Edition')
        st.title(editions)

    with col2 :
        st.subheader('Hosts')
        st.title(cities)

    with col3 :
        st.subheader('Sports')
        st.title(sports)

    col1,col2,col3 = st.columns(3, gap= "large")

    with col1 :
        st.subheader('Nations')
        st.title(nations)

    with col2 :
        st.subheader('Athletes')
        st.title(athletes)

    with col3 :
        st.subheader('Events')
        st.title(events)

    nations_over_time = helper.perticipating_nations_over_time(df)
    fig = px.line(nations_over_time, x='Editions', y='No of Countries')
    st.title('Perticipating Nations over the Years')
    st.plotly_chart(fig)

    sports_over_time = helper.played_sports_over_time(df)
    fig = px.line(sports_over_time, x='Editions', y='No of Sports')
    st.title('No of Sports over the Years')
    st.plotly_chart(fig)

    athletess_over_time = helper.perticipating_athletes_over_time(df)
    fig = px.line(athletess_over_time, x='Editions', y='No of Athletes')
    st.title('Perticipating Athletes over the Years')
    st.plotly_chart(fig)

    events_over_time = helper.arranged_events_over_time(df)
    fig = px.line(events_over_time, x='Editions', y='No of Events')
    st.title('No of Events over the Years')
    st.plotly_chart(fig)


    st.title('No of Events Over Time (Every Sports)')
    fig, ax = plt.subplots(figsize=(20,20))
    x = df.drop_duplicates(['Year', "Sport", "Event"])
    ax = sns.heatmap(pd.pivot_table(x, index="Sport", values="Event", columns="Year", aggfunc='count').fillna(0).astype(int),
                annot=True)
    st.pyplot(fig)

    st.title('Most Successful Athelets')
    sport_list = df["Sport"].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sports = st.selectbox("Select a Sport",sport_list)
    x = helper.most_successful_athlete(df,selected_sports)
    st.table(x)

if user_menu == 'Country-wise Analysis':

    st.sidebar.title('Country-wise Analysis')
    country_list = df["region"].dropna().unique().tolist()
    country_list.sort()
    country_list.insert(0, 'Overall')
    selected_country = st.sidebar.selectbox("Select a Country", country_list)

    country_df = helper.year_wise_medal_tally(df, selected_country)
    fig = px.line(country_df, x ='Year', y ="Medal")
    st.title(selected_country+ ' Medal Tally over the Years')
    st.plotly_chart(fig)


    pt = helper.country_event_heatmap(df, selected_country)
    st.title(selected_country + ' excels in the following Sports')
    fig, ax = plt.subplots(figsize=(20, 20))

    ax = sns.heatmap(pt, annot=True)
    st.pyplot(fig)

    st.title(selected_country+ 's Most Successful Athelets')
    x = helper.countrys_successful_athlete(df, selected_country)
    st.table(x)


if user_menu == 'Athlete-wise Analysis':

    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df["Medal"] == "Gold"]["Age"].dropna()
    x3 = athlete_df[athlete_df["Medal"] == "Silver"]["Age"].dropna()
    x4 = athlete_df[athlete_df["Medal"] == "Bronze"]["Age"].dropna()

    fig = ff.create_distplot((x1, x2, x3, x4), ["Overall Age", "Gold Medalist", "Silver Medalist", "Bronze Medalist"],
                             show_hist=False, show_rug=False)

    st.title('Distribution of Age')
    fig.update_layout(autosize= False, height= 600, width = 800)

    st.plotly_chart(fig)


    st.title("Height vs Weight")
    sport_list = df["Sport"].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')
    selected_sports = st.selectbox("Select a Sport", sport_list)

    temp_df = helper.height_vs_weight(df,selected_sports)
    fig, ax = plt.subplots(figsize=(10,10))
    ax = sns.scatterplot(temp_df,x = "Weight", y = "Height", hue ='Medal',style ="Sex", s = 60)
    st.pyplot(fig)


    st.title("Men vs Women perticipation over the years")
    final = helper.man_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, height=600, width=800)
    st.plotly_chart(fig)

