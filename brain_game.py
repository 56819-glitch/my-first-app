import streamlit as st
import time

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="Brain Benders 🧠💥", page_icon="🤪", layout="centered")

# CSS ตกแต่งให้หน้าเว็บดูน่ารัก สดใส และกวนๆ
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f5;
    }
    .main-title {
        text-align: center;
        color: #ff4b4b;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #555;
        font-size: 1.1rem;
        margin-bottom: 20px;
    }
    .question-box {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 25px;
        border: 2px solid #ffeaa7;
    }
    .question-text {
        font-size: 1.4rem;
        font-weight: bold;
        color: #2d3436;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        font-size: 1.1rem;
        font-weight: bold;
        background-color: #ffffff;
        color: #2d3436;
        border: 2px solid #dfe6e9;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        border-color: #ff7675;
        color: #d63031;
        transform: translateY(-2px);
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# คลังคำถามสุดกวน (เพิ่ม/แก้ไขได้ง่ายๆ ตรงนี้)
# ---------------------------------------------------------
QUESTIONS = [
    {
        "q": "❓ คำถามข้อที่ 1: อะไรอยู่ตรงกลางระหว่าง 'ชลบุรี' กับ 'เชียงใหม่' ?",
        "options": [
            "กทม. / อยุธยา",
            "ตัว 'ง' (ตรงกลางของคำว่า ชลบุรี กับ เชียงใหม่)",
            "เทือกเขาเขาใหญ่",
            "ไม่มีอะไรเลย ถนนล้วนๆ"
        ],
        "answer": 1,
        "explain": "ถูกต้อง! 'ชลบุรี กับ เชียงใหม่' ตัวอักษรตรงกลางคือตัว 'ง' ไงล่ะ!"
    },
    {
        "q": "❓ คำถามข้อที่ 2: มีส้ม 10 ลูก คุณกินไป 3 ลูก คุณจะเหลือส้มกี่ลูก?",
        "options": [
            "7 ลูก (คิดเลขง่ายๆ)",
            "3 ลูก (อยู่ในท้องคุณไง)",
            "0 ลูก (เน่าหมดแล้ว)",
            "10 ลูก (ซื้อมาเติม)"
        ],
        "answer": 1,
        "explain": "ถูกต้อง! คุณกินไป 3 ลูก ส้ม 3 ลูกนั้นก็ยังเป็นของคุณ... แค่อยู่ในท้อง!"
    },
    {
        "q": "❓ คำถามข้อที่ 3: เดือนไหนใน 1 ปี มี 28 วัน?",
        "options": [
            "กุมภาพันธ์ เดือนเดียว",
            "ปีอธิกสุรทินเท่านั้น",
            "มีทุกเดือนนั่นแหละ!",
            "ไม่มีสักเดือน"
        ],
        "answer": 2,
        "explain": "เฉียบ! ทุกเดือนมีอย่างน้อย 28 วันอยู่แล้วมั้ยล่ะ!"
    },
    {
        "q": "❓ คำถามข้อที่ 4: อะไรยิ่งตัดยิ่งยาว?",
        "options": [
            "กระดาษ",
            "เชือก",
            "ถนน",
            "กางเกง"
        ],
        "answer": 2,
        "explain": "ใช่แล้ว! 'ตัดถนน' ยิ่งตัดเส้นทางก็ยิ่งยาวขึ้นไง!"
    },
    {
        "q": "❓ คำถามข้อที่ 5: ปุ่มไหนในหน้านี้ ห้ามกด เด็ดขาด!",
        "options": [
            "ปุ่มนี้แหละกดได้",
            "ห้ามกดปุ่มนี้!",
            "อย่ากดอันนี้นะ",
            "กดปุ่มนี้เพื่อชนะเกม"
        ],
        "answer": 3,
        "explain": "ยินดีด้วย! คุณตกหลุมพรางความอยากเอาชนะจนกดมันจนได้ 55555"
    }
]

# ---------------------------------------------------------
# System State Management
# ---------------------------------------------------------
if 'current_q' not in st.session_state:
    st.session_state.current_q = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'game_finished' not in st.session_state:
    st.session_state.game_finished = False

def restart_game():
    st.session_state.current_q = 0
    st.session_state.score = 0
    st.session_state.game_finished = False

def handle_answer(idx):
    q_data = QUESTIONS[st.session_state.current_q]
    if idx == q_data["answer"]:
        st.session_state.score += 1
        st.toast(f"🎉 {q_data['explain']}", icon="✅")
    else:
        st.toast("💀 ผิดจ้า! โดนสมองแกงเข้าให้แล้ว", icon="❌")
    
    time.sleep(1)
    if st.session_state.current_q + 1 < len(QUESTIONS):
        st.session_state.current_q += 1
    else:
        st.session_state.game_finished = True

# ---------------------------------------------------------
# UI Display
# ---------------------------------------------------------
st.markdown("<h1 class='main-title'>🧠 Brain Benders</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>เกมทดสอบIQ (สติ) สายปั่น — คิดแบบคนปกติเตรียมตัวแพ้!</p>", unsafe_allow_html=True)

if not st.session_state.game_finished:
    q_idx = st.session_state.current_q
    q_data = QUESTIONS[q_idx]

    # Progress Bar
    progress_val = (q_idx) / len(QUESTIONS)
    st.progress(progress_val)
    st.caption(f"ข้อที่ {q_idx + 1} จากทั้งหมด {len(QUESTIONS)} ข้อ")

    # Card คำถาม
    st.markdown(f"""
        <div class="question-box">
            <div class="question-text">{q_data['q']}</div>
        </div>
    """, unsafe_allow_html=True)

    # ตัวเลือก 4 ปุ่ม (จัดเลย์เอาต์ 2x2)
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button(f"A. {q_data['options'][0]}", key="opt_0"):
            handle_answer(0)
            st.rerun()
        if st.button(f"C. {q_data['options'][2]}", key="opt_2"):
            handle_answer(2)
            st.rerun()
            
    with col2:
        if st.button(f"B. {q_data['options'][1]}", key="opt_1"):
            handle_answer(1)
            st.rerun()
        if st.button(f"D. {q_data['options'][3]}", key="opt_3"):
            handle_answer(3)
            st.rerun()

else:
    # หน้าสรุปผลตอนจบเกม
    st.balloons()
    score = st.session_state.score
    total = len(QUESTIONS)
    
    st.markdown("<div class='question-box'>", unsafe_allow_html=True)
    st.subheader("🏁 สรุปผลการประมวลผลสมอง")
    st.markdown(f"### คุณได้คะแนน: **{score} / {total}**")
    
    # คำทำนายตลกๆ ตามคะแนน
    if score == total:
        st.success("🏆 ระดับสมอง: 'อัจฉริยะสายกวน' - สมองคุณล้ำเกินคนธรรมดาไปแล้ว!")
    elif score >= 3:
        st.warning("🤪 ระดับสมอง: 'คนเกือบปกติ' - ปั่นได้บ้าง แต่ยังมีตรรกะมนุษย์หลงเหลืออยู่")
    else:
        st.error("💀 ระดับสมอง: 'ใสซื่อบริสุทธิ์' - โดนเกมแกงทุกข้อ ไปฝึกมาใหม่นะ!")
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("🔄 เล่นอีกรอบ (ขอแก้ตัว!)"):
        restart_game()
        st.rerun()
