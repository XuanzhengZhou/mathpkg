---
role: proof
locale: en
of_concept: "let-and-be-complex-numbers-and-suppose-that"
source_book: gtm025
source_chapter: "Lp Spaces"
source_section: "15.4"
---

If $w = 0$, the inequality becomes $\frac{|z|^p}{2^{p-1}} \leq \frac{|z|^p}{2}$, which holds since $p - 1 \geq 1$. Thus we may suppose that $|z| \geq |w| > 0$. The inequality (i) is equivalent

Since $p \geq 2$, it is clear from (3) that $g'(\theta) \leq 0$ for $\theta \in \left[0, \frac{\pi}{2}\right]$. Therefore the function $g$ is nonincreasing in $\left[0, \frac{\pi}{2}\right]$, i.e., $g$ assumes its maximum value at 0. $\square$

(15.5) Clarkson's inequality for $p \geq 2$. For $p \geq 2$ and $f, g \in \mathfrak{L}_p$, we have

(i) $\left\| \frac{f + g}{2} \right\|_p^p + \left\| \frac{f - g}{2} \right\|_p^p \leq \frac{1}{2} \|f\|_p^p + \frac{1}{2} \|g\|_p^p$.

Proof. We may suppose that $f$ and $g$ assume complex values and are defined $\mu$-a.e. [(12.18) and (12.26)]. Then for all $x \in X$ such that $f(x)$ and $g(x)$ are defined, (15.4.i) implies that

$$\left| \frac{f(x) + g(x)}{2} \right|^p + \left| \frac{f(x) - g(x)}{2} \right|^p \leq \frac{|f(x)|^p}{2} + \frac{|g(x)|^p}{2}. \tag{1}$$

Integrating both sides of (1) over $X$, we obtain (i). $\square$

There is an analogue of (15.5.i) for $1 < p < 2$, which we establish next. The inequality and its proof, for some reason, are more complicated than for $p \geq 2$.
