import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Géré automatiquement
            'logged_in': False,  # Géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Géré automatiquement
            'logged_in': False,  # Géré automatiquement
            'role': 'administrateur'
        }
    }
}

# Fonction d'accueil pour les utilisateurs connectés
def accueil():
    st.title("Bienvenue sur le contenu réservé aux utilisateurs connectés")
    # Menu de navigation
    selection = option_menu(
        menu_title=None,
        options=["Accueil", "Photos de mon chat"],
        menu_icon="cast",  # Icône du menu
        default_index=0,   # Option par défaut sélectionnée
        orientation="vertical"  # Affiche verticalement
    )
    
    # Logique en fonction du menu sélectionné
    if selection == "Accueil":
        st.write("Bienvenue sur la page d'accueil !")
    elif selection == "Photos de mon chat":
        st.write("Voici les photos de mon chat (et d'autres animaux) :")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Un 1er chat")
            st.image("https://i-sam.unimedias.fr/2018/08/10/istock-160515715.jpg?auto=format%2Ccompress&crop=faces&cs=tinysrgb&fit=crop&h=501&w=890")
        with col2:
            st.header("Un autre chat")
            st.image("https://images.pexels.com/photos/104827/cat-pet-animal-domestic-104827.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2")
        with col3:
            st.header("Encore un autre chat")
            st.image("https://images.ctfassets.net/denf86kkcx7r/57uYN7JlyDtQ91KvRldrm9/0a0656983993f5e09c4daa0a4fd8f5e6/comment-punir-son-chat-91")

# Initialisation de l'authentificateur
authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie_name",  # Le nom du cookie, un str quelconque
    "cookie_key",  # La clé du cookie, un str quelconque
    30  # Le nombre de jours avant que le cookie expire
)

authenticator.login()

# Vérification de l'état d'authentification
if st.session_state.get("authentication_status"):
    accueil()
    # Bouton de déconnexion
    authenticator.logout("Déconnexion", key="logout")
elif st.session_state.get("authentication_status") is False:
    st.error("Le nom d'utilisateur ou le mot de passe est incorrect.")
elif st.session_state.get("authentication_status") is None:
    st.warning("Les champs nom d'utilisateur et mot de passe doivent être remplis.")
