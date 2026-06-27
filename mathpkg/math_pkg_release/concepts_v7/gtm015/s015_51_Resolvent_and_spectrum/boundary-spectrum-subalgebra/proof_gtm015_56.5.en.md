---
role: proof
locale: en
of_concept: boundary-spectrum-subalgebra
source_book: gtm015
source_chapter: "56"
source_section: "56.5"
---

# Proof of Boundary spectrum in subalgebra

(56.5) Theorem. Let $B$ be a closed subalgebra of $A$ containing 1 and let $x \in B$. Then

$$\partial \sigma_B(x) \subset \partial \sigma_A(x).$$

In particular, if $\sigma_B(x)$ has empty interior then $\sigma_B(x) = \sigma_A(x)$.

Proof. If $\lambda \in \partial \sigma_B(x)$, then $\lambda 1 - x$ is a TDZ in $B$ (56.4); a fortiori, $\lambda 1 - x$ is a TDZ in $A$, therefore $\lambda 1 - x$ is singular in $A$ (56.2), thus $\lambda \in \sigma_A(x)$. Since $\sigma_B(x) \supset \sigma_A(x)$, it follows that $\lambda$ is also a boundary point of $\sigma_A(x)$.

If int $\sigma_B(x) = \varnothing$ then $\sigma_B(x) = \partial \sigma_B(x) \subset \sigma_A(x) \subset \sigma_B(x)$.

In the notation of (56.5), $\sigma_B(x) - \sigma_A(x)$ is trivially open in $\sigma_B(x)$; surprisingly, it is even open in $\mathbb{C}$:
