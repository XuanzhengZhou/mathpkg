---
role: proof
locale: en
of_concept: gcd-in-ufd
source_book: gtm028
source_chapter: "I"
source_section: "14"
---

Let $a, b$ be elements of a UFD $R$. If either is zero, their GCD is the other (or any associate thereof). Assume both are non-zero. By UF1, each can be factored into irreducibles. Collecting associate irreducible factors, we may write

$$a = \epsilon \prod_{i} p_i^{\alpha_i}, \quad b = \eta \prod_{i} p_i^{\beta_i},$$

where $\epsilon, \eta$ are units, the $p_i$ are pairwise non-associate irreducibles, and $\alpha_i, \beta_i \geq 0$ (allowing zero exponents for irreducibles not appearing in one factorization). By UF2, this representation is essentially unique.

Define $d = \prod_i p_i^{\min(\alpha_i, \beta_i)}$. Then $d$ divides both $a$ and $b$. If $c$ is any common divisor of $a$ and $b$, then in the irreducible factorization of $c$, each irreducible factor $p_i$ can appear with exponent at most $\min(\alpha_i, \beta_i)$, hence $c \mid d$. Thus $d$ is a greatest common divisor of $a$ and $b$.
