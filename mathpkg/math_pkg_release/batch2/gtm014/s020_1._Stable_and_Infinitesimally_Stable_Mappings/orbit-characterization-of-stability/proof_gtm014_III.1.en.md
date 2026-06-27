---
role: proof
locale: en
of_concept: orbit-characterization-of-stability
source_book: gtm014
source_chapter: "III"
source_section: "§1. Stable and Infinitesimally Stable Mappings"
---

Let $g \in \operatorname{Diff}(X)$ and $h \in \operatorname{Diff}(Y)$. Let $\gamma_{(g,h)}: C^\infty(X, Y) \to C^\infty(X, Y)$ be induced by the action of $\operatorname{Diff}(X) \times \operatorname{Diff}(Y)$ on $C^\infty(X, Y)$. Thus $\gamma_{(g,h)} = h_* \circ (g^{-1})^*$ and $\gamma_{(g,h)}$ is continuous by Proposition II.3.5. Moreover $\gamma_{(g,h)}$ is a homeomorphism since $\gamma_{(g^{-1}, h^{-1})} \circ \gamma_{(g,h)} = \operatorname{id}_{C^\infty(X, Y)}$.

Now observe that $f'$ is in the orbit of $f$ if and only if $f'$ is equivalent to $f$. Also the orbit of $f$ is open if and only if there is an open neighborhood of $f$ in $C^\infty(X, Y)$ contained in the orbit of $f$ (since any such neighborhood can be translated by an element of $\operatorname{Diff}(X) \times \operatorname{Diff}(Y)$, i.e., by $\gamma_{(g,h)}$, to an open neighborhood around any other point in the orbit). These two facts taken together immediately yield that $f$ is stable if and only if the orbit $G \cdot f$ is open.
