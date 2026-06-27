---
role: proof
locale: en
of_concept: topology-determined-by-algebra
source_book: gtm027
source_chapter: "7"
source_section: "S"
---

# Proof of Topology of C(X) Determined by Algebraic Operations

The topology of $C(X)$ is entirely determined by the algebraic operations. In detail: $f \geq 0$ iff $f$ is a square in $C(X)$, i.e., $f = g^2$ for some $g \in C(X)$. The norm $\|f\|$ can be characterized algebraically: $\|f\| = \inf\{\lambda > 0 : \lambda^2 \cdot 1 - f^2 \text{ is a square}\}$.

**Proof.** In $C(X)$, a function $f$ is nonnegative iff it admits a continuous square root $g = \sqrt{f} \in C(X)$. Thus the order structure is algebraically determined. The uniform norm can be recovered via:

$$\|f\| = \inf\{\lambda > 0 : \lambda^2 - f^2 \geq 0\} = \inf\{\lambda > 0 : \lambda^2 \cdot 1 - f^2 \text{ is a square}\}.$$

Indeed, $\|f\| = \sup_{x \in X} |f(x)|$, so $\lambda \geq \|f\|$ iff $\lambda^2 - f(x)^2 \geq 0$ for all $x \in X$, which means $\lambda^2 \cdot 1 - f^2$ is a nonnegative function, hence a square.

The algebraic operations (addition, multiplication, scalar multiplication) together with the characterization of the order and norm show that the entire topological (metric) structure of $C(X)$ is determined algebraically.
