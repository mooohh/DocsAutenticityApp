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

## 🛠 Technologies utilisées

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) — pour l’interface utilisateur
- [hashlib](https://docs.python.org/3/library/hashlib.html) — pour le calcul cryptographique

---

##  Structure du projet

