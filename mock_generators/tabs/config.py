import streamlit as st
from constants import *
from file_utils import load_json, load_string
from models.generator import Generator, generators_from_json
import os
import sys
import logging

def config_tab() -> list[Generator]:

    col1, col2 = st.columns([1,11])
    with col1:
        st.image("mock_generators/media/options.gif")
    with col2:
        st.write("Optionally change the export path, source locations for importing and reading generator specifications and code files. Generators are code functions used to generate specific types of mock data (ie: email generator for creating mock email addresses).")
    st.markdown("--------")

    # Load export path
    new_exports_filepath = st.text_input("Generated Data filepath", st.session_state[EXPORTS_PATH])
    if new_exports_filepath != st.session_state[EXPORTS_PATH]:
        st.session_state[EXPORTS_PATH] = new_exports_filepath

    # Load new generator template file
    cc1, cc2 = st.columns([1,2])
    with cc1:
        new_template_filepath = st.text_input("Generator Code Template file", st.session_state[CODE_TEMPLATE_FILE])
        if new_template_filepath != st.session_state[CODE_TEMPLATE_FILE]:
            st.session_state[CODE_TEMPLATE_FILE] = new_template_filepath
        with open(st.session_state[CODE_TEMPLATE_FILE], "r") as file:
            code_template = file.read()
    with cc2:
        st.write("Loaded code template file")
        with st.expander("Generator Code Template"):
            st.code(code_template)


    # Load generators
    gc1, gc2 = st.columns([1,2])
    with gc1:
        new_spec_filepath = st.text_input("Generators Spec filepath", st.session_state[SPEC_FILE])
        if new_spec_filepath != st.session_state[SPEC_FILE]:
            st.session_state[SPEC_FILE] = new_spec_filepath
    with gc2:
        generators = st.session_state[GENERATORS]
        try:
            with open(new_spec_filepath) as input:
                generators_file = input.read()
                generators_json = load_json(new_spec_filepath)
                new_generators = (generators_from_json(generators_json))
                if generators != new_generators:
                    st.session_state[GENERATORS] = new_generators

        except FileNotFoundError:
            st.error('File not found.')
        st.write("Loaded spec file")
        with st.expander("Generators Spec JSON"):
            st.code(generators_file)

    # Load generators code
    cc1, cc2 = st.columns([1,2])
    with cc1:
        new_code_filepath = st.text_input("Generators Code filepath", st.session_state[CODE_FILE])
        if new_code_filepath != st.session_state[CODE_FILE]:
            st.session_state[CODE_FILE] = new_code_filepath
    files = ""
    with cc2:
        st.write(f'Code Files in path: {st.session_state[CODE_FILE]}')
        try:
            # for root, dirs, files in os.walk(st.session_state[CODE_FILE]):
            #     for file in files:
            #         if file.endswith(".py"):
            #             files += file
            for root, dirs, files in os.walk(st.session_state[CODE_FILE]):
                for file in files:
                    if file.endswith(".py"):
                        try:
                            with st.expander(file):
                                with open(os.path.join(root, file), 'r') as f:
                                    st.text(f.read())
                        except:
                            logging.error(f"Error reading file: {file}")
        except:
            logging.error(f'config.py: Error retrieving generator .py files from {st.session_state[CODE_FILE]}: {sys.exc_info()[0]}')
    
    # TODO: Verify export path is available

    # TODO: Add resest




    st.markdown("Images by Freepik from [Flaticon](https://www.flaticon.com/)")