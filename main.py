import streamlit as st

# =========================================================================
# 1. 網頁全域配置
# =========================================================================
st.set_page_config(page_title="THE MATRIX: GOLD ARCHITECT V8", page_icon="👑", layout="wide")

# =========================================================================
# 2. 初始化核心狀態機
# =========================================================================
if "hacked" not in st.session_state:
    st.session_state.hacked = False

# =========================================================================
# 3. 皇家黑金與流金大理石數位雨特效（全網頁奢華金黑風格）
# =========================================================================
st.markdown("""
    <canvas id="matrix-canvas" style="position:fixed; top:0; left:0; width:100vw; height:100vh; z-index:-1;"></canvas>
    <script>
    const canvas = document.getElementById('matrix-canvas');
    const ctx = canvas.getContext('2d');
    function resizeCanvas() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);
    
    // 皇家金、香檳金、白金程式碼流混合
    const goldColors = ["#FFD700", "#FFA500", "#F0E68C", "#B8860B", "#DAA520"];
    const katakana = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789👑✨⚡";
    const fontSize = 16;
    let columns = canvas.width / fontSize;
    const rainDrops = Array(Math.floor(columns)).fill(1);
    
    function draw() {
        ctx.fillStyle = 'rgba(10, 8, 5, 0.06)'; // 帶有一點點暖深褐色調的黑，呈現黑大理石底色
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
    /* 全域奢華 UI 注入 */
    .stApp { background: transparent; }
    
    /* 主容器：黑大理石融合描金邊框 */
    .main .block-container { 
        background: linear-gradient(135deg, rgba(15, 12, 8, 0.9) 0%, rgba(30, 24, 16, 0.85) 100%); 
        border: 2px solid #D4AF37; 
        box-shadow: 0 0 25px rgba(212, 175, 55, 0.3);
        border-radius: 20px; 
        padding: 3rem; 
    }
    
    /* 文字全部改成奢華皇家金 */
    h1, h2, h3, label, p, span, div { 
        color: #D4AF37 !important; 
        font-family: 'Georgia', 'Times New Roman', serif; 
        letter-spacing: 1px;
    }
    
    /* 按鈕升級：黑金磨砂質感 */
    div.stButton > button { 
        background: linear-gradient(135deg, #1a140d 0%, #000000 100%); 
        color: #D4AF37; 
        border: 1px solid #D4AF37; 
        border-radius: 8px;
        width: 100%; 
        font-weight: bold; 
        transition: all 0.4s ease;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    }
    div.stButton > button:hover { 
        background: linear-gradient(135deg, #D4AF37 0%, #AA7C11 100%) !important; 
        color: #000000 !important; 
        border: 1px solid #FFF; 
        box-shadow: 0 0 15px #D4AF37;
        transform: translateY(-2px);
    }
    
    /* 輸入框升級：黑曜石磨砂 */
    .stTextInput>div>div>input { 
        background-color: rgba(20, 15, 10, 0.8) !important; 
        color: #FFF8DC !important; 
        border: 1px solid #DAA520 !important; 
        border-radius: 6px;
    }
    .stSelectbox>div>div>div { 
        background-color: rgba(20, 15, 10, 0.8) !important; 
        color: #FFF8DC !important; 
        border: 1px solid #DAA520 !important; 
        border-radius: 6px;
    }
    
    /* 動態流金大理石邊框動畫（用於五刀至尊套餐） */
    @keyframes liquidGold {
        0% { border-color: #D4AF37; box-shadow: 0 0 10px #D4AF37; }
        50% { border-color: #FFF; box-shadow: 0 0 25px #FFD700, inset 0 0 15px rgba(255,215,0,0.4); }
        100% { border-color: #D4AF37; box-shadow: 0 0 10px #D4AF37; }
    }
    .supreme-box {
        border: 3px solid #D4AF37 !important;
        background: linear-gradient(135deg, rgba(40, 30, 15, 0.75) 0%, rgba(15, 10, 5, 0.9) 100%) !important;
        padding: 22px; 
        border-radius: 15px; 
        min-height: 310px; 
        animation: liquidGold 4s infinite ease-in-out;
        backdrop-filter: blur(10px);
    }
    </style>
""", unsafe_allow_html=True)

