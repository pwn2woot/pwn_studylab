# Canary

스택 카나리와 정보 누출(leak)을 학습하기 위한 문제 모음입니다.

## 문제 목록

| 번호 | 문제 | 목표 |
|:---:|------|------|
| 01 | [canary_leak — 카나리 누출 연습](#01-canary-leak) | 카나리의 널 바이트를 덮었을 때 발생하는 정보 누출 관찰 |

## 실행 방법

제공된 `canary_leak`는 **Linux x86-64용 실행 파일**입니다. Windows에서는 WSL의 x86-64 Linux 환경을 사용하세요.

저장소 루트에서 문제 폴더로 이동한 뒤, 실행 권한을 부여하고 실행합니다.

```bash
cd Canary
chmod +x canary_leak
./canary_leak
```

<a id="01-canary-leak"></a>

## 01. canary_leak — 카나리 누출 연습

**제공 파일:** [canary_leak](canary_leak)

오버플로를 통해 **카나리의 널 바이트를 덮어 카나리 누출(leak)을 연습하는 문제**입니다.

널 바이트를 덮었을 때 나타나는 정보 누출을 관찰하며, **스택 카나리의 널 바이트와 정보 누출의 관계를 이해하는 것**이 목표입니다.
