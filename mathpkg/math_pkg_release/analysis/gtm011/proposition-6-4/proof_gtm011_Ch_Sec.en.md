---
role: proof
locale: en
of_concept: proposition-6-4
source_book: gtm011
source_chapter: ""
source_section: ""
---

Proof. Let $\gamma_1$ be a closed rectifiable curve

this assumption and providing the details to transform the preceding paragraph into a legitimate proof (Exercise 9). Indeed, in a course designed for physicists and engineers this is probably preferable. But this is not desirable for the training of mathematicians.

The statement of a theorem is not as important as its proof. Proofs are important in mathematics for several reasons, not the least of which is that a proof deepens our insight into the meaning of the theorems and gives a natural delineation of the extent of the theorem’s validity. Most important for the education of a mathematician, it is essential to examine other proofs because they reveal methods.

A good method is worth a thousand theorems. Not only is this statement valid as a value judgement, but also in a literal sense. An important method can be reused in other situations to obtain further results.

With this in mind a complete proof of Theorem 6.6 will be presented. In fact, we will prove a somewhat more general fact since the proof of this new result necessitates only a little more effort than the proof that $n(\gamma; w) = 0$ for $w$ in $\mathbb{C} - G$ whenever $\gamma \sim 0$. In fact, the proof of the next result more clearly reveals the usefulness of the method.

6.7 Cauchy’s Theorem (Third Version). If $\gamma_0$ and $\gamma_1$ are two closed rectifiable curves in $G$ and $\gamma_0 \sim \gamma_1$ then

$$\int_{\gamma_0} f = \int_{\gamma_1} f$$

for every function $f$ analytic on $G$.

Before proceeding let us consider a special case. Suppose $\Gamma$ satisfies (6.2) and also suppose $\Gamma$ has continuous second partial derivatives. Hence

$$\frac{\partial^2 \Gamma}{\partial s \partial t} = \frac{\partial^2 \Gamma}{\partial t \partial s}$$

throughout the square $I^2 = [0, 1] \times [0, 1]$. Define

$$g(t) = \int_0^1 f(\Gamma(s, t)) \frac{\partial \Gamma}{\partial s} (s, t) \, ds;$$

then $g(0) = \int_{\gamma_0

hence

$$g'(t) = f(\Gamma(1, t)) \frac{\partial \Gamma}{\partial t} (1, t) - f(\Gamma(0, t)) \frac{\partial \Gamma}{\partial t} (0, t).$$

Since $\Gamma(1, t) = \Gamma(0, t)$ for all $t$ we get $g'(t) = 0$ for all $t$. So $g$ is a constant; in particular $\int_{\gamma_0} f = \int_{\gamma_1} f$.

Proof of Theorem 6.7. Let $\Gamma: I^2 \rightarrow G$ satisfy (6.2). Since $\Gamma$ is continuous and $I^2$ is compact, $\Gamma$ is uniformly continuous and $\Gamma(I^2)$ is a compact subset of $G$. Thus

$$r = d(\Gamma(I^2), \mathbb{C} - G) > 0$$

and there is an integer $n$ such that if $(s - s')^2 + (t - t')^2 < 4/n^2$ then

$$|\Gamma(s, t) - \Gamma(s', t')| < r.$$

Let

$$Z_{jk} = \Gamma\left(\frac{j}{n}, \frac{k}{n}\right), \quad 0 \leq j, k \leq n$$

and put

$$J_{jk} = \left[ \frac{j}{n}, \frac{j+1}{n} \right] \times \left[ \frac{k}{n}, \frac{k+1}{n} \right]$$

for $0 \leq j, k \leq n - 1$. Since the diameter of the square $J_{jk}$ is $\frac{\sqrt{2}}{n}$, it follows that $\Gamma(J_{jk}) \subset B(Z_{jk}; r)$. So if
