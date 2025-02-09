import sys
import os
import subprocess
import shutil
from behave import __main__ as behave_executable

if __name__ == '__main__':
    # allure_results_dir = "allure_result"
    # if os.path.exists(allure_results_dir):
    #     shutil.rmtree(allure_results_dir)
    flags = None
    # flags = '-f allure_behave.formatter:AllureFormatter -o allure_result ./features'
    behave_executable.main(flags)
    # subprocess.run(["allure", "serve", "allure_result"])