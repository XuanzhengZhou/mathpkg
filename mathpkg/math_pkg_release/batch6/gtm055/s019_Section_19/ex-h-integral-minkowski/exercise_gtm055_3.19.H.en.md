---
role: exercise
locale: en
chapter: "3"
section: "19"
exercise_number: "H"
---

Let $(X, \mathbf{S}, \mu)$ and $(Y, \mathbf{T}, \nu)$ be measure spaces and let $f$ be a measurable function on the product space $X \times Y$ such that for almost every $y$ in $Y$ the function $x \to f(x, y)$ belongs to $\mathcal{L}_p(X)$ and such that the function $y \to \|f\|_{p, y}$ is integrable $[\nu]$ over $Y$. (Note that $\| f \|_{p, y}$ is a measurable function on $Y$ by Lemma 9.1.) Show that the function

$$\left| \int_Y f(x, y) d\nu(y) \right|^p$$

is integrable $[\mu]$ over $X$, and that

$$\left[ \int_X \left| \int_Y f(x, y) d\nu(y) \right|^p d\mu(x) \right]^{1/p} \leq \int_Y \| f \|_{p, y} d\nu(y).$$

(Hint: Show that it suffices to treat the case of a nonnegative simple function of the form $\sum_{i,j} t_{ij} \chi_{E_i \times F_j}$ where $\{E_1, \ldots, E_m\}$ and $\{F_1, \ldots, F_n\}$ are disjoint collections of measurable subsets of $X$ and $Y$, respectively.) Show also that this version of the Minkowski inequality implies Lemma 17.3.
