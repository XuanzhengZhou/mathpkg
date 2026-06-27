---
role: proof
locale: en
of_concept: nonconstant-homothety-homeomorphism
source_book: gtm015
source_chapter: "Chapter 2 – Topological Vector Spaces"
source_section: "11. Real and complex topological vector spaces"
---

# Proof of Nonconstant Homothety is a Homeomorphism

**Theorem (11.5).** In a TVS, every nonconstant homothety is a homeomorphism.

*Proof.* Say the homothety is $f(x) = \lambda x + a$, where $\lambda \neq 0$. Since the inverse of $f$ is also a homothety (namely $f^{-1}(y) = \lambda^{-1}(y - a)$), it suffices to show that $f$ is continuous. This is evident from the factorization $x \mapsto \lambda x \mapsto \lambda x + a$: the mapping $x \mapsto \lambda x$ is continuous by the continuity of scalar multiplication $(\lambda, x) \mapsto \lambda x$ (with $\lambda$ fixed), and the translation $y \mapsto y + a$ is continuous by the continuity of addition (with $a$ fixed). Hence $f$ is continuous. $\square$
