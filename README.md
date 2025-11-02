🤖 Bộ phân loại Email Rác (Spam Classifier)

Đây là một dự án ứng dụng web đơn giản sử dụng Flask và Scikit-learn để phân loại một email là "SPAM" (rác) hay "HAM" (không rác).

Mô hình được huấn luyện bằng Logistic Regression trên bộ dữ liệu spam.csv, với các kỹ thuật tiền xử lý NLTK và cân bằng dữ liệu SMOTE.

🚀 Cách chạy dự án này

1. Tải code về (Clone)

git clone <https://github.com/NhatTien1114/spam-classifier-flask>
cd <Phân loại mail rác>


2. Tạo môi trường ảo

(Khuyến khích)

python -m venv venv
source venv/bin/activate  # Trên Mac/Linux
venv\Scripts\activate     # Trên Windows


3. Cài đặt các thư viện

Dự án này cần một số thư viện. Hãy cài đặt chúng từ file requirements.txt:

pip install -r requirements.txt


4. ‼️ Bước quan trọng: Huấn luyện mô hình

Kho lưu trữ này không chứa các file mô hình (.pkl) đã huấn luyện (do chúng đã được thêm vào .gitignore). Bạn phải tự tạo ra chúng bằng cách chạy file Jupyter Notebook:

Khởi chạy Jupyter:

jupyter notebook


Mở file Phan_loai_mail_rac_fixed.ipynb.

Trên thanh menu, chọn "Kernel" -> "Restart & Run All".

Đợi cho nó chạy xong. Việc này sẽ tự động tạo ra thư mục model/ chứa các file spam_model.pkl và tfidf_vectorizer.pkl.

5. Chạy ứng dụng Flask

Bây giờ bạn đã có mô hình, hãy khởi chạy máy chủ web:

python app_fixed.py


6. Mở ứng dụng

Mở trình duyệt của bạn và truy cập: http://127.0.0.1:5000