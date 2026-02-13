# 🧪 XUSAN LAB TASK DASHBOARD

---

# 🌐 LOYIHA HAQIDA

**XUSAN Lab Task Dashboard** — bu Python asosida yaratilgan ta’limiy Client–Server arxitektura loyihasi.

Ushbu loyiha orqali quyidagi konseptlar amaliy ko‘rsatib beriladi:

- HTTP orqali client–server aloqa
- Agent ro‘yxatdan o‘tishi
- Heartbeat (muntazam ulanish tekshiruvi)
- Task queue (vazifalar navbati)
- Web dashboard orqali monitoring
- JSON API orqali ma’lumot almashish

⚠️ Loyiha faqat lokal laboratoriya muhiti uchun mo‘ljallangan.

---

# 🏗 TIZIM TUZILISHI

Loyiha ikki asosiy qismdan iborat:

## 1️⃣ SERVER — `app.py`

- Flask asosidagi web dashboard
- Agent sessiyalarini saqlash
- Task yuborish
- Natijalarni qabul qilish
- API endpointlar

## 2️⃣ AGENT — `agent.py`

- Serverga ro‘yxatdan o‘tadi
- Har 3 soniyada heartbeat yuboradi
- Serverdan vazifalarni oladi
- Natijani qaytaradi

---

# ⚙️ ASOSIY IMKONIYATLAR

- ✅ Agent avtomatik ro‘yxatdan o‘tishi
- ✅ Real vaqtga yaqin heartbeat monitoring
- ✅ Har bir agent uchun alohida task queue
- ✅ Web interfeys orqali sessiyalarni ko‘rish
- ✅ Natijalarni vaqt bilan saqlash
- ✅ Linux va Windows qo‘llab-quvvatlanadi
- ✅ JSON asosidagi API

---

# 🚀 O‘RNATISH

## 1️⃣ TALABLAR

- Python 3.8+
- pip
- Flask
- Requests

O‘rnatish:

```bash
pip install flask requests
