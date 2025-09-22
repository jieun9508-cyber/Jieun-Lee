import streamlit as st
if 'count' not in st.session_state :
    st.session_state.count = 0
if st.button('카운트 증가') :
    st.write('버튼 클릭됨')
    st.session_state['count'] += 1
st.write('현재 카운트:', st.session_state['count'])
st.json(st.session_state)  #세션 상태 확인
st.session_state.count += 1