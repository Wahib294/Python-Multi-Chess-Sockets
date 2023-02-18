from game.gui import ChessGUI
import PySimpleGUI as sg
import socket
import time
import game.con as con


def main():
    clientsocket = con.singleton(con.connection)

    sg.theme('Python')
    sg.set_options(font="Cambria 15")
    window = ChessGUI('Chess')
    while True:
        if window.board.turn:
            message = clientsocket.recv(4).decode()
            event = (ord(message[0]) - 97, int(message[1]) - 1)
            window.read(timeout=0)
            window.update_board(event)
            event = (ord(message[2]) - 97, int(message[3]) - 1)
            window.read(timeout=0)
            window.update_board(event)
            window.update_status()
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        window.update_board(event)
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        window.update_board(event)
        window.update_status()
        message = ""
        print("reset")
        window.refresh()

    window.close()


if __name__ == '__main__':
    main()
