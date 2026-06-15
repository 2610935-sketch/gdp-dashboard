import streamlit as st

# 1. 데이터 정의
stations = ["서울역", "강남역", "홍대입구역"]
facilities = ["엘리베이터 이용", "교통약자 화장실", "휠체어 리프트 보유"]

# 앱 제목
st.title("🚇 지하철 교통약자 편의정보 안내")

# --- 역 검색 섹션 ---
st.markdown("## 🔍 편의시설 검색")
search = st.text_input("검색할 역 이름을 입력하세요:", placeholder="예: 서울역, 강남역, 홍대입구역")

# 사용자가 입력값을 입력했을 때만 로직 실행
if search:
    if search in stations:
        i = stations.index(search)
        # st.success를 사용하여 시각적으로 강조된 결과 출력
        st.success(f"💡 **{search}**의 편의시설은 **[{facilities[i]}]** 입니다.")
    else:
        st.error("❌ 목록에 없는 역입니다. 정확한 역 이름을 입력해 주세요.")

# 섹션 구분을 위한 구분선
st.markdown("---")

# --- 제도 안내 섹션 ---
st.markdown("## ℹ️ 교통약자 제도 안내")

# 콘솔의 번호 입력을 스트림릿의 selectbox(드롭다운 부스)로 변환하여 사용자 편의성 향상
options = ["선택하세요", "1: 무임승차", "2: 바우처택시", "0: 종료"]
choice = st.selectbox("확인하고 싶은 제도를 선택하세요:", options)

# 선택된 항목에 따른 조건문 처리
if choice == "1: 무임승차":
    st.info("🎫 **무임승차 조건 안내입니다.** (만 65세 이상 어르신, 장애인, 국가유공자 등)")
    
elif choice == "2: 바우처택시":
    st.info("🚖 **바우처택시 신청 방법 안내입니다.** (관할 주민센터 또는 관련 포털 접수)")
    
elif choice == "0: 종료":
    st.warning("🏁 종료되었습니다. 다른 정보를 보시려면 메뉴를 다시 선택해 주세요.")
    
else:
    # '선택하세요' 상태일 때는 아무것도 띄우지 않거나 안내 메시지 출력
    st.write("메뉴를 선택하시면 상세 안내가 표시됩니다.")