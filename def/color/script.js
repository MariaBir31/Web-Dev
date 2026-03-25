let colorpicker = document.getElementById('colorpicker');
let box = document.querySelector('.box');

colorpicker.addEventListener('input', function(event){
    let color = event.target.value;
    
    box.style.backgroundColor = color;
});