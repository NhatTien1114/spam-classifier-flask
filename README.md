# 🤖 Bộ phân loại Email Rác (Spam Classifier)

Đây là một ứng dụng web đơn giản sử dụng **Flask** và **Scikit-learn** để phân loại email là **"SPAM" (rác)** hay **"HAM" (không rác)**.

Mô hình được huấn luyện bằng **Logistic Regression** trên bộ dữ liệu `spam.csv`, với các kỹ thuật tiền xử lý **NLTK** và **cân bằng dữ liệu SMOTE**.


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
├── app.py                  # Flask web app
├── Phan_loai_mail_rac.ipynb  # Notebook huấn luyện mô hình
├── requirements.txt              # Danh sách thư viện cần thiết
├── model/
│   ├── spam_model.pkl            # Mô hình Logistic Regression (tự tạo sau khi huấn luyện)
│   └── tfidf_vectorizer.pkl      # Vectorizer TF-IDF (tự tạo sau khi huấn luyện)
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
> 🌐 Repository: [https://github.com/NhatTien1114/spam-classifier-flask](https://github.com/NhatTien1114/spam-classifier-flask)
trình duyệt của bạn và truy cập: http://127.0.0.1:5000
