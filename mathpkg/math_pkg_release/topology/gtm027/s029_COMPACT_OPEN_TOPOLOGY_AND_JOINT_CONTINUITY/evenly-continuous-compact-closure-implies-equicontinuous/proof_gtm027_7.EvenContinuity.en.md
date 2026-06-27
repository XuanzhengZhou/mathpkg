---
role: proof
locale: en
of_concept: evenly-continuous-compact-closure-implies-equicontinuous
source_book: gtm027
source_chapter: "7"
source_section: "Even Continuity"
---

# Proof of Theorem 7.23 — Even Continuity with Compact Closure Implies Equicontinuity

Let $F$ be an evenly continuous family of functions on a topological space $X$ to a uniform space $Y$. Suppose $x \in X$ is such that the closure $F[x]^-$ is compact. We prove $F$ is equicontinuous at $x$.

Let $d$ be a pseudo-metric in the gage of $Y$ and let $r > 0$. For each $y \in F[x]^-$, by even continuity of $F$, there exist neighborhoods $W_y$ of $y$ and $V_y$ of $x$ such that: for all $f \in F$, if $f(x) \in W_y$, then $f[V_y]$ is contained in the sphere of $d$-radius $r/2$ about $y$.

Since $F[x]^-$ is compact, the open cover $\{W_y : y \in F[x]^-\}$ has a finite subcover $\{W_{y_1}, \dots, W_{y_n}\}$. Let $V_{y_1}, \dots, V_{y_n}$ be the corresponding neighborhoods of $x$, and set

$$V = \bigcap_{i=1}^n V_{y_i},$$

which is a neighborhood of $x$.

Now for any $f \in F$, we have $f(x) \in F[x] \subset F[x]^-$, so $f(x) \in W_{y_i}$ for some $i$. Then for any $v \in V \subset V_{y_i}$, we have $f(v)$ in the $d$-sphere of radius $r/2$ about $y_i$. Also $f(x) \in W_{y_i}$ implies $f[V_{y_i}]$ lies in that same sphere, so in particular $f(x)$ is in the $d$-sphere of radius $r/2$ about $y_i$. By the triangle inequality,

$$d(f(x), f(v)) \leq d(f(x), y_i) + d(y_i, f(v)) < r/2 + r/2 = r.$$

Thus $f[V]$ is contained in the $d$-sphere of radius $r$ about $f(x)$ for all $f \in F$. This proves $F$ is equicontinuous at $x$.
