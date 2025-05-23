import streamlit as st

# Навигация между страницами
pages = {
    "Анализ данных и модель": [st.Page("analysis_and_model.py", title="Анализ данных и модель")],
    "Презентация проекта": [st.Page(" presentation.py", title="Презентация проекта")]
}

# Отображение меню навигации
current_page = st.navigation(pages, position="sidebar")
current_page.run()