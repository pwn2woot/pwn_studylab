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
| 04 | [Maze Golf — `maze_golf`](pwntools_training/README.md#04-maze-golf) | 초급+ | WASD 미로 탈출과 Pwntools 풀이 파일 바이트 수 최적화 |

### [BufOverfow](BufOverfow/)

버퍼 오버플로를 학습하기 위한 문제 모음입니다.

| 번호 | 문제 | 난이도 | 설명 |
|:---:|------|:------:|------|
| 01 | [셸 호출 함수 실행 — `bof`](BufOverfow/README.md#01-bof) | 기초 | 바이너리 내부의 셸 호출 함수 실행 |
| 02 | [비밀번호 변경 — `password_bof`](BufOverfow/README.md#02-password-bof) | 기초 | 오버플로로 비밀번호를 변경한 뒤 인증해 셸 획득 |

### [Canary](Canary/)

스택 카나리와 정보 누출(leak)을 학습하기 위한 문제 모음입니다.

| 번호 | 문제 | 난이도 | 설명 |
|:---:|------|:------:|------|
| 01 | [카나리 누출 연습 — `canary_leak`](Canary/README.md#01-canary-leak) | 기초 | 오버플로로 카나리의 널 바이트를 덮어 leak 연습 |
| 02 | [카나리 누출 후 ret2win — `canary_ret2win`](Canary/README.md#02-canary-ret2win) | 쉬움 | 이름 출력에서 카나리를 구한 뒤 `win()`으로 복귀해 셸 실행 |

## Getting Started

저장소를 내려받습니다.

```bash
git clone https://github.com/pwn2woot/pwn_studylab.git
cd pwn_studylab
```

문제 목록에서 원하는 문제를 선택한 뒤, 해당 폴더의 `README.md`를 따라 진행합니다.

첫 연습은 [Pwntools Training](pwntools_training/)에서 시작할 수 있습니다. 실행 환경과 준비 방법은 해당 폴더의 README에 안내되어 있습니다.

문제마다 필요한 운영체제, 라이브러리, 실행 방법이 다를 수 있습니다.
