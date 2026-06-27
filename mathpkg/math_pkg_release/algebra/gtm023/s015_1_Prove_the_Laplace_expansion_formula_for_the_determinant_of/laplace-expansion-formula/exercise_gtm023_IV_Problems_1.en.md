---
role: exercise
locale: en
chapter: "IV"
section: "Problems"
exercise_number: 1
---

Prove the Laplace expansion formula for the determinant of an $(n \times n)$-matrix: Let $p$ ($1 \leq p \leq n-1$) be a fixed integer. Then

$$\det A = \sum_{v_1 < \dots < v_p} \varepsilon(v_1, \dots, v_p) \det A^{v_1 \dots v_p} \det B^{v_{p+1} \dots v_n}$$

where

$$A^{v_1 \dots v_p} = A_{1 \dots p}^{v_1 \dots v_p}$$

$$B^{v_{p+1} \dots v_n} = A_{p+1 \dots n}^{v_{p+1} \dots v_n}$$

and

$$\varepsilon(v_1, \dots, v_p) = (-1)^{\sum_{i=1}^{p} (v_i - i)}.$$
