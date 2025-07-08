## 🧠 Decoradores em Python com Loguru para Logging de Funções

### Introdução

Em Python, **decoradores** são uma forma elegante e poderosa de modificar ou estender o comportamento de funções ou métodos **sem alterar seu código original**. Eles funcionam como "funções que recebem outra função como argumento" e retornam uma nova função com comportamento adicional.

---

### O que são Decoradores?

Sintaxe básica de um decorador simples:

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
```

### Projeto
O projeto de ETL consiste em ler arquivos json e retornar o total do valor vendido para cada categoria de produto.
Também foi adicionado a funcionalidade de criar arquivos de log para cada etapa do processo de ETL, assim, facilitando a detecção de error no código.
