import streamlit as st
from PIL import Image
from finding_02 import find_menu

st.title("Распознать изображение")

uploaded_file = st.file_uploader("Выберите изображение", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    result_time = find_menu(uploaded_file)
    st.write("Нажмите на кнопку 'Распознать', чтобы увидеть результат")
    if st.button('Распознать'):
        st.write("Затраченное время на распознование = {:.2f} секунд".format(result_time))
        my_image = Image.open('new_image.jpg')
        st.image(my_image, caption='Результат', use_column_width=True)

