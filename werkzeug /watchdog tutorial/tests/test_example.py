import pytest
from src.example import add, subtract  # Adjusting import to match directory structure

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(1, 1) == 0
    assert subtract(1, -1) == 2



# !(venv) bee-ams@ams-development:~/Development/Flask/werkzeug /watchdog tutorial/tests$ ls
# ? __init__.py  __pycache__  test_example.py
# ! (venv) bee-ams@ams-development:~/Development/Flask/werkzeug /watchdog tutorial/tests$ pytest test_example.py 
# =========================================================================== test session starts ============================================================================
# platform linux -- Python 3.10.12, pytest-8.3.3, pluggy-1.5.0
# rootdir: /home/bee-ams/Development/Flask/werkzeug /watchdog tutorial/tests
# collected 2 items                                                                                                                                                          

# test_example.py ..                                                                                                                                                   [100%]

# ============================================================================ 2 passed in 0.00s =============================================================================
# (venv) bee-ams@ams-development:~/Development/Flask/werkzeug /watchdog tutorial/tests$ 

