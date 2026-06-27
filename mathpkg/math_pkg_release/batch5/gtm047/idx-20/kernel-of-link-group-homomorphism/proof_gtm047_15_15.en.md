---
role: proof
locale: en
of_concept: kernel-of-link-group-homomorphism
source_book: gtm047
source_chapter: "15"
source_section: "15"
---

**Proof.**

(1) It is easy to see that $N([R])$ is the set of all elements of $F(G)$ that are obtainable from elements of $[R]$ in a finite number of steps by multiplication, inversion, and conjugation. Since $\phi^*([r_i]) = \bar{e}$ for each $i$, it follows by induction that $[p] \in N([R]) \Rightarrow \phi^*([p]) = \bar{e}$. Thus $N([R]) \subset \ker \phi^*$.

(2) We need to show, conversely, that $\ker \phi^* \subset N([R])$. For each generator word $p$, we define $[p]$ as above. Obviously every element of $F(G)$ is $[p]$ for some generator word $p$; and if $[p] \in \ker \phi^*$, then $p \cong e$, so that $p$ is reducible to $e$ in a finite number of steps as in Theorem 2. Suppose that in one such step,

$$p = p_1 p_2 \mapsto p_1 g_i^{-1} r_j^{\pm 1} g_i p_2 = p'.$$

We assert that $[p] \equiv [p'] \bmod N([R])$; that is,

$$[p]^{-1}[p'] \in N([R]).$$

Now

$$[p]^{-1}[p'] = [p^{-1}p'] = [p_2^{-1}p_1^{-1} p_1 g_i^{-1} r_j^{\pm 1} g_i p_2] = [p_2^{-1}g_i^{-1} r_j^{\pm 1} g_i p_2],$$

so that $[p]^{-1}[p']$ is a conjugate of $[r_j]^{\pm 1}$, and therefore lies in $N([R])$. Since the reduction from $p$ to $e$ proceeds in a finite number of such steps, and each step preserves the congruence modulo $N([R])$, we conclude that $[p] \in N([R])$. Hence $\ker \phi^* \subset N([R])$.

Combining (1) and (2), $\ker \phi^* = N([R])$. The induced isomorphism follows immediately from the First Isomorphism Theorem.
