---
role: proof
locale: en
of_concept: order-preserving-function-inverse
source_book: gtm027
source_chapter: "Appendix"
source_section: "The Classification Axiom Scheme"
---

# Proof of Inverse of Order-Preserving Function

**Theorem (Inverse of Order-Preserving Function).** If $f$ is $r$-$s$ order preserving and one-to-one, then $f^{-1}$ is $s$-$r$ order preserving.

*Proof.* From the text following Theorem 94: If $f(u) = f(v)$, then it is impossible that $u r v$ or $v r u$, for in this case $f(u) s f(v)$ or $f(v) s f(u)$, contradicting the asymmetry of $s$ (Theorem 88). Hence $u = v$ and $f$ is one-to-one.

Now if $f^{-1}(a) s f^{-1}(b)$ were false while $a s b$, then setting $u = f^{-1}(a)$ and $v = f^{-1}(b)$, we would have $v r u$ (since $r$ connects the domain), which implies $b = f(v) s f(u) = a$, contradicting $a s b$ by asymmetry of $s$. Therefore $f^{-1}$ is $s$-$r$ order preserving.
