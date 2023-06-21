import streamlit as st
import json
from pathlib import Path
import requests
from gpt4free import you, theb
from streamlit_star_rating import st_star_rating
import requests
import time
from io import StringIO


st.text('')
st.title("Code Explainer")
st.text('')

source = st.radio("How would you like to start? Choose an option below",
                    ("I want to input some text", "I want to upload a file"))
st.text('')

s_example = """
            class Solution(object):
                def isValid(self, s):
                    stack = []
                    mapping = {")": "(", "}": "{", "]": "["}
                    for char in s:
                        if char in mapping:
                        top_element = stack.pop() if stack else '#'
                        if mapping[char] != top_element:
                            return False
                        else:
                            stack.append(char)
                    return not stack
            """

if source == 'I want to input some text':
    input_su = st.text_area("Use the example below or input your own code with appropriate indentations)", value=s_example, max_chars=10000, height=330)
    if st.button('Explain Code'):
        with st.spinner('Processing...'):
            time.sleep(2)
            st.markdown('___')
            prompt=f"Explain this code. Lets think Step by step. : {input_su}"
            response = []
            for token in theb.Completion.create(prompt):
                response.append(print(token, end='', flush=True))
            st.write('Results!')
            st.write("".join(response))
            stars = st_star_rating("How satisfied are you with the response?", 5, 0, 40)
            st.balloons()
if source == 'I want to upload a file':
    file = st.file_uploader('Upload your file here',type=['txt'])
    if file is not None:
        with st.spinner('Converting your code to explanations...'):
                time.sleep(2)
                stringio = StringIO(file.getvalue().decode("utf-8"))
                string_data = stringio.read()
                time.sleep(2)
                st.markdown('___')
                response = you.Completion.create(
                prompt=f"Explain this code. Lets think Step by step : {string_data}"
                )
            
                st.write(response.text)
                stars = st_star_rating("How satisfied are you with the response?", 5, 0, 40)
                st.caption("")
                st.balloons()
