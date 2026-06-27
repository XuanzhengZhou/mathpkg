---
role: proof
locale: en
of_concept: en-is-nowhere-dense
source_book: gtm002
source_chapter: "11"
source_section: "Nowhere Differentiable Functions"
---

Any continuous function on $[0, 1]$ can be approximated uniformly and arbitrarily closely by a piecewise-linear continuous function $g$. To show that $E_n$ is nowhere dense in $C$, it suffices to show that for any such function $g$, and for any $\varepsilon > 0$, there is a function $h \in C \setminus E_n$ such that $\varrho(g, h) \leq \varepsilon$.

Let $M$ be the maximum absolute value of the slopes of the linear segments that constitute the graph of $g$, and choose an integer $m$ such that $m \varepsilon > n + M$. Let $\phi$ denote the "saw-tooth" function
$$\phi(x) = \min(x - [x], [x] + 1 - x),$$
which equals the distance from $x$ to the nearest integer. Define
$$h(x) = g(x) + \varepsilon \phi(m x).$$

Then at each point of $[0, 1)$ the function $h$ has a one-sided derivative on the right numerically greater than $n$. This is clear, since $\varepsilon \phi(m x)$ has everywhere in $[0, 1)$ a right derivative equal to $\pm \varepsilon m$, and $g$ has a right derivative with absolute value at most equal to $M$. Therefore $h \in C \setminus E_n$.

Since $\varrho(g, h) = \varepsilon/2$, and $\varepsilon > 0$ was arbitrary, it follows that $E_n$ is nowhere dense in $C$.
