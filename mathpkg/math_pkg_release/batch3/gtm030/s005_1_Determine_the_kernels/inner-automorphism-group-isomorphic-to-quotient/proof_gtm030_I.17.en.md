---
role: proof
locale: en
of_concept: inner-automorphism-group-isomorphic-to-quotient
source_book: gtm030
source_chapter: "I"
source_section: "17"
---

Let $C_{a_1}$ and $C_{a_2}$ be inner automorphisms. Then

$$x C_{a_1} C_{a_2} = a_2^{-1} a_1^{-1} x a_1 a_2 = (a_1 a_2)^{-1} x (a_1 a_2) = x C_{a_1 a_2}$$

so that

$$C_{a_1 a_2} = C_{a_1} C_{a_2}.$$

This equation shows that the correspondence $a \rightarrow C_a$ is a homomorphism of $\mathfrak{G}$ into its group of automorphisms. It follows (Theorem 6) that the image set $\mathfrak{J}$ is a subgroup of $\mathfrak{A}$. Now let $\alpha$ be any automorphism and consider the product $\alpha^{-1} C_a \alpha$.

Since

$$x \alpha^{-1} C_a \alpha = (a^{-1}(x \alpha^{-1}) a) \alpha = (a^{-1} \alpha) x (a \alpha)$$

$$= (a \alpha)^{-1} x (a \alpha)$$

$$= x C_{a \alpha},$$

$$\alpha^{-1} C_a \alpha = C_{a \alpha}.$$

This shows that $\mathfrak{J}$ is invariant in $\mathfrak{A}$. The kernel of the homomorphism $a \rightarrow C_a$ consists of the elements $c$ such that $c^{-1} x c = x$ for all $x$, i.e., $c x = x c$ for all $x$. This is exactly the center $\mathfrak{C}$ of $\mathfrak{G}$. By the fundamental theorem of homomorphism $\mathfrak{J} \cong \mathfrak{G}/\mathfrak{C}$.
