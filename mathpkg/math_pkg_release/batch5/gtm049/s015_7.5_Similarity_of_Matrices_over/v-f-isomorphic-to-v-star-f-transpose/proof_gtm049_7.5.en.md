---
role: proof
locale: en
of_concept: v-f-isomorphic-to-v-star-f-transpose
source_book: gtm049
source_chapter: "7"
source_section: "7.5"
---

Let $V_f = [a_1]_f \oplus \cdots \oplus [a_k]_f$ be the invariant factor decomposition according to Theorem 1, and write $M_i = [a_i]_f$. For each $i$, define
$$N_i = \bigcap_{j \neq i} M_j^\circ,$$
where $M_j^\circ = \{\varphi \in V^* : M_j \varphi = 0\}$ is the annihilator of $M_j$ in $V^*$. Then the pairing
$$(m_1 + \cdots + m_k)(\nu_1 + \cdots + \nu_k) = m_1 \nu_1 + \cdots + m_k \nu_k$$
(where $m_i \in M_i$, $\nu_i \in N_i$) is nondegenerate, and therefore the subspace of $V^*$ spanned by the $N_i$ is their direct sum. Since $\dim N_i = \dim M_i$ for all $i$, we obtain $V^* = N_1 \oplus \cdots \oplus N_k$.

By the definition of $f^t$ and because each $M_i$ is $f$-invariant, each $N_i$ is $f^t$-invariant. Thus
$$(V^*)_{f^t} = (N_1)_{f^t} \oplus \cdots \oplus (N_k)_{f^t}.$$

If $\nu \in N_i$, then $\nu = 0$ if and only if $M_i \nu = 0$. Hence $p \in a(N_i)$ if and only if $M_i p(f) = 0$, i.e., $p \in a(M_i)$. This shows that $a(N_i) = a(M_i)$, so $(N_i)_{f^t} \cong (M_i)_f$ as $F[X]$-modules. Consequently, $(V^*)_{f^t} \cong V_f$, and the invariant factors and elementary divisors coincide.
