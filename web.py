import streamlit
from word import file
st = streamlit
slova = file("Enersol.txt")
# toto je nayov v kornom rohu

# podnatpis

for slovo in slova:
    if "$" in slovo:
        st.title(slovo.replace("$", ""))
    elif slovo.startswith("#"):
        st.subheader(slovo.replace("#", ""))
    else:
        st.write(slovo)

# kontext
