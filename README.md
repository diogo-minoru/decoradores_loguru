## 🧠 Decoradores em Python com Loguru para Logging de Funções

### O que são Decoradores?

Decoradores em Python são uma forma elegante de **adicionar funcionalidades a uma função sem modificar seu código original**. Eles funcionam como funções que recebem outra função como argumento e retornam uma nova função com comportamento adicional.

```python
def meu_decorador(func):
    def wrapper(*args, **kwargs):
        print("Algo antes da função")
        resultado = func(*args, **kwargs)
        print("Algo depois da função")
        return resultado
    return wrapper

@meu_decorador
def minha_funcao():
    print("Executando função")

minha_funcao()
# decoradores_loguru
