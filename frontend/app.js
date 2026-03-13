async function analyze(){

let code = document.getElementById("code").value;

let response = await fetch("http://127.0.0.1:8000/analyze",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body:JSON.stringify({code:code})
});

let data = await response.json();

document.getElementById("result").innerText =
JSON.stringify(data.analysis,null,2);

}