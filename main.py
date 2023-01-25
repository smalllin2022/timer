def on_button_pressed_a():
    global 倒數計時
    倒數計時 += 1
    basic.show_number(倒數計時)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global temp
    temp = 倒數計時
    for index in range(倒數計時):
        temp += -1
        basic.show_number(temp)
input.on_button_pressed(Button.B, on_button_pressed_b)

temp = 0
倒數計時 = 0
倒數計時 = 0

def on_forever():
    pass
basic.forever(on_forever)
