---
role: proof
locale: en
of_concept: lattice-isomorphism-of-submodules
source_book: gtm013
source_chapter: "1"
source_section: "3. Homomorphisms of Modules"
---

**Proof.** By the First Isomorphism Theorem (3.7.1), the epimorphism $f: M \to N$ with kernel $K$ induces an isomorphism $\eta: M/K \to N$ such that the diagram
$$\begin{CD}
M @>f>> N \\
@Vn_K VV @| \\
M/K @>\eta>> N
\end{CD}$$
commutes, where $n_K$ is the natural epimorphism. Clearly, $\eta$ induces a lattice isomorphism between $\mathcal{S}(M/K)$ and $\mathcal{S}(N)$. But by (2.9), the natural epimorphism $n_K$ induces a lattice isomorphism between $\mathcal{S}(M)/K$ (the lattice of submodules of $M$ containing $K$) and $\mathcal{S}(M/K)$. Composing these isomorphisms yields the inverse lattice isomorphisms between $\mathcal{S}(M)/K$ and $\mathcal{S}(N)$. $\square$
