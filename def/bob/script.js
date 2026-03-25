let colorpicker = document.getElementById('colorpicker');
// let box = document.getElementsByClassName('box');
// console.log(box[0]);
let box = document.querySelector('.box');
colorpicker.addEventListener('input', function(event) {
    // alert("input is changed");
    let color = event.target.value;
    box.style.backgroundColor = color;
});