
from PIL import Image
import io
import hashlib
import fitz  # PyMuPDF

import streamlit as st



# def display_different_pages(file1, file2, different_pages, dpi=200):
    # file1.seek(0)
    # file2.seek(0)
    # doc1 = fitz.open(stream=file1.read(), filetype="pdf")
    # doc2 = fitz.open(stream=file2.read(), filetype="pdf")

    # for page_num in different_pages:
    #     st.markdown(f"### 🔍 Différence à la page {page_num}")
        
    #     col1, col2 = st.columns(2)
        
    #     with col1:
    #         st.markdown("**Document Initial**")
    #         pix1 = doc1[page_num - 1].get_pixmap(dpi=dpi)
    #         img1 = Image.open(io.BytesIO(pix1.tobytes("png")))
    #         st.image(img1, use_container_width=True)

        # with col2:
        #     st.markdown("**Document à Vérifier**")
        #     pix2 = doc2[page_num - 1].get_pixmap(dpi=dpi)
        #     img2 = Image.open(io.BytesIO(pix2.tobytes("png")))
        #     st.image(img2, use_container_width=True)

import difflib

import fitz  # PyMuPDF
import io
from difflib import SequenceMatcher

def highlight_differences_in_pdf(file_initial, file_verif, pages_to_check):
    file_initial.seek(0)
    file_verif.seek(0)

    doc_initial = fitz.open(stream=file_initial.read(), filetype="pdf")
    doc_verif = fitz.open(stream=file_verif.read(), filetype="pdf")

    for page_num in pages_to_check:
        text_initial = doc_initial[page_num - 1].get_text()
        text_verif = doc_verif[page_num - 1].get_text()

        words_initial = text_initial.split()
        words_verif = text_verif.split()

        # SequenceMatcher (du module difflib) est un outil intelligent pour comparer deux listes et repérer :
        # il retourne 
            # mots égaux "equal"
 
            # mots ajoutés insert"

            # mots modifiés "replace"

            # mots supprimés "delete"


        matcher = SequenceMatcher(None, words_initial, words_verif)

        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag in ["replace", "insert"]:  # mots modifiés ou ajoutés
                for word in words_verif[j1:j2]:
                    # if len(word) <= 2:
                    #     continue  
                    rects = doc_verif[page_num - 1].search_for(word)
                    for rect in rects:
                        doc_verif[page_num - 1].add_highlight_annot(rect)

    # Sauvegarde en mémoire
    output_buffer = io.BytesIO()
    doc_verif.save(output_buffer)
    output_buffer.seek(0)
    return output_buffer




def extract_text_per_page_with_text(file_):
    file_.seek(0)
    doc = fitz.open(stream=file_.read(), filetype="pdf")
    page_texts = {}
    for i, page in enumerate(doc):
        text = page.get_text("text")
        page_texts[i + 1] = text
    file_.seek(0)
    return page_texts


# def extract_text_per_page(file_):
#     file_.seek(0)
#     doc = fitz.open(stream=file_.read(), filetype="pdf")
#     text_hashes = {}
    
#     for i, page in enumerate(doc):
#         text = page.get_text("text")  # texte brut
#         h = hashlib.sha256(text.encode("utf-8")).hexdigest()
#         text_hashes[i + 1] = h

#     file_.seek(0)
#     return text_hashes



# def hash_pdf_page_images(file_, dpi=200):
#     file_.seek(0)
#     doc = fitz.open(stream=file_.read(), filetype="pdf")
#     image_hashes = {}

#     for i, page in enumerate(doc):
#         pix = page.get_pixmap(dpi=dpi)
#         img_bytes = pix.tobytes("png")
#         h = hashlib.sha256(img_bytes).hexdigest()
#         image_hashes[i + 1] = h

#     file_.seek(0)
#     return image_hashes



def compare_all_pages(dict1, dict2):
    all_pages = sorted(set(dict1.keys()) | set(dict2.keys()))  # union des pages
    differences = {}

    for page in all_pages:
        hash1 = dict1.get(page)
        hash2 = dict2.get(page)

        if hash1 != hash2:
            differences[page] = {
                "hash1": hash1,
                "hash2": hash2
            }

    return differences




def caculate_hash(file_, hash_type="sha256"):
    """
    Calculate the SHA-256 hash of a file.
    
    :param file_path: Path to the file
    :return: SHA-256 hash of the file
    """
    
    hash_func = hashlib.new(hash_type)
    
    
    while chunk := file_.read(4096):
            hash_func.update(chunk)
            
    # Convertit le hash en une chaîne de caractères hexadécimale (donc lisible).    
    return hash_func.hexdigest()


def check_docs_authenticity(intial_file, file_to_be_verified, hash_type="sha256"):
    
    """
    Check the integrity of a file by comparing its hash with the original file's hash.
    
    :param intial_file: Path to the original file
    :param file_to_be_verified: Path to the file to be verified
    :param hash_type: Type of hash to use (default is SHA-256)
    :return: True if the hashes match, False otherwise
    """
    
    # Calculate the hash of the original file
    intial_file_hash = caculate_hash(intial_file, hash_type)
    
    # Calculate the hash of the file to be verified
    file_to_be_verified_hash = caculate_hash(file_to_be_verified, hash_type)
    
    # Compare the hashes
    return intial_file_hash == file_to_be_verified_hash





def extract_text_from_pdf(file_):
    file_.seek(0)
    doc = fitz.open(stream=file_.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    file_.seek(0)
    return text


def display_different_pages(file1, file2, different_pages, dpi=200):
    # Créer un PDF avec surlignage des différences
    highlighted_pdf = highlight_differences_in_pdf(file1, file2, different_pages)

    # Réinitialiser les pointeurs de fichiers
    file1.seek(0)
    doc_initial = fitz.open(stream=file1.read(), filetype="pdf")

    highlighted_pdf.seek(0)
    doc_highlighted = fitz.open(stream=highlighted_pdf.read(), filetype="pdf")

    for page_num in different_pages:
        st.markdown(f"### 📄 Comparaison de la page {page_num}")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**🔹 Document Initial (non modifié)**")
            pix_initial = doc_initial[page_num - 1].get_pixmap(dpi=dpi)
            img_initial = Image.open(io.BytesIO(pix_initial.tobytes("png")))
            st.image(img_initial, use_container_width=True)

        with col2:
            st.markdown("**🟡 Document Vérifié (avec surlignage)**")
            pix_modified = doc_highlighted[page_num - 1].get_pixmap(dpi=dpi)
            img_modified = Image.open(io.BytesIO(pix_modified.tobytes("png")))
            st.image(img_modified, use_container_width=True)

    # Bouton de téléchargement du PDF annoté
    st.download_button(
        label="📥 Télécharger le PDF avec surlignage",
        data=highlighted_pdf,
        file_name="document_surligné.pdf",
        mime="application/pdf"
    )


