---
role: proof
locale: en
of_concept: hom-tensor-adjunction
source_book: gtm013
source_chapter: "20"
source_section: "20.6"
---

The map $\phi$ is defined by $\phi(\gamma)(w \otimes m) = [\gamma(m)](w)$. First verify that $\phi(\gamma)$ is well-defined as an $S$-homomorphism: For each $m \in M$, $\gamma(m) \in \operatorname{Hom}_S(W, N)$, so $[\gamma(m)](w) \in N$. The map $(w, m) \mapsto [\gamma(m)](w)$ is $R$-balanced because for $r \in R$:

$$[\gamma(rm)](w) = [r \cdot \gamma(m)](w) = [\gamma(m)](wr)$$

since the bimodule structure gives $\gamma(m)(wr) = [\gamma(m) \cdot r](w) = [\gamma(rm)](w)$. Thus $\phi(\gamma): W \otimes_R M \to N$ is a well-defined $S$-homomorphism.

The inverse of $\phi$ is given by: for $\alpha \in \operatorname{Hom}_S(W \otimes_R M, N)$, define $\psi(\alpha): M \to \operatorname{Hom}_S(W, N)$ by $[\psi(\alpha)(m)](w) = \alpha(w \otimes m)$. One checks that $\psi(\alpha)(m) \in \operatorname{Hom}_S(W, N)$ and that $\psi(\alpha)$ is $R$-linear. Then $\phi$ and $\psi$ are mutual inverses.

Naturality in $M$: For $f: {}_R M \to {}_R M'$, the diagram

$$\begin{CD}
\operatorname{Hom}_R(M', \operatorname{Hom}_S(W, N)) @>{\operatorname{Hom}(f, \operatorname{Hom}(W, N))}>> \operatorname{Hom}_R(M, \operatorname{Hom}_S(W, N))\\
@V{\phi}VV @VV{\phi}V\\
\operatorname{Hom}_S(W \otimes_R M', N) @>{\operatorname{Hom}(W \otimes f, N)}>> \operatorname{Hom}_S(W \otimes_R M, N)
\end{CD}$$

commutes since for $\gamma: M' \to \operatorname{Hom}_S(W, N)$ and $w \otimes m \in W \otimes_R M$:

$$[\phi(\gamma \circ f)](w \otimes m) = [\gamma(f(m))](w) = \phi(\gamma)(w \otimes f(m)) = [\phi(\gamma) \circ (W \otimes f)](w \otimes m).$$

Naturality in $N$ and $W$ is verified similarly using the functoriality of Hom and tensor products.
