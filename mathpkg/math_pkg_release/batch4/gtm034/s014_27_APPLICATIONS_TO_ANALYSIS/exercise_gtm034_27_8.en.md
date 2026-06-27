---
role: exercise
locale: en
chapter: "27"
section: "APPLICATIONS TO ANALYSIS"
exercise_number: 8
---

Consider simple random walk in three dimensions. Let $C$ be the family of all regular functions $f$ normalized so that $f(0) = 1$, and with the property that there is a constant $M < \infty$ such that $f(x) \leq M G(0,x)$ for $x \in R$. Show that $C$ is non-empty and compact in the topology of pointwise convergence. Enumerate the points in $R$ as $x_1, x_2, \dots$
Let $C_0 = C$,
$$C_1 = \left\{ \varphi \mid \varphi \in C; \varphi(x_1) = \max_{f \in C} f(x_1) \right\},$$
$$C_{n+1} = \left\{ \varphi \mid \varphi \in C_n; \varphi(x_{n+1}) = \max_{f \in C_n} f(x_{n+1}) \right\},$$
and show that $\bigcap_{n=0}^{\infty} C_n$ consists of a single regular function $\bar{f}(x)$. Show that this is a minimal regular function, i.e., that $f \in C$ and $f \leq \bar{f}$ on $R$ implies that $f = \bar{f}$. But
$$\bar{f}(x) = \sum_{y \in R} P(x,y)\bar{f}(y) = \sum_{z \in R} P(0,z)\bar{f}(z) \frac{\bar{f}(z+x)}{\bar{f}(z)}$$
exhibits $\bar{f}$ as a convex combination of the functions
$$\varphi_z(x) = \frac{\bar{f}(z+x)}{\bar{f}(z)}$$
which are in $C$. Since $\bar{f}$ is minimal one can conclude that $\varphi_z = \bar{f}$ whenever $P(0,z) > 0$. Consequently $\bar{f}(z+x) = \bar{f}(z)\bar{f}(x)$ for all $x,z \in R$, which shows that $\bar{f}$ is an exponential. Prove that $\bar{f}$ is constant and conclude that simple random walk has only constant regular functions.
