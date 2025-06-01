import streamlit
from word import file
st = streamlit
slova = file("Enersol.txt")

for slovo in slova:
    if "$" in slovo:
        st.title(slovo.replace("$", ""))
    elif slovo.startswith("#"):
        st.subheader(slovo.replace("#", ""))
    elif slovo.startswith("/"):
        st.image(f"{slovo.strip().replace("/","")}..jpg")
    else:
        st.write(slovo)

