import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")
    
    st.info(
        f"**General Information**\n"
        f"The client is interested in conducting a study to visually differentiate a cherry leaf that"
        f" is healthy from one that contains powdery mildew. "
        f"The client is interested in predicting if a cherry leaf is healthy or contains"
        f" powdery mildew.\n\n"
        f"Mildew is a white covering over the leaves that can be wiped off with the fingers." 
        f" In extreme cases, it should be brought under control.\n"
        f"The client does not want to supply the market with a product of compromised quality.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset is available on Kaggle and contains 4208 images of cherry leaves with and without powdery mildew."
    )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/jw-coder84/CI-Project-Portfolio-5/blob/main/README.md).")

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in having a study to differentiate "
        f"a cherry leaf that's healthy and a cherry leaf that has powdery mildew.\n"
        f"* 2 - The client is interested in telling whether a given cherry leaf has powdery mildew on the surface or not."
        )