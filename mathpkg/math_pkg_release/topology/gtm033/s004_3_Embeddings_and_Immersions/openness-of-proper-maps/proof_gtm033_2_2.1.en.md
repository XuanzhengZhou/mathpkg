---
role: proof
locale: en
of_concept: openness-of-proper-maps
source_book: gtm033
source_chapter: "2. Function Spaces"
source_section: "2.1"
---

# Proof of Openness of Proper Maps in the Strong Topology (Theorem 1.5)

**Theorem 1.5.** The set $\operatorname{Prop}^r(M,N)$ of proper $C^r$ maps $M \to N$ is open in $C^r_S(M,N)$, $r \geqslant 0$.

*Proof.* For any map $f: M \to N$ there is a compact cover $\{K_i\}_{i \in \Lambda}$ of $M$ and an open cover $\mathcal{V} = \{V_i\}_{i \in \Lambda}$ of $N$ with $f(K_i) \subset V_i$. If $f$ is proper, $\mathcal{V}$ can be chosen locally finite. (Reason: since $f$ is proper, the sets $f(K_i)$ form a locally finite family of compact sets in $N$; we can then pick a locally finite open cover $\mathcal{V}$ such that $f(K_i) \subset V_i$ for each $i$.)

There is a neighborhood $\mathcal{N}$ of $f$ in $C^r_S(M,N)$ such that if $g \in \mathcal{N}$ then $g(K_i) \subset V_i$ for all $i$. (Such a neighborhood exists by the definition of the strong topology: we require the $C^0$ closeness condition on each compact set $K_i$ with charts mapping into $V_i$.)

To see that such a $g$ is proper, let $L \subset N$ be compact. Since $\mathcal{V}$ is locally finite, $L$ meets only a finite number of $V_i$. Hence $g^{-1}(L)$ is a closed subset of $M$ which is covered by finitely many of the compact sets $K_i$; therefore $g^{-1}(L)$ is compact.

$\square$

**Remark.** Since an embedding $f: M \to N$ is proper if and only if $f(M)$ is closed in $N$, Theorem 1.5 combined with Theorem 1.4 implies that the set of closed embeddings is open in the strong topology.
