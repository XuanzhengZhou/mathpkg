---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.4"
proof_technique: translation
locale: en
content_hash: ""
written_against: ""
---
Let $\phi = \psi - b 1_E \in \operatorname{Hom}_K(E,E)$. Then $q = (x - b)^r$ is the minimal polynomial of $\psi$ iff $x^r$ is the minimal polynomial of $\phi$ (since $\phi^r = (\psi - b 1_E)^r = q(\psi) = 0$). The two $K[x]$-module structures induced by $\phi$ and $\psi$ are related by $f(x)v$ (in $\phi$-structure) $= f(x - b)v$ (in $\psi$-structure). Consequently, $E$ is $\phi$-cyclic iff $E$ is $\psi$-cyclic. Apply Theorem 4.3 to $\phi$ to get a basis where $\phi$ has the companion matrix of $x^r$, then translate back to $\psi = \phi + b 1_E$ to obtain the Jordan block.
