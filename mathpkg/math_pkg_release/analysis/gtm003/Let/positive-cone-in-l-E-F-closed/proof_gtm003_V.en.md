---
role: proof
locale: en
of_concept: positive-cone-in-l-E-F-closed
source_book: gtm003
source_chapter: "V"
source_section: "5.1"
---

The bilinear map $(u, x) \mapsto u(x)$ is separately continuous, so $f_x: u \mapsto u(x)$ is continuous. Since $\mathcal{H} = \bigcap \{f_x^{-1}(D): x \in C\}$ where $D$ is the positive cone of $F$ (closed), $\mathcal{H}$ is closed. For properness: $u \in \mathcal{H} \cap -\mathcal{H}$ implies $u(x)=0$ for $x \in C$, so $u=0$ if $C$ is total. Conversely, if $C$ is not total, Hahn-Banach gives $f \in E'$ with $f \neq 0$ but $f(C)=\{0\}$; then $u = f \otimes y$ ($y \neq 0$) satisfies $u \in \mathcal{H} \cap -\mathcal{H}$.
