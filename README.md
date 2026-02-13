🧪 XUSAN Lab Task Dashboard
Python asosidagi Client–Server Tajriba Loyihasi
🌐 Loyiha haqida (Overview)

XUSAN Lab Task Dashboard — bu Python asosida yaratilgan ta’limiy loyiha bo‘lib, unda:

HTTP orqali client–server muloqoti

Agent ro‘yxatdan o‘tishi va heartbeat mexanizmi

Oddiy task queue tizimi

Web dashboard orqali sessiyalarni ko‘rish

JSON API orqali ma’lumot almashish

kabi backend konseptlar amaliy ko‘rsatib beriladi.

Loyiha faqat lokal laboratoriya muhiti uchun mo‘ljallangan.

🏗 Tizim Arxitekturasi

Loyiha ikki asosiy qismdan iborat:

1️⃣ Server (app.py)

Flask asosidagi web dashboard

Agent sessiyalarini saqlash

Vazifalar (task) yuborish

Natijalarni qabul qilish va ko‘rsatish

2️⃣ Agent (agent.py)

Serverga ro‘yxatdan o‘tadi

Har 3 soniyada heartbeat yuboradi

Serverdan vazifani oladi

Natijani qaytaradi

🛠 Texnik Imkoniyatlar (Features)

🔗 Agent avtomatik ro‘yxatdan o‘tishi

📡 Heartbeat monitoring

📋 Har bir agent uchun alohida task queue

📊 Web interfeys orqali kuzatish

📑 Natijalarni vaqt bilan saqlash

🖥 Linux va Windows qo‘llab-quvvatlanadi

⚙️ JSON asosidagi API

🚀 O‘rnatish va Ishga Tushirish
1️⃣ Talablar

Python 3.8+

pip

Flask

Requests

O‘rnatish:

pip install flask requests

2️⃣ Serverni ishga tushirish
python3 app.py


Server ochiladi:

http://127.0.0.1:5000

3️⃣ Agentni ishga tushirish
python3 agent.py


Yoki server manzilini qo‘lda berish mumkin:

python3 agent.py http://127.0.0.1:5000

🔌 API Endpoints
Endpoint	Method	Vazifasi
/api/beacon/register	POST	Agent ro‘yxatdan o‘tishi
/api/beacon/heartbeat	POST	Heartbeat va task olish
/api/beacon/result	POST	Natijani yuborish
/api/task	POST	Agentga task qo‘shish
/api/results/<id>	GET	Natijalarni olish
📚 O‘rganish Uchun Foydali Mavzular

Ushbu loyiha quyidagi backend konseptlarni tushunishga yordam beradi:

REST API dizayni

Flask arxitekturasi

Client polling modeli

Session boshqaruvi

Task lifecycle

JSON asosidagi ma’lumot almashinuvi

🔐 Xavfsizlik Ogohlantirishi

⚠️ Muhim:

Loyihani faqat o‘zingizga tegishli tizimda sinab ko‘ring.

Serverni internetga ochmang.

Izolyatsiyalangan muhit (VM yoki Docker) tavsiya etiladi.

Real tizimlarda qo‘llashdan oldin autentifikatsiya qo‘shing.

📈 Kelajakdagi Rejalar

🔑 Token-based autentifikatsiya

📜 Command allow-list

🐳 Docker qo‘llab-quvvatlash

📊 Log tizimi

🎨 UI dizaynini yaxshilash

👨‍💻 Muallif

Xusan

Agar loyiha sizga foydali bo‘lsa, GitHub’da ⭐ bosishni unutmang.
