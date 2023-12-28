"""
This Streamlit web application is designed for revising Japanese language patterns, specifically focusing
on JLPT-N5 level. Users can select a range of chapters to revise and navigate through different patterns,
viewing Japanese and English examples.
"""

import streamlit as st
import unicodedata

from datetime import datetime
from patterns import PATTERN_DICT
from utils import empty_space
from itertools import chain

def handleClick():
    st.session_state.current_index += 1

# page config
st.set_page_config(
    page_title="日本語-patterns",
    menu_items={
        "Report a Bug": "mailto:jubinben@gmail.com",
        "About": f"""
                  #### Made with :heart: by Jubin Ben :)
                  ###### Deployed on :red[{datetime.now().strftime("%d-%m-%Y %H:%M")}]
                  """
    }
)

# title
st.write("""
# 日本語 Pattern Revision JLPT-N5 
""")
st.caption(f"""
Deployed on :red[{datetime.now().strftime("%d-%m-%Y")}]
""")

empty_space(st, 3)
with st.container(border=True):
    # select chapters
    st.write("""### Range of chapters to revise""",)
    chapters = st.slider('chapter-slider', 1, 10, (1, 2), label_visibility="hidden")

    dict_keys = list(PATTERN_DICT.keys())
    patterns = []
    if chapters[0] in dict_keys and chapters[1] in dict_keys:
        patterns = list(chain(*[PATTERN_DICT[i] for i in range(chapters[0], chapters[1] + 1)]))
    else:
        st.write(f"##### Please select chapter range from {dict_keys[0]} to {dict_keys[-1]}")

    # Show and revise the patterns
    if "current_index" not in st.session_state:
        st.session_state.current_index = 0

    empty_space(st, 3)
    if chapters[0] > 0 and st.session_state.current_index < len(patterns) and len(patterns) > 0:
        tab1, tab2, tab3 = st.tabs(["##### Pattern", "##### Japanese example", "##### English example"])
        with tab1:
            st.write(f"#### &nbsp; {patterns[st.session_state.current_index]['pattern']}")
        with tab2:
            for i in patterns[st.session_state.current_index]['example']:
                st.write(f"#### &nbsp; {unicodedata.normalize('NFKC', i)}")
        with tab3:
            for i in patterns[st.session_state.current_index]['example_english']:
                st.write(f"#### &nbsp; {i}")

        empty_space(st, 2)
        submit = st.button('Next Pattern &nbsp; :arrow_forward:', on_click=handleClick)
        empty_space(st, 1)

    # finish message
    if st.session_state.current_index == len(patterns):
        empty_space(st, 5)
        st.text("Patterns finished, press the Reset button to start over.")
        empty_space(st, 6)
    st.empty()

# reset button & re-run
empty_space(st, 3)
_, _, col, _, _ = st.columns(5)
with col:
    if st.button("Reset", type="primary"):
        st.session_state.current_index = 0
        st.rerun()


