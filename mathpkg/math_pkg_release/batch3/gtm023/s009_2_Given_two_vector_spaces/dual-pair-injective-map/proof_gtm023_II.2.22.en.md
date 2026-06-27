---
role: proof
locale: en
of_concept: dual-pair-injective-map
source_book: gtm023
source_chapter: "II"
source_section: "2.22"
---

Fix a vector $a^* \in E^*$. Then a linear function $f_{a^*}$ is defined in $E$ by
$$f_{a^*}(x) = \langle a^*, x \rangle, \quad x \in E.$$
The bilinearity of the scalar product ensures $f_{a^*}$ is linear. Define $\Phi(a^*) = f_{a^*}$. Then $\Phi: E^* \rightarrow L(E)$ is linear because for $a^*, b^* \in E^*$ and scalars $\lambda$,
$$\Phi(\lambda a^* + b^*)(x) = \langle \lambda a^* + b^*, x \rangle = \lambda \langle a^*, x \rangle + \langle b^*, x \rangle = (\lambda \Phi(a^*) + \Phi(b^*))(x).$$
To show injectivity, suppose $\Phi(a^*) = 0$, i.e., $\Phi(a^*)(x) = \langle a^*, x \rangle = 0$ for all $x \in E$. Since the scalar product is non-degenerate, this implies $a^* = 0$. Hence $\Phi$ is injective.
