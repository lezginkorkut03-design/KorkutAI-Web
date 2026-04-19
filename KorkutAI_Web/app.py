import streamlit as st
import time

# ─── 1. PAGE CONFIG (TEK VE EN ÜSTTE OLMALI) ──────────────────────────────────
st.set_page_config(
    page_title="KorkutAI | Otonom Sistemler Portalı",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── 2. GOOGLE DOĞRULAMA (GİZLİ MÜHÜR) ────────────────────────────────────────
st.markdown('<meta name="google-site-verification" content="mdeBBR-q7en4diGzZmaNGYBYA6aWSH8Vk48qqvem2KE" />', unsafe_allow_html=True)



# ─── GLOBAL CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Rajdhani:wght@400;500;600;700&family=Orbitron:wght@400;700;900&display=swap');

/* ── Root Variables ── */
:root {
  --bg-deep:    #050810;
  --bg-card:    #0d1117;
  --bg-panel:   #111722;
  --orange:     #ff4d00;
  --orange-glow:#ff6a2a;
  --cyan:       #00e5ff;
  --cyan-dark:  #00b8cc;
  --text-main:  #e8eaf0;
  --text-muted: #7a8499;
  --border:     rgba(0,229,255,0.15);
  --font-head:  'Orbitron', monospace;
  --font-body:  'Rajdhani', sans-serif;
  --font-code:  'Space Mono', monospace;
}

/* ── Global Reset ── */
html, body, [data-testid="stAppViewContainer"] {
  background-color: var(--bg-deep) !important;
  color: var(--text-main) !important;
  font-family: var(--font-body) !important;
}

[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stToolbar"] { display: none !important; }
footer { display: none !important; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
  background: var(--bg-card) !important;
  border-right: 1px solid var(--border) !important;
}
[data-testid="stSidebar"] * { color: var(--text-main) !important; }
[data-testid="stSidebar"] .stRadio label {
  font-family: var(--font-body) !important;
  font-size: 15px !important;
  font-weight: 600 !important;
  letter-spacing: 0.5px;
  padding: 6px 0 !important;
  cursor: pointer;
  transition: color .2s;
}
[data-testid="stSidebar"] .stRadio label:hover { color: var(--cyan) !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg-deep); }
::-webkit-scrollbar-thumb { background: var(--cyan-dark); border-radius: 3px; }

/* ── Headings ── */
h1, h2, h3, h4 {
  font-family: var(--font-head) !important;
  letter-spacing: 1px;
}

/* ── Buttons ── */
.stButton > button {
  background: transparent !important;
  border: 1px solid var(--cyan) !important;
  color: var(--cyan) !important;
  font-family: var(--font-body) !important;
  font-weight: 700 !important;
  font-size: 14px !important;
  letter-spacing: 1.5px !important;
  text-transform: uppercase;
  padding: 10px 22px !important;
  border-radius: 3px !important;
  transition: all .25s !important;
}
.stButton > button:hover {
  background: var(--cyan) !important;
  color: var(--bg-deep) !important;
  box-shadow: 0 0 20px rgba(0,229,255,0.4) !important;
}

/* ── Text Input / Text Area ── */
.stTextInput input, .stTextArea textarea {
  background: var(--bg-panel) !important;
  border: 1px solid var(--border) !important;
  color: var(--text-main) !important;
  font-family: var(--font-code) !important;
  font-size: 13px !important;
  border-radius: 3px !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
  border-color: var(--cyan) !important;
  box-shadow: 0 0 12px rgba(0,229,255,0.25) !important;
}

/* ── Code blocks ── */
.stCode, .stCodeBlock, pre {
  font-family: var(--font-code) !important;
  background: #080c12 !important;
  border: 1px solid var(--border) !important;
  border-radius: 4px !important;
}

/* ── Select / Radio ── */
.stSelectbox select {
  background: var(--bg-panel) !important;
  color: var(--text-main) !important;
  border: 1px solid var(--border) !important;
}

/* ── Divider ── */
hr { border-color: var(--border) !important; }

/* ──────────────────────────────────────────────────────
   CUSTOM COMPONENT CLASSES
────────────────────────────────────────────────────── */

/* Hero */
.hero-section {
  position: relative;
  min-height: 420px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 60px 48px;
  overflow: hidden;
  background: var(--bg-deep);
  border-bottom: 1px solid var(--border);
  margin-bottom: 40px;
}
.hero-bg {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse 70% 60% at 80% 50%, rgba(0,229,255,0.07) 0%, transparent 70%),
    radial-gradient(ellipse 40% 40% at 10% 80%, rgba(255,77,0,0.08) 0%, transparent 60%);
  pointer-events: none;
}
.circuit-overlay {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(0,229,255,0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0,229,255,0.04) 1px, transparent 1px);
  background-size: 40px 40px;
  pointer-events: none;
}
.hero-badge {
  display: inline-block;
  border: 1px solid var(--orange);
  color: var(--orange);
  font-family: var(--font-code);
  font-size: 11px;
  letter-spacing: 3px;
  text-transform: uppercase;
  padding: 4px 12px;
  margin-bottom: 24px;
  width: fit-content;
}
.hero-title {
  font-family: var(--font-head);
  font-size: clamp(28px, 4.5vw, 58px);
  font-weight: 900;
  line-height: 1.08;
  color: #fff;
  margin: 0 0 20px;
  text-shadow: 0 0 60px rgba(255,77,0,0.2);
}
.hero-title .accent { color: var(--orange); }
.hero-sub {
  font-family: var(--font-body);
  font-size: clamp(14px, 1.6vw, 19px);
  font-weight: 500;
  color: var(--text-muted);
  max-width: 680px;
  line-height: 1.7;
  margin: 0 0 36px;
}
.hero-stats {
  display: flex;
  gap: 48px;
  flex-wrap: wrap;
  margin-top: 10px;
}
.stat-item { display: flex; flex-direction: column; gap: 4px; }
.stat-num {
  font-family: var(--font-head);
  font-size: 28px;
  font-weight: 700;
  color: var(--cyan);
}
.stat-label {
  font-family: var(--font-code);
  font-size: 10px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--text-muted);
}
.scan-line {
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, var(--cyan), transparent);
  animation: scan 4s linear infinite;
}
@keyframes scan {
  0%   { top: 0%; opacity: 1; }
  80%  { opacity: 1; }
  100% { top: 100%; opacity: 0; }
}

