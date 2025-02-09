import sys
import os
import subprocess
import shutil
from behave import __main__ as behave_executable

if __name__ == '__main__':
    allure_results_dir = "allure_result"
    if os.path.exists(allure_results_dir):
        shutil.rmtree(allure_results_dir)
    # flags = None
    flags = '-f allure_behave.formatter:AllureFormatter -o allure_result ./features'
    behave_executable.main(flags)
    subprocess.run(
        [r"C:\Users\avumag\Downloads\allure-2.32.2\allure-2.32.2\bin", "generate", "allure-result", "-o", "allure-report", "--clean"],
        check=True)
    subprocess.run(["allure", "serve", "C:\\Projects\\OldProjects\myrepo_3rdFeb\\allure_result"], shell=True)