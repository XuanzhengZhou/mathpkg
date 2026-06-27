---
role: proof
locale: en
of_concept: zero-set-of-continuous-function-is-g-delta
source_book: gtm027
source_chapter: "4"
source_section: "J"
---

# Proof of Theorem J(a): The zero set of a continuous real-valued function is a $G_\delta$ set

**Theorem.** If $f: X \to \mathbb{R}$ is a continuous real-valued function on a topological space $X$, then $f^{-1}[\{0\}]$ is a $G_\delta$ set in $X$.

**Proof.** In the space $\mathbb{R}$ of real numbers with the usual topology, the singleton $\{0\}$ is a $G_\delta$ set. Indeed,

$$\{0\} = \bigcap_{n=1}^{\infty} \left(-\frac{1}{n}, \frac{1}{n}\right),$$

which expresses $\{0\}$ as a countable intersection of open sets.

Since $f$ is continuous, the preimage of each open set $\left(-\frac{1}{n}, \frac{1}{n}\right)$ is open in $X$. Moreover, the preimage operation commutes with arbitrary intersections:

$$f^{-1}[\{0\}] = f^{-1}\left[\bigcap_{n=1}^{\infty} \left(-\frac{1}{n}, \frac{1}{n}\right)\right] = \bigcap_{n=1}^{\infty} f^{-1}\left[\left(-\frac{1}{n}, \frac{1}{n}\right)\right].$$

Each set $f^{-1}[(-\frac{1}{n}, \frac{1}{n})]$ is open in $X$, so the right-hand side is a countable intersection of open sets. By definition, $f^{-1}[\{0\}]$ is a $G_\delta$ set in $X$. $\square$
