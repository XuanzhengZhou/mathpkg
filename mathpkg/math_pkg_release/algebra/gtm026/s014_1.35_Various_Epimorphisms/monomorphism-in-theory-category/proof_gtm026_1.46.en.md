---
role: proof
locale: en
of_concept: monomorphism-in-theory-category
source_book: gtm026
source_chapter: "1"
source_section: "1.46"
---

Clearly, mono in $\mathcal{K}$ implies mono in $\mathcal{K}^T$. For the converse, let $t, u: C \longrightarrow A$ be arbitrary morphisms in $\mathcal{K}$. Let $t^{\#}, u^{\#}$ be the unique homomorphic extensions of $t$, $u$ as provided by the universal property of $(CT, C\mu)$ (see 1.4.12) and shown below (the breaks in the arrows denote that the morphisms are only in $\mathcal{K}$, not in $\mathcal{K}^T$).

$$
\begin{array}{ccc}
(CT, C\mu) & \xrightarrow{t^{\#}} & (A, \xi) \\
& u^{\#} & f \\
& C\eta & u
\end{array}
$$

If $f \cdot t = f \cdot u$ in $\mathcal{K}$, then $f \cdot t^{\#} = f \cdot u^{\#}$ as $T$-homomorphisms. Since $f$ is mono in $\mathcal{K}^T$, we have $t^{\#} = u^{\#}$, whence $t = t^{\#} \cdot \eta_C = u^{\#} \cdot \eta_C = u$. Thus $f$ is mono in $\mathcal{K}$.
