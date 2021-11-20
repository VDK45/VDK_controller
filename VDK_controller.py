import pygame
import os
import sys
import webbrowser
import socket
import pyperclip



try:
    file = open('ip_server.txt', 'r')
    line = file.readline()
    file.close()
    ip = line
    print(f'Connecting to: {ip}')
except FileNotFoundError:
    ip = 'vdk45.ddns.net'   # Менять


def client_send(mes):
    global ip
    mes = mes.encode('utf-8')
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((ip, 4545))
        sock.send(mes)  # send byte
    except (TimeoutError, OSError) as err:
        print("Не удалось установить соединение.")
        print("Проверьте IP адрес!")
        sock.close()
        ip_server()
    sock.close()


def test():
    print('Conecting to server')
    client_send('Test connect')
    print(f'Connected to ip {ip}')


def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


icon_win = resource_path('img/icon.png')
pygame.display.set_icon(pygame.image.load(icon_win))

# game option
FPS = 15
white = (255, 255, 255)
black = (0, 0, 0)
gray = (120, 120, 120)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

pygame.init()
pygame.font.init()
shrift = resource_path('font/comicsansms3.ttf')
my_font = pygame.font.Font(shrift, 30)
win = pygame.display.set_mode((750, 940))  # Размер окна
pygame.display.set_caption("VDK controller")  # Название окна
pygame.font.init()
tf2build_font1 = resource_path('font/tf2build.ttf')
tf2secondary_font1 = resource_path('font/tf2secondary.ttf')
smallfon = pygame.font.Font(tf2build_font1, 18)
myfont = pygame.font.Font(tf2build_font1, 16)
font_menu = pygame.font.Font(tf2build_font1, 30)
font2 = pygame.font.Font(tf2build_font1, 50)
clock = pygame.time.Clock()


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def ip_server():
    global FPS
    global ip
    click = False
    win = pygame.display.set_mode((750, 940))
    font = pygame.font.Font(tf2build_font1, 30)
    # clock = pygame.time.Clock()
    input_box = pygame.Rect(100, 150, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    ok_text = ''

    while True:
        win.fill(gray)

        # button_my_ip
        mx, my = pygame.mouse.get_pos()
        button_my_ip = pygame.Rect(50, 500, 350, 50)
        if button_my_ip.collidepoint((mx, my)):
            if click:
                print('VDK45 IP')
                ip = 'vdk45.ddns.net'
                f = open('ip_server.txt', 'w+')
                f.write(f'{ip}')
                f.close()
                joystick()
        pygame.draw.rect(win, blue, button_my_ip)
        click = False

        keys_pres = pygame.key.get_pressed()
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if keys_pres[pygame.K_ESCAPE]:
                main_menu()
            if even.type == pygame.MOUSEBUTTONDOWN:
                if button_my_ip.collidepoint(even.pos):
                    if even.button == 1:
                        click = True
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(even.pos):
                    ip = pyperclip.paste()  # Paste copy
                    text_hind = ''
                    f = open('ip_server.txt', 'w+')
                    f.write(f'{ip}')
                    f.close()
                    # Toggle the active variable.
                    active = not active
                    ok_text = 'Reset app!'
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if even.type == pygame.KEYDOWN:
                if even.key == pygame.K_RETURN:
                    f = open('ip_server.txt', 'w+')
                    f.write(f'{ip}')
                    f.close()
                    print(ip)
                    ip = ''
                    ok_text = 'Reset app!'
                elif even.key == pygame.K_BACKSPACE:
                    ip = ip[:-1]
                else:
                    ip += even.unicode
                    ok_text = 'Reset app!'

        # Render the current text.
        txt_surface = font.render(ip, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        win.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(win, color, input_box, 2)
        draw_text('VDK45 offline. Try again:', font, (0, 0, 0), win, 50, 50)
        draw_text('Введите ip стримера', font, (0, 0, 0), win, 50, 90)
        draw_text('И перезагрузить программу!', font, (0, 0, 0), win, 50, 250)
        draw_text(ok_text, font, red, win, 50, 300)
        draw_text('Connect to VDK45', font, white, win, 80, 515)
        draw_text('игра выключена', font, white, win, 50, 415)
        draw_text('или VDK45 Не в сети ', font, white, win, 50, 460)
        draw_text('IP:', font, (0, 0, 0), win, 50, 155)

        pygame.display.update()
        clock.tick(FPS)


def joystick():
    test()
    win = pygame.display.set_mode((750, 400))
    global FPS
    click = False
    while True:
        win.fill(gray)
        mx, my = pygame.mouse.get_pos()

        button_w = pygame.Rect(150, 50, 100, 100)
        button_s = pygame.Rect(150, 250, 100, 100)
        button_a = pygame.Rect(50, 150, 100, 100)
        button_d = pygame.Rect(250, 150, 100, 100)
        button_b = pygame.Rect(450, 120, 100, 100)
        button_p = pygame.Rect(350, 280, 80, 50)
        button_space = pygame.Rect(490, 250, 200, 100)

        if button_w.collidepoint((mx, my)):
            if click:
                print('Button W')
        if button_s.collidepoint((mx, my)):
            if click:
                print('Button S')
        if button_a.collidepoint((mx, my)):
            if click:
                print('Button A')
        if button_d.collidepoint((mx, my)):
            if click:
                print('Button D')
        if button_b.collidepoint((mx, my)):
            if click:
                print('Button B')
        if button_p.collidepoint((mx, my)):
            if click:
                print('Pause')
        if button_space.collidepoint((mx, my)):
            if click:
                print('Space')
        pygame.draw.rect(win, blue, button_w)
        pygame.draw.rect(win, blue, button_s)
        pygame.draw.rect(win, blue, button_a)
        pygame.draw.rect(win, blue, button_d)
        pygame.draw.rect(win, blue, button_p)
        pygame.draw.rect(win, blue, button_space)
        pygame.draw.rect(win, gray, button_b)
        pygame.draw.circle(win, blue, (500, 170), 50)
        click = False
        keys_pres = pygame.key.get_pressed()
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if keys_pres[pygame.K_ESCAPE]:
                main_menu()
            if even.type == pygame.KEYDOWN:
                if even.key == pygame.K_a:
                    client_send('!left')
                    print('a')
                elif even.key == pygame.K_d:
                    client_send('!right')
                    print('d')
                elif even.key == pygame.K_s:
                    client_send('!down')
                    print('s')
                elif even.key == pygame.K_w:
                    client_send('!up')
                    print('w')
                elif even.key == pygame.K_b:
                    client_send('!shoot')
                    print('B')
                elif even.key == pygame.K_p:
                    client_send('!pause')
                    print('Pause')
                elif even.key == pygame.K_SPACE:
                    client_send('!jump')
                    print('space')

            # Key up
            if even.type == pygame.KEYUP:
                if even.key == pygame.K_a:
                    client_send('#left')
                elif even.key == pygame.K_d:
                    client_send('#right')
                elif even.key == pygame.K_s:
                    client_send('#down')
                elif even.key == pygame.K_w:
                    client_send('#up')
                elif even.key == pygame.K_b:
                    client_send('#shoot')
                elif even.key == pygame.K_p:
                    client_send('#pause')
                elif even.key == pygame.K_SPACE:
                    client_send('#jump')

            if keys_pres[pygame.K_ESCAPE]:
                main_menu()

            # Mouse controls
            if even.type == pygame.MOUSEBUTTONDOWN:
                if button_w.collidepoint(even.pos):
                    if even.button == 1:
                        click = True
                        client_send('!up')
                if button_s.collidepoint(even.pos):
                    if even.button == 1:
                        click = True
                        client_send('!down')
                if button_a.collidepoint(even.pos):
                    if even.button == 1:
                        click = True
                        client_send('!left')
                if button_d.collidepoint(even.pos):
                    if even.button == 1:
                        click = True
                        client_send('!right')
                if button_b.collidepoint(even.pos):
                    if even.button == 1:
                        click = True
                        client_send('!shoot')
                if button_p.collidepoint(even.pos):
                    if even.button == 1:
                        click = True
                        client_send('!pause')
                if button_space.collidepoint(even.pos):
                    if even.button == 1:
                        click = True
                        client_send('!jump')

            if even.type == pygame.MOUSEBUTTONUP:
                if button_w.collidepoint(even.pos):
                    if even.button == 1:
                        click = False
                        client_send('#up')
                if button_s.collidepoint(even.pos):
                    if even.button == 1:
                        click = False
                        client_send('#down')
                if button_a.collidepoint(even.pos):
                    if even.button == 1:
                        click = False
                        client_send('#left')
                if button_d.collidepoint(even.pos):
                    if even.button == 1:
                        click = False
                        client_send('#right')
                if button_b.collidepoint(even.pos):
                    if even.button == 1:
                        click = False
                        client_send('#shoot')
                if button_p.collidepoint(even.pos):
                    if even.button == 1:
                        click = False
                        client_send('#pause')
                if button_space.collidepoint(even.pos):
                    if even.button == 1:
                        click = False
                        client_send('#jump')

            if even.type == pygame.MOUSEBUTTONUP:
                click = False
                client_send('')

        draw_text('w', font_menu, white, win, 185, 85)
        draw_text('s', font_menu, white, win, 185, 285)
        draw_text('a', font_menu, white, win, 85, 185)
        draw_text('d', font_menu, white, win, 285, 185)
        draw_text('Space', font_menu, white, win, 540, 285)
        draw_text('B', font_menu, white, win, 490, 160)
        draw_text('P', font_menu, white, win, 380, 290)
        pygame.display.update()
        clock.tick(FPS)


def main_menu():
    global FPS
    click = False
    win = pygame.display.set_mode((750, 940))
    while True:

        win.fill(gray)

        mx, my = pygame.mouse.get_pos()

        button_3 = pygame.Rect(50, 100, 300, 50)
        button_2 = pygame.Rect(50, 200, 250, 50)
        button_1 = pygame.Rect(50, 300, 300, 50)
        button_4 = pygame.Rect(50, 500, 150, 30)
        button_5 = pygame.Rect(50, 560, 300, 30)
        if button_1.collidepoint((mx, my)):
            if click:
                print('Next version')
        if button_2.collidepoint((mx, my)):
            if click:
                print('Button_2')
        if button_3.collidepoint((mx, my)):
            if click:
                print('Button_3')
        if button_4.collidepoint((mx, my)):
            if click:
                print('Donation')
                webbrowser.open('https://www.donationalerts.com/r/vdk45')
        if button_5.collidepoint((mx, my)):
            if click:
                print('download')
                webbrowser.open('https://cloud.mail.ru/public/VX9G/PwVvRWGoF')
        pygame.draw.rect(win, gray, button_1)
        pygame.draw.rect(win, (20, 120, 120), button_2)
        pygame.draw.rect(win, (20, 120, 120), button_3)
        pygame.draw.rect(win, (255, 120, 0), button_4)
        pygame.draw.rect(win, blue, button_5)
        click = False
        keys_pres = pygame.key.get_pressed()
        for even in pygame.event.get():
            if even.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if keys_pres[pygame.K_ESCAPE]:
                joystick()
            if even.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(even.pos):
                    if even.button == 1:
                        click = True
                        print('Play')
                if button_2.collidepoint(even.pos):
                    if even.button == 1:
                        click = True
                        ip_server()
                if button_3.collidepoint(even.pos):
                    if even.button == 1:
                        click = True
                        joystick()
                if button_4.collidepoint(even.pos):
                    if even.button == 1:
                        click = True
                if button_5.collidepoint(even.pos):
                    if even.button == 1:
                        click = True
        draw_text('VDK controller', font_menu, (255, 255, 255), win, 75, 110)
        draw_text('VDK IP', font_menu, (255, 255, 255), win, 80, 215)
        draw_text('', font_menu, (255, 255, 255), win, 80, 315)
        draw_text('Support me', smallfon, (255, 255, 255), win, 65, 508)
        draw_text('Download vdk controller', smallfon, (255, 255, 255), win, 63, 569)
        draw_text('version v.1.0.1', smallfon, (255, 255, 255), win, 500, 850)
        pygame.display.update()
        clock.tick(FPS)


# test()
joystick()
