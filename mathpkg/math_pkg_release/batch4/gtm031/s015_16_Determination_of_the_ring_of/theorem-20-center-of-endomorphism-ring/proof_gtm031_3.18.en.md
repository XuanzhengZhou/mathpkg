---
role: proof
locale: en
of_concept: theorem-20-center-of-endomorphism-ring
source_book: gtm031
source_chapter: "3"
source_section: "18"
---

We have already seen that $\mathfrak{o}_l \subseteq \mathfrak{C}$ (scalar multiplications commute with all endomorphisms). It remains to prove $\mathfrak{C} \subseteq \mathfrak{o}_l$.

Let $C \in \mathfrak{C}$ be any central element. For each $k = 1, 2, \ldots, t$, define $E_k$ to be the $\mathfrak{o}$-endomorphism such that $f_j E_k = \delta_{jk} f_k$ for $j = 1, 2, \ldots, t$. By the existence result of Section 16, such endomorphisms exist (the order ideal of $\delta_{jk} f_k$ is $(\delta_k)$, which divides $(\delta_j)$ whenever $\delta_{jk} \neq 0$, and the normalization ensures existence).

Also, there exist $\mathfrak{o}$-endomorphisms $E_{tk}$ such that $f_j E_{tk} = \delta_{jt} f_k$ for $j, k = 1, \ldots, t$. These are the "matrix unit" endomorphisms sending $f_t$ to $f_k$ and annihilating other generators.

Since $C$ is central, it commutes with $E_t$:

$$f_t C = (f_t E_t) C = (f_t C) E_t.$$

Now $f_t C = \sum_{j} \gamma_j f_j$ for some $\gamma_j \in \mathfrak{o}$. Applying $E_t$ gives $(f_t C) E_t = \gamma_t f_t$. On the other hand, since $C \in \mathfrak{C}$, we also have

$$f_t C = (f_t E_t) C = (f_t C) E_t = \gamma_t f_t, \quad \gamma_t \in \mathfrak{o}.$$

Next, using $E_{tk}$ for any $k$:

$$f_k C = (f_t E_{tk}) C = (f_t C) E_{tk} = (\gamma_t f_t) E_{tk} = \gamma_t f_k.$$

Thus $C$ acts on every generator $f_k$ as multiplication by the same scalar $\gamma_t$. Since $C$ is $\mathfrak{o}$-linear and every element of $\mathfrak{R}$ is an $\mathfrak{o}$-linear combination of the generators, $C$ acts as scalar multiplication by $\gamma_t$ on all of $\mathfrak{R}$. Therefore $C \in \mathfrak{o}_l$, completing the proof.
