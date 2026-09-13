<p align="center">
  <img src="assets/study.png" alt="Study" width="360">
</p>

# Pwn Study Lab

시스템 해킹과 바이너리 분석을 공부하기 위한 Pwn 문제 모음입니다.

각 문제의 설명, 실행 환경, 제공 파일은 해당 문제 폴더에서 확인할 수 있습니다.

## Problems

### [Pwntools Training](pwntools_training/)

메뉴 조작, 바이트 전송, 반복 입출력을 익히는 기초 연습 세트입니다.

| 번호 | 문제 | 난이도 | 설명 |
|:---:|------|:------:|------|
| 01 | [랜덤 비밀번호 입력 — `01_menu`](pwntools_training/README.md#01-menu) | 기초 | 메뉴 자동화, 비밀번호 추출, `sendlineafter()` |
| 02 | [64비트 정수 전송 — `02_pack64`](pwntools_training/README.md#02-pack64) | 기초 | 리틀 엔디언, `p64()`, `sendafter()` |
| 03 | [3초 덧셈 계산기 — `03_rounds`](pwntools_training/README.md#03-rounds) | 기초 | 숫자 추출, 반복문, `sendline()` |

### [BufOverfow](BufOverfow/)

버퍼 오버플로를 학습하기 위한 문제 모음입니다.

| 번호 | 문제 | 난이도 | 설명 |
|:---:|------|:------:|------|
| 01 | [셸 호출 함수 실행 — `bof`](BufOverfow/README.md#01-bof) | 기초 | 바이너리 내부의 셸 호출 함수 실행 |

## Getting Started

저장소를 내려받습니다.

```bash
git clone https://github.com/pwn2woot/pwn_studylab.git
cd pwn_studylab
```

문제 목록에서 원하는 문제를 선택한 뒤, 해당 폴더의 `README.md`를 따라 진행합니다.

첫 연습은 [Pwntools Training](pwntools_training/)에서 시작할 수 있습니다. 실행 환경과 준비 방법은 해당 폴더의 README에 안내되어 있습니다.

문제마다 필요한 운영체제, 라이브러리, 실행 방법이 다를 수 있습니다.
