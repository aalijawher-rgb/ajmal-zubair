
import streamlit as st
import random

st.set_page_config(
    page_title="Quiz Master",
    page_icon="🎯",
    layout="centered"
)

# ------------------ DESIGN ------------------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #10152f, #202b50);
    color: white;
}
h1, h2, h3, p, label {
    color: white !important;
}
.hero {
    text-align: center;
    padding: 25px 10px;
    background: linear-gradient(120deg, #6c45f5, #00bcd4);
    border-radius: 20px;
    margin-bottom: 25px;
}
.hero h1 {
    color: white !important;
    font-size: 36px;
}
.hero p {
    color: white !important;
}
.question-box {
    background: #263253;
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #46547b;
    margin: 15px 0;
}
.stButton button {
    width: 100%;
    border-radius: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ------------------ QUESTIONS ------------------

questions = {
    "English": [
        ("What is the capital of India?",
         ["Mumbai", "New Delhi", "Chennai", "Kolkata"], 1),
        ("Which planet is called the Red Planet?",
         ["Earth", "Venus", "Mars", "Jupiter"], 2),
        ("Who invented the telephone?",
         ["Newton", "Alexander Graham Bell", "Einstein", "Tesla"], 1),
        ("What is 12 × 8?",
         ["88", "96", "108", "86"], 1),
        ("Which is the largest ocean?",
         ["Atlantic", "Indian", "Arctic", "Pacific"], 3)
    ],
    "Malayalam": [
        ("ഇന്ത്യയുടെ തലസ്ഥാനം ഏതാണ്?",
         ["മുംബൈ", "ന്യൂഡൽഹി", "ചെന്നൈ", "കൊൽക്കത്ത"], 1),
        ("ചുവന്ന ഗ്രഹം എന്നറിയപ്പെടുന്നത് ഏത്?",
         ["ഭൂമി", "ശുക്രൻ", "ചൊവ്വ", "വ്യാഴം"], 2),
        ("കേരളത്തിന്റെ സംസ്ഥാന മൃഗം ഏതാണ്?",
         ["കടുവ", "ആന", "സിംഹം", "മാൻ"], 1),
        ("12 × 8 എത്രയാണ്?",
         ["88", "96", "108", "86"], 1),
        ("ഇന്ത്യയുടെ ദേശീയ പക്ഷി ഏതാണ്?",
         ["തത്ത", "മയിൽ", "പ്രാവ്", "കാക്ക"], 1)
    ],
    "Arabic": [
        ("ما عاصمة الهند؟",
         ["مومباي", "نيودلهي", "تشيناي", "كولكاتا"], 1),
        ("ما الكوكب المعروف بالكوكب الأحمر؟",
         ["الأرض", "الزهرة", "المريخ", "المشتري"], 2),
        ("كم عدد أيام الأسبوع؟",
         ["خمسة", "ستة", "سبعة", "ثمانية"], 2),
        ("كم حاصل ضرب 12 × 8؟",
         ["88", "96", "108", "86"], 1),
        ("ما أكبر محيط في العالم؟",
         ["الأطلسي", "الهندي", "المتجمد الشمالي", "الهادئ"], 3)
    ],
    "Hindi": [
        ("भारत की राजधानी क्या है?",
         ["मुंबई", "नई दिल्ली", "चेन्नई", "कोलकाता"], 1),
        ("लाल ग्रह किसे कहा जाता है?",
         ["पृथ्वी", "शुक्र", "मंगल", "बृहस्पति"], 2),
        ("एक सप्ताह में कितने दिन होते हैं?",
         ["पाँच", "छह", "सात", "आठ"], 2),
        ("12 × 8 कितना होता है?",
         ["88", "96", "108", "86"], 1),
        ("भारत का राष्ट्रीय पक्षी कौन है?",
         ["तोता", "मोर", "कबूतर", "कौआ"], 1)
    ]
}

# ------------------ SESSION STATE ------------------

if "started" not in st.session_state:
    st.session_state.started = False

if "index" not in st.session_state:
    st.session_state.index = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "selected" not in st.session_state:
    st.session_state.selected = None

if "finished" not in st.session_state:
    st.session_state.finished = False


def start_quiz():
    st.session_state.started = True
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected = None
    st.session_state.finished = False


def next_question():
    st.session_state.index += 1
    st.session_state.answered = False
    st.session_state.selected = None

    if st.session_state.index >= len(
        st.session_state.quiz_questions
    ):
        st.session_state.finished = True


# ------------------ HEADER ------------------

st.markdown("""
<div class="hero">
    <h1>🎯 QUIZ MASTER</h1>
    <p>🌍 Learn • Think • Challenge Yourself</p>
    <p>One Quiz. Four Languages. Endless Learning!</p>
</div>
""", unsafe_allow_html=True)

# ------------------ HOME PAGE ------------------

if not st.session_state.started:

    st.subheader("🚀 Welcome to Quiz Master!")
    st.write("Choose your language and test your knowledge.")

    language = st.selectbox(
        "🌐 Select Quiz Language",
        ["English", "Malayalam", "Arabic", "Hindi"]
    )

    count = st.selectbox(
        "📝 Number of Questions",
        [5],
        format_func=lambda x: f"{x} Questions"
    )

    st.info("🏆 Score points by choosing the correct answers.")

    if st.button("🚀 START QUIZ", type="primary"):
        st.session_state.language = language
        st.session_state.quiz_questions = random.sample(
            questions[language],
            min(count, len(questions[language]))
        )
        start_quiz()
        st.rerun()

# ------------------ QUIZ PAGE ------------------

elif not st.session_state.finished:

    quiz = st.session_state.quiz_questions
    index = st.session_state.index
    question, options, correct = quiz[index]

    st.progress((index + 1) / len(quiz))

    col1, col2 = st.columns(2)
    col1.metric("Question", f"{index + 1}/{len(quiz)}")
    col2.metric("Current Score", st.session_state.score)

    st.markdown(
        f'<div class="question-box"><h3>❓ {question}</h3></div>',
        unsafe_allow_html=True
    )

    selected = st.radio(
        "Choose your answer:",
        options,
        index=None,
        key=f"answer_{index}",
        disabled=st.session_state.answered
    )

    if not st.session_state.answered:
        if st.button("✅ SUBMIT ANSWER", type="primary"):
            if selected is None:
                st.warning("Please select an answer first!")
            else:
                st.session_state.selected = selected
                st.session_state.answered = True

                if options.index(selected) == correct:
                    st.session_state.score += 1

                st.rerun()

    else:
        if options.index(st.session_state.selected) == correct:
            st.success("🎉 Correct answer! Well done!")
        else:
            st.error("❌ Incorrect answer!")

        st.info(f"Correct answer: {options[correct]}")

        if st.button(
            "🏁 SEE RESULTS"
            if index == len(quiz) - 1
            else "➡️ NEXT QUESTION",
            type="primary"
        ):
            next_question()
            st.rerun()

# ------------------ RESULTS PAGE ------------------

else:
    total = len(st.session_state.quiz_questions)
    score = st.session_state.score
    percentage = score / total * 100

    st.balloons()
    st.subheader("🏆 Quiz Completed!")

    st.metric("Your Score", f"{score} / {total}")
    st.metric("Percentage", f"{percentage:.0f}%")

    st.progress(percentage / 100)

    if percentage == 100:
        st.success("🌟 PERFECT SCORE! Amazing!")
    elif percentage >= 60:
        st.success("👏 Great job! Keep learning!")
    else:
        st.warning("💪 Keep practising. You can do it!")

    if st.button("🔄 PLAY AGAIN", type="primary"):
        st.session_state.started = False
        start_quiz()
        st.session_state.started = False
        st.rerun()

    if st.button("🏠 HOME"):
        st.session_state.started = False
        st.session_state.finished = False
        st.rerun()

st.markdown("---")
st.caption("🎯 Quiz Master | Powered by Python & Streamlit")
