#!/bin/bash                                                                     

echo "Quelle site souhaitez-vous visiter ?"
echo "1. Introduction à Flask"
echo "2. Informations sur des bouquins"
echo "3. Informations sur des bouquins à l'aide de BD"
echo "4. Formulaire"
echo "5. Ajout de fonctionnalités"

read rep

# if rep not in [1, 2] ask again
while [ $rep -ne 1 ] && [ $rep -ne 2 ] && [ $rep -ne 3 ] && [ $rep -ne 4 ] && [ $rep -ne 5 ]
do
    echo "Veuillez choisir 1, 2, 3, 4 ou 5"
    read rep
done

source venv/bin/activate

if [ $rep -eq 1 ]
then
    cd 1.IntroductionFlask
    flask run
elif [ $rep -eq 2 ]
then
    cd 2.Templates-Bootstrap
    flask run
elif [ $rep -eq 3 ]
then
    cd 3.SQLAlchemy
    flask run
elif [ $rep -eq 4 ]
then
    cd 4.Formulaire
    flask run
elif [ $rep -eq 5 ]
then
    cd 5.Ajout-Fonctionnalites
    flask run
fi