import pandas as pd
import streamlit as st
from PIL import Image
import time


DATA_URL = "https://data-nces.opendata.arcgis.com/datasets/a15e8731a17a46aabc452ea607f172c0_0.csv?outSR=%7B%22latestWkid%22%3A4269%2C%22wkid%22%3A4269%7D"
data_file = pd.read_csv("Postsecondary_School_Locations_-_Current.csv",
                       index_col='NAME', parse_dates=['SCHOOLYEAR'], header=0)

state_list = data_file["STATE"].unique()

st.title("Book Store Investment")

st.write("Created by Shawn Cheng")

#st.set_page_config(page_title='noshow')

INDEX = []
NAME = []
X = []
Y = []
STATE = []

# ----------------------------------- Interactive Functions ----------------------------------- #

def df(): #Create dataframe
    data = {'name' : NAME,
            'lon' : X,
            'lat' : Y,
            'state': STATE,
            }
    df = pd.DataFrame(data, index= INDEX)
#    df['reg_date'] = pd.to_datetime(df['reg_date'])
    return df

def map():
    @st.cache
    def load_data(nrows):
        data = pd.read_csv('Postsecondary_School_Locations_-_Current.csv', nrows=nrows)
        lowercase = lambda x: str(x).lower()
        return data

    data = load_data(10000)
    data = pd.DataFrame({'lat': data['Y'], 'lon': data['X']})

    st.subheader('Map of Colleges and Universities in USA')
    st.map(data)

def datasets():

    sentiment_count = data_file["STATE"].value_counts()

    data = pd.DataFrame({
        'index': data_file["STATE"].unique(),
        'state_number': sentiment_count
    }).set_index('index')

    display1 = st.button('Click to see Dataset')
    if display1:
        st.write('This Datasets show us the distribution of colleges and universities in United States.', data_file)

    display2 = st.button('Click to see Chart')
    if display2:
        st.bar_chart(data)

    display3 = st.button('Click to see Partial Data')
    if display3:
        st.write(data)



# ----------------------------------- Home ----------------------------------- #

def option1(): #Home page

    st.image('./bookstore.jpg', caption='picture download from google ')

    st.markdown('''Welcome book lovers who have a dream to open a bookstore. Having a desire location with lots of foot traffics near school areas could be an optimal choice to start a bookstore. 
    Before clicking into my interactive application with secondary colleges and universities data, please complete the form on your left hand side with your name and simply answer a question. 
    After that, I’ll walk you through the application with graphical representation and aim to give you a better idea of finding the best location based on your own preference for living and opening your own bookstore.
    
    • Coding Fundamentals: data types, if statements, loops, formatting, etc. 
    • Functions:  passing positional and optional arguments,  returning values
    • Files: Reading data from a CSV file into a DataFrame
    • Pandas: Module functions and DataFrames to manipulate large data sets
    • MatPlotLib or pandas: Creating different types of charts
    • StreamLit.io: Displaying interactive widgets and charts
    ''')

    today = pd.to_datetime("today")
    col1, col2 = st.beta_columns(2)
    image = Image.open('./icon.png')
    col1.image(image,
               caption='Streamlit Logo',
               use_column_width=True)
    col2.write(today, width=300)

###
# ----------------------------------- Map ----------------------------------- #
def option2():

    map()

    if st.button('\nAre you ready for next page?'):
        st.write('Good Job! Lets go!')
    else:
        st.write('Noy yet...')

###
# ----------------------------------- Ranking ----------------------------------- #

def option3():

     # Choose Type of Chart
    st.markdown("### Type of chart to rank the number")
    select = st.selectbox("Chart Type", ["Bar Chart", "Area Chart"],
                                   key ="2")

    sentiment_count = data_file["STATE"].value_counts()
    state_choices = st.multiselect("Select States:",data_file["STATE"].unique(),
                                  help="Please select more than one option to make successfully a chart."
                                              "If happens any error, please re-run the site.") #Multiselect widget
    state_frame = pd.DataFrame(sentiment_count, index=state_choices)

    # hide the chart if do not want to display

    if not st.checkbox("Hide", True):
       st.markdown('### Number of University by State')
       if select == "Bar Chart":
           st.bar_chart(state_frame)
       elif select == "Area Chart":
           st.area_chart(state_frame)

    st.write(state_frame)


    #state_options = sorted(list(set(state_choices))) #Create unique list of the county list
    #ranking = pd.DataFrame(state_options, index="a")
    #st.bar_chart(ranking)
    #st.write(ranking)


# ----------------------------------- Datasets ----------------------------------- #
def option4():

    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f'loading {i+1} %')
        bar.progress(i + 1)
        time.sleep(0.05)

    datasets()

# ---------------------------------- sidebar --------------------------------- #

st.sidebar.header('Let me walk through my project!!')

name = st.sidebar.text_input('Please tell me your name?')
st.sidebar.write(f'Thank you {name} and welcome to my presentation!')

invest = st.sidebar.selectbox('Do you want to own a bookstore for investment?', ['Yes', 'No'])

if invest == "Yes":
    st.sidebar.write("Awesome! You will like my presentation today")
elif invest == "No":
    st.sidebar.write("No worries! I can show you my coding just for five minutes.")


menu = st.sidebar.radio(
    'Which page do you want to go through first?',
    ('Home', 'Map', 'Ranking', 'Datasets'))
if menu == "Home":
    option1()
elif menu == "Map":
    option2()
elif menu == "Ranking":
    option3()
elif menu == "Datasets":
    option4()


if st.sidebar.checkbox('Show Raw Data'):
    '# College & Universities in USA ', data_file

expander = st.sidebar.beta_expander("Before you click the checkbox...")
expander.write(f"If you want to get the complehensive dataset, you can download here:\n{DATA_URL}")
df = df()

# streamlit-to-heroku-tutorial
# streamlit-to-heroku-tutorial
# streamlit-to-heroku-tutorial
