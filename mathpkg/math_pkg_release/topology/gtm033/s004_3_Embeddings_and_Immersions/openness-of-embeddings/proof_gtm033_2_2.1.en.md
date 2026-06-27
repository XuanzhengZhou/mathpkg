---
role: proof
locale: en
of_concept: openness-of-embeddings
source_book: gtm033
source_chapter: "2. Function Spaces"
source_section: "2.1"
---

# Proof of Openness of Embeddings in the Strong Topology (Theorem 1.4)

**Theorem 1.4.** The set $\operatorname{Emb}^r(M,N)$ of $C^r$ embeddings of $M$ in $N$ is open in $C^r_S(M,N)$, $r \geqslant 1$.

*Proof.* It suffices to take $r = 1$. Let $f \in \operatorname{Emb}^1(M,N)$. By using the preceding lemma (local injectivity lemma for immersions) we can find the following objects:

- a locally finite atlas $\Phi = \{\varphi_i, U_i\}_{i \in \Lambda}$ of $M$;
- a set $\Psi = \{\psi_i, V_i\}_{i \in \Lambda}$ of charts for $N$ with $f(U_i) \subset V_i$;
- compact sets $K_i \subset U_i$ covering $M$;
- open sets $A_i \subset V_i$ and $B_i \subset V_i$ with $f(K_i) \subset A_i$, $\overline{A_i} \cap \overline{B_i} = \varnothing$, and $f(M - U_i) \subset B_i$ (using that $f$ is a homeomorphism onto its image and the atlas is locally finite);
- numbers $\varepsilon_i > 0$ such that any $g$ with local representations $\varepsilon_i$-close to $f$ on $K_i$ is an immersion on $U_i$ and injective on a neighborhood of $K_i$.

Define the strong basic neighborhood $\mathcal{N} = \mathcal{N}^1(f; \Phi, \Psi, \{K_i\}, \{\varepsilon_i\})$. We claim every $g \in \mathcal{N}$ is an embedding.

For injectivity: if $g(x) = g(y)$ and $x \in K_i$, then $g(x) \in A_i$ while for $y \in M - U_i$ we have $g(y) \in B_i$, so $g(x) \neq g(y)$. Thus $y \in U_i$, and by the local injectivity from the lemma, $g$ is injective on $U_i$, hence $x = y$.

To see that $g: M \to g(M)$ is a homeomorphism, it suffices to show that if $y_n$ is a sequence in $M$ such that $g(y_n) \to g(x)$ then $y_n \to x$. If $x \in K_i$ then $g(x) \in A_i$; hence only a finite number of the $g(y_n)$ can be in $B_i$, so all but a finite number of $y_n$ are in $U_i$. Since $g|U_i: U_i \to g(U_i)$ is a homeomorphism (being an injective immersion that is a homeomorphism onto its image locally), it follows that $y_n \to x$.

Thus $g$ is an embedding and $\operatorname{Emb}^1(M,N)$ is open in $C^1_S(M,N)$.

$\square$
