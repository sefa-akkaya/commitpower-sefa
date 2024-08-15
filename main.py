# Hatalı Python Kodu

def faulty_function(a, b)
    # Parantez eksik, SyntaxError
    result = a + b
    return result

def another_faulty_function(a, b):
    if a > b:
    # Eksik girinti (IndentationError)
    print("a is greater than b")
    else:
    print("b is greater than or equal to a")

def logic_error(x, y):
    # Mantıksal hata: yanlışlıkla çarpma yerine toplama kullanılmış
    return x + y  # Çarpma (*) olmalıydı

def undefined_variable():
    # Tanımsız değişken hatası (NameError)
    print(undeclared_variable)

def division_by_zero():
    # Sıfıra bölme hatası (ZeroDivisionError)
    return 1 / 0

def wrong_return_type():
    # Hatalı dönüş türü
    return "string"  # Bu aslında bir sayı döndürmeliydi
