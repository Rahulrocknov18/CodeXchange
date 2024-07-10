import streamlit as st
from google.generativeai import generate_text, configure

st.set_page_config(
    page_title="CodeXchange: AI-Powered Code Translation Tool",
    page_icon=":computer:",
    layout="wide",
)

st.title("CodeXchange: AI-Powered Code Translator Tool")
st.markdown("""<h2>Project Description</h2>
            <p>CodeXchange is an innovative web application designed to streamline code translation and facilitate seamless collaboration among developers working with different programming languages. Whether you're transitioning applications between platforms, collaborating in multilingual teams, or reusing code across projects, CodeXchange empowers developers to effortlessly translate code snippets between various programming languages. Leveraging advanced translation algorithms and syntax analysis, CodeXchange ensures accurate and reliable code conversion while preserving the original functionality and logic. With its intuitive interface and comprehensive language support, CodeXchange revolutionizes the development workflow, enabling teams to work together efficiently, enhance code reusability, and accelerate project delivery.</p>"""
            , unsafe_allow_html = True)

st.markdown("""<h2>Scensrio 1: Platform Transition</h2>
        <p>CodeXchange assists developers in transitioning applications from one platform to another. For instance, a team working on an application written in Python needs to migrate it to Java to leverage Java's robustness and scalability in an enterprise environment. By inputting the Python code snippets and selecting Java as the target language, developers receive accurately translated code that maintains the original functionality, streamlining the migration process and minimizing the risk of introducing errors.</p>"""
        , unsafe_allow_html = True)

st.markdown("""<h2>Scenario 2: Multilingual Collaboration</h2>
        <p>In a collaborative project where team members use different programming languages, CodeXchange facilitates seamless integration by translating code snippets as needed. Suppose one part of the team is proficient in C++ while another prefers Python. Developers can write code in their preferred language and use CodeXchange to translate it, ensuring all team members can work together efficiently without being constrained by language barriers. This enhances productivity and reduces the learning curve associated with adopting new languages.</p>"""
        , unsafe_allow_html = True)

st.markdown("""<h2>Scenario 3: Code Reusability Across Projects</h2>
        <p>CodeXchange promotes code reusability by enabling developers to translate existing code into different languages for new projects. For example, a developer has written a set of utility functions in Java that would be beneficial for a new project being developed in C++. By translating these Java functions into C++ using CodeXchange, the developer can quickly integrate proven code into the new project, saving time and ensuring consistency across different projects.<p>"""
        , unsafe_allow_html = True)
st.header("Code Translation")

code_input = st.text_area("Enter your code snippet:", height=200)
target_language = st.selectbox(
    "Select target language:",
    ("Python", "Java", "C++"),
)

if st.button("Translate Code"):
    with st.spinner("Translating..."):
        if code_input:
            try:
                configure(api_key="AIzaSyC5nwVSrise7ZgA8Xw81lsGWAnbnU4aALY")  # Ensure API key is correct and authorized
                prompt = f"""
                Translate the following code snippet from {code_input.split("\n")[0].split(" ")[0]} to {target_language}:

                {code_input}
                """
                print(prompt)  # Print prompt for debugging purposes
                response = generate_text(
                    model="models/text-bison-001",
                    prompt=prompt,
                    temperature=0.7,
                    max_output_tokens=500,
                )
                print(response)  # Print response for inspection

                # Extract the translated code from the response
                translated_code = response.result
                st.code(translated_code, language=target_language.lower())
            except Exception as e:
                st.error(f"Error during translation: {str(e)}")
        else:
            st.warning("Please enter a code snippet.")
