import streamlit as st
import random

st.title("Optionator")

# Initialize session state for options if it doesn't exist
if 'options' not in st.session_state:
    st.session_state.options = []

# Input form for new options
with st.form("add_option_form"):
    new_option = st.text_input("Enter all your options:")
    submitted = st.form_submit_button("Add Option")
    
    if submitted and new_option:
        st.session_state.options.append(new_option)
        st.success(f"Added: {new_option}")

# Display current options
if st.session_state.options:
    st.subheader("Current Options:")
    for i, option in enumerate(st.session_state.options):
        st.write(f"{i+1}. {option}")
    
    # Button to randomly select an option
    if st.button("Let Optionator Decide"):
        if st.session_state.options:
            selected_index = random.randint(0, len(st.session_state.options) - 1)
            selected_option = st.session_state.options[selected_index]
            st.success(f"Selected option: {selected_option}")
        else:
            st.warning("Please add at least one option first.")
else:
    st.info("No options added yet. Please add some options above to let Optionator decide what's next.") 