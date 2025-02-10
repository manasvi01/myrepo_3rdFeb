# PetStore Swagger API regression pack
3 regression features created as follows:
Pet.feature
Store.feature
User.feature

There are 4 step definition files as follows:
Pets.Py - for executing steps in Pet.feature file
Store.py - for executing steps in Store.feature file
User.py - for executing steps in User.feature file
Common.py - for executing common steps in all feature files

test_config_pet_store.json file - this has all the test data used in regression pack. 

allure_result folder - for generating allure reports

Test_Data_Extractor.py file for extracting test data from test_config_pet_store.json file

environment.py file

Please run RunBehave file to execute feature files - @wipmanasvi tag is used for all the features

if flag is set to "-f allure_behave.formatter:AllureFormatter -o allure_result ./features" then allure results will get generated
Please use command - allure serve (path to allure results folder)
to generate reports

if flag is set to None, Then allure result will not get generated