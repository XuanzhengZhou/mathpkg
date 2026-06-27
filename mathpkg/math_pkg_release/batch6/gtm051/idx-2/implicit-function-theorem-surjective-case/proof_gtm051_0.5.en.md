---
role: proof
locale: en
of_concept: implicit-function-theorem-surjective-case
source_book: gtm051
source_chapter: "0"
source_section: "0.5"
---

Suppose $dF_0: \mathbb{R}^n \rightarrow \mathbb{R}^m$ is surjective. Decompose $\mathbb{R}^n = \mathbb{R}'^m \oplus \mathbb{R}''^{n-m}$ so that $dF_0|_{\mathbb{R}'^m}: \mathbb{R}'^m \rightarrow \mathbb{R}^m$ is a bijection. Define $\tilde{h}: \mathbb{R}^n = \mathbb{R}'^m \oplus \mathbb{R}''^{n-m} \rightarrow \mathbb{R}^n = \mathbb{R}'^m \oplus \mathbb{R}''^{n-m}$ in a neighborhood of zero by $v = (v', v'') \mapsto (F(v), v'')$. Here we identify $\mathbb{R}'^m$ on the right-hand side with $\mathbb{R}^m$.

Since $d\tilde{h}_0 = dF_0|_{\mathbb{R}'^m} + \text{id}|_{\mathbb{R}''^{n-m}}$ is bijective (it is an isomorphism on both factors of the direct sum), $\tilde{h}$ has a local inverse $h = \tilde{h}^{-1}$ by the inverse function theorem. Since $h \circ \tilde{h} = \text{id}$ locally, $h(F(v', v''), v'') = (v', v'')$ and therefore $F \circ h(F(v', v''), v'') = F(v', v'')$. This means $F \circ h(x', x'') = x'$ in the new coordinates $(x', x'') = \tilde{h}(v', v'')$, so $F$ is locally equivalent to the projection onto the first $m$ coordinates.
