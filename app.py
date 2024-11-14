import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Benhur's Portfolio", page_icon=":tada:", layout="wide")

st.markdown("""
    <style>
   

input[type=message], input[type=email], input[type=text], textarea {
    width: 100%; /* Full width */
    padding: 12px; /* Some padding */ 
    border: 1px solid #ccc; /* Gray border */
    border-radius: 4px; /* Rounded borders */
    box-sizing: border-box; /* Make sure that padding and width stays in place */
    margin-top: 6px; /* Add a top margin */
    margin-bottom: 16px; /* Bottom margin */
    resize: vertical /* Allow the user to vertically resize the textarea (not horizontally) */
  }
  
  /* Style the submit button with a specific background color etc */
  button[type=submit] {
    background-color: #04AA6D;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  /* When moving the mouse over the submit button, add a darker green color */
  button[type=submit]:hover {
    background-color: #45a049;
  }
  
  
  /* Hide Streamlit Branding */
  #MainMenu {visibility: hidden;}
  footer {visibility: hidden;}
  header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)


def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load lottie animations
lottie_coding = "https://lottie.host/830014b5-5a11-4ee1-bedf-d067169a7392/6ABC3Iw8yT.json"
Face = "https://lottie.host/b0331b9a-3ebc-4b45-8314-23fedec4c1a0/dak5mbdjNX.json"
Job = "https://lottie.host/a57e5622-4bd5-41a2-87ed-649a2ea836e2/DDH1oeewlr.json"
Drum = "https://lottie.host/c9c9076c-a2b2-42c1-a715-811024345258/35cOlDCtbJ.json"
Dice = "https://lottie.host/74d3c284-b129-41cb-9c81-a59446f946be/Msuk7q5GWM.json"
Email="https://lottie.host/5150118a-7e30-4af8-ac13-abd84e6704fd/0l9iJLoYI4.json"

# Header
with st.container():
    left_column, right_column = st.columns(2)

    with left_column:
        st.subheader("Hi, I am Benhur Stephen :wave:")
        st.title("AI&ML Engineering Scholar")
        st.write("I am passionate about coding and actively seeking impactful, innovative opportunities. I am committed to expanding my expertise and driving advancements in emerging technologies.")
        st.subheader("Connect with me")
        st.markdown("[LinkedIn](https://www.linkedin.com/in/benhurstephenkumar?lipi=urn%3Ali%3Apage%3Ad_flagship3_messaging_conversation_detail%3BaKQOFmP1S4mhv%2BrCfIByyQ%3D%3D)")
        st.markdown("[GitHub Profile](https://github.com/Benlite777)")
        

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

st.write("---")

# Projects
with st.container():
    st.title("MY PROJECTS")
    st.write("##")

    # Automated Attendance System
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(Face, height=300, key="Face")
    with text_column:
        st.title("Automated Attendance System")
        st.write("I have developed an Automated Attendance System using machine learning and computer vision to recognize faces, log attendance automatically, and streamline attendance processes in educational institutions, reducing time and effort.")
        st.markdown("[Github Repository](https://github.com/Benlite777/Automated-Attendance-System)")

    # JobConnect
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(Job, height=300, key="Job")
    with text_column:
        st.title("Job Connect")
        st.write("I have developed JobConnect, an online job portal that connects job seekers and recruiters, offering features for job search, application submission, and recruitment management.")
        st.markdown("[Github Repository](https://github.com/Benlite777/JobConnect)")

    # Concert Craze
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(Job, height=300, key="Music")
    with text_column:
        st.title("Concert Craze")
        st.write("I have developed ConcertCraze, a dynamic web application built with Django, HTML, CSS, and Bootstrap, enabling users to explore upcoming concerts, browse artist profiles, and stay updated with the latest music events.")
        st.markdown("[Github Repository](https://github.com/Benlite777/JobConnect)")

    # Drum Kit
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(Drum, height=300, key="Drum")
    with text_column:
        st.title("Drum Kit")
        st.write("I have created a drumkit using HTML, CSS, JavaScript, and the DOM, offering a digital version of a physical drum set that can be played with a computer keyboard or mouse.")
        st.markdown("[Github Repository](https://benlite777.github.io/Drum-Kit/)")

    # Dice Game
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st_lottie(Dice, height=300, key="Dice")
    with text_column:
        st.title("Dice Game")
        st.write("I have developed the Dice Game, a web-based game built using HTML, CSS, and JavaScript, allowing users to roll dice and interact with the game through a dynamic, engaging interface.")
        st.markdown("[Github Repository](https://benlite777.github.io/Dice-Game/)")

# Contact Form
    with st.container():
        st.header("Get In Touch With Me")
        st.write("##")

        contact_form = """
        <form action="https://formsubmit.co/benhurskumar@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            <textarea name="message" placeholder="Your Message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st_lottie(Email, height=300, key="Email")
