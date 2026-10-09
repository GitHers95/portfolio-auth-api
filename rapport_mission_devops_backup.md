# RAPPORT DE MISSION – ENVIRONNEMENT LOCAL DEV AVEC DOCKER
**Session du 26 août 2026**  
*Rédigé dans le cadre de la formation DevOps/SysOps*

---

### 1. Contexte et objectifs

**Mission confiée :**  
Mettre en place un environnement de développement local avec microservices et Docker, tout en acquérant les bases de l'administration système Linux et des pratiques DevOps.

**Objectifs spécifiques (échéance : vendredi 21) :**
- Installer et configurer WSL sur le poste de travail.
- Installer et configurer Docker, avec création d’un utilisateur dédié.
- Fournir un fichier récapitulatif des commandes utilisées (`commande_linux_devops_p001.md`).

---

### 2. Synthèse des travaux réalisés

| Phase | Actions menées | Résultat |
|-------|----------------|----------|
| **Audit initial** | Vérification des distributions WSL et de leur version | WSL2 actif avec plusieurs distributions (Ubuntu, Debian, Ubuntu-24.04) |
| **Choix de l’environnement** | Sélection de Debian comme distribution de travail | Environnement stable et documenté |
| **Gestion des utilisateurs** | Réinitialisation du mot de passe de l'utilisateur `admin` (via root) | Accès `sudo` rétabli |
| **Ajout du dépôt Docker** | Téléchargement de la clé GPG officielle et ajout du dépôt Docker dans les sources APT | Dépôt Docker reconnu par le gestionnaire de paquets |
| **Installation de Docker** | Installation de `docker-ce`, `docker-ce-cli` et `containerd.io` | Docker Engine 29.7.2 installé |
| **Configuration des droits** | Ajout de l'utilisateur `admin` au groupe `docker` | Utilisation de Docker sans `sudo` |
| **Validation** | Exécution du conteneur de test `hello-world` | Confirmation du bon fonctionnement |
| **Livrable** | Création du fichier `commande_linux_devops_p001.md` contenant toutes les commandes utilisées | Document structuré et commenté |

---

### 3. État des lieux final

- ✅ **WSL** : installé et fonctionnel (version 2). Distribution Debian active.
- ✅ **Docker** : installé, service actif, utilisateur `admin` autorisé.
- ✅ **Fichier de commandes** : produit et disponible dans le répertoire `~/projects/portfolio-auth-api/`.
- ✅ **Compétences** : acquisition des commandes de base (administration système, paquets, gestion des droits, Docker).

---

### 4. Compétences clés acquises

| Domaine | Compétences |
|---------|-------------|
| **WSL / Windows** | `wsl --list --verbose`, `wsl -d <distro>`, `wsl -u root` |
| **Linux (Debian)** | `sudo`, `apt update/install`, `passwd`, `usermod`, `service docker status` |
| **Sécurité / Dépôts** | Ajout de clé GPG, ajout de dépôt sécurisé (`tee`, `curl`, `gpg`) |
| **Docker** | `docker --version`, `docker run hello-world` |
| **Édition / Documentation** | `nano`, `cat`, création de fichier Markdown |

---

### 5. Difficultés rencontrées et solutions apportées

| Difficulté | Solution |
|------------|----------|
| Mot de passe de l'utilisateur `admin` inconnu | Connexion en root (`wsl -d Debian -u root`) et réinitialisation avec `passwd admin` |
| Commande `lsb_release` non trouvée lors de l'ajout du dépôt Docker | Utilisation directe du nom de code Debian (`trixie`) dans la ligne de source |
| Utilisation de `wsl` à l'intérieur du terminal Linux | Rappel de la distinction entre PowerShell (pour `wsl`) et Linux (pour les commandes natives) |

---

### 6. Prochaines étapes (recommandations)

- **Dockeriser l’API `portfolio-auth-api`** (FastAPI) :
  - Rédiger un `Dockerfile`.
  - Créer un `docker-compose.yml` pour associer l’API à une base PostgreSQL.
- **Approfondir** :
  - Gestion des volumes Docker.
  - Variables d’environnement et fichiers `.env`.
  - Réseaux Docker.

---

### 7. Annexes

**Fichier produit :** `commande_linux_devops_p001.md`  
**Emplacement :** `~/projects/portfolio-auth-api/commande_linux_devops_p001.md`  
**Contenu :** récapitulatif des commandes utilisées, organisé par thème (WSL, utilisateurs, paquets, Docker, dépôts) avec commentaires explicatifs.

---

### 8. Conclusion

L’ensemble des objectifs fixés a été atteint dans les délais impartis. L’approche progressive (planification → validation → exécution → vérification) a permis d’assimiler les concepts tout en évitant les erreurs majeures. L’apprenant a su faire preuve d’autonomie et de rigueur, notamment en diagnostiquant et corrigeant les problèmes rencontrés en cours de route.

**Statut : Mission validée – prêt pour la suite du projet.**

---

*Document rédigé par l’apprenant, avec l’accompagnement d’un expert DevOps, le 26 août 2026.*
