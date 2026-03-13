async function analyzeCode(){

let code=editor.getValue()

let response=await fetch("http://127.0.0.1:8000/analyze",{

method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({code:code})

})

let data=await response.json()

displayResult(data.analysis)

}


async function explainCode(){

let code=editor.getValue()

let response=await fetch("http://127.0.0.1:8000/explain",{

method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({code:code})

})

let data=await response.json()

document.getElementById("result").innerText=data.explanation.join("\n")

}


async function autoFix(){

let code=editor.getValue()

let response=await fetch("http://127.0.0.1:8000/autofix",{

method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({code:code})

})

let data=await response.json()

let output="Auto Fix Suggestions\n\n"

data.fix.forEach(item=>{
output+="Problem: "+item.problem+"\n"
output+="Fix: "+item.fix+"\n\n"
})

document.getElementById("result").innerText=output

}


async function optimizeCode(){

let code=editor.getValue()

let response=await fetch("http://127.0.0.1:8000/optimize",{

method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({code:code})

})

let data=await response.json()

let output="Optimization Suggestions\n\n"

data.optimization.forEach(item=>{
output+="Issue: "+item.issue+"\n"
output+="Suggestion: "+item.suggestion+"\n\n"
})

document.getElementById("result").innerText=output

}


async function uploadFile(){

let file=document.getElementById("fileInput").files[0]

let formData=new FormData()

formData.append("file",file)

let response=await fetch("http://127.0.0.1:8000/upload",{
method:"POST",
body:formData
})

let data=await response.json()

editor.setValue(data.code)

displayResult(data.analysis)

}


async function analyzeRepo(){

let repo=prompt("Enter GitHub Repository URL")

let response=await fetch("http://127.0.0.1:8000/analyze-repo",{

method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({repo:repo})

})

let data=await response.json()

let explorer=document.getElementById("fileExplorer")

explorer.innerHTML=""

data.files.forEach(file=>{

let div=document.createElement("div")

div.innerText=file.file

div.onclick=function(){
editor.setValue(file.code)
}

explorer.appendChild(div)

})

displayResult(data.report.flatMap(f=>f.issues))

}


function displayResult(issues){

let output="Code Analysis\n\n"

issues.forEach(issue=>{
output+="Issue: "+issue.issue+"\n"
output+="Severity: "+issue.severity+"\n"
output+="Line: "+issue.line+"\n\n"
})

document.getElementById("result").innerText=output

}