# 🤖 Bộ phân loại Email Rác (Spam Classifier)

Đây là một ứng dụng web đơn giản sử dụng **Flask** và **Scikit-learn** để phân loại email là **"SPAM" (rác)** hay **"HAM" (không rác)**.

Mô hình được huấn luyện bằng **Logistic Regression** trên bộ dữ liệu `spam.csv`, với các kỹ thuật tiền xử lý **NLTK** và **cân bằng dữ liệu SMOTE**.

---

## 🚀 Cách chạy dự án này

### 1️⃣ Tải code về (Clone)

```bash
git clone https://github.com/NhatTien1114/spam-classifier-flask
cd "Phân loại mail rác"
```

---

### 2️⃣ Tạo môi trường ảo (khuyến khích)

```bash
python -m venv venv
# Trên Mac/Linux
source venv/bin/activate

# Trên Windows
venv\Scripts\activate
```

---

### 3️⃣ Cài đặt các thư viện cần thiết

Dự án này cần một số thư viện Python. Hãy cài đặt chúng từ file `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Huấn luyện mô hình (rất quan trọng ⚠️)

Kho lưu trữ này **không chứa** các file mô hình đã huấn luyện (`.pkl`), vì chúng được thêm vào `.gitignore`.

Bạn cần tự huấn luyện mô hình bằng cách:

1. Khởi chạy Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

2. Mở file **`Phan_loai_mail_rac_fixed.ipynb`**.

3. Trên thanh menu, chọn **"Kernel" → "Restart & Run All"**.

4. Đợi chạy xong. Sau đó, thư mục **`model/`** sẽ được tạo tự động, chứa:
   - `spam_model.pkl`
   - `tfidf_vectorizer.pkl`

---

### 5️⃣ Chạy ứng dụng Flask

Sau khi có mô hình, bạn có thể khởi chạy web app bằng:

```bash
python app_fixed.py
```

---

### 6️⃣ Mở ứng dụng trên trình duyệt

Truy cập địa chỉ:

👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

Tại đây, bạn có thể nhập nội dung email và xem mô hình dự đoán đó là **Spam** hay **Không Spam**.

---

## 🧠 Công nghệ sử dụng

- Python 3.x  
- Flask  
- Scikit-learn  
- Pandas  
- NLTK  
- Imbalanced-learn (SMOTE)  
- HTML + CSS (Frontend)

---

## 📁 Cấu trúc thư mục

```
📦 spam-classifier-flask
├── app_fixed.py                  # Flask web app
├── Phan_loai_mail_rac_fixed.ipynb  # Notebook huấn luyện mô hình
├── requirements.txt              # Danh sách thư viện cần thiết
├── model/
│   ├── spam_model.pkl            # Mô hình Logistic Regression (tự tạo sau khi huấn luyện)
│   └── tfidf_vectorizer.pkl      # Vectorizer TF-IDF (tự tạo sau khi huấn luyện)
├── static/
│   └── style.css                 # CSS cho giao diện web
├── templates/
│   └── index.html                # Giao diện web
└── data/
    └── spam.csv                  # Bộ dữ liệu huấn luyện
```

---

## 🧩 Demo

Nhập thử email ví dụ:

- ✉️ `"Congratulations! You have won a $1000 gift card!"` → **SPAM**
- ✉️ `"Hey, are we still meeting for lunch today?"` → **HAM**

---

## 📜 Giấy phép

Dự án này được phát triển cho mục đích **học tập** và **nghiên cứu**.

---

> 👨‍💻 Tác giả: **Nhật Tiến**  
> 📅 Năm: 2025  
> 🌐 Repository: [https://github.com/NhatTien1114/spam-classifier-flask](https://github.com/NhatTien1114/spam-classifier-flask)
trình duyệt của bạn và truy cập: http://127.0.0.1:5000