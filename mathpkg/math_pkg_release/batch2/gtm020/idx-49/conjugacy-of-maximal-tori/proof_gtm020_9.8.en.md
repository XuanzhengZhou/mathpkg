---
role: proof
locale: en
of_concept: conjugacy-of-maximal-tori
source_book: gtm020
source_chapter: "9"
source_section: "8"
---

**Proof.** Since $T'$ is a torus, it is monic by Theorem 8.5. Let $a$ be a generator of $T'$. Since $T$ is a maximal torus, we have $G = \bigcup_{s \in G} sTs^{-1}$, so $a \in sTs^{-1}$ for some $s \in G$. This implies $a^k \in sTs^{-1}$ for all $k \geq 0$. Since $\{a^k : k \geq 0\}$ is dense in $T'$ and $sTs^{-1}$ is closed, we obtain $T' \subset sTs^{-1}$.

If $T' = sTs^{-1}$, then $G = \bigcup_{g \in G} gT'g^{-1}$, so $T'$ is a maximal torus. Conversely, if $T'$ is a maximal torus, then $T' \subset sTs^{-1}$ and symmetrically $T \subset tT't^{-1}$, which gives $s^{-1}T's \subset T \subset ts^{-1}T's(ts^{-1})^{-1} = ts^{-1}T'st^{-1}$. Hence $T \subset ts^{-1}T'st^{-1}$. But both $T$ and $ts^{-1}T'st^{-1}$ are tori of the same dimension (since conjugation is a homeomorphism), and a torus cannot properly contain another torus of the same dimension. Therefore $T = ts^{-1}T'st^{-1}$, which implies $T' = sTs^{-1}$. $\square$
