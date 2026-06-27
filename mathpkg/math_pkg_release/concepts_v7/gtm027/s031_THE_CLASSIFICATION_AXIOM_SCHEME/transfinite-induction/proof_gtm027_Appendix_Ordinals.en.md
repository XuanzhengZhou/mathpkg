---
role: proof
locale: en
of_concept: transfinite-induction
source_book: gtm027
source_chapter: "Appendix"
source_section: "Ordinals"
---

# Proof of Transfinite Induction

**Theorem 127-128 (Transfinite Induction).** Given a function $g$, there exists a unique function $f$ defined on an ordinal such that $f(x) = g(f|x)$ for every ordinal $x$ in its domain.

*Proof.* First, comparability (Theorem 127): Let $f$ and $h$ be functions with ordinal domains satisfying $f(u) = g(f|u)$ and $h(u) = g(h|u)$. Since both domains are ordinals, Theorem 109 implies one is contained in the other; assume $\text{domain } f \subset \text{domain } h$. If $f \neq h$, let $u$ be the $E$-first member of domain $f$ where they differ. Then $f|u = h|u$ and $f(u) = g(f|u) = g(h|u) = h(u)$, contradiction. Hence $f \subset h$ or $h \subset f$.

Now construct $f$: let $f$ be the union of all functions $h$ such that domain $h$ is an ordinal and $h(z) = g(h|z)$ for $z$ in domain $h$. By the comparability lemma, these functions are compatible, so $f$ is a function. Its domain is a set of ordinals, hence an ordinal. For any $x$ in domain $f$, $x$ belongs to some $h$'s domain, so $f(x) = h(x) = g(h|x) = g(f|x)$. If domain $f$ is not all of $R$, a contradiction is reached by considering $g(f)$ and extending $f$, so domain $f = R$. Uniqueness follows from comparability.
