input.onButtonPressed(Button.A, function () {
    倒數計時 += 1
    basic.showNumber(倒數計時)
})
input.onButtonPressed(Button.B, function () {
    temp = 倒數計時
    for (let index = 0; index < 倒數計時; index++) {
        temp += -1
        basic.showNumber(temp)
    }
})
let temp = 0
let 倒數計時 = 0
倒數計時 = 0
basic.forever(function () {
	
})
