import streamlit as st
from constants import *
import uuid

def relationship_row(relationship: dict):

    if relationship is None:
        id = str(uuid.uuid4())[:8]
        type = ""
        properties = []
        fromId = ""
        toId = ""
    else:
        id = relationship.get("id")
        type = relationship.get("type")
        fromId = relationship.get("fromId")
        toId = relationship.get("toId")
        if 'properties' in relationship:
            properties = [(k,v) for k,v in relationship.get("properties").items()]
        else:
            properties = []

    with st.expander(f"relationship id: {id}, type: {type}, from: {fromId}, to: {toId}"):
        st.write('Property assignments')