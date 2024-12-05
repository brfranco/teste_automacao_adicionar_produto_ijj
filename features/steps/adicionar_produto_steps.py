from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que estou na página de login')
def step_impl(context):
    context.driver.get('https://projetofinal.jogajuntoinstituto.org/')
    print("Navegou para a página de login")

@when('eu insiro credenciais válidas')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.NAME, 'email'))
    ).send_keys('brfranco@gmail.com')
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.ID, 'outlined-adornment-password'))
    ).send_keys('wonzuh-xutgoc-Pyfcy7')
    print("Inseriu credenciais válidas")

@when('eu clico no botão de login')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Iniciar sessão')]"))
    ).click()
    print("Clicou no botão de login")

@then('eu devo ser redirecionado para o painel')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(
        EC.url_to_be('https://projetofinal.jogajuntoinstituto.org/products')
    )
    print("Redirecionado para o painel")

@then('eu clico no botão "+ Adicionar"')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Adicionar')]"))
    ).click()
    print("Clicou no botão + Adicionar")

@then('eu preencho o campo "Nome do Produto" com "Camiseta"')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Camiseta...']"))
    ).send_keys('Camiseta')
    print("Preencheu o campo Nome do Produto")

@then('eu preencho o campo "Descrição do Produto" com "Camiseta de algodão"')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Camisa branca tamanho P']"))
    ).send_keys('Camiseta de algodão')
    print("Preencheu o campo Descrição do Produto")

@then('eu seleciono a categoria "ROUPAS"')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Roupas']"))
    ).click()
    print("Selecionou a categoria ROUPAS")

@then('eu preencho o campo "Preço" com "29.99"')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.NAME, 'price'))
    ).send_keys('29.99')
    print("Preencheu o campo Preço")

@then('eu adiciono a imagem "camiseta.jpg"')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    ).send_keys('/Users/brfranco/Downloads/camiseta.jpg')
    print("Adicionou a imagem camiseta.jpg")

@then('eu preencho o campo "Frete" com "5.00"')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.NAME, 'shipment'))
    ).send_keys('5.00')
    print("Preencheu o campo Frete")

@then('eu clico no botão "Salvar"')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(
        EC.visibility_of_element_located((By.XPATH, "//button[@type='submit' and text()='ENVIAR NOVO PRODUTO']"))
    )
    WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and text()='ENVIAR NOVO PRODUTO']"))
    ).click()
    print("Clicou no botão Salvar")

@then('eu devo ver uma mensagem de sucesso')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@role='status' and contains(text(), 'Produto enviado com sucesso!!')]"))
    )
    print("Viu a mensagem de sucesso")