import streamlit as st
import pandas as pd

# Cấu hình trang
st.set_page_config(page_title="Hệ thống CRM Ngân hàng", layout="wide")

st.title("🏦 HỆ THỐNG QUẢN LÝ KHÁCH HÀNG & TRUYỀN THÔNG NGÂN HÀNG")

# Tạo 4 Tab tương ứng với 4 yêu cầu của đề tài
tab1, tab2, tab3, tab4 = st.tabs([
    "📋 1. Nhập & Lưu Lead", 
    "📞 2. Kịch Bản Cuộc Gọi", 
    "🎭 3. Tình Huống Đóng Vai", 
    "🎬 4. Poster & Video Ads"
])

# --- TAB 1: THIẾT KẾ APP LƯU THÔNG TIN KHÁCH HÀNG ---
with tab1:
    st.header("👤 Nhập thông tin khách hàng tiềm năng")
    
    # Khởi tạo bộ nhớ tạm để lưu danh sách khách hàng
    if "data_kh" not in st.session_state:
        st.session_state.data_kh = pd.DataFrame(columns=["SĐT", "Tên KH", "Địa chỉ", "Nhu cầu", "Phân loại", "Ghi chú"])

    col1, col2 = st.columns(2)
    with col1:
        sdt = st.text_input("📱 Số điện thoại")
        ten = st.text_input("👤 Tên khách hàng")
        dia_chi = st.text_input("📍 Địa chỉ")
    with col2:
        nhu_cau = st.selectbox("💳 Nhu cầu dịch vụ", ["Vay mua nhà", "Mở thẻ tín dụng", "Gửi tiết kiệm", "Vay tiêu dùng"])
        phan_loai = st.selectbox("🔥 Phân loại Lead", ["Hot (Cần gấp)", "Warm (Cân nhắc)", "Cold (Chưa rõ nhu cầu)"])
        ghi_chu = st.text_area("📝 Ghi chú")

    if st.button("💾 Lưu thông tin khách hàng"):
        if sdt and ten:
            new_data = pd.DataFrame([{
                "SĐT": sdt, "Tên KH": ten, "Địa chỉ": dia_chi, 
                "Nhu cầu": nhu_cau, "Phân loại": phan_loai, "Ghi chú": ghi_chu
            }])
            st.session_state.data_kh = pd.concat([st.session_state.data_kh, new_data], ignore_index=True)
            st.success(f"Đã lưu thành công khách hàng: {ten}")
        else:
            st.warning("Vui lòng nhập ít nhất SĐT và Tên khách hàng!")

    st.subheader("📊 Danh sách khách hàng đã lưu")
    st.dataframe(st.session_state.data_kh, use_container_width=True)

# --- TAB 2: TRÌNH BÀY ĐOẠN HỘI THOẠI CALL ---
with tab2:
    st.header("📞 Kịch bản Telesales tư vấn Thẻ tín dụng")
    st.write("**NV ngân hàng:** *Em chào anh/chị, em gọi từ Ngân hàng X. Em thấy mình vừa tìm hiểu gói ưu đãi hoàn tiền 10% đúng không ạ?*")
    st.write("**Khách hàng:** *Ừ em, nhưng anh/chị thấy phí thường niên hơi đắt nên chưa muốn mở.*")
    st.write("**NV ngân hàng (Xử lý từ chối):** *Dạ, thẻ này đang được miễn phí năm đầu khi đạt hạn mức chi tiêu nhỏ. Nếu mình chi tiêu gia đình hàng tháng thì tiền hoàn lại cao hơn phí rất nhiều ạ!*")

# --- TAB 3: ĐÓNG VAI NHÂN VIÊN & KHÁCH HÀNG ---
with tab3:
    st.header("🎭 Phân công đóng vai thực hành")
    st.markdown("""
    * **Nhân viên Ngân hàng (Thành viên A):** Tư vấn chuyên nghiệp, lắng nghe nhu cầu, giải đáp thắc mắc về phí.
    * **Khách hàng tiềm năng (Thành viên B):** Đặt câu hỏi về lãi suất, phí ẩn và thể hiện sự băn khoăn thực tế.
    """)

# --- TAB 4: SÁNG TẠO POSTER & VIDEO ADS ---
with tab4:
    st.header("🎨 Sản phẩm Truyền thông & Quảng cáo")
    st.subheader("🖼️ Poster Quảng cáo")
    # Thay link ảnh poster của nhóm vào bên dưới
    st.image("https://via.placeholder.com/800x400.png?text=Poster+Quang+Cao+Ngan+Hang", caption="Mẫu Poster ưu đãi mở thẻ")
    
    st.subheader("🎥 Video Quảng cáo")
    # Thay link video YouTube hoặc file mp4 của nhóm vào đây
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
