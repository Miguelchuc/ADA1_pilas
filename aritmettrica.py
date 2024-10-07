class operaciones:
    def post(self, expresion):
        pila = []
        op = set(['+', '-', '*', '/'])

        for i in expresion.split():
            if i not in op:
            
                pila.append(float(i))
            else:
            
                b = pila.pop()
                a = pila.pop()
                
                if i == '+':
                    pila.append(a + b)
                elif i == '-':
                    pila.append(a - b)
                elif i == '*':
                    pila.append(a * b)
                elif i == '/':
                    pila.append(a / b)

        return pila[0]
    

    def pref(self, expresion):
        pila = []
        op = set(['+', '-', '*', '/'])

        
        for i in reversed(expresion.split()):
            if i not in op:
                pila.append(float(i))
            else:
                a = pila.pop()
                b = pila.pop()
                if i == '+':
                    pila.append(a + b)
                elif i == '-':
                    pila.append(a - b)
                elif i == '*':
                    pila.append(a * b)
                elif i == '/':
                    pila.append(a / b)

        return pila[0]



result= operaciones()

pf = "3  4 + 2 * 7 + 9 "
resu = result.post (pf)
print("Resultado de la expresión posfija:", resu)

ef = "+ * 2 4  5 "
resultado = result.pref(ef)
print("Resultado de la expresión prefija:", resultado)
