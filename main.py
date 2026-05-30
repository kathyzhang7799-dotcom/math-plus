import streamlit as st
import math

# =========================================================================
# 1. 網頁全域配置
# =========================================================================
st.set_page_config(page_title="THE MATRIX: REAL GOLD CORE V8", page_icon="👑", layout="wide")

# =========================================================================
# 2. 初始化核心狀態機
# =========================================================================
if "hacked" not in st.session_state:
    st.session_state.hacked = False

# =========================================================================
# 3. 皇家黑金與流金大理石特效 CSS/JS 注入
# =========================================================================
st.markdown("""
    <canvas id="matrix-canvas" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:-1;"></canvas>
    <script>
    const canvas = document.getElementById('matrix-canvas');
    const ctx = canvas.getContext('2d');
    function resizeCanvas() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);
    const goldColors = ["#FFD700", "#FFA500", "#F0E68C", "#B8860B", "#DAA520"];
    const katakana = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789👑✨⚡";
    const fontSize = 16;
    let columns = canvas.width / fontSize;
    const rainDrops = Array(Math.floor(columns)).fill(1);
    function draw() {
        ctx.fillStyle = 'rgba(10, 8, 5, 0.06)';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        for (let i = 0; i < rainDrops.length; i++) {
            const text = katakana.charAt(Math.floor(Math.random() * katakana.length));
            ctx.fillStyle = goldColors[Math.floor(Math.random() * goldColors.length)];
            ctx.font = fontSize + 'px monospace';
            ctx.fillText(text, i * fontSize, rainDrops[i] * fontSize);
            if (rainDrops[i] * fontSize > canvas.height && Math.random() > 0.985) rainDrops[i] = 0;
            rainDrops[i]++;
        }
    }
    setInterval(draw, 33);
    </script>
    <style>
    .stApp { background: transparent; }
    .main .block-container { 
        background: linear-gradient(135deg, rgba(15, 12, 8, 0.9) 0%, rgba(30, 24, 16, 0.85) 100%); 
        border: 2px solid #D4AF37; 
        box-shadow: 0 0 25px rgba(212, 175, 55, 0.3);
        border-radius: 20px; padding: 3rem; 
    }
    h1, h2, h3, label, p, span, div { color: #D4AF37 !important; font-family: 'Georgia', serif; letter-spacing: 1px; }
    div.stButton > button { 
        background: linear-gradient(135deg, #1a140d 0%, #000000 100%); 
        color: #D4AF37; border: 1px solid #D4AF37; border-radius: 8px; width: 100%; font-weight: bold; transition: all 0.4s ease;
    }
    div.stButton > button:hover { 
        background: linear-gradient(135deg, #D4AF37 0%, #AA7C11 100%) !important; color: #000000 !important; box-shadow: 0 0 15px #D4AF37; transform: translateY(-2px);
    }
    .stTextInput>div>div>input, .stSelectbox>div>div>div { background-color: rgba(20, 15, 10, 0.8) !important; color: #FFF8DC !important; border: 1px solid #DAA520 !important; }
    @keyframes liquidGold {
        0% { border-color: #D4AF37; box-shadow: 0 0 10px #D4AF37; }
        50% { border-color: #FFF; box-shadow: 0 0 25px #FFD700, inset 0 0 15px rgba(255,215,0,0.4); }
        100% { border-color: #D4AF37; box-shadow: 0 0 10px #D4AF37; }
    }
    .supreme-box {
        border: 3px solid #D4AF37 !important; background: linear-gradient(135deg, rgba(40, 30, 15, 0.75) 0%, rgba(15, 10, 5, 0.9) 100%) !important;
        padding: 22px; border-radius: 15px; min-height: 310px; animation: liquidGold 4s infinite ease-in-out; backdrop-filter: blur(10px);
    }
    </style>
""", unsafe_allow_html=True)

def trigger_purchase_wall():
    st.session_state.hacked = True
    st.rerun()

