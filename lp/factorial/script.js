document.getElementById('btn').addEventListener('click',()=>{
    const a = Number(document.querySelector("#a").value)
    y = 0
    x = 1
    while (x<= a){
    ++y;
    x *= y;
    }
    if  (x-a >= a - x/y ){
        x /= y;
        --y
    }
    alert(x)
   })