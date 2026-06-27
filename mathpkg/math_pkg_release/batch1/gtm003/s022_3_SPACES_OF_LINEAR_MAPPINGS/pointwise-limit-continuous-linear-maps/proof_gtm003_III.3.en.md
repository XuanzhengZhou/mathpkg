---
role: proof
locale: en
of_concept: pointwise-limit-continuous-linear-maps
source_book: gtm003
source_chapter: "III"
source_section: "3"
---

Let \(E_M\) be the linear hull of \(M\); \(E_M\) is a non-meager subspace of \(E\), and hence a Baire space. Denote by \(\tilde{u}_n\) the restriction of \(u_n\) to \(E_M\) (\(n \in \mathbb{N}\)). By hypothesis, \(\lim \tilde{u}_n(x) = \tilde{u}(x)\) exists for all \(x \in E_M\). 

By the corollary of Theorem 4.2 (uniform boundedness principle), the sequence \(\{u_n\}\) is norm bounded (or simply bounded) in \(\mathcal{L}(E, F)\) and hence equicontinuous by Theorem 4.2. By Proposition 4.3, the equicontinuity passes to the closure, so the set \(H = \{u_n : n \in \mathbb{N}\} \cup \{u\}\) is equicontinuous (where \(u\) is the unique continuous extension of \(\tilde{u}\) to \(E\)).

Now by Proposition 4.5, on the equicontinuous set \(H\), the uniformity of simple convergence on a total set coincides with that of precompact convergence. Since \(u_n \to u\) pointwise on the total set \(E_M\), the convergence is uniform on every precompact (or, if \(E\) is complete, on every compact) subset of \(E\).