# 攔截點擊事件
def trigger_purchase_wall():
    st.session_state.hacked = True
    st.rerun()

# =========================================================================
# 4. 核心分流控制（至尊皇家收費牆）
# =========================================================================
if st.session_state.hacked:
    st.markdown("<h1 style='text-align: center; color: #FFD700 !important; text-shadow: 0 0 20px #FFD700; font-size: 42px; font-weight: bold;'>👑 ROYAL ACCESS RESTRICTED 👑</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #FFF8DC !important; font-size: 18px; font-style: italic;'>Your trial key has expired. Please upgrade to a licensed architect tier to unlock the core logic matrix.</p>", unsafe_allow_html=True)
    st.markdown("<br><h3 style='text-align: center; color: #D4AF37 !important; border-bottom: 1px solid #D4AF37; padding-bottom: 15px; letter-spacing: 2px;'>⚡ CHOOSE YOUR ARCHITECT PLAN ⚡</h3>", unsafe_allow_html=True)
    
    # 三套餐橫向佈局
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div style="border:1.5px solid #DAA520; background:rgba(25, 20, 15, 0.75); padding:22px; border-radius:12px; min-height: 310px; backdrop-filter: blur(5px);">
                <h3 style="color:#F0E68C !important; margin:0; font-weight: bold;">💡 LITE CORE</h3>
                <h2 style="color:#FFD700 !important; font-size:34px; margin:15px 0;">$2.00 <span style="font-size:16px; color:#DAA520;">USD</span></h2>
                <p style="color:#FFF8DC !important; font-size:13px; line-height:1.7;">
                    • Full Web Interface Access<br>
                    • Secure Personal Identity Key<br>
                    • Standard Infrastructure Speed<br>
                    • Basic Mathematical Module
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
            <div style="border:2px solid #D4AF37; background:rgba(35, 25, 15, 0.8); padding:22px; border-radius:12px; min-height: 310px; box-shadow: 0 4px 15px rgba(0,0,0,0.6); backdrop-filter: blur(5px);">
                <h3 style="color:#FFD700 !important; margin:0; font-weight: bold;">🔥 ELITE ARCHITECT</h3>
                <h2 style="color:#FFD700 !important; font-size:34px; margin:15px 0;">$4.00 <span style="font-size:14px; color:#DAA520;">USD</span></h2>
                <p style="color:#FFF8DC !important; font-size:13px; line-height:1.7;">
                    • Full Web Interface Access<br>
                    • Secure Personal Identity Key<br>
                    • <strong style="color:#FFD700 !important;">COMPLETE PYTHON SOURCE CODE</strong><br>
                    • Lifetime Core Updates & Support
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        # 使用頂部定義好的 .supreme-box 樣式，帶有動態流金閃爍效果與高級毛玻璃質感
        st.markdown("""
            <div class="supreme-box">
                <h3 style="color:#FFF !important; margin:0; font-weight: bold; text-shadow: 0 0 10px #FFD700;">👑 SUPREME ARCHITECT</h3>
                <h2 style="color:#FFD700 !important; font-size:34px; margin:15px 0; font-weight: bold;">$5.00 <span style="font-size:14px; color:#FFF;">USD</span></h2>
                <p style="color:#FFF8DC !important; font-size:13px; line-height:1.7;">
                    • Everything in Elite Architect Tier<br>
                    • <strong style="color:#FFF !important; text-shadow: 0 0 5px #FFD700;">AI AUTO-SOLVER LOGIC ENGINE</strong><br>
                    • Multi-Threaded Cloud Acceleration<br>
                    • <strong>1-on-1 Premium Signed Certificate</strong>
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br><br><p style='text-align: center; color: #FFF !important; font-weight: bold; font-size: 16px; text-shadow: 0 0 8px #FFD700;'>>>> SYSTEM PROMPT: PLEASE CONTACT ARCHITECT (HARRY) TO INITIATE TRANSACTION <<<</p>", unsafe_allow_html=True)
    
    # 底部偷偷保留的暗門重設按鈕
    st.markdown("---")
    if st.button("🔄 RESET CORE (ADMIN ONLY)"):
        st.session_state.hacked = False
        st.rerun()

else:
    # --- 【未付費狀態】：顯示極度奢華的黑金主介面 ---
    menu = st.sidebar.selectbox("請選擇模組功能 (SYSTEM MENU):", [
        "1. Addition Mode", "2. Subtraction Mode", "3. Multiplication Mode", "4. Division Mode",
        "5. Advanced Formulas Selection", "6. Multi-functional Data Charts", "7. Perimeter Formulas Module",
        "8. Hexadecimal ASCII Cipher Encryption", "9. Hexadecimal ASCII Cipher Decryption"
    ])
    st.sidebar.markdown("---")
    st.sidebar.error("🔴 LICENSE: UNLICENSED DEMO")
    
    st.title("⚡ THE MATRIX: GOLD LOGIC ENGINE V8")
    st.write("Welcome to the Premium Math Engine Web Interface. STATUS: [TRIAL CORE]")

    # 各功能模組渲染
    if menu == "1. Addition Mode":
        st.subheader("➕ [Addition Mode]")
        st.text_input("Enter 1st addend:")
        st.text_input("Enter 2nd addend:")
        if st.button("EXECUTE ADDITION"): trigger_purchase_wall()

    elif menu == "2. Subtraction Mode":
        st.subheader("➖ [Subtraction Mode]")
        st.text_input("Enter minuend:")
        st.text_input("Enter subtrahend:")
        if st.button("EXECUTE SUBTRACTION"): trigger_purchase_wall()

    elif menu == "3. Multiplication Mode":
        st.subheader("✖️ [Multiplication Mode]")
        st.text_input("Enter 1st factor:")
        st.text_input("Enter 2nd factor:")
        if st.button("EXECUTE MULTIPLICATION"): trigger_purchase_wall()

    elif menu == "4. Division Mode":
        st.subheader("➗ [Division Mode]")
        st.text_input("Enter dividend:")
        st.text_input("Enter divisor:")
        if st.button("EXECUTE DIVISION"): trigger_purchase_wall()

    elif menu == "5. Advanced Formulas Selection":
        st.subheader("🧠 [Advanced Formulas Menu]")
        adv_choice = st.selectbox("Select an advanced formula:", [
            "1. Quadratic Equation Root Solver", "2. Perfect Square Expansion", 
            "3. Pythagorean Theorem Unknown Side", "4. Area Formulas Core", "5. Volume Formulas Core"
        ])
        st.text_input("Parameter A:")
        st.text_input("Parameter B:")
        if st.button("CALCULATE FORMULA"): trigger_purchase_wall()

    elif menu == "6. Multi-functional Data Charts":
        st.subheader("📚 [Data Reference Charts]")
        st.selectbox("Select Database Chart:", ["1. Multiplication Table", "2. Prime Numbers Chart"])
        if st.button("LOAD DATABASE CHART"): trigger_purchase_wall()

    elif menu == "7. Perimeter Formulas Module":
        st.subheader("📏 [Perimeter Calculation Mode]")
        st.text_input("Enter dimension data:")
        if st.button("CALCULATE PERIMETER"): trigger_purchase_wall()

    elif menu == "8. Hexadecimal ASCII Cipher Encryption":
        st.subheader("🔒 [Hexadecimal ASCII Cipher Encryption]")
        st.text_input("Enter plaintext:")
        if st.button("RUN ENCRYPTION MODULE"): trigger_purchase_wall()

    elif menu == "9. Hexadecimal ASCII Cipher Decryption":
        st.subheader("🔓 [Hexadecimal ASCII Cipher Decryption]")
        st.text_input("Enter ciphertext:")
        if st.button("RUN DECRYPTION MODULE"): trigger_purchase_wall()
