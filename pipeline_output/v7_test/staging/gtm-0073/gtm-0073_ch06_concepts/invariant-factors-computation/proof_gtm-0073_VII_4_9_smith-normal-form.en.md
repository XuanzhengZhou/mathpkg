---
role: proof
source_book: gtm-0073
chapter: VII
section: "VII.4"
proof_technique: smith-normal-form
locale: en
content_hash: ""
written_against: ""
---
Let $\phi : K^n \to K^n$ be the $K$-linear transformation with matrix $A = (a_{ij})$ relative to the standard basis. View $K^n$ as a $K[x]$-module with structure induced by $\phi$. Let $F$ be a free $K[x]$-module with basis $\{u_1, \ldots, u_n\}$ and let $\pi : F \to K^n$ be the $K[x]$-module homomorphism sending $u_i \mapsto \varepsilon_i$ (standard basis).

Define $\psi : F \to F$ by $\psi(u_i) = xu_i - \sum_{j} a_{ij} u_j$. One shows that $\operatorname{Ker} \pi = \operatorname{Im} \psi$, yielding $K^n \cong F / \operatorname{Im} \psi$. The matrix of $\psi$ relative to $\{u_i\}$ is $xI_n - A$.

Apply Proposition 2.11 (Smith normal form) to $xI_n - A$ over the PID $K[x]$, obtaining a diagonal matrix with diagonal entries $f_1 \mid \cdots \mid f_n$. The structure theorem for modules over a PID (Theorem IV.6.12) then identifies the non-constant $f_i$ as the invariant factors of the $K[x]$-module $K^n$, which are exactly the invariant factors of $A$.
