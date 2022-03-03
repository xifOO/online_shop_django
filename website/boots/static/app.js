$(document).ready(function(){
var summ = 0;
$(".app").each(function(){
summ += parseInt($(this).html(), 10);
document.getElementById('summ').innerHTML = summ;
})
console.log(summ)
});