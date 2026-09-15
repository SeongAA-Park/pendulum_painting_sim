# Spherical pendulum simulation

Pygame과 NumPy를 사용한 감쇠 구면 진자의 궤적 시뮬레이션입니다. 위에서 본 화면과 옆에서 본 화면을 각각 실행할 수 있습니다.

## 실행

Python 가상환경에서 `pip install -r requirements.txt`로 의존성을 설치한 뒤 다음 중 하나를 실행하세요.

```bash
python "(top)spherical_pendulum_with_dissipation_2020251096_박성아.py"
python "(side)spherical_pendulum_with_dissipation_2020251096_박성아.py"
```

`T` 키로 궤적 표시를 전환하고, `C` 키로 궤적을 지울 수 있습니다.

## 참고 코드

이 시뮬레이션은 [apf99의 SphericalPendulumAnimation](https://github.com/apf99/SphericalPendulumAnimation) 코드를 참고해 작성했습니다.
