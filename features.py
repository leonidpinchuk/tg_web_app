from browser import *

items = document.select('.item')
btn = document.select('.btn')

input_1_btn_class = document.select('.input_1_btn_class')
input_1_items = document.select('.input_1_item')

input_2_btn_class = document.select('.input_2_btn_class')
input_2_items = document.select('.input_2_item')


def change_text(event):
    text_in_field = document['for-input'].select('input')[0].value
    items[0].text = text_in_field

    text_btn_field = document['for-input'].select('input')[0].value
    btn[0].text = text_btn_field

def change_text1(event):
    text_in_field1 = document['input_1'].select('input')[0].value
    input_1_items[0].text = text_in_field1

    text_btn_field1 = document['input_1'].select('input')[0].value
    input_1_btn_class[0].text = text_btn_field1

def change_text2(event):
    text_in_field1 = document['input_2'].select('input')[0].value
    input_2_items[0].text = text_in_field1

    text_btn_field2 = document['input_2'].select('input')[0].value
    input_2_btn_class[0].text = text_btn_field2




def change_text_class(event):
    if 'colored' in items[1].classList:
        items[1].classList.remove('colored')
        items[1].classList.add('colored1')
    elif 'colored1' in items[1].classList:
        items[1].classList.add('colored')
        items[1].classList.remove('colored1')
    else:
        items[1].classList.add('colored')

angle = 30

@bind('#btn-3', 'click')
def rotate(event):
    global angle
    items[2].style.transform = 'rotate({}deg)'.format(angle)
    angle += 30


document['btn-1'].bind('click', change_text)
#document['btn-2'].bind('click', change_text)

document['btn-3'].bind('click', change_text_class)
document['btn-4'].bind('click', change_text_class)


document['input_1_btn'].bind('click', change_text1)
document['input_2_btn'].bind('click', change_text2)
