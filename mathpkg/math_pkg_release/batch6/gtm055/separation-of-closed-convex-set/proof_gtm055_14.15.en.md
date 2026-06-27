---
role: proof
locale: en
of_concept: separation-of-closed-convex-set
source_book: gtm055
source_chapter: "14"
source_section: "15"
---

Let $V$ be a convex open neighborhood of $x_0$ that does not meet $C$. Then, as was seen in the proof of Proposition 14.14, there exists a continuous nonzero real linear functional $f$ on $\mathcal{E}$ such that $f(u) \leq f(v)$ whenever $u \in C$ and $v \in V$. Set $c = \sup\{f(u) : u \in C\}$, and let $g$ be the complex linear functional on $\mathcal{E}$ such that $\text{Re } g = f$ (see the proof of Theorem 14.3). Then $g$ is continuous along with $f$, and $\text{Re } g(x) \leq c$ for all $x \in C$. To complete the proof we note that $f(V)$ is an open set in $\mathbb{R}$: fix $z_0$ with $f(z_0) \neq 0$, and for each $v \in V$ choose $\delta > 0$ such that $v + tz_0 \in V$ for all $-\delta < t < +\delta$. Then $f(V)$ contains $\{f(v) + tf(z_0) : -\delta < t < +\delta\}$. Hence if $V$ contained any $v$ with $f(v) = c$, then $V$ would also contain vectors $v'$ with $f(v') > c$, contradicting the definition of $c$. Thus $\text{Re } g(x_0) = f(x_0) > c$.
