---
role: proof
locale: en
of_concept: zeta-function-integral-bound
source_book: gtm011
source_chapter: "7"
source_section: "8"
---

(a) Since $e^t - 1 \geq t$ for all $t \geq 0$, we have that for $0 < t \leq 1$ and $z$ in $S$,

$$|(e^t - 1)^{-1} t^{z-1}| \leq t^{a-2}.$$

Since $a > 1$, the function $t^{a-2}$ is integrable on $(0, 1]$. Hence for any $\epsilon > 0$ there exists $\delta > 0$ such that

$$\left| \int_\alpha^\beta (e^t - 1)^{-1} t^{z-1} \, dt \right| \leq \int_\alpha^\beta t^{a-2} \, dt < \epsilon$$

whenever $\delta > \beta > \alpha > 0$. This proves (a).

(b) For $t \geq 1$ and $z$ in $S$, we have $e^t - 1 \geq \frac{1}{2} e^t$ (since $e^t \geq 2$ for $t \geq \log 2$, and for $t \geq 1$ we have $e^t - 1 = e^t(1 - e^{-t}) \geq e^t(1 - e^{-1}) \geq \frac{1}{2} e^t$). Thus

$$|(e^t - 1)^{-1} t^{z-1}| \leq 2 e^{-t} t^{\text{Re } z - 1} \leq 2 e^{-t} t^{A-1}$$

for all $t \geq 1$ and $z$ in $S$. Since $e^{-t} t^{A-1}$ is integrable on $[1, \infty)$ for any fixed $A$, there exists $\kappa > 1$ such that

$$\left| \int_\alpha^\beta (e^t - 1)^{-1} t^{z-1} \, dt \right| \leq 2 \int_\alpha^\beta e^{-t} t^{A-1} \, dt < \epsilon$$

whenever $\beta > \alpha > \kappa$. This proves (b).
