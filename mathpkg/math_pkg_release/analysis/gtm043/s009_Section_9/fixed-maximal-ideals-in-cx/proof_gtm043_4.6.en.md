---
role: proof
locale: en
of_concept: fixed-maximal-ideals-in-cx
source_book: gtm043
source_chapter: "4"
source_section: "4.6"
---

\(M_p\) is the kernel of the homomorphism \(f \mapsto f(p)\) of \(C(X)\) into \(\mathbf{R}\). Since \(r(p) = r\) for each real number \(r\) (viewed as a constant function), the homomorphism is onto the field \(\mathbf{R}\). Hence its kernel \(M_p\) is a maximal ideal.

Uniqueness of \(p\) is an immediate consequence of the complete regularity of \(X\): if \(p \neq q\), complete regularity yields a function \(f \in C(X)\) with \(f(p) = 0\) and \(f(q) \neq 0\), so \(f \in M_p \setminus M_q\); thus \(M_p \neq M_q\).

On the other hand, if \(M\) is any fixed ideal in \(C(X)\), there exists a point \(p \in \bigcap Z[M]\). Evidently, \(M \subseteq M_p\), which has just been shown to be a proper ideal. Hence if \(M\) is maximal, we must have \(M = M_p\).

The isomorphism \(C(X)/M_p \cong \mathbf{R}\) follows from the first isomorphism theorem: the evaluation map \(f \mapsto f(p)\) is a surjective homomorphism with kernel \(M_p\).
