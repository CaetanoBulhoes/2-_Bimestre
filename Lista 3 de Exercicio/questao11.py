# 11.Escreva um algoritmo para conversão de temperatura. O usuário deve escolher se a conversão será de (1) grau Celsius para Fahrenheit ou de (2) Fahrenheit para Celsius, e em seguida deve entrar com uma temperatura. As fórmulas de conversão estão descritas abaixo:
# F : Temperatura em Fahrenheit; C :Temperatura em Celsius
# Celsius-Fahrenheit: F = (9 * C + 160) / 5
# Fahrenheit-Celsius: C = (F - 32) * (5 / 9);

print("Conversão de temperatura\nCelsius -> Fahrenheit = 1\nFahrenheit -> Celsius = 2")

opcao = int(input("Digite um desses números:"))

while True:
    if opcao == 1:
    
        temp = float(input("Digite a temperatura em °C:"))
        fahrenheit = (9 * temp + 160) / 5

        print(f"Convertendo a temperatura {temp}°C para Fahrenheit fica: {fahrenheit}°F")
        break

    elif opcao == 2:
        temp = float(input("Digite a temperatura em °F:"))
        celsius = (temp - 32) * (5 / 9)

        print(f"Convertendo a temperatura {temp}°F para Celsius fica: {celsius}°C")
        break

    else:
        print("Essa opção não existe")
        break 