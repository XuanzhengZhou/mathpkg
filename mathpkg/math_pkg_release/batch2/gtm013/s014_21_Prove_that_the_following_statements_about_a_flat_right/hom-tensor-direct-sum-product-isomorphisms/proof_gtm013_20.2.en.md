---
role: proof
locale: en
of_concept: hom-tensor-direct-sum-product-isomorphisms
source_book: gtm013
source_chapter: "20"
source_section: "20.2"
---

These are rephrasings of (16.5). The proof follows from the universal properties of direct sums and products.

For (1): An $R$-homomorphism $f: \bigoplus_A U_\alpha \to M$ is uniquely determined by its restrictions $f|_{U_\alpha}: U_\alpha \to M$, which gives an isomorphism $\operatorname{Hom}_R(\bigoplus_A U_\alpha, M) \cong \prod_A \operatorname{Hom}_R(U_\alpha, M)$. Given $g: M \to N$, the naturality square

$$\begin{CD}
\operatorname{Hom}_R(\bigoplus U_\alpha, M) @>{\operatorname{Hom}(\bigoplus U_\alpha, g)}>> \operatorname{Hom}_R(\bigoplus U_\alpha, N)\\
@V{\cong}VV @VV{\cong}V\\
\prod \operatorname{Hom}_R(U_\alpha, M) @>{\prod \operatorname{Hom}(U_\alpha, g)}>> \prod \operatorname{Hom}_R(U_\alpha, N)
\end{CD}$$

commutes because both paths send $f \mapsto g \circ f$, and on the bottom row the $\alpha$-component is $g \circ f|_{U_\alpha}$.

For (2): An $R$-homomorphism $f: M \to \prod_A U_\alpha$ is determined by its coordinate maps $\pi_\alpha \circ f: M \to U_\alpha$, giving $\operatorname{Hom}_R(M, \prod_A U_\alpha) \cong \prod_A \operatorname{Hom}_R(M, U_\alpha)$. Naturality follows similarly.

For (3): Using the isomorphism $M \otimes_R (\bigoplus_A U_\alpha) \cong \bigoplus_A (M \otimes_R U_\alpha)$ from (19.9). If $f: M \to N$, then naturality follows from

$$(f \otimes 1)(m \otimes (u_\alpha)) = f(m) \otimes (u_\alpha)$$

which maps to $\bigoplus (f(m) \otimes u_\alpha) = (\bigoplus (f \otimes 1))(m \otimes u_\alpha)$.
