---
role: proof
locale: en
of_concept: uniqueness-of-identity-arrow
source_book: gtm005
source_chapter: "I"
source_section: "1"
content_hash: "eea337db0609c1f1"
written_against: "2b6417b481ae979a"
---

Let $u, v : b \rightarrow b$ be two arrows of $C$ both satisfying the unit law for the object $b$, i.e., for all $f: a \rightarrow b$ and all $g: b \rightarrow c$,
$$u \circ f = f, \quad g \circ u = g, \qquad v \circ f = f, \quad g \circ v = g.$$
Taking $f = v$ (so $a = b$) in the first equation for $u$ yields $u \circ v = v$.
Taking $g = u$ (so $c = b$) in the second equation for $v$ yields $u \circ v = u$.
Therefore $u = u \circ v = v$. Hence the identity arrow for $b$ is unique.
