---
role: exercise
locale: en
chapter: "III"
section: "e"
exercise_number: 15
---

Using random numbers, estimate the 4-dimensional integral $\int_{[0,1]^4} \prod_{i=1}^4 (1-u_i/2) du_1\cdots du_4$ with $n=15$ samples. The exact value is $(\int_0^1 (1-u/2)du)^4 = (3/4)^4 = 81/256 \approx 0.3164$. With only 15 samples, the Monte Carlo estimate will have substantial variability (standard error $\approx \sigma/\sqrt{15}$).
