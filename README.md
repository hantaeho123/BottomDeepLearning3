# 🏸 민턴 각? (Minton-Angle)

<div align="center">
  <img src="https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <br>
  <i>"오늘 배드민턴 각?" 배드민턴 입문자를 위한 실시간 AI 코칭 앱</i>
  <br><br>
  <b>🔗 서비스 링크:</b> <a href="https://minton-angle.vercel.app">minton-angle.vercel.app</a>
</div>

---

## 🎯 1. 프로젝트 개요 (Overview)
배드민턴은 남녀노소 즐기는 압도적인 인기 스포츠이지만, 입문자들이 겪는 진입 장벽이 존재합니다. 레슨을 받기에는 시간과 장소가 한정적이고 비용이 부담되며, 기존 서비스들은 "스윙을 열심히 연습해보세요"와 같은 추상적인 피드백을 제공하여 자기주도 학습에 한계가 있었습니다.

> **민턴 각?**은 이러한 문제를 해결하기 위해 **컴퓨터 비전(CV)과 LLM을 결합**하여, 스마트폰 하나로 언제 어디서나 전문가 수준의 1:1 맞춤형 AI 코칭을 받을 수 있는 서비스를 제공합니다.

---

## ✨ 2. 주요 기능 (Key Features)

### 🏸 그립 교정 (Grip Correction)
* 부상 방지와 실력 향상의 기초인 **'올바른 포핸드 그립'** 여부를 실시간으로 판별합니다.
* 오답 클래스(테니스 그립, 검지 펴짐, 엄지 펴짐 등)를 직관적으로 분석하여 피드백을 제공합니다.

### 🧍‍♂️ 기본 스윙 자세 교정 (Swing Posture Correction)
* 스윙을 **3단계(준비, 백스윙, 임팩트/팔로우)** 로 구분하여 세분화된 자세 분석을 제공합니다.
* 전문가(국가대표 선출 코치)의 정석 자세(Ground Truth)와 내 자세를 1:1로 비교 시각화하여 문제점을 정확히 짚어줍니다.

### 📊 LLM 종합 AI 피드백 리포트 (Comprehensive Report)
* 과거 기록을 바탕으로 주/월 단위 성장 추이와 자세 변동성을 분석합니다.
* 점수가 낮고 변동성이 큰 동작을 찾아내어, **RAG 기반 맞춤형 코칭 피드백**과 연관된 **유튜브 추천 영상**을 제공합니다.

---

## 🛠 3. 기술 스택 (Tech Stack)

### 💻 Frontend & Backend
<img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"> <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"> <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"> <img src="https://img.shields.io/badge/Vercel-000000?style=flat-square&logo=vercel&logoColor=white">
<br>
<img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"> <img src="https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazon-aws&logoColor=white"> <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white">
<br>
<img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white">

### 🧠 AI & Computer Vision
<img src="https://img.shields.io/badge/YOLO11n-00FFFF?style=flat-square&logo=yolo&logoColor=black"> <img src="https://img.shields.io/badge/MediaPipe-005571?style=flat-square"> <img src="https://img.shields.io/badge/TrackNetV3-FF4B4B?style=flat-square"> <img src="https://img.shields.io/badge/Llama_3.1-0466C8?style=flat-square&logo=meta&logoColor=white">

---

## 🏗 4. 시스템 아키텍처 및 API 설계

### 🗄 Database (ERD 요약)
* `USER`: 사용자 계정 및 인증 정보 관리
* `POST`: 분석 세션 관리 (실시간/동영상) 및 종합 점수
* `FILE`: 키프레임 이미지 및 영상 파일 경로 저장
* `ANALYSIS`: CV 분석 결과 및 단계별 오차/점수 저장
* `LLM_REPORT`: 생성된 맞춤형 LLM 피드백 보관

### 📡 주요 API (FastAPI)
| Domain | Method | Endpoint | Description |
| :--- | :---: | :--- | :--- |
| **User** | `GET` | `/api/auth/check-id` | 아이디 중복 확인 |
| (Auth) | `POST`/`PUT` | `/api/auth/signup`, `me` | 회원가입, 정보수정 |
| **Realtime** | `POST` | `/api/realtime/analyze-swing`| 실시간 스윙 분석 (웹캠 3회) |
| **Upload** | `POST` | `/api/upload/video` | 동영상 업로드 및 분석 |
| **Report** | `GET` | `/api/report/analysis/...` | 스윙 분석/LLM 리포트 조회 |
| **Grip** | `POST` | `/api/grip/analyze` | 그립 이미지 분석 진단 |

---

## 🧠 5. 핵심 AI 알고리즘 (Core AI Algorithms)

### 5.1. 그립 분류 알고리즘 (YOLO11n)
* **접근 방식의 전환:** 초기 MediaPipe의 한계(손가락 겹침 등)를 극복하고자 단순 각도 계산 방식을 버리고 **YOLO 기반의 객체 분류(Classification) 모델로 재정의**했습니다.
* **모델 최적화:** 정확도(mAP50 0.987)와 추론 속도, 모델 크기를 평가하여 **YOLO11n**을 최종 채택했습니다. (클래스 6종 판별)

