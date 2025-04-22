#  DocsAuthenticityApp

Une application simple et sécurisée permettant de vérifier si deux documents sont **identiques** en utilisant l’empreinte cryptographique **SHA-256**.

---

##  Fonctionnalités

-  Upload de deux fichiers (.pdf ou .docx)
-  Calcul de l’empreinte SHA-256 de chaque fichier
-  Comparaison des empreintes pour vérifier l’authenticité
-  Résultat clair : document authentique ou modifié

---

##  Principe

L’application utilise la fonction de hachage **SHA-256** pour générer une empreinte unique de chaque fichier.  
La moindre modification dans le contenu d’un fichier change complètement son hash.  
Ainsi, si les deux empreintes sont **identiques**, les fichiers le sont aussi.

---

##  Technologies utilisées

- Python
- Streamlit — pour l’interface utilisateur
- hashlib — pour le calcul cryptographique

---

##  Structure du projet


├── app.py                     # Interface utilisateur Streamlit  
├── check_authenticity.py     # Fonctions de calcul et de comparaison de hash  
├── README.md                  # Ce fichier

---

##  Lancer l’application 
- https://docsautenticityapp.streamlit.app/ 

###  Prérequis

- Python 3.11 installé
- Streamlit installé :  
  `pip install streamlit`

### Exécution

Dans le terminal :

```bash
streamlit run app.py
