# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session

helpful_links = [
    "https://docs.streamlit.io",
    "https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit",
    "https://github.com/Snowflake-Labs/snowflake-demo-streamlit",
    "https://docs.snowflake.com/en/release-notes/streamlit-in-snowflake"
]

# Write directly to the app
st.title(" :cup_with_straw: Customize your Smoothie ! :cup_with_straw:")
st.write(
    f""" Choose the fruits you want in your Smoothie! """
)

from snowflake.snowpark.functions import col

# Get the current credentials
session = get_active_session()

name = st.text_input("Your name :","",20)
#st.write ("Entered name :"+name)
#option = st.selectbox(
#    "What is your favourite fruits ?",
#    ("Apple","Watermelon","Strawberries","Banana","Peaches"),
#)

#st.write("Your favourite fruit :", option)

#session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect('Choose any 5 ingredients :',my_dataframe,max_selections =5)
if ingredients_list:
   # st.write(ingredients_list)
   # st.text(ingredients_list)
    ingredients_string = ''
    for fruits_chosen in ingredients_list:
        ingredients_string += fruits_chosen+' '
    st.write(ingredients_string)
    my_insert_stmt = """ insert into smoothies.public.orders (ingredients,name_on_order)
            values ('""" + ingredients_string + """','""" + name + """')"""
    #st.write(my_insert_stmt)
    time_to_submit = st.button('Submit order')
    if time_to_submit:
        session.sql(my_insert_stmt).collect()
        st.success('Your Smoothie is ordered!'+ name, icon="✅")
        st.stop


    



