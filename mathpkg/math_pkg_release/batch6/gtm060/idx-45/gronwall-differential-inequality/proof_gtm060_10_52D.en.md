---
role: proof
locale: en
of_concept: gronwall-differential-inequality
source_book: gtm060
source_chapter: "10"
source_section: "52D"
---

$|z(t)|$ is no greater than the solution $y(t)$ of the equation $\dot{y} = ay + b$, $y(0) = d$. Solving this equation, we find

$$y = Ce^{at}, \quad \dot{C}e^{at} = b, \quad \dot{C} = e^{-at}b, \quad C(0) = d,$$

hence $C \leq d + bt$. Therefore $|z(t)| \leq y(t) = Ce^{at} \leq (d + bt)e^{at}$.
