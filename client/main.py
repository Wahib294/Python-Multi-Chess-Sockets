from game.gui import ChessGUI
import PySimpleGUI as sg
import game.con as con

s = con.singleton(con.connection)


def main():
    sg.theme('Python')
    sg.set_options(font="Cambria 15")
    window = ChessGUI('Chess')
    while True:
        if not window.board.turn:
            message = s.recv(4).decode()
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
        window.update_status()
        window.refresh()
    window.close()


if __name__ == '__main__':
    main()
