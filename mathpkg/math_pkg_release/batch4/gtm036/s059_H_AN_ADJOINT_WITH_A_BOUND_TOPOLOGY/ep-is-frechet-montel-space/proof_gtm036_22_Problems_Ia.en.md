---
role: proof
locale: en
of_concept: ep-is-frechet-montel-space
source_book: gtm036
source_chapter: "22"
source_section: "Problems I(a)"
---
To show that $E_p$ is a Montel space, it suffices to prove that every closed bounded set $B \subseteq E_p$ is compact. Since $E_p$ is a Fréchet space, by the metrization theorem it is enough to show that $B$ is totally bounded.

Fix $\varepsilon > 0$ and an index $n$. The boundedness of $B$ implies that for each $n$, the set $B$ is bounded with respect to the norm $\|\cdot\|_n$ in $l^p(\omega_n)$. By the specific choice of the weight sequence $\omega_n$, one can construct a bounded finite-dimensional set $B'$ such that every point of $B$ lies within distance $\varepsilon$ of $B'$ in the norm $\|\cdot\|_n$. This finite-dimensional approximation property, together with the fact that closed bounded subsets of finite-dimensional spaces are compact, implies that $B$ is totally bounded and hence compact in $E_p$.
