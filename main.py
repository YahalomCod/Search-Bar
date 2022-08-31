import streamlit as st
import pandas as pd

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    local_css("style.css")
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
    # st.header('People Search')
    st.write("Search :sunglasses:")
    selected = st.text_input("", "")
    cars = pd.read_csv(r'cars.csv')
    if len(selected) != 0:
        ans = cars.loc[cars["Car Names"].str.contains(selected)][["Car Names", "Reviews"]]
        st.write(ans.reset_index(drop=True))

