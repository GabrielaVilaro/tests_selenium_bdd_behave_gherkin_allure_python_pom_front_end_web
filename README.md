# test_bdd_behave_gherkin_python_front_end_web
Framework test con Selenium, BDD, Behave, Gherkin, Python, Unittest, Allure Framework, Patrón Page Object Model (POM) (Y varias liberías más) en Front-End Web

Inicio 20/07/20

Proyecto con el fin de practicar BDD.

Página a automatizar http://automationpractice.com/index.php

Requisitos:

    Python >= 3.5
    Instalar las dependencias del proyecto: pip3 install -r requirements.txt
    Pycharm
    

**Reporte HTML usando Allure Framework, para correr allure:**

     Lanzar todos los tests:

     behave -f allure_behave.formatter:AllureFormatter -o allure_result_folder ./features
     
     Abrir el reporte HTML:

     allure serve allure_result_folder
 
 <a href="https://ibb.co/9HgWKBp"><img src="https://i.ibb.co/MkS7wKg/Screen-Shot-2020-07-21-at-18-42-23.png" alt="Screen-Shot-2020-07-21-at-18-42-23" border="0"></a>


