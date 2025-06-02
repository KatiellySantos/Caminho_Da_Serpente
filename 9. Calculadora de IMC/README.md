# 🧮 Calculadora de IMC

Este script calcula o IMC (Índice de Massa Corporal) de uma pessoa, levando em consideração o sexo e a idade, e fornece uma classificação personalizada.

---

## ⚙️ Funcionalidades

- Calcula o IMC com base no peso e altura
- Apresenta a classificação padrão do IMC
- Ajusta a classificação para homens, mulheres e idosos (65+)

---

## 📌 Fórmula Utilizada

IMC = peso / (altura ** 2)

---

## 📊 Classificação do IMC

| IMC               | Classificação           |
|------------------|--------------------------|
| Menor que 18.5   | Abaixo do peso           |
| 18.5 - 24.9      | Peso normal              |
| 25.0 - 29.9      | Sobrepeso                |
| 30.0 - 34.9      | Obesidade grau I         |
| 35.0 - 39.9      | Obesidade grau II        |
| 40.0 ou mais     | Obesidade grau III       |

Além disso:
- Mulheres com IMC < 19 recebem observação especial
- Homens com IMC < 20 também
- Pessoas com 65 anos ou mais recebem ajuste se o IMC estiver entre 22 e 27

---

## ▶️ Como Executar

1. Salve o código como `calculadora_IMC.py`
2. Execute no terminal:
   ```bash
   python calculadora_IMC.py
3. Insira os dados solicitados

💡 Exemplo de Saída

- Digite seu sexo (homem/mulher): mulher
  - Digite sua idade: 70
- Digite seu peso (kg): 65
  - Digite sua altura (m): 1.60
- **Seu IMC é 25.39. Classificação: Sobrepeso (IMC considerado adequado para idosos)**



