import streamlit as st
from google import genai

# Configure Streamlit page
st.set_page_config(
    page_title="🎓 AI Learning Buddy Ketki",
    page_icon="🎓"
)

st.title("🎓 AI Learning Buddy Ketki")

# Create Gemini client
client = genai.Client(
    api_key=st.secrets["GOOGLE_API_KEY"]
)

# User Input
topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"""
            Explain {topic} in simple language suitable for a beginner.
            Use easy words and a real-life example.
            """

        elif option == "Real-Life Example":
            prompt = f"""
            Give one simple real-life example to explain {topic}.
            """

        elif option == "Generate Quiz":
            prompt = f"""
            Create 5 multiple-choice questions on {topic}.

            Each question should have:
            - Four options (A, B, C, D)
            - Correct answer
            - Short explanation
            """

        else:
            prompt = topic

        try:

            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt
            )

            st.success("Response Generated Successfully!")

            st.write(response.text)

        except Exception as e:

            st.error(f"Error: {e}")
