---
role: proof
locale: en
of_concept: kernel-is-proper-ideal
source_book: gtm008
source_chapter: "1"
source_section: "Boolean Algebra"
---

**Proof.** Since $f(0) = 0$, $0 \in \ker(f)$. If $a, b \in \ker(f)$, then $f(a + b) = f(a) + f(b) = 0 + 0 = 0$, so $a + b \in \ker(f)$. If $a \in \ker(f)$ and $b \in |B|$, then $f(ab) = f(a)f(b) = 0 \cdot f(b) = 0$, so $ab \in \ker(f)$. Since $f(1) = 1 \neq 0$, $1 \notin \ker(f)$, so $\ker(f)$ is proper. If $\ker(f) = \{0\}$ and $f(a) = f(b)$, then $f(a(-b) + b(-a)) = 0$, so $a(-b) + b(-a) = 0$, implying $a = b$, so $f$ is injective.
