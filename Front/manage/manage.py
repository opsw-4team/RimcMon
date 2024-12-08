import streamlit as st
import requests
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")
from Python_Script.select_from_db import get_mysql_data
from Python_Script_Manage.select_from_db import get_user_data

# 데이터 수정
def edit_entry(data, entry_id, updated_entry):
    for i, item in enumerate(data):
        if item["id"] == entry_id:
            data[i] = updated_entry
            break
    return data

def page_1():
    if "page" not in st.session_state:
        st.session_state["page"] = "list"  # 기본 페이지는 리스트

    # 현재 데이터베이스의 공모전 JSON 데이터를 로드
    data = get_mysql_data()

   # 목록 페이지
    if st.session_state["page"] == "list":
        st.title("공모전 관리 (" + str(len(data)) + ")")

        # 데이터 출력
        for entry in data:
            col1, col2, col3 = st.columns([1, 8, 2])
            with col1:
                st.write(entry["id"])
            with col2:
                st.write(entry["title"])
            with col3:
                edit_btn = st.button("수정", key=f"edit-{entry['id']}")

                if edit_btn:
                    st.session_state["edit_id"] = entry["id"]
                    st.session_state["page"] = "edit"
                    st.rerun()

    # 수정 페이지
    elif st.session_state["page"] == "edit":
        st.title("게시판 수정")

        # 수정할 데이터 가져오기
        edit_id = st.session_state.get("edit_id")
        entry_to_edit = next((item for item in data if item["id"] == edit_id), None)

        if entry_to_edit:
            # 수정 폼
            updated_title = st.text_input("제목", value=entry_to_edit["title"])
            updated_date = st.text_input("날짜", value=entry_to_edit["date"])
            updated_image = st.text_input("이미지 URL", value=entry_to_edit["image"])

            col1, col2, col3, col4 = st.columns([1,1,1,7])
            # 저장 버튼
            with col1:
                if st.button("저장"):
                    updated_entry = {
                        "id": edit_id,
                        "title": updated_title,
                        "date": updated_date,
                        "image": updated_image,
                    }
                    data = edit_entry(data, edit_id, updated_entry)

                    # 요청을 보낼 URL
                    url = "http://opsw4.dothome.co.kr/update_crawl_data.php"
                    response = requests.get(url, params=updated_entry)

                    # 응답 출력
                    if response.status_code == 200:
                        print("응답 성공:", response.text)
                    else:
                        print("요청 실패:", response.status_code)

                    st.session_state["page"] = "list"
                    st.rerun()
            with col2:
                # 삭제 버튼
                if st.button("삭제"):
                    # 요청을 보낼 URL
                    url = "http://opsw4.dothome.co.kr/delete_crawl_data.php"
                    response = requests.get(url, params={"id": edit_id})

                    # 응답 출력
                    if response.status_code == 200:
                        print("응답 성공:", response.text)
                    else:
                        print("요청 실패:", response.status_code)

                    st.session_state["page"] = "list"
                    st.rerun()
            with col3: 
                # 취소 버튼
                if st.button("취소"):
                    st.session_state["page"] = "list"
                    st.rerun()
            with col4:
                pass
        else:
            st.error("수정할 항목을 찾을 수 없습니다.")
            if st.button("목록으로 돌아가기"):
                st.session_state["page"] = "list"
                st.rerun()


def page_2():
    if "page" not in st.session_state:
        st.session_state["page"] = "list"  # 기본 페이지는 리스트

    # 현재 데이터베이스의 유저 JSON 데이터를 로드
    data = get_user_data()

   # 목록 페이지
    if st.session_state["page"] == "list":
        st.title("유저 정보 관리 (" + str(len(data)) + ")")

        # 데이터 출력
        for entry in data:
            col1, col2, col3 = st.columns([1, 8, 2])
            with col1:
                st.write(entry["id"])
            with col2:
                st.write(entry["name"])
            with col3:
                edit_btn = st.button("수정", key=f"edit-{entry['id']}")

                if edit_btn:
                    st.session_state["edit_id"] = entry["id"]
                    st.session_state["page"] = "edit"
                    st.rerun()
    
    # 수정 페이지
    elif st.session_state["page"] == "edit":
        st.title("게시판 수정")

        # 수정할 데이터 가져오기
        edit_id = st.session_state.get("edit_id")
        entry_to_edit = next((item for item in data if item["id"] == edit_id), None)

        if entry_to_edit:
            # 수정 폼
            updated_name = st.text_input("이름", value=entry_to_edit["name"])
            updated_bio = st.text_input("bio", value=entry_to_edit["bio"])
            updated_tool = st.text_input("tool", value=entry_to_edit["tool"])

            col1, col2, col3, col4 = st.columns([1,1,1,7])
            # 저장 버튼
            with col1:
                if st.button("저장"):
                    updated_entry = {
                        "id": edit_id,
                        "name": updated_name,
                        "bio": updated_bio,
                        "tool": updated_tool,
                    }
                    data = edit_entry(data, edit_id, updated_entry)

                    # 요청을 보낼 URL
                    url = "http://opsw4.dothome.co.kr/update_user_data_manage.php"
                    response = requests.get(url, params=updated_entry)

                    # 응답 출력
                    if response.status_code == 200:
                        print("응답 성공:", response.text)
                    else:
                        print("요청 실패:", response.status_code)

                    st.session_state["page"] = "list"
                    st.rerun()
            with col2:
                # 삭제 버튼
                if st.button("삭제"):
                    # 요청을 보낼 URL
                    url = "http://opsw4.dothome.co.kr/delete_user_data_manage.php"
                    response = requests.get(url, params={"id": edit_id})

                    # 응답 출력
                    if response.status_code == 200:
                        print("응답 성공:", response.text)
                    else:
                        print("요청 실패:", response.status_code)

                    st.session_state["page"] = "list"
                    st.rerun()
            with col3: 
                # 취소 버튼
                if st.button("취소"):
                    st.session_state["page"] = "list"
                    st.rerun()
            with col4:
                pass
        else:
            st.error("수정할 항목을 찾을 수 없습니다.")
            if st.button("목록으로 돌아가기"):
                st.session_state["page"] = "list"
                st.rerun()



pg = st.navigation([st.Page(page_1, title="공모전 정보"), st.Page(page_2, title="유저 정보")])
pg.run()