/* Section */
.section-title {
  font-family: var(--font-head);
  font-size: 22px;
  font-weight: 700;
  color: #fff;
  border-left: 3px solid var(--orange);
  padding-left: 16px;
  margin: 36px 0 20px;
  letter-spacing: 1px;
}
.section-sub {
  font-family: var(--font-code);
  font-size: 11px;
  letter-spacing: 3px;
  color: var(--cyan);
  text-transform: uppercase;
  margin-bottom: 8px;
}

/* Cards */
.card {
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 28px;
  transition: border-color .3s, box-shadow .3s;
  height: 100%;
}
.card:hover {
  border-color: rgba(0,229,255,0.45);
  box-shadow: 0 0 30px rgba(0,229,255,0.08);
}
.card-icon { font-size: 28px; margin-bottom: 14px; }
.card-title {
  font-family: var(--font-head);
  font-size: 14px;
  font-weight: 700;
  color: #fff;
  margin-bottom: 10px;
  letter-spacing: 0.5px;
}
.card-body {
  font-family: var(--font-body);
  font-size: 15px;
  color: var(--text-muted);
  line-height: 1.7;
}

/* Project card */
.proj-card {
  background: var(--bg-panel);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 20px 24px;
  margin-bottom: 14px;
  transition: border-color .3s;
}
.proj-card:hover { border-color: var(--orange); }
.proj-title {
  font-family: var(--font-head);
  font-size: 13px;
  font-weight: 700;
  color: var(--orange);
  letter-spacing: 1px;
  margin-bottom: 8px;
}
.proj-meta {
  font-family: var(--font-code);
  font-size: 11px;
  color: var(--text-muted);
  letter-spacing: 1px;
}

/* Tag */
.tag {
  display: inline-block;
  border: 1px solid var(--cyan);
  color: var(--cyan);
  font-family: var(--font-code);
  font-size: 10px;
  letter-spacing: 1.5px;
  text-transform: uppercase;
  padding: 2px 8px;
  border-radius: 2px;
  margin: 2px 3px 2px 0;
}
.tag.orange { border-color: var(--orange); color: var(--orange); }

/* Timeline */
.timeline-item {
  position: relative;
  padding-left: 32px;
  margin-bottom: 32px;
}
.timeline-item::before {
  content: '';
  position: absolute;
  left: 0; top: 6px;
  width: 10px; height: 10px;
  background: var(--cyan);
  border-radius: 50%;
  box-shadow: 0 0 10px var(--cyan);
}
.timeline-item::after {
  content: '';
  position: absolute;
  left: 4px; top: 20px;
  width: 2px; height: calc(100% + 8px);
  background: var(--border);
}
.timeline-item:last-child::after { display: none; }
.timeline-year {
  font-family: var(--font-code);
  font-size: 11px;
  color: var(--orange);
  letter-spacing: 2px;
  margin-bottom: 6px;
}
.timeline-text {
  font-family: var(--font-body);
  font-size: 15px;
  color: var(--text-muted);
  line-height: 1.6;
}

/* Contact */
.contact-row {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 18px 24px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: 6px;
  margin-bottom: 12px;
}
.contact-icon { font-size: 22px; }
.contact-label {
  font-family: var(--font-code);
  font-size: 11px;
  letter-spacing: 2px;
  color: var(--cyan);
  text-transform: uppercase;
  margin-bottom: 2px;
}
.contact-value {
  font-family: var(--font-body);
  font-size: 16px;
  font-weight: 600;
  color: var(--text-main);
}

/* Sidebar logo */
.sb-logo {
  font-family: var(--font-head);
  font-size: 20px;
  font-weight: 900;
  color: #fff;
  letter-spacing: 2px;
  padding: 16px 0 4px;
  text-align: center;
}
.sb-logo span { color: var(--orange); }
.sb-divider {
  border: none;
  border-top: 1px solid var(--border);
  margin: 12px 0;
}
.sb-section {
  font-family: var(--font-code);
  font-size: 9px;
  letter-spacing: 3px;
  text-transform: uppercase;
  color: var(--text-muted);
  padding: 10px 4px 4px;
}

/* AI Response box */
.ai-response {
  background: var(--bg-panel);
  border: 1px solid var(--border);
  border-left: 3px solid var(--cyan);
  border-radius: 4px;
  padding: 20px 24px;
  font-family: var(--font-body);
  font-size: 16px;
  color: var(--text-main);
  line-height: 1.7;
  margin-top: 14px;
}
.ai-label {
  font-family: var(--font-code);
  font-size: 10px;
  letter-spacing: 2px;
  color: var(--cyan);
  text-transform: uppercase;
  margin-bottom: 10px;
}

