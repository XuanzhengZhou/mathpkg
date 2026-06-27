---
role: proof
locale: en
of_concept: theorem-1-44
source_book: gtm040
source_chapter: "1"
source_section: "44"
---

**Proof:** Since the $\{f_n\}$ increase with $n$, so do the $\left\{\int_E f_n d\mu\right\}$. Therefore

$$k = \lim_{n \to \infty} \int_E f_n d\mu$$

exists. Since $f$ is non-negative and is the limit of measurable functions, we know that $\int_E f d\mu$ exists, and since $f_n \leq f$, we have

$$\int_E f_n d\mu \leq \int_E f d\mu$$

for every $n$. Therefore, $k \leq \int_E f d\mu$. Let $c$ be a real number satisfying $

so that $E_1 \subset E_2 \subset E_3 \subset \cdots$. Then $E = \bigcup_{n=1}^{\infty} E_n$. For any $n$ we have

$$k \geq \int_E f_n d\mu \geq \int_{E_n} f_n d\mu \geq c \int_{E_n} sd\mu.$$

Since the integral is a completely additive set function (Theorem 1-41), we have by Proposition 1-16

$$\lim_{n \to \infty} c \int_{E_n} sd\mu = c \int_E sd\mu.$$

Thus, as $n \to \infty$,

$$k \geq c \int_E sd\mu.$$

Letting $c \to 1$, we have $k \geq \int_E sd\mu$, and taking the supremum over all $s$, we find $k \geq \int_E fd\mu$.
