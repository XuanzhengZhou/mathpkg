---
role: proof
locale: en
of_concept: subbundle-inclusion-as-bundle-morphism
source_book: gtm020
source_chapter: "3"
source_section: "3.3"
---

This follows directly from the definition of a subbundle and the definition of a bundle morphism. Since $(E', p', B')$ is a subbundle of $(E, p, B)$, we have $E' \subset E$, $B' \subset B$, and $p' = p|_{E'}$. Let $u: E' \to E$ and $f: B' \to B$ be the inclusion maps. For any $x \in E'$, we have $p(u(x)) = p(x)$ and $f(p'(x)) = p'(x) = p(x)$ (since $x \in E'$), hence $p(u(x)) = f(p'(x))$. Thus $pu = fp'$, which is exactly the condition for $(u, f)$ to be a bundle morphism.
