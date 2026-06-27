---
role: proof
locale: en
of_concept: "let-be-a-complex-valued--measurable-function-on-then"
source_book: gtm025
source_chapter: "The Lebesgue Integral"
source_section: "12.28"
---

Conclusion (i) follows directly from the inequalities

$$|f| \leq |\text{Re} f| + |\text{Im} f| \leq 2|f|$$

and the fact that $|g| = g^+ + g^-$ for real-valued $g$'s. To prove (ii), repeat the argument of (9.4).

(12.29) Note. To find necessary and sufficient conditions for equality in the inequality $\left| \int_X f d\mu \right| \leq \int_X |f| d\mu$, consider $h \in \mathfrak{L}_1$. We then ask when the equality

$$|\int h d\mu| = \int |h| d\mu$$

holds. It clearly suffices to have $h = \exp(i\alpha)|h|$ where $\alpha$ is any real number. We now show that this condition is also necessary. Suppose then that $\int h d\mu = \exp(i\beta)\int |h| d\mu$ for a real number $\beta$, and

Then $\lim_{n \to \infty} f_n \in \mathfrak{L}_1$ and

$$\lim_{n \to \infty} \int_X f_n d\mu = \int_X \lim_{n \to \infty} f_n d\mu.$$

Proof. Let $f(x) = \lim_{n \to \infty} f_n(x)$ whenever this limit exists. Clearly $f$ is defined a.e. on $X$ and is $\mathcal{A}$-measurable. Also $|f(x) - f_n(x)| \leq |f(x)| + |f_n(x)| \leq 2s(x)$ for all $n \in N$ and $\lim_{n \to \infty} |f(x) - f_n(x)| = 0$ a.e. Thus, by (12.24) and (12.28.ii), we have

$$\left| \int_X f d\mu - \int_X f_n d\mu \right| \leq \int_X |f - f_n| d\mu \rightarrow \int_X 0 d\mu = 0.$$
