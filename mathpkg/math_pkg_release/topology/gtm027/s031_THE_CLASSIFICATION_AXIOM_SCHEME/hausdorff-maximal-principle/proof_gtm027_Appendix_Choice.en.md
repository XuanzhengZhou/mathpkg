---
role: proof
locale: en
of_concept: hausdorff-maximal-principle
source_book: gtm027
source_chapter: "Appendix"
source_section: "Choice"
---

# Proof of Hausdorff Maximal Principle

PROOF The proof is by transfinite induction; intuitively we select a nest and then a larger nest, and “keep going,” knowing that, because $R$ is not a set, the set of all nests which are contained in $x$ will be exhausted before the class $R$ of ordinals. For each $h$ let $g(h) = c(\{m: m is a nest, m \subset x and p in range h, p \subset m and p \neq m\})$, where $c$ is a choice function satisfying the axiom of choice. (Intuitively select $g(h)$ to be a nest in $x$ containing properly each previously selected nest.) By theorem 128 there is a function $f$ such that domain $f$ is an ordinal and $f(u) = g(f|u)$ for each ordinal number $u$. From the definition of $g$ it follows that, if $u \in domain f$, then $f(u) \subset x$ and $f(u)$ is a nest, and if $u$ and $v$ are members of domain $f$ and $u < v$, then $f(u) \subset f(v)$ and $f(u) \neq f(v)$. Consequently $f$ is 1-1, $f^{-1}$ is a function and, since $x$ is a set, domain $f
