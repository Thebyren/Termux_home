from pyfiglet import Figlet
import curses
import pyfiglet
import subprocess
menu = ['inicio','partida','creditos', 'cartas','salir']

cartas=['uno','dos','tres','cuatro']

def draw_text(text):
    if text != None:
        banner=(( colored(pyfiglet.figlet_format(str(text),font='banner', justify='center'), color="blue")))
        return banner

    else:
        return "hola"




def print_menu(stdscr, selected_row_idx):
    stdscr.clear()
    h, w =stdscr.getmaxyx()
    for idx, row in enumerate(menu):
        x = w//2 - len(row)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y,x,row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y,x,row)
    stdscr.refresh()

f = Figlet(font='banner')

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_GREEN)
    current_row_idx = 0
    wind = curses.newwin(25,60, 3,2)


    print_menu(stdscr, current_row_idx)
    while 1:
        key= stdscr.getch()
        stdscr.clear()
        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1

        elif key == curses.KEY_DOWN and current_row_idx < len(menu) -1:
            current_row_idx += 1

        elif key == curses.KEY_ENTER or key in [10,13]:

            wind.clear()
            stdscr.addstr(0,0,",{}".format(menu[current_row_idx]))
            wind.addstr(f.renderText(str("{}".format(menu[current_row_idx]))))
            stdscr.refresh()
            wind.refresh()
            stdscr.getch()

            if current_row_idx == len(menu)-2:
                wind.addstr(0,0,str(cartas))
                stdscr.refresh()
                stdscr.getch()
            elif current_row_idx == len(menu)-1:
                break
        print_menu(stdscr, current_row_idx)
    stdscr.refresh()


curses.wrapper(main)




