---
role: proof
locale: en
of_concept: t-i-natural-map
source_book: gtm052
source_chapter: "III"
source_section: "12"
---

Since $T^i$ is a functor, we have a natural map, for any $M$,

$$M = \operatorname{Hom}(A, M) \xrightarrow{\psi} \operatorname{Hom}(T^i(A), T^i(M)).$$

This gives $\varphi$, by setting

$$\varphi\left(\sum a_i \otimes m_i\right) = \sum \psi(m_i)(a_i).$$

Since $T^i$ and $\otimes$ commute with direct limits, it will be sufficient to consider finitely generated $A$-modules $M$. Write $M$ as a quotient of a free finitely generated $A$-module $E$, with kernel $R$:

$$0 \to R \to E \to M \to 0.$$

Applying $T^i$ and using that $T^i$ is exact in the middle (Proposition 12.1), we obtain a commutative diagram with exact rows:

$$\begin{CD}
T^i(A) \otimes R @>>> T^i(A) \otimes E @>>> T^i(A) \otimes M @>>> 0 \\
@VVV @VVV @VVV \\
T^i(R) @>>> T^i(E) @>>> T^i(M)
\end{CD}$$

The first two vertical arrows are isomorphisms because $T^i$ commutes with finite direct sums (being additive) and $\varphi$ is clearly an isomorphism when $M$ is free. The five-lemma (or a simple diagram chase) now shows that:

(i) $\Rightarrow$ (ii): If $T^i$ is right exact, the bottom row is exact at the right end, and the map $T^i(A) \otimes M \to T^i(M)$ is an isomorphism.

(ii) $\Rightarrow$ (iii) is trivial.

(iii) $\Rightarrow$ (i): If $\varphi(M)$ is surjective for all $M$, then for any exact sequence $M \to M'' \to 0$, the commutativity of the diagram

$$\begin{CD}
T^i(A) \otimes M @>>> T^i(A) \otimes M'' @>>> 0 \\
@VVV @VVV \\
T^i(M) @>>> T^i(M'')
\end{CD}$$

together with the surjectivity of the right vertical map, implies the surjectivity of $T^i(M) \to T^i(M'')$. Since $T^i$ is exact in the middle, this shows $T^i$ is right exact.
