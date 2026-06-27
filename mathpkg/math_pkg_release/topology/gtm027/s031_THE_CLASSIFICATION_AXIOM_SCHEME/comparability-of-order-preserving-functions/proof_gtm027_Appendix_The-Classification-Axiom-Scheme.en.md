---
role: proof
locale: en
of_concept: comparability-of-order-preserving-functions
source_book: gtm027
source_chapter: "Appendix"
source_section: "The Classification Axiom Scheme"
---

# Proof of Comparability of Order-Preserving Functions

**Theorem 97.** If $f$ and $g$ are $r$-$s$ order preserving, domain $f$ and domain $g$ are $r$-sections of $x$, and range $f$ and range $g$ are $s$-sections of $y$, then $f \subset g$ or $g \subset f$.

*Proof.* By Theorem 92, either $\text{domain } f \subset \text{domain } g$ or $\text{domain } g \subset \text{domain } f$. It suffices to prove $f(u) = g(u)$ for all $u$ belonging to the domain of both. If the class $\{z : z \in (\text{domain } f) \cap (\text{domain } g) \text{ and } g(z) \neq f(z)\}$ is non-empty, let $u$ be its $r$-first member. Then $f(u) \neq g(u)$; suppose $f(u) s g(u)$. Since range $g$ is an $s$-section, $g(v) = f(u)$ for some $v$ in $x$ with $v r u$ (because $g^{-1}$ is order preserving). But $u$ is the $r$-first point where the functions differ, so $f(v) = g(v) = f(u)$, which contradicts $v r u$ and $f(v) s f(u)$ (since $f$ is order preserving).