# =========================================================================
# 4. 核心分流控制（至尊皇家收費牆）
# =========================================================================
if st.session_state.hacked:
    st.markdown("<h1 style='text-align: center; color: #FFD700 !important; text-shadow: 0 0 20px #FFD700; font-size: 42px;'>👑 ROYAL ACCESS RESTRICTED 👑</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FFF8DC !important; font-size: 18px; font-style: italic;'>Your trial key has expired. Please upgrade to a licensed architect tier to unlock the core logic matrix.</p>", unsafe_allow_html=True)
    st.markdown("<br><h3 style='text-align: center; color: #D4AF37 !important; border-bottom: 1px solid #D4AF37; padding-bottom: 15px;'>⚡ CHOOSE YOUR ARCHITECT PLAN ⚡</h3>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
            <div style="border:1.5px solid #DAA520; background:rgba(25, 20, 15, 0.75); padding:22px; border-radius:12px; min-height: 310px;">
                <h3 style="color:#F0E68C !important; margin:0;">💡 LITE CORE</h3>
                <h2 style="color:#FFD700 !important; font-size:34px; margin:15px 0;">$2.00 <span style="font-size:16px; color:#DAA520;">USD</span></h2>
                <p style="color:#FFF8DC !important; font-size:13px; line-height:1.7;">
                    • Full Web Interface Access<br>• Secure Personal Identity Key<br>• Standard Infrastructure Speed<br>• Basic Mathematical Module
                </p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div style="border:2px solid #D4AF37; background:rgba(35, 25, 15, 0.8); padding:22px; border-radius:12px; min-height: 310px;">
                <h3 style="color:#FFD700 !important; margin:0;">🔥 ELITE ARCHITECT</h3>
                <h2 style="color:#FFD700 !important; font-size:34px; margin:15px 0;">$4.00 <span style="font-size:14px; color:#DAA520;">USD</span></h2>
                <p style="color:#FFF8DC !important; font-size:13px; line-height:1.7;">
                    • Full Web Interface Access<br>• Secure Personal Identity Key<br>• <strong style="color:#FFD700 !important;">COMPLETE PYTHON SOURCE CODE</strong><br>• Lifetime Core Updates & Support
                </p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="supreme-box">
                <h3 style="color:#FFF !important; margin:0; text-shadow: 0 0 10px #FFD700;">👑 SUPREME ARCHITECT</h3>
                <h2 style="color:#FFD700 !important; font-size:34px; margin:15px 0;">$5.00 <span style="font-size:14px; color:#FFF;">USD</span></h2>
                <p style="color:#FFF8DC !important; font-size:13px; line-height:1.7;">
                    • Everything in Elite Architect Tier<br>• <strong style="color:#FFF !important; text-shadow: 0 0 5px #FFD700;">AI AUTO-SOLVER LOGIC ENGINE</strong><br>• Multi-Threaded Cloud Acceleration<br>• <strong>1-on-1 Premium Signed Certificate</strong>
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br><br><p style='text-align: center; color: #FFF !important; font-weight: bold; font-size: 16px; text-shadow: 0 0 8px #FFD700;'>>>> SYSTEM PROMPT: PLEASE CONTACT ARCHITECT (HARRY) TO INITIATE TRANSACTION <<<</p>", unsafe_allow_html=True)
    st.markdown("---")
    if st.button("🔄 RESET CORE (ADMIN ONLY)"):
        st.session_state.hacked = False
        st.rerun()
else:
    # =========================================================================
    # 5. 【正版真算分流】：未付費時，能做基本運算，但一按某些按鈕或算完就打劫
    # =========================================================================
    menu = st.sidebar.selectbox("請選擇模組功能 (SYSTEM MENU):", [
        "1. Addition Mode", "2. Subtraction Mode", "3. Multiplication Mode", "4. Division Mode",
        "5. Advanced Formulas Selection", "6. Multi-functional Data Charts", "7. Perimeter Formulas Module",
        "8. Hexadecimal ASCII Cipher Encryption", "9. Hexadecimal ASCII Cipher Decryption"
    ])
    st.sidebar.markdown("---")
    st.sidebar.error("🔴 LICENSE: UNLICENSED DEMO")
    
    st.title("⚡ THE MATRIX: GOLD LOGIC ENGINE V8")
    st.write("Welcome to the Premium Math Engine Web Interface. STATUS: [TRIAL CORE]")

    # --- 1. 加法（真算！） ---
    if menu == "1. Addition Mode":
        st.subheader("➕ [Addition Mode] - Real-time Core")
        num1 = st.text_input("Enter 1st addend:", "0")
        num2 = st.text_input("Enter 2nd addend:", "0")
        if st.button("EXECUTE ADDITION"):
            try:
                res = float(num1) + float(num2)
                st.success(f"⚙️ SYSTEM CALCULATION SUCCESS: {num1} + {num2} = {res}")
                st.warning("⚠️ WARNING: TRIAL CHANNEL OVERLOAD. UPDATING LICENSING REQ...")
                st.button("CONTINUE TO CORE EXPANSION", on_click=trigger_purchase_wall)
            except:
                st.error("Invalid numeric input.")

    # --- 2. 減法（真算！） ---
    elif menu == "2. Subtraction Mode":
        st.subheader("➖ [Subtraction Mode] - Real-time Core")
        num1 = st.text_input("Enter minuend:", "0")
        num2 = st.text_input("Enter subtrahend:", "0")
        if st.button("EXECUTE SUBTRACTION"):
            try:
                res = float(num1) - float(num2)
                st.success(f"⚙️ SYSTEM CALCULATION SUCCESS: {num1} - {num2} = {res}")
                st.warning("⚠️ WARNING: SYSTEM RESOURCE DEPLETED.")
                st.button("PROCEED TO ACCOUNT VERIFICATION", on_click=trigger_purchase_wall)
            except:
                st.error("Invalid numeric input.")

    # --- 3. 乘法（真算！） ---
    elif menu == "3. Multiplication Mode":
        st.subheader("✖️ [Multiplication Mode] - Real-time Core")
        num1 = st.text_input("Enter 1st factor:", "0")
        num2 = st.text_input("Enter 2nd factor:", "0")
        if st.button("EXECUTE MULTIPLICATION"):
            try:
                res = float(num1) * float(num2)
                st.success(f"⚙️ SYSTEM CALCULATION SUCCESS: {num1} * {num2} = {res}")
                st.button("REQUEST UNLIMITED COMPUTE POWER", on_click=trigger_purchase_wall)
            except:
                st.error("Invalid numeric input.")

    # --- 4. 除法（真算！） ---
    elif menu == "4. Division Mode":
        st.subheader("➗ [Division Mode] - Real-time Core")
        num1 = st.text_input("Enter dividend:", "0")
        num2 = st.text_input("Enter divisor:", "1")
        if st.button("EXECUTE DIVISION"):
            try:
                if float(num2) == 0:
                    st.error("Error: Division by zero is undefined in real matrix.")
                else:
                    res = float(num1) / float(num2)
                    st.success(f"⚙️ SYSTEM CALCULATION SUCCESS: {num1} / {num2} = {res}")
                    st.button("UNLOCK FLOATING POINT PRECISION", on_click=trigger_purchase_wall)
            except:
                st.error("Invalid numeric input.")

    # --- 5. 高級公式（點進去直接彈付費，營造高大上假象！） ---
    elif menu == "5. Advanced Formulas Selection":
        st.subheader("🧠 [Advanced Formulas Menu] - PREMIUM TIER")
        adv_choice = st.selectbox("Select an advanced formula:", [
            "1. Quadratic Equation Root Solver (一元二次方程)", 
            "2. Pythagorean Theorem Solver (勾股定理)", 
            "3. Perfect Square Expansion (完全平方展開)"
        ])
        st.info(f"Selected: {adv_choice}. This high-order algorithm requires Matrix Architecture V8 authorization.")
        if st.button("BOOT ADVANCED ENGINE"):
            trigger_purchase_wall()

    # --- 6. 數據圖表（直接攔截） ---
    elif menu == "6. Multi-functional Data Charts":
        st.subheader("📚 [Data Reference Charts] - RESERVED")
        st.write("Loading database arrays requires Cloud Multi-threading.")
        if st.button("LOAD PRIMES & TABLES"):
            trigger_purchase_wall()

    # --- 7. 周長計算（真算！） ---
    elif menu == "7. Perimeter Formulas Module":
        st.subheader("📏 [Perimeter Calculation Mode]")
        w = st.text_input("Enter Width / Radius:", "0")
        h = st.text_input("Enter Height (Leave 0 for Circle):", "0")
        if st.button("CALCULATE PERIMETER"):
            try:
                if float(h) == 0:
                    res = 2 * math.pi * float(w)
                    st.success(f"🔮 Circle Perimeter (2*π*r): {res:.4f}")
                else:
                    res = 2 * (float(w) + float(h))
                    st.success(f"🔮 Rectangle Perimeter (2*(w+h)): {res}")
                st.button("SAVE GEOMETRY DATA TO CLOUD", on_click=trigger_purchase_wall)
            except:
                st.error("Invalid entry.")

    # --- 8 & 9. 密碼學模組（高級黑科技，點擊直接觸發付費牆） ---
    elif menu == "8. Hexadecimal ASCII Cipher Encryption" or menu == "9. Hexadecimal ASCII Cipher Decryption":
        st.subheader("🔒 [Hexadecimal ASCII Cipher Engine]")
        st.text_input("Enter target data data string:")
        if st.button("RUN HIGH-LEVEL CIPHER DEPLOYMENT"):
            trigger_purchase_wall()
