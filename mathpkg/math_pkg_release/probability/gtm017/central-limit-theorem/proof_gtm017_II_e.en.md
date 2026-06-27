---
role: proof
locale: en
of_concept: central-limit-theorem
source_book: gtm017
source_chapter: "II"
source_section: "e"
---
The proof (Petrovsky-Kolmogorov) uses two lemmas.

\textbf{Lemma 1:} For $V(x,t) = \Phi(x/\sqrt{t}) + \varepsilon t$, and sufficiently large $n$,
$V(x, t + 1/n) > \int V(x-\xi,t) dF_n(\xi)$ in $t > \delta$.

\textbf{Lemma 2:} For distribution functions $G_1, G_2$ with zero mean and variance $< \beta$:
$G_1(x) - G_2(x+2\alpha) \leq \beta/\alpha^2$ for all $x, \alpha > 0$.

The proof replaces each of the $n$ distribution functions $F_n(x)$ by $\Phi(\sqrt{n}x)$, then uses the "upper function" $V(x,t)$ and "lower function" analogous arguments to sandwich $U_n(x)$. Through careful error estimates, $\lim_{n \to \infty} U_n(x) = \Phi(x)$ is obtained.
