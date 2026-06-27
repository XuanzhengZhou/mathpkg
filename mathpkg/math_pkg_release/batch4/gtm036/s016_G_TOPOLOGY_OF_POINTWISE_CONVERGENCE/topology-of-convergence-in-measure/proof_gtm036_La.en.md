---
role: proof
locale: en
of_concept: topology-of-convergence-in-measure
source_book: gtm036
source_chapter: "L"
source_section: "L(a)"
---

To verify that $\{U_n\}$ is a local base for a vector topology, one checks the standard axioms: each $U_n$ is balanced (since $|\lambda f(x)| > 1/n$ implies $|f(x)| > 1/(n|\lambda|)$, and for $|\lambda| \leq 1$ this set is contained in the defining set) and absorbing (for any $f$, $\mu\{x : |f(x)| > m/n\} \to 0$ as $m \to \infty$, so scaling $f$ appropriately puts it in $U_n$). The addition map is continuous since $U_{\lfloor n/2\rfloor} + U_{\lfloor n/2\rfloor} \subseteq U_n$ (if $|f(x)+g(x)| > 1/n$, then either $|f(x)| > 1/(2n)$ or $|g(x)| > 1/(2n)$). The scalar multiplication is similarly continuous. Since the family is countable, the topology is pseudo-metrizable.
