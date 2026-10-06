turno = input("Em que turno você estuda? Digite M-Matutino, V-Vespertino ou N-Noturno: ").strip().upper()

match turno:
    case "M":
        print("Bom dia!")
    case "V":
        print("Boa Tarde!")
    case "N":
        print("Boa Noite!")
    case _:
        print("Valor Inválido")
