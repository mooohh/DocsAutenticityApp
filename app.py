import streamlit as st

from Check_autenticity import check_docs_authenticity
from Check_autenticity import display_different_pages
from Check_autenticity import extract_text_per_page_with_text
from Check_autenticity import compare_all_pages, extract_text_per_page_with_text


st.set_page_config(
    page_title="DocsAutenticityApp",
    page_icon=":guardsman:",    
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("DocsAutenticityApp")


st.sidebar.title("Navigation")

st.sidebar.markdown(
    """
    - [Home](#home)
    - [About](#about)
    - [Contact](#contact)
    """
)
st.sidebar.markdown(
    """
    - [GitHub](https://github.com/mooohh)
    """
)

st.markdown("## Upload the Initial Document")
uploaded_initial_file = st.file_uploader("Choose the initial file", type=["pdf", "docx"])

st.markdown("## Upload the Document to be Verified")
uploaded_file_to_be_verified = st.file_uploader("Choose the file to be Verified", type=["pdf", "docx"])

if uploaded_initial_file and uploaded_file_to_be_verified:
    if st.button("🔍 Vérifier et surligner dans le PDF"):
        result = check_docs_authenticity(uploaded_initial_file, uploaded_file_to_be_verified)

        if result:
            st.success("Le document est authentique.")
        else:
            st.error("Le document n'est pas authentique.")

            diff_page_hash = compare_all_pages(
                extract_text_per_page_with_text(uploaded_initial_file),
                extract_text_per_page_with_text(uploaded_file_to_be_verified)
            )
            display_different_pages(uploaded_initial_file, uploaded_file_to_be_verified, diff_page_hash.keys())

else:
    st.warning("Please upload both files to check authenticity.")
    
        




    
    
    