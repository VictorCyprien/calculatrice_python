# Calculatrice Python
Application de calculatrice en Python

## Lancer l'application
Depuis un terminal :
* `git clone https://github.com/VictorCyprien/calculatrice_python.git`
* `cd calculatrice_python/`

On crée un virtualenv
* `virtualenv venv`
* __Windows__
    * `source venv/Scripts/activate`
* __Linux__
    * `source venv/bin/activate`

Puis on installe les librairies
* `pip install -r requirements.txt`

## Exécuter l'application avec Python
* `python calculatrice.py`

__NOTE :__ En cas d'erreur d'execution sur Linux, installer la dépendence python3.8-tk sur un autre terminal
* `sudo apt-get install python3.8-tk`

## Générer l'application
* `pyinstaller.exe --onefile calculatrice.py`

## Emplacement de l'application
* `/dist/calculatrice`

## Exécuter l'application sur Windows
* Double clique sur calculatrice.exe 

## Exécuter l'application sur Windows
* Depuis le dossier dist : `./calculatrice`