/* Vision box */
.vision-box {
  background: linear-gradient(135deg, rgba(255,77,0,0.07), rgba(0,229,255,0.05));
  border: 1px solid rgba(255,77,0,0.3);
  border-radius: 6px;
  padding: 32px 36px;
  text-align: center;
  margin: 30px 0;
}
.vision-quote {
  font-family: var(--font-head);
  font-size: clamp(16px, 2vw, 22px);
  font-weight: 700;
  color: #fff;
  line-height: 1.5;
}
.vision-quote .accent { color: var(--orange); }
</style>
""", unsafe_allow_html=True)

# ─── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown('<div class="sb-logo">KORKUT<span>.</span>AI</div>', unsafe_allow_html=True)
    st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)
    st.markdown('<div class="sb-section">Navigasyon</div>', unsafe_allow_html=True)

    page = st.radio("", [
        "🧬  Ana Sayfa",
        "🛠️  Ar-Ge & İnovasyon",
        "🤖  Otonom Sistemler & Robotik",
        "🖥️  Arduino & Gömülü Sistemler",
        "🧑‍💻  Python & Yapay Zeka",
        "👨‍🏫  Hakkımızda & Vizyon",
        "📞  İletişim",
    ], label_visibility="collapsed")

    st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)
    st.markdown('<div class="sb-section">Teknik Danışmanlık</div>', unsafe_allow_html=True)

    with st.expander("🤖 AI Asistan", expanded=False):
        soru = st.text_area("Sorunuzu yazın:", placeholder="Örn: Servo motor için hangi Arduino kütüphanesi kullanılmalı?", height=100, key="ai_soru")
        if st.button("Gönder ›", key="ai_btn"):
            if soru.strip():
                with st.spinner("İşleniyor..."):
                    # Gemini-style canned responses (can be replaced with real API)
                    if "servo" in soru.lower():
                        cevap = "Servo motorlar için **Servo.h** kütüphanesini kullanın. `#include <Servo.h>` ile dahil edin, `servo.attach(pin)` ile pini bağlayın, `servo.write(açı)` ile 0-180° arasında konumlandırın."
                    elif "led" in soru.lower():
                        cevap = "LED yakma için `pinMode(pin, OUTPUT)` ve `digitalWrite(pin, HIGH/LOW)` yeterlidir. PWM için `analogWrite(pin, 0-255)` kullanın."
                    elif "python" in soru.lower():
                        cevap = "Python ile Arduino iletişimi için `pyserial` kütüphanesi kullanın: `pip install pyserial`. `serial.Serial('/dev/ttyUSB0', 9600)` ile bağlantı kurun."
                    elif "motor" in soru.lower():
                        cevap = "DC motor kontrolü için L298N veya L293D motor sürücü kullanın. PWM ile hız, dijital çıkışla yön kontrol edilir. Güç kaynağını ayrı tutun."
                    else:
                        cevap = f"'{soru[:60]}...' sorunuzu aldım. Otonom sistemler, gömülü sistemler, Arduino, Python veya robotik konularında daha spesifik sorular için yanıt kalitesi artacaktır. Teknik detay ekleyebilirsiniz."
                    st.markdown(f'<div class="ai-response"><div class="ai-label">⚡ Korkut.AI Yanıtı</div>{cevap}</div>', unsafe_allow_html=True)
            else:
                st.warning("Lütfen bir soru girin.")

    st.markdown('<hr class="sb-divider">', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center;padding:8px 0">
      <div style="font-family:'Space Mono',monospace;font-size:9px;color:#7a8499;letter-spacing:2px">v2.4.1 — KORKUT.AI</div>
      <div style="font-family:'Space Mono',monospace;font-size:9px;color:#7a8499;margin-top:4px">© 2024 Lezgin Korkut</div>
    </div>
    """, unsafe_allow_html=True)

