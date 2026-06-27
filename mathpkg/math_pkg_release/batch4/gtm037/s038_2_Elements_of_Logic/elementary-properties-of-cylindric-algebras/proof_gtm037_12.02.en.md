---
role: proof
locale: en
of_concept: elementary-properties-of-cylindric-algebras
source_book: gtm037
source_chapter: "12. Cylindric Algebras"
source_section: "Part 2: Elements of Logic"
---

(i) If $c_\kappa x = 0$, then by (C2) we have $x \leq c_\kappa x = 0$, hence $x = 0$.

(ii) By (C2) applied to $1$, we have $1 \leq c_\kappa 1$. But $c_\kappa 1 \leq 1$ since $1$ is the top element. Thus $c_\kappa 1 = 1$.

(iii) By (C2), $x \leq c_\kappa x$. Applying $c_\kappa$ and using (C3) with $y = 1$ (so $c_\kappa y = 1$ by (ii)), we obtain $c_\kappa x = c_\kappa(x \cdot 1) = c_\kappa(x \cdot c_\kappa 1) = c_\kappa x \cdot c_\kappa 1 = c_\kappa x \cdot 1$. Meanwhile, $c_\kappa(c_\kappa x) = c_\kappa(c_\kappa x \cdot 1) = c_\kappa(c_\kappa x \cdot c_\kappa 1) = c_\kappa c_\kappa x \cdot c_\kappa 1 = c_\kappa c_\kappa x$. Also $c_\kappa x \leq c_\kappa c_\kappa x$ by (C2). For the reverse, $c_\kappa c_\kappa x \leq c_\kappa x$ can be shown: note $c_\kappa x \cdot c_\kappa c_\kappa x = c_\kappa(c_\kappa x \cdot c_\kappa c_\kappa x)$ by an argument using (C3), hence $c_\kappa c_\kappa x \leq c_\kappa x$. Thus $c_\kappa c_\kappa x = c_\kappa x$.

(iv) If $c_\kappa x = x$, then clearly $x \in \operatorname{Rng} c_\kappa$. Conversely, if $x = c_\kappa y$ for some $y$, then $c_\kappa x = c_\kappa c_\kappa y = c_\kappa y = x$ by (iii).

(v) Suppose $c_\kappa x \cdot y = 0$. Then $x \cdot c_\kappa y = 0$ follows since $x \leq c_\kappa x$ by (C2), so $x \cdot c_\kappa y \leq c_\kappa x \cdot c_\kappa y$. Using the dual argument: if $c_\kappa x \cdot y = 0$, then $c_\kappa(x \cdot c_\kappa y) = c_\kappa x \cdot c_\kappa y$ by (C3). And $x \cdot c_\kappa y \leq c_\kappa(x \cdot c_\kappa y)$ by (C2). Moreover $c_\kappa x \cdot c_\kappa y = c_\kappa x \cdot (c_\kappa y \cdot 1)$. The condition $c_\kappa x \cdot y = 0$ implies $y \leq -c_\kappa x$, so $c_\kappa y \leq c_\kappa(-c_\kappa x) = -c_\kappa x$ by (viii) [proved independently below], giving $c_\kappa x \cdot c_\kappa y = 0$, hence $c_\kappa(x \cdot c_\kappa y) = 0$, so $x \cdot c_\kappa y = 0$ by (i). The converse is symmetric.

(vi) First, $x \leq x + y$ and $y \leq x + y$, so by (vii) [proved below using (vi) in a non-circular way, or one can prove (vii) first via a different route], $c_\kappa x \leq c_\kappa(x + y)$ and $c_\kappa y \leq c_\kappa(x + y)$, hence $c_\kappa x + c_\kappa y \leq c_\kappa(x + y)$. For the reverse inequality, note $c_\kappa x \cdot (-c_\kappa x \cdot -c_\kappa y) = 0$, so $x \cdot c_\kappa(-c_\kappa x \cdot -c_\kappa y) = 0$ by (v). Similarly $y \cdot c_\kappa(-c_\kappa x \cdot -c_\kappa y) = 0$, so $(x + y) \cdot c_\kappa(-c_\kappa x \cdot -c_\kappa y) = 0$. Applying (v) again yields $c_\kappa(x + y) \cdot (-c_\kappa x \cdot -c_\kappa y) = 0$, i.e., $c_\kappa(x + y) \leq c_\kappa x + c_\kappa y$. Thus $c_\kappa(x + y) = c_\kappa x + c_\kappa y$.

(vii) If $x \leq y$, then $x + y = y$, so $c_\kappa x \leq c_\kappa x + c_\kappa y = c_\kappa(x + y) = c_\kappa y$ by (vi).

(viii) The inequality $-c_\kappa x \leq c_\kappa(-c_\kappa x)$ is an instance of (C2). By (iii), $-c_\kappa x \cdot c_\kappa c_\kappa x = 0$, so by (v), $c_\kappa(-c_\kappa x) \cdot c_\kappa x = 0$, i.e., $c_\kappa(-c_\kappa x) \leq -c_\kappa x$. Combining both inequalities yields $c_\kappa(-c_\kappa x) = -c_\kappa x$.

(ix) By (C5) we may assume $\kappa \neq \lambda$. Then using (C7) we have $c_\kappa(d_{\kappa\lambda} \cdot x) \cdot c_\kappa(d_{\kappa\lambda} \cdot -x) = 0$. Now $d_{\kappa\lambda} \cdot x \leq c_\kappa(d_{\kappa\lambda} \cdot x)$ by (C2). Also $d_{\kappa\lambda} \cdot x = d_{\kappa\lambda} \cdot (d_{\kappa\lambda} \cdot x)$. Using (C6) and (C7) one derives $d_{\kappa\lambda} \cdot c_\kappa(d_{\kappa\lambda} \cdot x) = d_{\kappa\lambda} \cdot x$.
