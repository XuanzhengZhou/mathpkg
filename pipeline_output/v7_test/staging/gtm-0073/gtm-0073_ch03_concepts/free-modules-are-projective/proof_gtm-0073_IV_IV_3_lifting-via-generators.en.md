---
role: proof
source_book: gtm-0073
chapter: IV
section: "IV.3"
proof_technique: lifting-via-generators
locale: en
content_hash: ""
written_against: ""
---
Given $g: A \to B$ epi and $f: F \to B$ with $F$ free on $X$ ($\iota: X \to F$). For each $x \in X$, $f(\iota(x)) \in B$. Since $g$ is epi, there exists $a_x \in A$ with $g(a_x) = f(\iota(x))$. The map $X \to A$ given by $x \mapsto a_x$ induces $h: F \to A$ such that $h(\iota(x)) = a_x$. Then $gh(\iota(x)) = g(a_x) = f(\iota(x))$, so $gh\iota = f\iota$. By uniqueness in Theorem 2.1(iv), $gh = f$.
