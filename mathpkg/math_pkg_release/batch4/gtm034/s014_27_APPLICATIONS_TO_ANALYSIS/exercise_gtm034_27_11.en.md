---
role: exercise
locale: en
chapter: "27"
section: "APPLICATIONS TO ANALYSIS"
exercise_number: 11
---

It is not known whether the Wiener-Hopf equation
$$\sum_{y=0}^{\infty} P(x,y)f(y) = f(x), \quad x \geq 0,$$
has a solution for every transient random walk (excluding of course the trivial case with $P(0,x) = 0$ for $x \geq 0$ and $P(0,0) < 1$, when there is obviously no solution). Demonstrate, however, that example E27.3 does not extend to transient random walk, for the following reason. Take a random walk with negative mean, satisfying in addition the hypotheses in P19.6. Show that the unique non-negative solution of the above Wiener-Hopf equation is then of the form
$$f(x) = \sum_{k=0}^{\infty} r^k u(x-k), \quad x \geq 0,$$
where $r$ is a constant satisfying $0 < r < 1$, and where $u(x)$ is the function from the Wiener-Hopf factorization for this random walk. Conclude that $f(0) = 1/(1-r)$.
