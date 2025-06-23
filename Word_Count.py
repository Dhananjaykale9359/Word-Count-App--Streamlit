import streamlit as st

# App title
st.title("📝 Word and Character Counter App")

# User input
text_input = st.text_area("Enter your text below:")

# Count words and characters
if text_input:
    words = text_input.split()
    word_count = len(words)
    char_count = len(text_input)

    st.write(f"🔤 **Word Count:** {word_count}")
    st.write(f"🧮 **Character Count (including spaces):** {char_count}")
else:
    st.write("👆 Please enter some text above to see the word and character count.")
