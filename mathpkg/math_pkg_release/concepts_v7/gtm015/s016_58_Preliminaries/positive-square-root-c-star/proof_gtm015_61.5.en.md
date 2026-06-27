---
role: proof
locale: en
of_concept: positive-square-root-c-star
source_book: gtm015
source_chapter: "Chapter 7: C*-Algebras"
source_section: "58. Preliminaries"
---

# Proof of Existence and Uniqueness of Positive Square Root

Proof. Since $aa^*$ and $a^*a$ have the same nonzero spectra (51.16), one also has $-aa^* \geq 0$. Write $a = b + ic$ with $b$ and $c$ self-adjoint. Elementary algebra yields

$$a^*a + aa^* = 2b^2 + 2c^2.$$

Since $b^* = b$, it is clear from (59.2) (or from (53.3)) that $2b^2 \geq 0$. Similarly $2c^2 \geq 0$, thus

$$a^*a = 2b^2 + 2c^2 - aa^* \geq 0$$

by (61.6). From $-a^*a \geq 0$ and $a^*a \geq 0$ we infer that $\sigma(a^*a) = \{0\}$, whence $a^*a = 0$ (58.3) and therefore $a = 0$.
