from selenium.webdriver.common.by import By
from selenium import webdriver
from dash.testing.application_runners import import_app

driver = webdriver.Chrome('chromedriver.exe')  

def test_header_presence(dash_duo):
    app = import_app('app.app')  
    dash_duo.start_server(app)
    
    header = dash_duo.wait_for_element(By.CSS_SELECTOR, 'h1')  
    assert header.text != '', "The header should contain text."

def test_visualization_presence(dash_duo):
    app = import_app('app.app')
    dash_duo.start_server(app)
    
    graph = dash_duo.wait_for_element(By.ID, 'example-graph')  
    assert graph, "The visualization (graph) should be present in the app."

def test_region_picker_presence(dash_duo):
    app = import_app('app.app')
    dash_duo.start_server(app)
    
    dropdown = dash_duo.wait_for_element(By.ID, 'region-dropdown')  
    assert dropdown, "The region picker (dropdown) should be present in the app."
