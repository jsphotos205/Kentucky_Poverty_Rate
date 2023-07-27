import streamlit as st
import pandas as pd
import os
import pandas_profiling

from streamlit_pandas_profiling import st_profile_report

@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def centered_header(text):
    st.markdown(f"<h1 style='text_align: center;'>{text}</h1>",
                unsafe_allow_html=True)
    
def centered_subheader(text):
    st.markdown(f"<h2 style='text-align: center;'>{text}</h2>",
                unsafe_allow_html=True)

def load_markdown_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def main():
    st.set_page_config(page_title='Kentucky Poverty Rate Machine Learning Model',
                       page_icon=':banjo:',
                       layout='wide',
                       initial_sidebar_state='expanded')
    epsilon = st.sidebar.slider('Step size',
                      min_value=0.0,
                      max_value=0.25,
                      format='%.3f')
    alpha = st.sidebar.slider('Max perturbation',
                              min_value=0.00,
                              max_value=0.250,
                              step=0.001,
                              value=0.025,
                              format='%.3f')
    n_steps = st.sidebar.number_input('Number of steps',
                                      step=1,
                                      min_value=1,
                                      max_value=50,
                                      value=9)
    #home_content is the markdown file located in streamlit/pages/md
    home_content = load_markdown_file('streamlit/pages/md/Home.md')
    st.markdown(home_content, unsafe_allow_html=True)

    data_dir = 'streamlit/data/'
    csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
    selected_file = st.selectbox('Select', csv_files, index=0)

    if selected_file:
        file_path = os.path.join(data_dir, selected_file)

        selected_file_name = selected_file.rstrip('.csv')

        kentucky_pov = load_data(file_path)

        st.header(f'{selected_file_name}:')
        st.dataframe(kentucky_pov)
        
        # pr = kentucky_pov.profile_report()
        # st_profile_report(pr)

if __name__ == '__main__':
    main()