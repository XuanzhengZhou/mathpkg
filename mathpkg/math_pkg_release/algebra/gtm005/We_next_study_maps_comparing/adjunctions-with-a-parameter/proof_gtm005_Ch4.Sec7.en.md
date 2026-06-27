---
role: proof
locale: en
of_concept: adjunctions-with-a-parameter
source_book: gtm005
source_chapter: "IV"
source_section: "7"
---

**Proof.** The condition that the adjunction be natural in $p \in P$ is the commutativity of the square
\[
\begin{array}{ccc}
\hom(F(x, p), a) & \cong & \hom(x, G(p, a)) \\
\hom(F(x, h), a) \downarrow & & \downarrow \hom(x, G(h, a)) \\
\hom(F(x, p'), a) & \cong & \hom(x, G(p', a))
\end{array}
\]
for each arrow $h : p \to p'$ in $P$. This commutativity (for all $x$ and $a$) states precisely that the natural transformation
$$G(h, -) : G(p', -) \to G(p, -)$$
must be chosen as the conjugate (in the sense of Theorem 2) to the natural transformation
$$F(-, h) : F(-, p) \to F(-, p').$$
By Theorem 2, this conjugate exists uniquely. Hence there is a unique assignment of arrows $G(h, a)$ making $G$ a bifunctor $P^{\text{op}} \times A \to X$ and making the adjunction natural in $p$.
