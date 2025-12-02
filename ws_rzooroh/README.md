# Atelier RZooRoH

Presenters:
* Mathieu Gautier
* Tom Druet

Data for this workshop can be downloaded [here](https://filesender.renater.fr/?s=download&token=6f29876f-6be2-423b-bfd0-5f942bbeaa69).

That link will only be available around the time of the workshop.

## Message from the presenters

Les données nécessaires à la réalisation du TD, ainsi qu’un notebook récapitulatif, sont téléchargeables à partir du lien suivant (valide jusqu’au 13/12/2025) :
https://filesender.renater.fr/?s=download&token=6f29876f-6be2-423b-bfd0-5f942bbeaa69
Merci de vous assurer que tous les paquets R requis sont installés. Deux options s’offrent à vous :

i. Méthode recommandée (notamment pour les utilisateurs de Mac récents) : suivre les instructions d’installation détaillées ici (ci-bas de cette page) :
    https://github.com/3nrique0/DevOcGen_workshop/tree/main/ws_rzooroh

i. Utiliser votre propre installation de R : dans ce cas, assurez-vous d’installer les packages suivants ainsi que leurs dépendances :
            -RZooRoH (depuis le CRAN) p.e. avec la commande R install.packages("RZooRoH")
            -SNPRelate (depuis Bioconductor) p.e. avec la commande suivante
                if (!requireNamespace("BiocManager", quietly = TRUE)){install.packages("BiocManager")}
                BiocManager::install("SNPRelate")
            NB: il est recommandé de ne pas mettre à jour tous les packages comme BioConductor vous le proposera surement avec cette méthode

N’hésitez pas à nous contacter en cas de problème d’installation ou de compatibilité.


## To finish the installation of the R libraries

Follow these instructions. Installation can be a bit slow

```
# Install BioC, RZooRoH, SNPRelate
pixi run install_rlibs

# Test installs
pixi run test_rlibs
```

The last command should show no errors and the following statements:

- "Package RZooRoH loaded successfully" + version of the package
- "Package SNPRelate loaded successfully" + version of the package

## Message from the presenters

Les données nécessaires à la réalisation du TD, ainsi qu’un notebook récapitulatif, sont téléchargeables à partir du lien suivant (valide jusqu’au 13/12/2025) :
https://filesender.renater.fr/?s=download&token=6f29876f-6be2-423b-bfd0-5f942bbeaa69
Merci de vous assurer que tous les paquets R requis sont installés. Deux options s’offrent à vous :
    i) Méthode recommandée (notamment pour les utilisateurs de Mac récents) : suivre les instructions d’installation détaillées ici :
https://github.com/3nrique0/DevOcGen_workshop
    ii) Utiliser votre propre installation de R : dans ce cas, assurez-vous d’installer les packages suivants ainsi que leurs dépendances :
            -RZooRoH (depuis le CRAN) p.e. avec la commande R install.packages("RZooRoH")
            -SNPRelate (depuis Bioconductor) p.e. avec la commande suivante
                if (!requireNamespace("BiocManager", quietly = TRUE)){install.packages("BiocManager")}
                BiocManager::install("SNPRelate")
            NB: il est recommandé de ne pas mettre à jour tous les packages comme BioConductor vous le proposera surement avec cette méthode

N’hésitez pas à nous contacter en cas de problème d’installation ou de compatibilité.