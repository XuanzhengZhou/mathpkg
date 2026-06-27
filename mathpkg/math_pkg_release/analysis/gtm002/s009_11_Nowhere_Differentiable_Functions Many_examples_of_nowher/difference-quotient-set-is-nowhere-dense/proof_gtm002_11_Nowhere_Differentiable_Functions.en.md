---
role: proof
locale: en
of_concept: difference-quotient-set-is-nowhere-dense
source_book: gtm002
source_chapter: "11"
source_section: "Nowhere Differentiable Functions"
---

Any continuous function on $[0, 1]$ can be approximated uniformly and arbitrarily closely by a piecewise-linear continuous function $g$. To show that $E_n$ is nowhere dense in $C$, it suffices to show that for any such function $g$ and any $\varepsilon > 0$, there is a function $h \in C \setminus E_n$ such that $\varrho(g, h) \leq \varepsilon$.

Let $M$ be the maximum absolute value of the slopes of the linear segments that constitute the graph of $g$, and choose an integer $m$ such that $m\varepsilon > n + M$. Let $\phi$ denote the saw-tooth function

$$\phi(x) = \min(x - [x], [x] + 1 - x),$$

i.e., the distance from $x$ to the nearest integer. Put

$$h(x) = g(x) + \varepsilon \phi(mx).$$

Then at each point of $[0, 1)$ the function $h$ has a one-sided derivative on the right numerically greater than $n$. This is clear, since $\varepsilon \phi(mx)$ has everywhere in $[0, 1)$ a right derivative equal to $\pm \varepsilon m$, and $g$ has a right derivative with absolute value at most equal to $M$; therefore the right derivative of $h$ has absolute value at least $\varepsilon m - M > n$.

Consequently $h \notin E_n$, i.e., $h \in C \setminus E_n$. Since $\varrho(g, h) = \varepsilon \sup_{x} |\phi(mx)| = \varepsilon/2 \leq \varepsilon$, it follows that $E_n$ is nowhere dense in $C$.
