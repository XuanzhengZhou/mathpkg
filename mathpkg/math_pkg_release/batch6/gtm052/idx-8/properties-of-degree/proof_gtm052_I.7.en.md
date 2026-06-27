---
role: proof
locale: en
of_concept: properties-of-degree
source_book: gtm052
source_chapter: "I"
source_section: "7"
---

(a) Since $Y \neq \emptyset$, $P_Y$ is a nonzero polynomial of degree $r = \dim Y$. By (7.3a), $\deg Y = c_0$ where $c_0$ is the leading coefficient of $P_Y$ multiplied by $r!$, which is an integer. It is a positive integer because for $l \gg 0$, $P_Y(l) = \dim_k S(Y)_l > 0$.

(b) Let $I_1, I_2$ be the homogeneous ideals of $Y_1, Y_2$. The condition $\dim(Y_1 \cap Y_2) < r$ implies that the Hilbert polynomials satisfy $P_{Y_1 \cup Y_2} = P_{Y_1} + P_{Y_2}$ up to lower-degree terms. Comparing leading coefficients and multiplying by $r!$ gives the additivity.

(c) For $\mathbf{P}^n$, the homogeneous coordinate ring is $S = k[x_0, \ldots, x_n]$, so $P_{\mathbf{P}^n}(l) = \binom{l+n}{n}$, which is a polynomial of degree $n$ with leading coefficient $1/n!$. Hence $\deg \mathbf{P}^n = n! \cdot (1/n!) = 1$.

(d) If $I_H = (f)$ with $f$ homogeneous of degree $d$, then from the exact sequence $0 \to S(-d) \xrightarrow{f} S \to S/(f) \to 0$, we obtain $P_H(l) = \binom{l+n}{n} - \binom{l-d+n}{n}$. The leading term is $\frac{d}{(n-1)!} l^{n-1}$, so $\deg H = (n-1)! \cdot \frac{d}{(n-1)!} = d$.
