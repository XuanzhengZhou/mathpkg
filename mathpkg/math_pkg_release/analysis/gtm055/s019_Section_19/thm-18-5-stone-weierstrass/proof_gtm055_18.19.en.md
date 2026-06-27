---
role: proof
locale: en
of_concept: thm-18-5-stone-weierstrass
source_book: gtm055
source_chapter: "18"
source_section: "19"
---

The proof is fairly lengthy and given in part as a sequence of preparatory propositions and lemmas. The first step is to elucidate the role of the hypothesis of self-conjugacy via Lemma 18.6: a self-conjugate subalgebra $\mathcal{A}$ of $\mathcal{C}(X)$ is closed under taking real and imaginary parts.

Next, one uses the Taylor series for $\sqrt{1-\lambda}$ to construct a sequence of polynomials $\{p_n(t)\}$ converging uniformly to $\sqrt{1-t}$ on $[0,1]$, with each $p_n$ having no constant term. This leads to Proposition 18.8 (Kakutani): every closed subalgebra of $\mathcal{C}_{\mathbb{R}}(X)$ is also a sublattice, since for any $f$ in the subalgebra one can approximate $|f|$ by $r_n \circ (f/\|f\|_\infty)^2$ where $\{r_n\}$ are polynomials with zero constant term converging to $\sqrt{t}$.

Lemma 18.9 then shows that a strongly separating subalgebra $\mathcal{A}$ of $\mathcal{C}_{\mathbb{R}}(X)$ has the property that for distinct points $x_1, x_2$ in $X$ and any real numbers $t_1, t_2$, there exists $f \in \mathcal{A}$ with $f(x_1) = t_1$ and $f(x_2) = t_2$.

Finally, to prove density of $\mathcal{A}$: given any $g \in \mathcal{C}_{\mathbb{R}}(X)$ and $\varepsilon > 0$, for each $x \in X$ and each $y \in X$ one constructs functions $F_y \in \mathcal{A}$ with $F_y(x) = g(x)$ and $F_y > g - \varepsilon$. By compactness, finitely many neighborhoods cover $X$, and taking the infimum of the corresponding $F_y$ yields a function $G \in \mathcal{A}$ with $\|G - g\| \leq \varepsilon$. This proves $\mathcal{A}$ is dense in $\mathcal{C}_{\mathbb{R}}(X)$.
