#this is for seatwork 2 2nd quarter
from pyscript import display, document

def calculate_grade(e):
    m = float(document.getElementById('math').value)
    s = float(document.getElementById('science').value)
    en = float(document.getElementById('english').value)
    ss = float(document.getElementById('social_studies').value)
    avg = (m + s + en + ss) / 4
    display(f'Average: {avg}')