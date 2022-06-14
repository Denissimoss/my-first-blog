let btn_one = document.getElementById("1");
let btn_two = document.getElementById("2");
let span_one = document.getElementById("11");
let span_two = document.getElementById("22");
let count_one = 0;
let count_two = 0;
span_one.innerHTML = count_one;
span_two.innerHTML = count_two;
function change_one() {
    count_one++;
    if (count_two <= 1 & count_two == 0) {
            span_one.innerHTML = count_one;
    }
    else{
        alert("Вы уже проголосовали");
    }
}
function change_two() {
    count_two++;
    if (count_two <= 1 & count_one==0) {
        span_two.innerHTML = count_two;
    }
    else{
        alert("Вы уже проголосовали");
    }   
    // span_two.innerHTML = count_two;
}