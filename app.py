import streamlit as st
import json
import os
from nano_prompt import generate_image_json

st.set_page_config(
    page_title="Image Prompt Architect",
    page_icon="",
    layout="centered"
)

st.title("Architecte de Prompt Image")
st.markdown("""
Transforme une idée vague en une **spécification JSON complète** pour la génération d'images (Nano Banana, Midjourney, DALL-E, Stable Diffusion).
""")
st.markdown("""
La description générée peut ensuit être facilement modifiée pour correspondre préciséement à vos besoins avant de l'utiliser dans votre outil de génération d'images préféré. 
""")

raw_text = st.text_area(
    "Description de l'image", 
    height=150, 
    placeholder="Ex: Une photo cyberpunk d'un chat qui mange des nouilles sous la pluie, ambiance néon..."
)

if st.button("Générer la description complète", type="primary"):
    if not raw_text:
        st.warning("Merci d'écrire une description d'abord.")
    else:
        with st.spinner("Construction de la scène et extrapolation des détails..."):
            try:
                image_data = generate_image_json(raw_text)
                
                json_str = json.dumps(image_data, ensure_ascii=False, indent=2)
                
                st.success("Prompt structuré généré avec succès !")
                
                st.code(json_str, language="json")
                
                filename = "prompt.json"
                if "intent" in image_data:
                     filename = f"{image_data['intent'].replace(' ', '_')[:20]}.json"

                st.download_button(
                    label="Télécharger le JSON",
                    data=json_str,
                    file_name=filename,
                    mime="application/json"
                )
                    
            except Exception as e:
                st.error(f"Une erreur est survenue : {e}")

st.markdown("---")
st.caption("Assistant de Prompt Engineering pour la génération visuelle par Alexandre Eberhardt.")