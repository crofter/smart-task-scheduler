
import streamlit as st
import json
import pandas as pd
from task_parser import parse_task

st.set_page_config(page_title="Smart Task Scheduler", layout="wide")
st.title("Smart Task Scheduler")

st.markdown("Enter your to-do tasks (one per line):")
task_input = st.text_area("Tasks", height=200)

if st.button("Parse Tasks"):
    tasks = task_input.strip().splitlines()
    parsed_tasks = [parse_task(task) for task in tasks]
    df = pd.DataFrame(parsed_tasks)
    st.session_state["parsed_df"] = df

if "parsed_df" in st.session_state:
    st.markdown("### Parsed Tasks (editable):")
    edited_df = st.data_editor(st.session_state["parsed_df"], num_rows="dynamic")
    if st.button("Save Tasks"):
        with open("tasks.json", "w") as f:
            json.dump(edited_df.to_dict(orient="records"), f, indent=2)
        st.success("Tasks saved!")
