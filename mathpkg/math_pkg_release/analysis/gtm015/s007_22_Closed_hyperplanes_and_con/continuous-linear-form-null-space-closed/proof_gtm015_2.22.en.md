---
role: proof
locale: en
of_concept: continuous-linear-form-null-space-closed
source_book: gtm015
source_chapter: "2"
source_section: "22"
---

# Proof of Continuity of linear form equivalent to closed null space

Since $M = f^{-1}(\{0\})$ and $\{0\}$ is closed, the continuity of $f$ implies that $M$ is also closed.

Suppose, conversely, that $M$ is closed. If $f$ is identically zero, there is nothing to prove. Assuming $f$ nonzero, $E/M$ is one-dimensional (21.3). Let $\pi: E \rightarrow E/M$ be the canonical mapping and equip $E/M$ with the quotient topology; then $E/M$ is a TVS and, since $M$ is closed, $E/M$ is separated (11.8). Let $g: E/M \rightarrow \mathbb{K}$ be the unique vector space isomorphism such that $g(\pi(x)) = f(x)$ for all $x \in E$. Then $g$ is continuous by the theorem, therefore $f = g \circ \pi$ is also continuous.
