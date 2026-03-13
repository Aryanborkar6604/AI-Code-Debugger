def analyze_code(code, language=None):

    issues=[]
    lines=code.split("\n")

    for i,line in enumerate(lines,start=1):

        line_lower=line.lower()

        if "while true" in line_lower:

            issues.append({
                "issue":"Possible Infinite Loop",
                "severity":"MEDIUM",
                "line":i,
                "explanation":"Loop condition always true.",
                "suggestion":"Add break condition."
            })

        if line_lower.startswith("for"):

            if i<len(lines):

                next_line=lines[i].strip().lower()

                if next_line.startswith("for"):

                    issues.append({
                        "issue":"Nested Loop Detected",
                        "severity":"LOW",
                        "line":i,
                        "explanation":"Nested loops increase time complexity.",
                        "suggestion":"Optimize algorithm."
                    })

        vulnerabilities={
            "eval(":("Unsafe code execution using eval()","HIGH"),
            "exec(":("Unsafe code execution using exec()","HIGH"),
            "password":("Hardcoded credential detected","HIGH"),
            "select * from":("Possible SQL injection vulnerability","HIGH")
        }

        for pattern,(message,severity) in vulnerabilities.items():

            if pattern in line_lower:

                issues.append({
                    "issue":"Security Vulnerability",
                    "severity":severity,
                    "line":i,
                    "explanation":message,
                    "suggestion":"Secure this code section."
                })

    if not issues:

        issues.append({
            "issue":"No Major Issues",
            "severity":"INFO",
            "line":"-",
            "explanation":"Code appears safe.",
            "suggestion":"No fix required."
        })

    return issues


def explain_code(code):

    lines=code.split("\n")
    explanation=[]

    for line in lines:

        if "for" in line or "while" in line:
            explanation.append("The program uses loops.")

        if "print(" in line:
            explanation.append("The program prints output.")

    explanation.append("Overall Explanation: The program runs sequential instructions.")

    return explanation


def auto_fix_code(code):

    fixes=[]

    if "while true" in code.lower():

        fixes.append({
            "problem":"Infinite Loop",
            "fix":"Add break condition."
        })

    if "eval(" in code.lower():

        fixes.append({
            "problem":"Unsafe eval() usage",
            "fix":"Avoid eval()."
        })

    if "password" in code.lower():

        fixes.append({
            "problem":"Hardcoded password",
            "fix":"Use environment variables."
        })

    if not fixes:

        fixes.append({
            "problem":"No fixes required",
            "fix":"Code appears safe."
        })

    return fixes


def optimize_code(code):

    suggestions=[]

    if "range(len(" in code.lower():

        suggestions.append({
            "issue":"Inefficient Loop",
            "suggestion":"Use direct iteration instead of indexing.",
            "optimized_code":
"""for item in arr:
    print(item)"""
        })

    if not suggestions:

        suggestions.append({
            "issue":"No Optimization Needed",
            "suggestion":"Code already optimized.",
            "optimized_code":""
        })

    return suggestions