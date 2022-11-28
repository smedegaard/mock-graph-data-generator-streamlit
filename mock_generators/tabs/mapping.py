import streamlit as st
from constants import *
import json
import logging
from widgets.node_row import nodes_row
from widgets.relationship_row import relationship_row

def mapping_tab():

    col1, col2 = st.columns([1,11])
    with col1:
        st.image("mock_generators/media/shuffle.gif")
    with col2:
        st.write("Create and edit mock data generation options. \n\nNodes and relationships are default EXCLUDED from mapping, meaning no data will be generated for them. Expand options for each node or relationship, verify/edit labels and properties before enabling each for mock data generation by clicking on the 'Generate Data for this Node' or 'Generate Data for this Relationship' checkbox.")
    uploaded_file = st.session_state[IMPORTED_FILE]
    if uploaded_file is not None:
        with st.expander("Imported File"):
            st.text(uploaded_file)
    st.markdown("--------")

    # Default options
    # Matching arrows.json dict format
    nodes = [{
        "id": "1",
        "caption": "Person",
        "labels": [],
        "properties": {
            "name": "string",
        }
    },
    {
        "id": "2",
        "caption": "Company",
        "labels": [],
        "properties": {
            "name": "string",
        }
    }]
    relationships = [{
        "id": "r1",
        "type": "WORKS_AT",
        "fromId": "1",
        "toId": "2",
        "properties": {
        }
    }]

    # Convert uploaded file (if available) to json
    # Supporting arrows 0.5.4
    if uploaded_file is not None:
        try:
            json_file = json.loads(uploaded_file)
            nodes = json_file["nodes"]
            relationships = json_file["relationships"]
            
        except json.decoder.JSONDecodeError:
            st.error('JSON file is not valid.')

    st.write("NODES:")
    num_nodes = st.number_input("Number of nodes", min_value=1, value=len(nodes), key="mapping_number_of_nodes")
    for i in range(num_nodes):
        if i < len(nodes):
            nodes_row(nodes[i])
        else:
            nodes_row(None)

    st.write("RELATIONSHIPS:")
    num_relationships = st.number_input("Number of relationships", min_value=1, value=len(relationships), key="mapping_number_of_relationships")
    for i in range(num_relationships):
        if i < len(relationships):
            relationship_row(relationships[i])
        else:
            relationship_row(None)