# Canary

스택 카나리와 정보 누출(leak)을 학습하기 위한 문제 모음입니다.

## 문제 목록

| 번호 | 문제 | 목표 |
|:---:|------|------|
| 01 | [canary_leak — 카나리 누출 연습](#01-canary-leak) | 카나리의 널 바이트를 덮었을 때 발생하는 정보 누출 관찰 |
| 02 | [canary_ret2win — 카나리 누출 후 ret2win](#02-canary-ret2win) | 카나리를 복구하며 반환 주소를 `win()`으로 변경해 셸 실행 |

## 실행 방법

제공된 실행 파일은 **Linux x86-64용**입니다. Windows에서는 WSL의 x86-64 Linux 환경을 사용하세요.

저장소 루트에서 문제 폴더로 이동한 뒤, 실행 권한을 부여하고 실행합니다.

```bash
cd Canary
chmod +x canary_leak canary_ret2win
```

원하는 문제를 하나씩 실행합니다.

- **1번 문제:** `./canary_leak`
- **2번 문제:** `./canary_ret2win`

<a id="01-canary-leak"></a>

## 01. canary_leak — 카나리 누출 연습

**제공 파일:** [canary_leak](canary_leak)

오버플로를 통해 **카나리의 널 바이트를 덮어 카나리 누출(leak)을 연습하는 문제**입니다.

널 바이트를 덮었을 때 나타나는 정보 누출을 관찰하며, **스택 카나리의 널 바이트와 정보 누출의 관계를 이해하는 것**이 목표입니다.

<a id="02-canary-ret2win"></a>

## 02. canary_ret2win — 카나리 누출 후 ret2win

**제공 파일:** [canary_ret2win](canary_ret2win)

프로그램에는 **1번 이름 입력**과 **2번 메시지 입력** 기능이 있습니다.

이름 입력 과정에서 오버플로를 이용해 **스택 카나리를 누출(leak)**하고, 메시지 입력 과정에서 누출한 카나리를 보존하면서 **저장된 반환 주소를 변경하는 문제**입니다.

```text
1) Enter another name
2) Leave a message and exit
3) Quit
choice>
```

누출한 카나리를 올바른 위치에 다시 넣어 스택 보호를 통과하고, 반환 주소를 목표 함수로 바꿔 **셸을 실행하는 것**이 목표입니다.