# ─── PAGE: ANA SAYFA ──────────────────────────────────────────────────────────
if "Ana Sayfa" in page:
    st.markdown("""
    <div class="hero-section">
      <div class="hero-bg"></div>
      <div class="circuit-overlay"></div>
      <div class="scan-line"></div>
      <div class="hero-badge">// KORKUT.AI — Otonom Sistemler Portalı</div>
      <div class="hero-title">GELECEĞE HAZIR<br><span class="accent">DİJİTAL SİSTEMLER.</span></div>
      <div class="hero-sub">Otonom mobiliteden yapay zeka entegrasyonlarına, endüstriyel Ar-Ge'den özel yazılım mimarilerine kadar geleceği bugün inşa ediyoruz.</div>
      <div class="hero-stats">
        <div class="stat-item"><div class="stat-num">47+</div><div class="stat-label">Tamamlanan Proje</div></div>
        <div class="stat-item"><div class="stat-num">12</div><div class="stat-label">Aktif Ar-Ge</div></div>
        <div class="stat-item"><div class="stat-num">3</div><div class="stat-label">Patent Başvurusu</div></div>
        <div class="stat-item"><div class="stat-num">99%</div><div class="stat-label">Yerli Kod Oranı</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-sub">// Temel Yetkinlikler</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Ne Yapıyoruz?</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="card">
          <div class="card-icon">🤖</div>
          <div class="card-title">Otonom Robotik</div>
          <div class="card-body">Sensör füzyonu, gerçek zamanlı karar algoritmaları ve edge computing ile çalışan otonom platform tasarımı.</div>
        </div>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="card">
          <div class="card-icon">🧠</div>
          <div class="card-title">Yapay Zeka Entegrasyonu</div>
          <div class="card-body">Bilgisayarlı görü, doğal dil işleme ve pekiştirmeli öğrenme tabanlı çözümler. Gömülü sistemlere entegre AI.</div>
        </div>""", unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="card">
          <div class="card-icon">⚡</div>
          <div class="card-title">Gömülü Sistem Tasarımı</div>
          <div class="card-body">Arduino, ESP32, STM32 tabanlı özel donanım tasarımı. Gerçek zamanlı kontrol ve IoT entegrasyonu.</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    c4, c5, c6 = st.columns(3)
    with c4:
        st.markdown("""
        <div class="card">
          <div class="card-icon">🔬</div>
          <div class="card-title">Endüstriyel Ar-Ge</div>
          <div class="card-body">TÜBİTAK destekli araştırma projeleri. Prototipten üretime kadar tam süreç yönetimi.</div>
        </div>""", unsafe_allow_html=True)
    with c5:
        st.markdown("""
        <div class="card">
          <div class="card-icon">🖥️</div>
          <div class="card-title">Yazılım Mimarisi</div>
          <div class="card-body">Mikroservis, event-driven ve CQRS pattern'larıyla kurumsal ölçekli backend sistemleri.</div>
        </div>""", unsafe_allow_html=True)
    with c6:
        st.markdown("""
        <div class="card">
          <div class="card-icon">📡</div>
          <div class="card-title">IoT & Telemetri</div>
          <div class="card-body">MQTT, LoRa ve 5G tabanlı uzak izleme sistemleri. Gerçek zamanlı veri akışı ve dashboard entegrasyonu.</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div class="vision-box">
      <div class="vision-quote">
        "Teknolojide dışa bağımlılığı azaltmak,<br>
        <span class="accent">yerli ve milli otonom çözümler</span> geliştirmek,<br>
        açık kaynak ruhuyla bilgi paylaşımını desteklemek."
      </div>
    </div>
    """, unsafe_allow_html=True)

# ─── PAGE: AR-GE & İNOVASYON ─────────────────────────────────────────────────
elif "Ar-Ge" in page:
    st.markdown("""
    <div class="hero-section" style="min-height:220px;padding:40px 48px">
      <div class="hero-bg"></div><div class="circuit-overlay"></div>
      <div class="hero-badge">// AR-GE & İNOVASYON</div>
      <div class="hero-title" style="font-size:clamp(22px,3vw,40px)">ARAŞTIRMA &<br><span class="accent">GELİŞTİRME</span></div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([3, 2])
    with c1:
        st.markdown('<div class="section-title">Ar-Ge Nedir?</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-body" style="font-size:16px;line-height:1.9;color:#c0c8d8">
        <strong style="color:#fff">Araştırma ve Geliştirme (Ar-Ge)</strong>, mevcut bilgi birikimini artırmak
        ve bu birikimi yeni uygulama, ürün ve süreçler geliştirmek için kullanan sistematik çalışmalar bütünüdür.<br><br>
        Korkut.AI bünyesindeki Ar-Ge süreçleri üç aşamalı metodoloji üzerine kuruludur:<br><br>
        <span style="color:#00e5ff">▸ Temel Araştırma:</span> Bilimsel ilkelerin keşfi ve teorik modelleme.<br>
        <span style="color:#00e5ff">▸ Uygulamalı Araştırma:</span> Teorinin gerçek dünya problemlerine uyarlanması.<br>
        <span style="color:#00e5ff">▸ Deneysel Geliştirme:</span> Prototip üretimi, test ve doğrulama döngüleri.<br><br>
        Her proje, <strong style="color:#ff4d00">ISO 9001</strong> kalite yönetim sistemi ve
        <strong style="color:#ff4d00">PRINCE2</strong> proje metodolojisi çerçevesinde yürütülmektedir.
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-title">İnovasyon Süreci</div>', unsafe_allow_html=True)
        steps = [
            ("Problem Tanımlama", "Saha analizi, kullanıcı araştırması ve veri odaklı problem formülasyonu."),
            ("Hipotez Oluşturma", "Mühendislik modelleri ve matematiksel simülasyonlarla çözüm hipotezleri."),
            ("Prototipleme", "Rapid prototyping ile MVP (Minimum Viable Product) geliştirme."),
            ("Test & Validasyon", "A/B testleri, stres testleri ve gerçek ortam doğrulama."),
            ("Ölçeklendirme", "Başarılı prototiplerin üretim ortamına taşınması ve deployment."),
        ]
        for i, (title, desc) in enumerate(steps):
            st.markdown(f"""
            <div class="timeline-item">
              <div class="timeline-year">AŞAMA {i+1:02d}</div>
              <div style="font-family:'Rajdhani',sans-serif;font-size:17px;font-weight:700;color:#fff;margin-bottom:4px">{title}</div>
              <div class="timeline-text">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="section-title">Güncel Projeler</div>', unsafe_allow_html=True)
        projects = [
            ("KORKUT-DRONE v3", "Otonom İHA", ["ROS2", "Python", "LIDAR"]),
            ("EdgeAI-Embedded", "Gömülü Yapay Zeka", ["TensorFlow Lite", "ESP32"]),
            ("AgroBot-TR", "Tarım Robotu", ["Arduino", "CV", "LoRa"]),
            ("CyberShield-IDS", "Ağ Güvenliği", ["Python", "ML", "FastAPI"]),
        ]
        for p, sub, tags in projects:
            tag_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
            st.markdown(f"""
            <div class="proj-card">
              <div class="proj-title">{p}</div>
              <div class="proj-meta" style="margin-bottom:10px;color:#c0c8d8">{sub}</div>
              {tag_html}
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="section-title">Teknoloji Yığını</div>', unsafe_allow_html=True)
        techs = ["Python", "C++", "ROS2", "TensorFlow", "PyTorch", "OpenCV", "MQTT", "Docker", "Kubernetes", "FastAPI", "STM32", "ESP32"]
        tag_html = "".join(f'<span class="tag {"orange" if i%3==0 else ""}">{t}</span>' for i, t in enumerate(techs))
        st.markdown(f'<div style="margin-top:8px">{tag_html}</div>', unsafe_allow_html=True)

# ─── PAGE: OTONOM SİSTEMLER ───────────────────────────────────────────────────
elif "Otonom" in page:
    st.markdown("""
    <div class="hero-section" style="min-height:220px;padding:40px 48px">
      <div class="hero-bg"></div><div class="circuit-overlay"></div>
      <div class="hero-badge">// OTONOM SİSTEMLER & ROBOTİK</div>
      <div class="hero-title" style="font-size:clamp(22px,3vw,40px)">OTONOM<br><span class="accent">MİMARİLER</span></div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="section-title">Veri İşleme Mimarisi</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card-body" style="font-size:15px;line-height:1.9;color:#c0c8d8">
        Otonom bir sistem, çevresinden topladığı ham veriyi gerçek zamanlı karar mekanizmalarına dönüştüren
        çok katmanlı bir bilişsel mimariye sahiptir:
        <br><br>
        <span style="color:#ff4d00">① ALGILAMA KATMANI</span><br>
        LIDAR, kamera, IMU, GPS ve ultrasonik sensörlerden ham veri toplanır. Sensör füzyonu algoritmaları
        (Kalman Filter, EKF) birden fazla kaynaktan gelen belirsiz verileri birleştirir.
        <br><br>
        <span style="color:#ff4d00">② HARITALAMA & LOKALİZASYON</span><br>
        SLAM (Simultaneous Localization and Mapping) algoritmaları, bilinmeyen ortamda harita oluştururken
        robotun konumunu belirler. Occupancy grid ve point cloud temsilleri kullanılır.
        <br><br>
        <span style="color:#ff4d00">③ KARAR VERME MOTORU</span><br>
        Davranış ağaçları (Behavior Tree), durum makineleri ve pekiştirmeli öğrenme ile yüksek seviyeli
        görev planlaması gerçekleştirilir.
        <br><br>
        <span style="color:#ff4d00">④ KONTROL KATMANI</span><br>
        PID, MPC (Model Predictive Control) kontrolcüler ile aktüatörlere komut gönderilir.
        Gerçek zamanlı döngü frekansı 100-1000 Hz arasında çalışır.
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="section-title">Sistem Bileşenleri</div>', unsafe_allow_html=True)
        components = [
            ("🎯", "Görev Planlayıcı", "A*, D*, RRT* algoritmaları ile global rota optimizasyonu."),
            ("👁️", "Bilgisayarlı Görü", "YOLOv8, DepthAnything ile nesne algılama ve derinlik tahmini."),
            ("🧭", "Navigasyon", "Nav2 / Move Base ile dinamik engel kaçınma."),
            ("⚙️", "Haberleşme", "ROS2 DDS, CAN Bus, EtherCAT protokolleri."),
            ("🔋", "Güç Yönetimi", "Adaptif güç dağıtımı ve batarya yönetim sistemi (BMS)."),
            ("🛡️", "Güvenlik", "Watchdog timer, fail-safe mekanizmaları, redundant sistemler."),
        ]
        for icon, title, desc in components:
            st.markdown(f"""
            <div class="card" style="margin-bottom:12px;padding:18px 22px">
              <div style="display:flex;align-items:flex-start;gap:14px">
                <div style="font-size:22px;min-width:32px">{icon}</div>
                <div>
                  <div class="card-title" style="margin-bottom:4px">{title}</div>
                  <div class="card-body" style="font-size:14px">{desc}</div>
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)

# ─── PAGE: ARDUINO & GÖMÜLÜ SİSTEMLER ────────────────────────────────────────
elif "Arduino" in page:
    st.markdown("""
    <div class="hero-section" style="min-height:220px;padding:40px 48px">
      <div class="hero-bg"></div><div class="circuit-overlay"></div>
      <div class="hero-badge">// ARDUİNO & GÖMÜLÜ SİSTEMLER</div>
      <div class="hero-title" style="font-size:clamp(22px,3vw,40px)">KOD<br><span class="accent">DEPOSU</span></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-sub">// İnteraktif Proje Kütüphanesi</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Örnek Projeler</div>', unsafe_allow_html=True)

    projects = {
        "💡 Arduino ile LED Yakma": {
            "desc": "Dijital çıkış ile LED kontrolü. PWM ile parlaklık ayarı.",
            "difficulty": "Başlangıç",
            "parts": ["Arduino Uno", "LED", "220Ω Direnç", "Breadboard", "Jumper kablo"],
            "code": """\
// ── KORKUT.AI — LED KONTROL PROJESİ ──────────────────
// Donanım: Arduino Uno + LED + 220Ω Direnç
// Bağlantı: LED(+) → D9 pin (PWM)
//            LED(-) → GND (220Ω direnç üzerinden)
// ──────────────────────────────────────────────────────

const int LED_PIN = 9;      // PWM destekli pin
const int FADE_SPEED = 5;   // Parlaklık değişim hızı (ms)

void setup() {
  pinMode(LED_PIN, OUTPUT);
  Serial.begin(9600);
  Serial.println("KorkutAI LED Kontrol - Başlatıldı");
}

void loop() {
  // Soluklaşma efekti (Fade In)
  for (int brightness = 0; brightness <= 255; brightness += FADE_SPEED) {
    analogWrite(LED_PIN, brightness);
    delay(15);
  }
  delay(300);

  // Soluklaşma efekti (Fade Out)
  for (int brightness = 255; brightness >= 0; brightness -= FADE_SPEED) {
    analogWrite(LED_PIN, brightness);
    delay(15);
  }
  delay(300);

  Serial.println("Döngü tamamlandı.");
}""",
            "schema": """
📐 DEVRE ŞEMASI:
─────────────────────────────────────────
  Arduino D9 (PWM) ──── [220Ω] ──── LED (+)
                                        │
  Arduino GND      ────────────── LED (-)
─────────────────────────────────────────
⚠️  NOT: Direnç olmadan LED kalıcı olarak zarar görebilir!
    Direnç değeri = (Vcc - V_LED) / I_LED = (5V - 2V) / 20mA ≈ 150Ω–220Ω
"""
        },
        "📡 Mesafe Sensörü Entegrasyonu": {
            "desc": "HC-SR04 ultrasonik sensör ile mesafe ölçümü ve seri port çıkışı.",
            "difficulty": "Orta",
            "parts": ["Arduino Uno", "HC-SR04 Ultrasonik Sensör", "Breadboard", "Jumper kablo", "16x2 LCD (opsiyonel)"],
            "code": """\
// ── KORKUT.AI — ULTRASONİK MESAFE SENSÖRÜ ────────────
// Donanım: Arduino Uno + HC-SR04
// Bağlantı: VCC→5V | GND→GND | TRIG→D7 | ECHO→D6
// ──────────────────────────────────────────────────────

#define TRIG_PIN   7
#define ECHO_PIN   6
#define LED_ALARM  13    // Dahili LED uyarı
#define ALARM_CM   30    // Uyarı mesafesi (cm)

long duration;
float distance_cm;
float distance_inch;

void setup() {
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(LED_ALARM, OUTPUT);
  Serial.begin(9600);
  Serial.println("KorkutAI Mesafe Sensörü Aktif");
  Serial.println("Mesafe(cm) | Mesafe(inch) | Durum");
  Serial.println("─────────────────────────────────");
}

void loop() {
  // TRIG pini tetikle
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // ECHO süresini ölç
  duration = pulseIn(ECHO_PIN, HIGH);

  // Mesafe hesapla (ses hızı = 343 m/s)
  distance_cm    = (duration * 0.0343) / 2.0;
  distance_inch  = distance_cm / 2.54;

  // Uyarı kontrolü
  bool alarm = (distance_cm > 0 && distance_cm < ALARM_CM);
  digitalWrite(LED_ALARM, alarm ? HIGH : LOW);

  // Seri port çıkışı
  Serial.print(distance_cm, 1);
  Serial.print(" cm    | ");
  Serial.print(distance_inch, 2);
  Serial.print(" in  | ");
  Serial.println(alarm ? "⚠ YAKIN!" : "✓ Normal");

  delay(200);
}""",
            "schema": """
📐 DEVRE ŞEMASI:
─────────────────────────────────────────────
  HC-SR04     Arduino Uno
  ───────     ──────────
  VCC    ─── 5V
  GND    ─── GND
  TRIG   ─── D7 (Digital Output)
  ECHO   ─── D6 (Digital Input)
─────────────────────────────────────────────
📌 ÖNEMLİ:
  • HC-SR04 çalışma gerilimi: 5V (3.3V sistemlerde voltaj bölücü kullanın)
  • Ölçüm aralığı: 2cm – 400cm
  • Hassasiyet: ±3mm
  • Koni açısı: 15°
"""
        },
        "⚙️ Motor Sürücü Kontrolü": {
            "desc": "L298N motor sürücü ile DC motor hız ve yön kontrolü.",
            "difficulty": "İleri",
            "parts": ["Arduino Uno", "L298N Motor Sürücü", "DC Motor (6-12V)", "Güç Kaynağı", "Breadboard", "Jumper kablo"],
            "code": """\
// ── KORKUT.AI — L298N MOTOR SÜRÜCÜ KONTROLÜ ──────────
// Donanım: Arduino Uno + L298N + 2x DC Motor
// Motor A: ENA→D10(PWM) | IN1→D8 | IN2→D9
// Motor B: ENB→D5(PWM)  | IN3→D6 | IN4→D7
// ──────────────────────────────────────────────────────

// Motor A Pinleri
const int ENA = 10;   // PWM Hız (Enable A)
const int IN1 = 8;    // Yön kontrolü
const int IN2 = 9;

// Motor B Pinleri
const int ENB = 5;    // PWM Hız (Enable B)
const int IN3 = 6;
const int IN4 = 7;

// Motor kontrol fonksiyonu
void motorA(int speed, bool forward) {
  // speed: 0-255 | forward: true=ileri, false=geri
  speed = constrain(speed, 0, 255);
  analogWrite(ENA, speed);
  digitalWrite(IN1, forward ? HIGH : LOW);
  digitalWrite(IN2, forward ? LOW  : HIGH);
}

void motorB(int speed, bool forward) {
  speed = constrain(speed, 0, 255);
  analogWrite(ENB, speed);
  digitalWrite(IN3, forward ? HIGH : LOW);
  digitalWrite(IN4, forward ? LOW  : HIGH);
}

void dur() {
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
  digitalWrite(IN1, LOW); digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW); digitalWrite(IN4, LOW);
}

void setup() {
  int pins[] = {ENA, IN1, IN2, ENB, IN3, IN4};
  for (int i = 0; i < 6; i++) pinMode(pins[i], OUTPUT);
  Serial.begin(9600);
  Serial.println("KorkutAI Motor Kontrolü Başlatıldı");
}

void loop() {
  Serial.println("→ İleri | %80 hız");
  motorA(200, true);
  motorB(200, true);
  delay(2000);

  Serial.println("⏸ Dur (0.5s)");
  dur();
  delay(500);

  Serial.println("← Geri | %60 hız");
  motorA(150, false);
  motorB(150, false);
  delay(1500);

  Serial.println("↻ Sağa Dön");
  motorA(180, true);   // Sol motor ileri
  motorB(180, false);  // Sağ motor geri
  delay(800);

  dur();
  delay(1000);
}""",
            "schema": """
📐 DEVRE ŞEMASI (L298N):
──────────────────────────────────────────────────
  Arduino → L298N            L298N → Motorlar
  ─────────────              ────────────────
  D10(PWM) → ENA             OUT1 ─── Motor A (+)
  D8       → IN1             OUT2 ─── Motor A (-)
  D9       → IN2             OUT3 ─── Motor B (+)
  D5(PWM)  → ENB             OUT4 ─── Motor B (-)
  D6       → IN3
  D7       → IN4
  GND      → GND (paylaşımlı)

  Güç: 7-12V ──→ L298N VCC
       GND   ──→ L298N GND (Arduino ile ortak)
──────────────────────────────────────────────────
⚠️  NOT: Motor gücü ve Arduino gücünü AYRI tutun!
    L298N 5V çıkışını Arduino'ya bağlayabilirsiniz.
"""
        },
        "🔄 Servo Motor + Potansiyometre": {
            "desc": "Potansiyometre ile servo motor açı kontrolü.",
            "difficulty": "Başlangıç-Orta",
            "parts": ["Arduino Uno", "SG90 Servo Motor", "10kΩ Potansiyometre", "Breadboard", "Jumper kablo"],
            "code": """\
// ── KORKUT.AI — SERVO + POTANSİYOMETRE ───────────────
// Donanım: Arduino Uno + SG90 Servo + 10k Pot
// Servo: Sinyal→D9 | VCC→5V | GND→GND
// Pot:   Sol→GND | Orta→A0 | Sağ→5V
// ──────────────────────────────────────────────────────

#include <Servo.h>

Servo myServo;

const int POT_PIN   = A0;   // Potansiyometre analog girişi
const int SERVO_PIN = 9;    // Servo sinyal pini

int potValue  = 0;
int angle     = 0;
int lastAngle = -1;

void setup() {
  myServo.attach(SERVO_PIN);
  Serial.begin(9600);
  Serial.println("KorkutAI Servo Kontrol Başlatıldı");
  Serial.println("Pot Değeri | Açı (°) | Durum");
  Serial.println("──────────────────────────────");
}

void loop() {
  potValue = analogRead(POT_PIN);              // 0-1023
  angle    = map(potValue, 0, 1023, 0, 180);  // 0°-180° eşle

  // Yalnızca değişiklikte güncelle (gereksiz titreme önlemi)
  if (abs(angle - lastAngle) > 1) {
    myServo.write(angle);
    lastAngle = angle;

    Serial.print(potValue);
    Serial.print("       | ");
    Serial.print(angle);
    Serial.print("°      | ");
    Serial.println(angle < 60 ? "SOL" : angle > 120 ? "SAĞ" : "ORTA");
  }

  delay(20);  // 50 Hz güncelleme hızı
}""",
            "schema": """
📐 DEVRE ŞEMASI:
────────────────────────────────────────────────
  Potansiyometre      Arduino Uno
  ──────────────      ──────────
  Sol uç (-)   ─── GND
  Orta (wiper) ─── A0 (Analog Giriş)
  Sağ uç (+)   ─── 5V

  SG90 Servo          Arduino Uno
  ──────────          ──────────
  Kahverengi   ─── GND
  Kırmızı      ─── 5V
  Turuncu/Sarı ─── D9 (PWM Sinyal)
────────────────────────────────────────────────
📌 SG90 Specs: 0°-180° | 4.8-6V | 1.8 kg/cm tork
   Sinyal frekansı: 50Hz | Nabız: 1ms-2ms
"""
        },
    }

    selected = st.selectbox("Proje Seçin:", list(projects.keys()),
                            format_func=lambda x: x)

    if selected:
        proj = projects[selected]
        diff_color = {"Başlangıç": "#00e5ff", "Orta": "#ff9500", "İleri": "#ff4d00", "Başlangıç-Orta": "#00cc88"}
        dc = diff_color.get(proj["difficulty"], "#fff")

        st.markdown(f"""
        <div class="proj-card" style="margin-top:20px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
            <div class="proj-title" style="font-size:16px;margin:0">{selected}</div>
            <span style="font-family:'Space Mono',monospace;font-size:11px;color:{dc};border:1px solid {dc};padding:2px 10px;border-radius:2px">{proj["difficulty"]}</span>
          </div>
          <div class="card-body">{proj["desc"]}</div>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns([2, 1])
        with c1:
            st.markdown('<div class="section-title" style="margin-top:20px">Arduino Kodu</div>', unsafe_allow_html=True)
            st.code(proj["code"], language="cpp")

        with c2:
            st.markdown('<div class="section-title" style="margin-top:20px">Gerekli Malzemeler</div>', unsafe_allow_html=True)
            for part in proj["parts"]:
                st.markdown(f'<div style="font-family:\'Rajdhani\',sans-serif;padding:8px 12px;border-left:2px solid #00e5ff;margin-bottom:6px;color:#c0c8d8;font-size:15px">▸ {part}</div>', unsafe_allow_html=True)

            st.markdown('<div class="section-title">Devre Şeması</div>', unsafe_allow_html=True)
            st.code(proj["schema"], language="text")

# ─── PAGE: PYTHON & YAPAY ZEKA ────────────────────────────────────────────────
elif "Python" in page:
    st.markdown("""
    <div class="hero-section" style="min-height:220px;padding:40px 48px">
      <div class="hero-bg"></div><div class="circuit-overlay"></div>
      <div class="hero-badge">// PYTHON & YAPAY ZEKA</div>
      <div class="hero-title" style="font-size:clamp(22px,3vw,40px)">KOD &<br><span class="accent">ALGORİTMA</span></div>
    </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["🐍 Python Temelleri", "🧠 Makine Öğrenmesi", "👁️ Bilgisayarlı Görü", "🤖 Seri Haberleşme"])

    with tabs[0]:
        st.markdown('<div class="section-title">Sensör Verisi İşleme</div>', unsafe_allow_html=True)
        st.code("""\
import serial
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

# Arduino ile seri haberleşme
port   = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
buffer = deque(maxlen=100)   # Son 100 ölçüm

def read_sensor():
    line = port.readline().decode('utf-8').strip()
    try:
        return float(line)
    except ValueError:
        return None

def moving_average(data, window=5):
    \"\"\"Hareketli ortalama filtresi\"\"\"
    return np.convolve(data, np.ones(window)/window, mode='valid')

# Gerçek zamanlı veri toplama döngüsü
while True:
    val = read_sensor()
    if val is not None:
        buffer.append(val)
        filtered = moving_average(list(buffer))
        print(f"Ham: {val:.2f} | Filtreli: {filtered[-1]:.2f}")
""", language="python")

    with tabs[1]:
        st.markdown('<div class="section-title">Anomali Tespiti</div>', unsafe_allow_html=True)
        st.code("""\
from sklearn.ensemble import IsolationForest
import pandas as pd
import numpy as np

# Sensör verisi yükle
df = pd.read_csv('sensor_data.csv')
X  = df[['temperature', 'vibration', 'current']].values

# Isolation Forest modeli
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,   # %5 anomali oranı bekleniyor
    random_state=42
)
model.fit(X)

# Tahmin
df['anomaly'] = model.predict(X)
df['score']   = model.score_samples(X)

# Anomalileri filtrele
anomalies = df[df['anomaly'] == -1]
print(f"Toplam: {len(df)} | Anomali: {len(anomalies)}")
print(anomalies[['timestamp', 'temperature', 'score']].head())
""", language="python")

    with tabs[2]:
        st.markdown('<div class="section-title">YOLOv8 ile Nesne Tespiti</div>', unsafe_allow_html=True)
        st.code("""\
from ultralytics import YOLO
import cv2

# Model yükle (önceden eğitilmiş veya özel)
model = YOLO('yolov8n.pt')   # nano model (hızlı)

# Kamera akışı
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Çıkarım
    results = model(frame, conf=0.5, verbose=False)

    # Bounding box çiz
    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls  = int(box.cls[0])
            conf = float(box.conf[0])
            label = f"{model.names[cls]} {conf:.0%}"

            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,229,255), 2)
            cv2.putText(frame, label, (x1, y1-8),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,229,255), 2)

    cv2.imshow('KorkutAI Vision', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
""", language="python")

    with tabs[3]:
        st.markdown('<div class="section-title">Arduino ↔ Python Köprüsü</div>', unsafe_allow_html=True)
        st.code("""\
import serial
import json
import time

class ArduinoBridge:
    \"\"\"Arduino ile iki yönlü haberleşme köprüsü\"\"\"

    def __init__(self, port='/dev/ttyUSB0', baud=115200):
        self.ser = serial.Serial(port, baud, timeout=1)
        time.sleep(2)   # Arduino reset süresi
        print(f"Bağlantı kuruldu: {port} @ {baud}")

    def send_command(self, cmd: dict):
        \"\"\"JSON formatında komut gönder\"\"\"
        payload = json.dumps(cmd) + '\\n'
        self.ser.write(payload.encode())

    def read_data(self) -> dict:
        \"\"\"JSON formatında veri al\"\"\"
        line = self.ser.readline().decode().strip()
        if line:
            try:
                return json.loads(line)
            except json.JSONDecodeError:
                return {"raw": line}
        return {}

    def close(self):
        self.ser.close()

# Kullanım
bridge = ArduinoBridge('/dev/ttyUSB0')

# Motor komut gönder
bridge.send_command({"motor": "A", "speed": 200, "dir": "forward"})
bridge.send_command({"servo": 1, "angle": 90})

# Sensör verisi oku
while True:
    data = bridge.read_data()
    if data:
        print(f"Sıcaklık: {data.get('temp', 'N/A')}°C | "
              f"Mesafe: {data.get('dist', 'N/A')}cm")
    time.sleep(0.1)
""", language="python")

# ─── PAGE: HAKKIMIZDA ─────────────────────────────────────────────────────────
elif "Hakkımızda" in page:
    st.markdown("""
    <div class="hero-section" style="min-height:220px;padding:40px 48px">
      <div class="hero-bg"></div><div class="circuit-overlay"></div>
      <div class="hero-badge">// HAKKIMIZDA & VİZYON</div>
      <div class="hero-title" style="font-size:clamp(22px,3vw,40px)">BİZ<br><span class="accent">KİMİZ?</span></div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([3, 2])
    with c1:
        st.markdown('<div class="section-title">Kurucu</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="card" style="margin-bottom:24px">
          <div style="display:flex;align-items:center;gap:20px;margin-bottom:20px">
            <div style="width:72px;height:72px;background:linear-gradient(135deg,#ff4d00,#ff9500);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:32px;flex-shrink:0">👨‍💻</div>
            <div>
              <div style="font-family:'Orbitron',monospace;font-size:20px;font-weight:700;color:#fff">Lezgin Korkut</div>
              <div style="font-family:'Space Mono',monospace;font-size:11px;color:#00e5ff;letter-spacing:2px;margin-top:4px">KURUCU & GENEL MÜDÜR</div>
            </div>
          </div>
          <div class="card-body" style="font-size:15px;line-height:1.9">
            Otonom sistemler, gömülü yazılım geliştirme ve yapay zeka entegrasyonu alanlarında uzmanlaşmış
            bir mühendis ve girişimci. Arduino'dan endüstriyel robot platformlarına, Python'dan
            gerçek zamanlı kontrol yazılımlarına kadar geniş bir teknik yelpazede faaliyet göstermektedir.<br><br>
            Diyarbakır merkezli bu girişimin amacı; Türkiye'nin teknolojik bağımsızlığına katkı sunmak
            ve yerel insan kaynağını dünya standartlarında mühendisler olarak yetiştirmektir.
          </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-title">Vizyonumuz</div>', unsafe_allow_html=True)
        visions = [
            ("🔬", "Ar-Ge Önceliği", "Her ürün ve hizmet, derinlemesine araştırma ve prototipleme sürecinden geçer."),
            ("🇹🇷", "Yerlilik", "Tasarımdan kodlamaya, tüm geliştirme süreçleri yerli mühendislik anlayışıyla yürütülür."),
            ("🌐", "Açık Kaynak", "Bilginin paylaşılması, toplumsal ilerlemenin temelidir."),
            ("🎓", "Eğitim", "Genç mühendislere mentörlük ve staj programları."),
        ]
        for icon, title, desc in visions:
            st.markdown(f"""
            <div class="card" style="margin-bottom:12px;padding:18px 22px">
              <div style="display:flex;align-items:flex-start;gap:14px">
                <div style="font-size:22px;min-width:32px">{icon}</div>
                <div>
                  <div class="card-title" style="margin-bottom:4px">{title}</div>
                  <div class="card-body" style="font-size:14px">{desc}</div>
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="section-title">Kilometre Taşları</div>', unsafe_allow_html=True)
        milestones = [
            ("2021", "Korkut.AI'nın kuruluşu. İlk gömülü sistem projeleri."),
            ("2022", "TÜBİTAK 1507 başvurusu. İlk otonom platform prototipi."),
            ("2023", "Ticari ürün lansmanları. İlk kurumsal müşteri kazanımı."),
            ("2024", "Patent başvuruları. Uluslararası konferans sunumu."),
            ("2025", "Ölçeklendirme ve takım büyümesi. Yeni Ar-Ge laboratuvarı."),
        ]
        for year, text in milestones:
            st.markdown(f"""
            <div class="timeline-item">
              <div class="timeline-year">{year}</div>
              <div class="timeline-text">{text}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div class="section-title">Yetkinlik Alanları</div>', unsafe_allow_html=True)
        skills = ["Arduino", "ESP32", "STM32", "Python", "C++", "ROS2", "TensorFlow", "OpenCV", "MQTT", "FastAPI", "Docker", "Git", "YOLO", "KiCAD", "Fusion 360"]
        html = "".join(f'<span class="tag {"orange" if i%4==0 else ""}">{s}</span>' for i, s in enumerate(skills))
        st.markdown(f'<div style="margin-top:8px">{html}</div>', unsafe_allow_html=True)

# ─── PAGE: İLETİŞİM ──────────────────────────────────────────────────────────
elif "İletişim" in page:
    st.markdown("""
    <div class="hero-section" style="min-height:220px;padding:40px 48px">
      <div class="hero-bg"></div><div class="circuit-overlay"></div>
      <div class="hero-badge">// İLETİŞİM</div>
      <div class="hero-title" style="font-size:clamp(22px,3vw,40px)">BİZE<br><span class="accent">ULAŞIN</span></div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2 = st.columns([3, 2])
    with c1:
        st.markdown('<div class="section-title">İletişim Bilgileri</div>', unsafe_allow_html=True)

        contacts = [
            ("📞", "Telefon", "0539 949 10 50"),
            ("📧", "E-posta", "lezginkorkut03@gmail.com"),
            ("📍", "Adres", "Diyarbakır / Kayapınar, Fırat Mahallesi 507. Sokak, Dicle Fırat Online Plaza Kat:6 Daire No:19"),
        ]
        for icon, label, value in contacts:
            st.markdown(f"""
            <div class="contact-row">
              <div class="contact-icon">{icon}</div>
              <div>
                <div class="contact-label">{label}</div>
                <div class="contact-value">{value}</div>
              </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown('<div class="section-title">Mesaj Gönderin</div>', unsafe_allow_html=True)

        with st.container():
            name  = st.text_input("Ad Soyad", placeholder="Adınız Soyadınız")
            email = st.text_input("E-posta", placeholder="ornek@mail.com")
            topic = st.selectbox("Konu", ["Proje Talebi", "Teknik Danışmanlık", "İş Birliği", "Staj / Kariyer", "Diğer"])
            msg   = st.text_area("Mesajınız", placeholder="Mesajınızı buraya yazın...", height=140)
            if st.button("Mesaj Gönder →"):
                if name and email and msg:
                    st.success(f"✅ Mesajınız alındı! En geç 24 saat içinde **{email}** adresinize dönüş yapılacaktır.")
                else:
                    st.warning("Lütfen tüm alanları doldurun.")

    with c2:
        st.markdown('<div class="section-title">Çalışma Saatleri</div>', unsafe_allow_html=True)
        hours = [
            ("Pazartesi – Cuma", "09:00 – 18:00"),
            ("Cumartesi", "10:00 – 15:00"),
            ("Pazar", "Kapalı"),
        ]
        for day, h in hours:
            closed = h == "Kapalı"
            color = "#7a8499" if closed else "#00e5ff"
            st.markdown(f"""
            <div style="display:flex;justify-content:space-between;align-items:center;
                        padding:14px 18px;border:1px solid rgba(0,229,255,0.12);
                        border-radius:4px;margin-bottom:8px;background:#0d1117">
              <div style="font-family:'Rajdhani',sans-serif;font-size:15px;font-weight:600;color:#c0c8d8">{day}</div>
              <div style="font-family:'Space Mono',monospace;font-size:13px;color:{color}">{h}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        <div class="card" style="text-align:center;padding:32px 24px">
          <div style="font-size:36px;margin-bottom:12px">🤝</div>
          <div class="card-title" style="font-size:16px;margin-bottom:12px">İş Birliği Yapalım</div>
          <div class="card-body" style="font-size:14px">
            Otonom sistemler, Ar-Ge projeleri veya yazılım geliştirme konusunda iş birliği
            tekliflerinizi bekliyoruz.
          </div>
        </div>
        """, unsafe_allow_html=True)
