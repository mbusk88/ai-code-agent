import subprocess

def run_agent_workflow(issue_title, issue_body, workspace_path):
    """Orchestrates the AI agent workflow using a sequence of prompts."""

    # 1. Analyze and Plan
    plan_prompt = f"""
    Your first task is to analyze the codebase to solve issue '#{issue_title}: {issue_body}'.
    1. Explore the directory structure and read the README to understand the project's purpose, language, and frameworks.
    2. Identify the existing architectural patterns and coding conventions.
    3. Based on your analysis and the issue, formulate a step-by-step plan for implementation. List the files you will create or modify and explain why.
    Output only the plan.
    """
    print("--- Running Gemini CLI for: PLAN ---")
    plan_result = subprocess.run(["gemini"], input=plan_prompt, capture_output=True, text=True, cwd=workspace_path)
    if plan_result.returncode != 0:
        print("Gemini planning failed:", plan_result.stderr)
        return False
    implementation_plan = plan_result.stdout
    print("Implementation Plan:")
    print(implementation_plan)

    # 2. Execute the Plan
    execute_prompt = f"""
    Excellent. Now, execute the following plan:
    {implementation_plan}
    
    Implement the code changes exactly as described in the plan.
    """
    print("--- Running Gemini CLI for: EXECUTE ---")
    execute_result = subprocess.run(["gemini"], input=execute_prompt, capture_output=True, text=True, cwd=workspace_path)
    if execute_result.returncode != 0:
        print("Gemini execution failed:", execute_result.stderr)
        return False
    print("Gemini execution output:")
    print(execute_result.stdout)

    # 3. Write Tests
    test_prompt = """
    The implementation is complete. Now, write the necessary tests to ensure the changes are correct and well-tested, following the project's existing testing conventions.
    """
    print("--- Running Gemini CLI for: TEST ---")
    test_result = subprocess.run(["gemini"], input=test_prompt, capture_output=True, text=True, cwd=workspace_path)
    if test_result.returncode != 0:
        print("Gemini testing failed:", test_result.stderr)
        return False
    print("Gemini testing output:")
    print(test_result.stdout)

    # 4. Final Review
    review_prompt = """
    Finally, review all your changes. Ensure they are consistent with the project's style. Prepare the final commit message.
    """
    print("--- Running Gemini CLI for: REVIEW ---")
    review_result = subprocess.run(["gemini"], input=review_prompt, capture_output=True, text=True, cwd=workspace_path)
    if review_result.returncode != 0:
        print("Gemini review failed:", review_result.stderr)
        return False
    print("Gemini review output:")
    print(review_result.stdout)

    return True