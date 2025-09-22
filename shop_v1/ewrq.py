import streamlit as st
import pandas as pd
import shopdbmng

st.set_page_config(layout="wide")

# ------------------------------------------------
# 초기 세션 상태
# ------------------------------------------------
if "show_list" not in st.session_state:
    st.session_state.show_list = False

if "members" not in st.session_state:
    datas = shopdbmng.readAll_customers()  # 예: [{'id':1,'name':'홍길동'}, ...] or list of tuples
    df = pd.DataFrame(datas)

    # ① 컬럼명 강제 통일: DB 컬럼이 id/name이어도 UI는 회원아이디/회원이름으로 씁니다.
    if not df.empty:
        # 열 이름 추정 & 매핑
        rename_map = {}
        cols = df.columns.tolist()
        if "회원아이디" not in cols:
            # 후보: id, member_id
            for cand in ["id", "member_id", "아이디"]:
                if cand in cols:
                    rename_map[cand] = "회원아이디"
                    break
        if "회원이름" not in cols:
            for cand in ["name", "member_name", "이름"]:
                if cand in cols:
                    rename_map[cand] = "회원이름"
                    break
        if rename_map:
            df = df.rename(columns=rename_map)

        # 최소한 필요한 컬럼만 남기기 (없으면 생성)
        if "회원아이디" not in df.columns:
            df["회원아이디"] = None
        if "회원이름" not in df.columns:
            df["회원이름"] = None

        # 인덱스 안정성 확보
        df = df.reset_index(drop=False).rename(columns={"index": "row_index"})
        df = df.set_index("row_index")
    else:
        df = pd.DataFrame(columns=["회원아이디", "회원이름"])

    st.session_state.members = df

if "selected_member_index" not in st.session_state:
    st.session_state.selected_member_index = None

left_col, right_col = st.columns([1, 3])

# ------------------------------------------
# ① 왼쪽: 회원 버튼
# ------------------------------------------
with left_col:
    st.header("회원")
    if st.button("회원 리스트 보기", type="primary"):
        st.session_state.show_list = True

# ------------------------------------------
# ② 오른쪽: 회원 리스트 & 입력폼
# ------------------------------------------
with right_col:
    st.header("회원 리스트")

    if st.session_state.show_list:
        df = st.session_state.members

        if df.empty:
            st.info("현재 등록된 회원이 없습니다.")
        else:
            st.dataframe(df[["회원아이디", "회원이름"]], use_container_width=True)

            # df.index(=row_index)를 옵션으로 사용 → 인덱스 꼬임 방지
            selected_index = st.selectbox(
                "회원 선택",
                options=df.index.tolist(),
                format_func=lambda idx: f"{df.loc[idx, '회원아이디']} - {df.loc[idx, '회원이름']}",
                key="member_selector"
            )
            if selected_index is not None:
                st.session_state.selected_member_index = selected_index

        st.divider()

        # 입력 영역
        if (not df.empty) and (st.session_state.selected_member_index is not None):
            selected = df.loc[st.session_state.selected_member_index]

            # 기존 회원 편집: PK는 읽기 전용
            member_id_str = st.text_input("회원아이디 (수정 불가)", value=str(selected.get("회원아이디", "")), disabled=True, key="edit_id")
            member_name = st.text_input("회원이름", value=str(selected.get("회원이름", "")), key="edit_name")

            col_a, col_b, col_c = st.columns(3)
            with col_a:
                if st.button("수정 저장"):
                    # 타입 정리
                    try:
                        member_id = int(member_id_str)
                    except:
                        st.error("회원아이디가 정수가 아닙니다. DB PK가 정수면 스키마를 확인하세요.")
                        st.stop()

                    # 세션 DF 업데이트
                    st.session_state.members.at[st.session_state.selected_member_index, "회원이름"] = member_name

                    # DB 업데이트 (시그니처 확인: 일반적으로 (id, name))
                    shopdbmng.update_customer(member_id, member_name)

                    st.success("수정 완료")
                    del st.session_state.members  # 캐시 무효화 → 상단에서 재로딩
                    st.rerun()
            with col_b:
                if st.button("입력 초기화"):
                    st.session_state.selected_member_index = None
                    st.rerun()
            with col_c:
                pass

        else:
            # 신규 등록
            st.subheader("신규 회원 등록")
            # 보통 PK는 AUTO_INCREMENT이므로 아이디는 입력 안 받는 것이 안전
            new_name = st.text_input("회원이름", key="new_name")

            col_a, col_b = st.columns(2)
            with col_a:
                if st.button("신규 저장"):
                    if not new_name.strip():
                        st.warning("회원이름을 입력하세요.")
                        st.stop()
                    # DB 삽입: create_customer(name)
                    shopdbmng.create_customer(new_name.strip())

                    st.success("회원 추가 완료")
                    # 테이블 최신화
                    del st.session_state.members
                    st.rerun()
            with col_b:
                if st.button("입력 초기화(신규)"):
                    st.session_state.selected_member_index = None
                    st.rerun()
    else:
        st.info("왼쪽에서 ‘회원 리스트 보기’를 클릭하세요.")
