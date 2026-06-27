---
role: proof
locale: en
of_concept: m-projective-equivalent-conditions
source_book: gtm013
source_chapter: "1"
source_section: "§16. The Hom Functors and Exactness—Projectivity and Injectivity"
---

(a) $\Leftrightarrow$ (b). By (16.6), condition (b) holds if and only if for every epimorphism $g: M \to N \to 0$ the sequence $Hom_R(U, M) \xrightarrow{g_*} Hom_R(U, N) \to 0$ is exact. But $g_*$ is epic if and only if for each $\gamma \in Hom(U, N)$ there is a $\bar{\gamma} \in Hom_R(U, M)$ such that $\gamma = g_*(\bar{\gamma}) = g\bar{\gamma}$, which is exactly condition (a).

(a) $\Rightarrow$ (c). This is clear by taking $N = M/K$ and $g = n_K$.

(c) $\Rightarrow$ (a). Suppose we have an epimorphism $g: M \to N$ with $K = Ker(g)$. By the Factor Theorem (3.6.1), there is an isomorphism $h: N \to M/K$ such that $h g = n_K$. If $\gamma: U \to N$, then $h\gamma$ factors through $n_K$ by hypothesis; that is, there exists $\bar{\gamma}$ such that $n_K \bar{\gamma} = h\gamma$. Since $h$ is an isomorphism, $g\bar{\gamma} = \gamma$ and $U$ is $M$-projective.
