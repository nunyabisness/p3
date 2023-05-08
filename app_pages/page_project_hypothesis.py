import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect cherry leaves can be identified as being healthy or having powdery mildew. "
        f"The powdery mildew is white so is easily identifiable against the green of the leaf. \n\n"
        f"* An Image Montage shows that typically a leaf with powdery mildew has clear white colouring "
        f"where the leaf has been affected."
        f"Average Image, Variability Image and Difference between Averages studies did not reveal "
        f"any clear pattern to differentiate one from another."

    )
