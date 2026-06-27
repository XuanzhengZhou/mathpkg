---
role: proof
locale: en
of_concept: yoneda-corollary
source_book: gtm005
source_chapter: "III"
source_section: "2"
---

Apply the Yoneda Lemma with $K = D(s, -)$. The Lemma gives a bijection

\[
\operatorname{Nat}(D(r, -), D(s, -)) \cong D(s, r).
\]

Under this bijection, a natural transformation $\alpha$ corresponds to the element $\alpha_r(1_r) \in D(s, r)$, which is an arrow $h: s \to r$. Tracing the inverse direction: the arrow $h: s \to r$ corresponds to the natural transformation $\alpha^h$ defined by $\alpha^h_d(f) = D(s, f)(h) = f \circ h$ for each $f: r \to d$. But $f \circ h = D(h, d)(f)$, where $D(h, -): D(r, -) \to D(s, -)$ is the natural transformation induced by precomposition with $h$. Thus every natural transformation from $D(r, -)$ to $D(s, -)$ is of the form $D(h, -)$ for a unique $h: s \to r$.
