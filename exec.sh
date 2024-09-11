echo "Quelle site souhaitez-vous visiter ?"
echo "1. Introduction à Flask"
echo "2. Informations sur des bouquins"

read rep

# if rep not in [1, 2] ask again
while [ $rep -ne 1 ] && [ $rep -ne 2 ]
do
    echo "Veuillez choisir 1 ou 2"
    read rep
done

source venv/bin/activate

if [ $rep -eq 1 ]
then
    cd Intro
    flask run
else
    cd Bouquins
    flask run
fi