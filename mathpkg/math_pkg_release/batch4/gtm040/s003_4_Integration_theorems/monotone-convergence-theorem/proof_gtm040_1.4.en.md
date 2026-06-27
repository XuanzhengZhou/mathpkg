---
role: proof
locale: en
of_concept: monotone-convergence-theorem
source_book: gtm040
source_chapter: "1"
source_section: "4"
---
Since the $\{f_n\}$ increase with $n$, so do the integrals, and $k = \lim_{n \to \infty} \int_E f_n d\mu$ exists. Since $f_n \leq f$, we have $k \leq \int_E f d\mu$. For the reverse inequality, let $c \in (0,1)$ and let $s$ be a simple function with $0 \leq s \leq f$. Set $E_n = \{x \in E \mid f_n(x) \geq c s(x)\}$. Then $E_1 \subset E_2 \subset \cdots$ and $E = \bigcup_n E_n$. We have $k \geq \int_{E_n} f_n d\mu \geq c \int_{E_n} s d\mu$. Since the integral is completely additive, $\lim_{n} c \int_{E_n} s d\mu = c \int_E s d\mu$, so $k \geq c \int_E s d\mu$. Letting $c \to 1$ and taking supremum over $s$ yields $k \geq \int_E f d\mu$.
