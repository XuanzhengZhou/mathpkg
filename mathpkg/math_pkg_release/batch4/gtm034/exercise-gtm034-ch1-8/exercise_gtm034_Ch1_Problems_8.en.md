---
role: exercise
locale: en
chapter: "1"
section: "Problems"
exercise_number: 8
---

8. Let $g_n^{(r)} = E[(n - N_n)^r], r \geq 0, n \geq 0$ where $N_n$ is the number of positive partial sums in time $n$. Prove that

$$g_n^{(r+1)} = n g_n^{(r)} - \sum_{m=0}^{n-1} a_{n-m} g_m^{(r)} \quad n \geq 1, \quad r \geq 0,$$

where $a_n = P[S_n > 0]$. Using this recurrence relation prove (following Kemperman [57], p. 93) that

$$\lim_{n \to \infty} n^{-r} g_n^{(r)} = (1 - \alpha) \left(1 - \frac{\alpha}{2}\right) \cdots \left(1 - \frac{\alpha}{r}\right)$$

for all $r \geq 1$ if and only if

$$\lim_{n \to \infty} \frac{a_1 + \cdots + a_n}{n} = \alpha.$$
