import PySimpleGUI as gui


def create_alphabet(start: int, end: int):
    alphabet = ""
    for k in range(start, end + 1):
        alphabet += chr(k)
    return alphabet


def create_dict_decode(cesar_key: int):
    start = 32
    end = 126
    size_alphabet = len(create_alphabet(start, end))
    return {chr(start + (i + cesar_key) % size_alphabet): chr(start + i) for i in range(size_alphabet)}


def cesar_decode(message: str, cesar_key: int):
    dict = create_dict_decode(cesar_key)
    message_encode = ""
    for char in message:
        message_encode += dict[char]
    return message_encode


def create_window(title: str, layout: list[list]):
    return gui.Window(title, layout)


def main():
    gui.theme("Reddit")

    cesar_key = 0

    layout = [
        [gui.Text("Chiffrement de César : décryptage")],
        [gui.Text("Message chiffré"), gui.InputText(key="encoded_input")],
        [gui.Text("Clé :"), gui.Text(str(cesar_key), key="display_key")],
        [gui.Text("Message décrypté :"), gui.Text(size=(40, 1), key="display_message")],
        [gui.Button("<"), gui.Button(">"), gui.Button("Quitter", button_color="#DD0000")]
    ]

    window = create_window("Chiffrement de César", layout)

    while True:
        event, values = window.read()

        if event == gui.WIN_CLOSED or event == "Quitter":
            break

        if event == "<" and cesar_key > 0:
            cesar_key -= 1
            window["display_key"].update(str(cesar_key))
            message_encode = values["encoded_input"]
            message_decode = cesar_decode(message_encode, cesar_key)
            window["display_message"].update(message_decode)
        if event == ">":
            cesar_key += 1
            window["display_key"].update(str(cesar_key))
            message_encode = values["encoded_input"]
            message_decode = cesar_decode(message_encode, cesar_key)
            window["display_message"].update(message_decode)


    window.close()


if __name__ == "__main__":
    main()
