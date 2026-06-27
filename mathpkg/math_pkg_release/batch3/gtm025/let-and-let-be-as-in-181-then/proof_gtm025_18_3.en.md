---
role: proof
locale: en
of_concept: "let-and-let-be-as-in-181-then"
source_book: gtm025
source_chapter: "Differentiation"
source_section: "18.3"
---

If $f = \xi_A$, where $A$ is a measurable subset of $]a, b[$, then $F(x

$x \in [a, b]$ (11.35). Write $S_n(x) = \int_a^x s_n(t) dt$ for $n \in N$; B. Levi's theorem (12.22) shows that

$$F(x) = \int_a^x f(t) dt = \lim_{n \to \infty} \int_a^x s_n(t) dt = \lim_{n \to \infty} S_n(x)$$

$$= S_1(x) + \sum_{n=1}^{\infty} [S_{n+1}(x) - S_n(x)]$$

(2)

for all $x \in [a, b]$. Each function $S_{n+1} - S_n$ is the integral of a nonnegative function and so is nondecreasing. Fubini's theorem (17.18) applied to (2) gives us the equalities

$$F'(x) = S_1'(x) + \sum_{n=1}^{\infty} [S_{n+1}'(x) - S_n'(x)]$$

$$= \lim_{n \to \infty} S_n'(x) \quad \text{a.e. in } ]a, b[$$

(3)

and (1) gives us

$$\lim_{n \to \infty} S_n'(x) = \lim_{n \to \infty} s_n(x) \quad \text{a.e. in } ]a, b[$$

(4)

Combining (3) and (4), we obtain (i).

Finally, if $f$ is an arbitrary function in $\mathfrak{L}_1([a, b])$, write

$$f = (f_1 - f_2) + i(f_3 - f_4)$$

where $f_j \in \mathfrak{L}_1^+$ and apply (i) for nonnegative functions. $\square$

Theorem (18.3) can be sharpened considerably, as the next two assertions show.
