document.getElementById('btn').addEventListener('click',()=>{
    const a = +document.querySelector("#a").value
    const b = +document.querySelector("#b").value
    const c = +document.querySelector("#c").value
    if (a + b > c && a + c > b && b + c > a){
        p = (a+b+c)/2;
        alert(Math.sqrt(p*(p-a)*(p-b)*(p-c)))}
    else {
        alert('Треугольник не существует')}
   })