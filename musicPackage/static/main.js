let images = document.getElementsByTagName('img')
let link = document.getElementsByTagName('a')
let song = document.getElementById('song')
let imagesList = Array.from(images);

for (var i = 0; i < images.length; i++) {
    images[i].addEventListener("click", function(event) {
        // Retrieve the id attribute of the clicked image
        var clickedImageId = event.target.id;
        song.setAttribute('src',`${clickedImageId}`)

        // Do something with the id, for example, log it to the console
        
        console.log("Clicked image ID: " + clickedImageId);
    });
   
}