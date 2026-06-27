---
role: proof
locale: en
of_concept: uniform-convergence-line-integral
source_book: gtm011
source_chapter: "2"
source_section: "2.7"
---

Let $\epsilon > 0$. Since $F_n \to F$ uniformly on $\{\gamma\}$, there exists an integer $N$ such that $|F_n(w) - F(w)| < \epsilon / V(\gamma)$ for all $w$ on $\{\gamma\}$ and $n \geq N$. Then by Proposition 1.17(b),

$$\left| \int_{\gamma} F - \int_{\gamma} F_n \right| = \left| \int_{\gamma} (F - F_n) \right| \leq \int_{\gamma} |F(w) - F_n(w)| \, |dw| \leq V(\gamma) \cdot \frac{\epsilon}{V(\gamma)} = \epsilon$$

whenever $n \geq N$. Hence $\int_{\gamma} F_n \to \int_{\gamma} F$ as $n \to \infty$.
