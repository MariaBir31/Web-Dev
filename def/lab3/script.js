let count = 0;

const counterVal = document.getElementById('counter-value');
const decrease = document.getElementById('decrease');
const reset = document.getElementById('reset');
const increase = document.getElementById('increase');

function updateDisplay(){
    counterVal.textContent = count;

    if(count > 0){
        counterVal.style.color = 'green';
    } else if (count < 0){
        counterVal.style.color = 'red';
    } else {
        counterVal.style.color = 'black';
    }
}

increase.addEventListener('click', function(){
    count = count + 1;
    updateDisplay();
});

reset.addEventListener('click', function(){
    count = 0;
    updateDisplay();
});

decrease.addEventListener('click', function(){
    count = count - 1;
    updateDisplay();
});
