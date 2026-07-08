# Django Study

Django 프로젝트 생성부터 템플릿, 모델, ORM, 폼, 정적 파일, 인증 시스템, REST API 구현까지 단계적으로 학습한 백엔드 실습 모음입니다. 단순 예제 실행을 넘어 Todo, Article, Diary, Account, Artist, Book, Station 같은 도메인을 직접 모델링하고, CRUD 화면과 API 응답까지 구현하는 흐름을 다루었습니다.

이 폴더는 Django를 사용해 웹 애플리케이션의 요청-응답 흐름, 데이터 저장, 사용자 인증, API 설계를 익혀간 기록입니다.

## 핵심 역량

- Django 프로젝트와 앱 구조 이해: `settings.py`, `urls.py`, `views.py`, `models.py`
- 요청-응답 흐름 구현: URL 라우팅, view 함수, template 렌더링
- Django Template Language 활용: 템플릿 상속, 조건문, 반복문, context 전달
- 모델링과 데이터베이스 연동: `models.Model`, migration, SQLite DB
- ORM 활용: 객체 생성, 조회, 수정, 삭제, QuerySet 처리
- CRUD 구현: 목록, 상세, 생성, 수정, 삭제 화면과 view 로직
- Django Form과 ModelForm: 입력 검증, 폼 렌더링, 저장 흐름 관리
- Static 파일 관리: 이미지, CSS, 로고 등 정적 자산 연결
- 인증 시스템 구현: 회원가입, 로그인, 로그아웃, 회원정보 수정, 비밀번호 변경
- Django REST Framework 기반 API: serializer, `@api_view`, `Response`, 상태 코드 처리

## 학습 자료

| 파일 | 내용 |
| --- | --- |
| `Django_study.pdf` | Django 학습 자료입니다. 프로젝트 구조, 템플릿, 모델/ORM, Form, Static, 인증, REST API 구현을 학습하며 참고한 문서입니다. |

## 폴더 구성

| 폴더 | 설명 |
| --- | --- |
| `1_Introduction_of_Django` | Django 입문 실습입니다. 프로젝트와 앱 생성, 기본 URL 연결, view 작성, 간단한 응답과 템플릿 렌더링을 다뤘습니다. |
| `2_templates` | Django 템플릿 실습입니다. 템플릿 상속, context 전달, 조건문/반복문을 사용해 동적인 HTML 화면을 구성했습니다. |
| `3_model` | 모델 기초 실습입니다. Django 모델 클래스를 정의하고 migration을 통해 데이터베이스 테이블을 생성하는 흐름을 학습했습니다. |
| `4_ORM` | ORM 실습입니다. Django shell과 view에서 QuerySet을 활용해 데이터를 생성, 조회, 수정, 삭제하는 방법을 다뤘습니다. |
| `5_ORM_with_view` | ORM과 view를 연결한 CRUD 실습입니다. 모델 데이터를 웹 화면에서 목록/상세/생성/수정/삭제할 수 있도록 구현했습니다. |
| `6_django_form` | Django Form과 ModelForm 실습입니다. 사용자 입력을 검증하고 모델 저장 흐름을 간결하게 관리하는 방법을 다뤘습니다. |
| `7_static` | 정적 파일 실습입니다. CSS, 이미지, 로고 등 static 자산을 Django 템플릿에 연결하고 화면을 구성했습니다. |
| `8_authentication_system_1` | 인증 시스템 기초입니다. 로그인, 로그아웃, 인증 여부에 따른 화면 분기와 접근 제어를 구현했습니다. |
| `9_authentication_system_2` | 인증 시스템 심화입니다. 회원가입, 회원정보 수정, 비밀번호 변경, 커스텀 유저 폼 등 사용자 관리 기능을 확장했습니다. |
| `10_rest_api_1` | Django REST Framework 기초입니다. serializer와 `@api_view`를 사용해 모델 데이터를 JSON API로 제공했습니다. |
| `11_rest_api_2` | REST API 심화입니다. 관계형 모델, nested serializer, 생성/수정/삭제 API, 상태 코드 처리를 확장했습니다. |

## 대표 구현 주제

| 주제 | 구현 예시 |
| --- | --- |
| 기본 요청 처리 | URL 라우팅, view 함수, template 렌더링, context 전달 |
| CRUD 웹 서비스 | Todo, Article, Diary 데이터의 목록/상세/생성/수정/삭제 |
| 모델과 ORM | `Todo`, `Article`, `Diary`, `Book`, `Artist`, `Station`, `Car` 모델 설계 |
| 폼 처리 | `ModelForm` 기반 입력 검증, 생성/수정 폼, 에러 처리 |
| 인증 기능 | 회원가입, 로그인, 로그아웃, 프로필, 회원정보 수정, 비밀번호 변경 |
| 정적 파일 관리 | static 이미지, CSS, 로고, ERD 이미지 연결 |
| REST API | 목록/상세 API, 생성/수정/삭제 API, serializer 분리, HTTP status 처리 |
| 관계형 API | `ForeignKey` 기반 추천, 위치-충전소-차량처럼 연결된 데이터 응답 |

## 실행 방법

각 실습은 대부분 독립적인 Django 프로젝트입니다. 실행하려는 과제 폴더로 이동한 뒤 가상환경을 만들고 의존성을 설치합니다.

```bash
cd Django/11_rest_api_2/django_ws_11_c
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

테스트 파일이 포함된 프로젝트는 다음 명령으로 확인할 수 있습니다.

```bash
python manage.py test
```

REST API 실습은 서버 실행 후 브라우저, Postman, Insomnia 같은 API 클라이언트로 엔드포인트를 호출해 확인할 수 있습니다.

## 학습 흐름

1. Django 프로젝트와 앱의 기본 구조를 이해하고 요청-응답 흐름을 구현했습니다.
2. 템플릿과 context를 활용해 서버 데이터를 HTML 화면에 렌더링했습니다.
3. 모델과 migration으로 데이터베이스 테이블을 정의했습니다.
4. ORM을 사용해 Python 코드로 데이터를 생성, 조회, 수정, 삭제했습니다.
5. view와 template을 연결해 CRUD 웹 서비스를 구현했습니다.
6. Form과 ModelForm으로 입력 검증과 저장 흐름을 정리했습니다.
7. static 파일과 인증 시스템을 붙여 실제 서비스에 가까운 구조로 확장했습니다.
8. Django REST Framework로 JSON API를 설계하고 serializer와 상태 코드를 다뤘습니다.
