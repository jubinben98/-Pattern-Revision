import streamlit as st
import unicodedata
from itertools import chain

def empty_space(height: int):
    for _ in range(height): st.write('\n')

def handleClick():
    st.session_state.current_index += 1

def input_dict(pattern:str, example_nihongo:list, example_english:list) -> dict:
    return {
        "pattern": pattern,
        "example": example_nihongo,
        "example_english": example_english
    }

# title
st.write(""" # 日本語　Pattern Revision JLPT-N5""")
empty_space(3)

# select chapters
st.write(""" ## Range of chapters to revise""")
chapters = st.slider('chapter-slider', 1, 10, (1, 2), label_visibility="hidden")

# patterns dictionary from each chapter
pattern_dict = {
    1: [
        input_dict("[N1] wa [N2] desu", ["わたしわ　マイク　ミラ　です。"], ["I'm Mike Miller."]),
        input_dict("[N1] wa [N2] ja (dewa) arimansen", ["サントスさんは　がくせい　じゃありません。"], ["Mr. Santosh is not a student."]),
        input_dict("[N1] wa [N2] desu ka", ["ミラさんは　アメリカじん　ですか。"], ["Is Mira san American?"]),
        input_dict("[N] mo", ["ミラさんは　かいしゃいん　です。グプタさんも　かいしゃいん　です。"], ["Mira san is company employee. Mr. Gupta san is also company employee."]),
        input_dict("[N1] no [N2]", ["ミラさんは　IMC　の　しゃいん　です。"], ["Mr. Mira is an employee of IMC."]),
    ],
    2:[
        input_dict("[N1] no [N2] (for things)", ["これは　コンピュタ　の　ほん　です。"], ["This is a book on computer."]),
    ]
}

dict_keys = list(pattern_dict.keys())
patterns = []
if chapters[0] in dict_keys and chapters[1] in dict_keys:
    patterns = list(chain(*[pattern_dict[i] for i in range(chapters[0], chapters[1]+1)]))
else:
    st.write(f"##### Please select chapter range from {dict_keys[0]} to {dict_keys[-1]}")

# Show and revise the patterns
if "current_index" not in st.session_state:
    st.session_state.current_index = 0

empty_space(3)
if chapters[0] > 0 and st.session_state.current_index < len(patterns) and len(patterns) > 0:
    tab1, tab2, tab3 = st.tabs(["Pattern", "Japanese example", "English example"])
    with tab1:
        st.write(f"### {patterns[st.session_state.current_index]['pattern']}")
    with tab2:
        for i in patterns[st.session_state.current_index]['example']:
            st.write(f"### {unicodedata.normalize('NFKC', i)}")
    with tab3:
        for i in patterns[st.session_state.current_index]['example_english']:
            st.write(f"### {i}")

    submit = st.button('Next Pattern', on_click=handleClick)

st.empty()

empty_space(6)
if st.button("Reset", type="primary"):
    st.session_state.current_index = 0
    st.rerun()


