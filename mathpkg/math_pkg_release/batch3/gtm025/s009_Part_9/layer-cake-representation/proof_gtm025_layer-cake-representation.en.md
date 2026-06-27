---
role: proof
locale: en
of_concept: layer-cake-representation
source_book: gtm025
source_chapter: "21"
source_section: "SS 21"
---

Since $\varphi(0)=0$ and $\varphi$ is absolutely continuous, $\varphi(f(x)) = \int_0^{f(x)} \varphi'(t)dt = \int_0^\infty \mathbf{1}_{[0,f(x)]}(t)\varphi'(t)dt$. Integrate over $E$ and apply Fubini's theorem (justified since $\varphi' \geq 0$): $\int_E \varphi(f(x))d\mu(x) = \int_0^\infty \varphi'(t) \mu(E \cap \{f > t\}) dt$.
