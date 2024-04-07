/** PLAN PLUS GRAND **/
function displayLargeImage() {

    const image = document.getElementById('plan');

    const modal = document.createElement('div');
    modal.classList.add('modal');

    const largeImage = document.createElement('img');
    largeImage.src = image.src;

    modal.appendChild(largeImage);

    document.body.appendChild(modal);

    modal.onclick = function() {
        modal.remove();
    }
}


/** BARRE DE RECHERCHE **/
document.getElementById("searchbar").addEventListener("keypress", function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        let trainID = this.value.trim();
        if (trainID !== "") {
            if (!isNaN(trainID)){
                if (trainID >= 1 && trainID <= 12)
                    window.location.href = "/show/" + trainID;
                else {
                    alert('ID inconnue ! Les trains vont de 1 à 12 ')
                }
            } else {
                alert("Il faut rentrer un nombre !")
            }

        }
    }
});