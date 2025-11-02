import flask
from flask import Flask, render_template, request
import pickle
import sys
import os
import re  
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

app = Flask(__name__)

try:
    stop_words = set(stopwords.words('english'))
except LookupError:
    print("Đang tải NLTK stopwords...")
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

stemmer = PorterStemmer() 

# --- Xác định đường dẫn và tải mô hình ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, 'model')

try:
    model_path = os.path.join(MODEL_DIR, 'spam_model.pkl')
    vectorizer_path = os.path.join(MODEL_DIR, 'tfidf_vectorizer.pkl')
    
    model = pickle.load(open(model_path, 'rb'))
    vectorizer = pickle.load(open(vectorizer_path, 'rb'))
    
except FileNotFoundError:
    print(f"LỖI: Không tìm thấy file .pkl trong thư mục '{MODEL_DIR}'.", file=sys.stderr)
    print("Hãy đảm bảo bạn đã tạo thư mục 'model' và đặt 2 file .pkl vào đó.", file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f"Lỗi không xác định khi tải file pickle: {e}", file=sys.stderr)
    sys.exit(1)


def preprocess_text(text):
    """
    Hàm này làm sạch văn bản thô từ web
    để nó khớp 100% với dữ liệu đã huấn luyện.
    """
    text = text.lower()
 
    text = re.sub(r'[^a-z]', ' ', text) # Thay thế tất cả ký tự không phải chữ cái bằng khoảng trắng
    
    # 3. Tách từ
    words = text.split()
    
    # 4. Xóa Stopwords và Stemming
    words = [stemmer.stem(word) for word in words if word not in stop_words]
    
    # 5. Ghép lại thành chuỗi
    return " ".join(words) 

# 

# --- Route chính (Trang chủ) ---
@app.route('/')
def home():
    return render_template('index.html', prediction_text=None, email='')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        email_content = request.form['email']
        
        # --- (SỬA LỖI 2) BẮT TRƯỜNG HỢP NHẬP RỖNG ---
        # .strip() để xóa các khoảng trắng thừa
        if not email_content.strip():
            # Nếu người dùng không nhập gì, trả về lỗi
            return render_template('index.html', 
                                   prediction_text="🚫 Vui lòng nhập nội dung email!", 
                                   prediction_class="result-spam", # Dùng màu đỏ để báo lỗi
                                   email='')

        # 1. Tiền xử lý văn bản thô từ người dùng
        processed_email = preprocess_text(email_content)
        
        # 2. Chuẩn bị dữ liệu
        data = [processed_email] 
        
        # 3. Vector hóa
        vect = vectorizer.transform(data)
        
        # 4. Dự đoán
        prediction = model.predict(vect)[0] 
        
        # 5. Logic trả kết quả (0=ham, 1=spam)
        if prediction == 1:
            pred_text = "🚫 Đây là SPAM!"
            pred_class = "result-spam"
        else:
            pred_text = "✅ Đây là email bình thường (HAM)"
            pred_class = "result-ham"

        # 6. Trả kết quả
        return render_template('index.html', 
                               prediction_text=pred_text, 
                               prediction_class=pred_class, 
                               email=email_content)

if __name__ == '__main__':
    app.run(debug=True)

