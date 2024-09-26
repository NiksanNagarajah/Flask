#!/bin/bash                                                                     

echo "Quelle site souhaitez-vous visiter ?"
echo "1. Introduction à Flask"
echo "2. Informations sur des bouquins"
echo "3. Informations sur des bouquins à l'aide de BD"

read rep

# if rep not in [1, 2] ask again
while [ $rep -ne 1 ] && [ $rep -ne 2 ] && [ $rep -ne 3 ]
do
    echo "Veuillez choisir 1 ou 2"
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
else
    cd 3.SQLAlchemy
    flask run
fi