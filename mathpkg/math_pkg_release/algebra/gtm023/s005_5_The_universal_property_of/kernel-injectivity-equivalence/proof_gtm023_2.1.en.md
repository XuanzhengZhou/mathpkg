---
role: proof
locale: en
of_concept: kernel-injectivity-equivalence
source_book: gtm023
source_chapter: "2"
source_section: "2.1"
---

If $\varphi$ is injective, there is at most one vector $x \in E$ with $\varphi x = 0$. Since $\varphi 0 = 0$, it follows that $\ker \varphi = \{0\}$.

Conversely, assume $\ker \varphi = \{0\}$. If $\varphi x_1 = \varphi x_2$ for $x_1, x_2 \in E$, then $\varphi(x_1 - x_2) = 0$, so $x_1 - x_2 \in \ker \varphi = \{0\}$. Hence $x_1 = x_2$, proving $\varphi$ is injective.
