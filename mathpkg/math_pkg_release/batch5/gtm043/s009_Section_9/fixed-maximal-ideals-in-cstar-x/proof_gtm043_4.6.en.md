---
role: proof
locale: en
of_concept: fixed-maximal-ideals-in-cstar-x
source_book: gtm043
source_chapter: "4"
source_section: "4.6"
---

The proof for \(C^*(X)\) is analogous to that for \(C(X)\). \(M^*_p\) is the kernel of the evaluation homomorphism \(f \mapsto f(p)\) from \(C^*(X)\) into \(\mathbf{R}\). Constant functions are bounded, so the homomorphism is onto \(\mathbf{R}\); hence its kernel \(M^*_p\) is a maximal ideal in \(C^*(X)\).

Distinctness follows from complete regularity: for \(p \neq q\), there exists \(f \in C^*(X)\) with \(f(p) = 0\) and \(f(q) \neq 0\) (one may take \(\min(|g|, 1)\) where \(g \in C(X)\) separates \(p\) and \(q\)).

If \(M^*\) is any fixed ideal in \(C^*(X)\), there exists \(p \in \bigcap Z[M^*]\). Since \(M^* \subseteq M^*_p\) and \(M^*_p\) is proper, maximality of \(M^*\) forces \(M^* = M^*_p\).

The isomorphism \(C^*(X)/M^*_p \cong \mathbf{R}\) follows from the first isomorphism theorem applied to the evaluation map.
