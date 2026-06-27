---
role: proof
locale: en
of_concept: monotone-convergence-theorem
source_book: gtm018
source_chapter: "V"
source_section: "26"
---

Since $\{f_n\}$ is a non-decreasing sequence, $\{\int f_n d\mu\}$ is a non-decreasing sequence of extended real numbers, so that $\lim_n \int f_n d\mu$ exists (finite or $+\infty$). Since $f_n \leq f$ a.e., we have $\int f_n d\mu \leq \int f d\mu$ for every $n$, and therefore

$$\lim_n \int f_n d\mu \leq \int f d\mu.$$

To prove the reverse inequality, let $g$ be any non-negative simple function such that $g \leq f$ a.e., and let $c$ be a real number with $0 < c < 1$. For each $n = 1, 2, \cdots$, define

$$E_n = \{x : f_n(x) \geq c g(x)\}.$$

Since $\{f_n\}$ is non-decreasing and converges to $f$ a.e., the sequence $\{E_n\}$ is increasing and $\lim_n E_n = X$ (up to a null set). Then

$$\int f_n d\mu \geq \int_{E_n} f_n d\mu \geq c \int_{E_n} g d\mu.$$

Since $g$ is a simple function, its indefinite integral is a finite measure, and by continuity from below (9.D),

$$\lim_n \int_{E_n} g d\mu = \int g d\mu.$$

Thus $\lim_n \int f_n d\mu \geq c \int g d\mu$. Since $c < 1$ is arbitrary, we have $\lim_n \int f_n d\mu \geq \int g d\mu$. Taking the supremum over all simple functions $g \leq f$ yields

$$\lim_n \int f_n d\mu \geq \int f d\mu,$$

which, together with the reverse inequality already established, completes the proof.
