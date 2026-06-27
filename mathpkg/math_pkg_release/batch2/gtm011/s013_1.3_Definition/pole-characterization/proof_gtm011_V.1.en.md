---
role: proof
locale: en
of_concept: pole-characterization
source_book: gtm011
source_chapter: "V"
source_section: "1"
---

Suppose that $f$ has a pole at $z = a$. Since $\lim_{z \to a} |f(z)| = \infty$, it follows that $[f(z)]^{-1}$ has a removable singularity at $z = a$ with limit $0$. Hence, define
$$h(z) = 
\begin{cases}
[f(z)]^{-1}, & z \neq a,\\
0, & z = a.
\end{cases}$$
Then $h$ is analytic in $B(a; R)$ for some $R > 0$. Since $h(a) = 0$, by Corollary IV.3.9 there exists an analytic function $h_1$ with $h_1(a) \neq 0$ and a positive integer $m$ such that
$$h(z) = (z-a)^m h_1(z).$$
Therefore, for $z \neq a$,
$$(z-a)^m f(z) = \frac{1}{h_1(z)},$$
which has a removable singularity at $z = a$. Define $g(z) = (z-a)^m f(z)$ for $z \neq a$ and $g(a) = 1/h_1(a)$. Then $g$ is analytic on $G$ and
$$f(z) = \frac{g(z)}{(z-a)^m}$$
for all $z \in G \setminus \{a\}$.
