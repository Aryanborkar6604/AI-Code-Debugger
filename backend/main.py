from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from analyzer import analyze_code, explain_code, auto_fix_code, optimize_code
from git import Repo
import os, shutil

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message":"AI Code Debugger Running"}


@app.post("/analyze")
def analyze(data:dict):
    return {"analysis":analyze_code(data["code"])}


@app.post("/explain")
def explain(data:dict):
    return {"explanation":explain_code(data["code"])}


@app.post("/autofix")
def autofix(data:dict):
    return {"fix":auto_fix_code(data["code"])}


@app.post("/optimize")
def optimize(data:dict):
    return {"optimization":optimize_code(data["code"])}


@app.post("/upload")
async def upload_file(file:UploadFile=File(...)):

    content=await file.read()
    code=content.decode()

    issues=analyze_code(code)

    return {"code":code,"analysis":issues}


@app.post("/analyze-repo")
def analyze_repo(data:dict):

    repo_url=data["repo"]
    repo_path="temp_repo"

    if os.path.exists(repo_path):
        shutil.rmtree(repo_path)

    Repo.clone_from(repo_url,repo_path)

    files_data=[]
    results=[]

    for root,dirs,files in os.walk(repo_path):

        for file in files:

            if file.endswith((".py",".js",".cpp",".java")):

                path=os.path.join(root,file)

                with open(path,"r",errors="ignore") as f:

                    code=f.read()

                    issues=analyze_code(code)

                    files_data.append({"file":file,"code":code})
                    results.append({"file":file,"issues":issues})

    return {"files":files_data,"report":results}