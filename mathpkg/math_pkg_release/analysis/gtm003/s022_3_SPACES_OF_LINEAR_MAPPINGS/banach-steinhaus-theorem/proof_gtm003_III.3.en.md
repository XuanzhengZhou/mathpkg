---
role: proof
locale: en
of_concept: banach-steinhaus-theorem
source_book: gtm003
source_chapter: "III"
source_section: "3"
---

For a given closed, convex, circled \(0\)-neighborhood \(V\) in \(F\), the set \(D = \bigcap_{u \in H} u^{-1}(V)\) is closed, convex, and circled. Since \(H\) is simply bounded, for each \(x \in E\) the set \(\{u(x) : u \in H\}\) is bounded in \(F\). Thus there exists \(\lambda > 0\) such that \(u(x) \in \lambda V\) for all \(u \in H\), i.e., \(x \in \lambda D\). Therefore \(D\) is radial (absorbing) and hence a barrel.

If \(E\) is barreled, every barrel is a \(0\)-neighborhood, so \(D\) is a \(0\)-neighborhood in \(E\). By Proposition 4.1(b), this means \(H\) is equicontinuous.

If \(E\) is a Baire space, then \(E\) is barreled (every Baire t.v.s. is barreled), and the same conclusion follows. More directly: since \(D\) is closed, convex, circled, and radial, and \(E\) is a Baire space, \(D\) has nonempty interior (by the Baire category theorem applied to the countable union \(E = \bigcup_n nD\)), hence \(D\) is a \(0\)-neighborhood.