### 5.2. 스윙 자세 교정 알고리즘 (MediaPipe & FastDTW)
국가대표 출신 코치의 완벽한 스윙 동작을 Ground Truth(GT)로 삼고 100점 만점 평가를 진행합니다.
* **전처리 및 동기화:** 어깨/골반 기준 스켈레톤 정규화 및 `FastDTW`를 이용한 전문가-사용자 프레임 동기화.
* **세부 평가 지표 (10종):** 팔꿈치 각도/높이, 스탠스 너비(Ready) / 회전율, 손목 깊이, L자 각도(Backswing) / 궤적 교차 검증(Impact & Follow).

### 5.3. 맞춤형 LLM 코칭 (RAG Architecture)
* 배드민턴 코칭 매뉴얼을 임베딩(`intfloat/multilingual-e5-base`)하여 벡터 DB에 구축.
* 분석된 약점 데이터를 바탕으로 Llama 3.1 모델이 구체적인 교정 방법과 리포트를 생성합니다.

---

## 🚀 6. R&D 및 트러블슈팅 (Troubleshooting)

* **🔴 셔틀콕 궤적 분석의 환경적 한계 (R&D):** 하얀 벽 보호색, 조명 노이즈 등으로 일반 체육관 환경에서 비전 AI의 추적 한계를 확인. 무리한 도입 대신 기능 보완 후 업데이트 예정.
* **🟢 브라우저 캐시 오염 동기화 에러:** 프론트/백엔드 연동 중 발생한 세션 오염 문제를 `localStorage.clear()` 로직 명시를 통해 데이터 싱크 실패 완벽 해결.
* **🟢 MediaPipe 그립 분석 한계 극복:** 촬영 구도에 따른 성능 편차 문제를 **YOLO11n 파인튜닝을 통한 객체 분류 방식으로 재정의**하여 해결.

---

## 👨‍💻 7. 팀원 소개 및 역할 (Team)

<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/팀원1아이디"><img src="https://github.com/팀원1아이디.png" width="100px;" alt=""/><br /><sub><b>노은서</b></sub></a><br />팀장/PM</td>
    <td align="center"><a href="https://github.com/팀원2아이디"><img src="https://github.com/팀원2아이디.png" width="100px;" alt=""/><br /><sub><b>김민지</b></sub></a><br />프론트엔드<br>스윙 알고리즘</td>
    <td align="center"><a href="https://github.com/팀원3아이디"><img src="https://github.com/팀원3아이디.png" width="100px;" alt=""/><br /><sub><b>이원호</b></sub></a><br />백엔드<br>LLM 리포트</td>
    <td align="center"><a href="https://github.com/팀원4아이디"><img src="https://github.com/팀원4아이디.png" width="100px;" alt=""/><br /><sub><b>권주은</b></sub></a><br />백엔드<br>자세교정 알고리즘</td>
    <td align="center"><a href="https://github.com/팀원5아이디"><img src="https://github.com/팀원5아이디.png" width="100px;" alt=""/><br /><sub><b>한태호</b></sub></a><br />셔틀콕 궤적<br>그립 알고리즘</td>
  </tr>
</table>
<p align="center"><i>멋쟁이사자처럼 AICV 3기 종합 프로젝트</i></p>





## ✨ 8. 데모 영상 (Demo & Features)

앱의 핵심 기능과 실제 동작 화면입니다.

| 🏸 8.1 그립 교정 | 🎥 8.2 실시간 레슨 모드 |
| :---: | :---: |
| <video src="https://github.com/user-attachments/assets/f5c024e4-2fc8-47ab-afb7-af6814f3000f" autoplay loop muted playsinline width="100%"></video> | <video src="https://github.com/user-attachments/assets/9aae412e-16f1-484b-815e-41b4d04210fe" autoplay loop muted playsinline width="100%"></video> |
| **YOLO11n 기반 실시간 판별**<br>올바른 그립과 잘못된 그립을 분류하고 즉각적인 피드백을 제공합니다. | **웹캠 기반 스윙 추적**<br>사용자의 스윙 동작을 3단계로 분석하여 음성 코칭과 가이드를 제공합니다. |

| 📊 8.3 전문가 vs 초보자 스윙 비교 |
| :---: |
| <video src="https://github.com/user-attachments/assets/f73b143d-3ac7-4096-91c4-07d7e8f035d6" autoplay loop muted playsinline width="60%"></video> |
| **정석 자세 1:1 시각화**<br>초보자(65점)와 전문가(90점)의 자세 차이를 직관적으로 비교 분석합니다. |

| 📅 8.4 성장 리포트 및 캘린더 | ⚙️ 8.5 마이페이지 (계정 관리) |
| :---: | :---: |
| <video src="https://github.com/user-attachments/assets/f78e6aa3-2811-4aa9-ae94-401de94775ac" autoplay loop muted playsinline width="120%"></video> | <video src="https://github.com/user-attachments/assets/74bed9c2-a241-4f32-b0a7-c5dc92c738f6" autoplay loop muted playsinline width="120%"></video> |
| **기간별 성장 추이 확인**<br>누적된 데이터를 바탕으로 LLM 종합 피드백과 유튜브 영상을 추천합니다. | **사용자 설정 및 탈퇴**<br>개인 정보 수정 및 안전한 계정 관리 기능을 제공합니다. |













