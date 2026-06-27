---
role: proof
locale: en
of_concept: gamma-theorem-set-recursively-enumerable
source_book: gtm037
source_chapter: "2"
source_section: "2.2"
---

For any $x \in \omega$, we have $x \in g^{+*}(\Gamma\text{-Thm})$ iff

$$\exists y \leq p_{\ln(x)}^{x \cdot \ln(x)} \; [y \in g^{+*}(\Gamma\text{-Prf}) \text{ and } (y)_{\ln(y)} = x].$$

That is, $x$ is the Godel number of a $\Gamma$-theorem iff there exists a $\Gamma$-proof $y$ whose last component is $x$. The bound on $y$ follows from the fact that the Godel number of a proof must be at least as large as the Godel number of its conclusion, and the prime factorization bounds give an explicit computable bound.

By Proposition 10.28, $g^{+*}(\Gamma\text{-Prf})$ is recursively enumerable. The condition $(y)_{\ln(y)} = x$ is a recursive relation. An existential quantifier over an r.e. relation yields an r.e. relation, so $g^{+*}(\Gamma\text{-Thm})$ is recursively enumerable.

More concretely, one can enumerate all $\Gamma$-theorems by: enumerate all natural numbers $y$; for each $y$, check whether it codes a $\Gamma$-proof (using the r.e. procedure for $\Gamma$-Prf); if it does, output its last component $(y)_{\ln(y)}$. This procedure enumerates exactly the $\Gamma$-theorems.
