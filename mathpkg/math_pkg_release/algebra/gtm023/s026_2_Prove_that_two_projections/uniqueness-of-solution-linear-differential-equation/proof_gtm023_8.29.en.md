---
role: proof
locale: en
of_concept: uniqueness-of-solution-linear-differential-equation
source_book: gtm023
source_chapter: "8"
source_section: "8.29"
---

Let $\varphi_1(t)$ and $\varphi_2(t)$ be two solutions and set $\varphi(t) = \varphi_2(t) - \varphi_1(t)$. Then $\varphi(t_0) = 0$ and $\dot{\varphi}(t) = \psi(t) \circ \varphi(t)$. Hence $|\varphi(t)| = |\int_{t_0}^{t} \dot{\varphi}(t) \, dt| \leq \int_{t_0}^{t} |\dot{\varphi}(t)| \, dt \leq M \int_{t_0}^{t} |\varphi(t)| \, dt$.

Define $F(t) = \int_{t_0}^{t} |\varphi(t)| \, dt$. Then $\dot{F}(t) = |\varphi(t)| \leq M F(t)$, so $\dot{F}(t) e^{-tM} - M e^{-tM} F(t) \leq 0$, i.e. $\frac{d}{dt}(F(t)e^{-tM}) \leq 0$. Integrating from $t_0$ to $t$ and using $F(t_0) = 0$ gives $F(t)e^{-tM} \leq 0$, so $F(t) \leq 0$. But $F(t) \geq 0$ by definition, hence $F(t) = 0$ and $\varphi(t) = 0$ for all $t$.
