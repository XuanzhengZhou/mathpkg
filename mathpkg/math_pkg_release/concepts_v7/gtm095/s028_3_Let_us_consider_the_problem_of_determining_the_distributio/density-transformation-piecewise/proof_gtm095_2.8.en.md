---
role: proof
locale: en
of_concept: density-transformation-piecewise
source_book: gtm095
source_chapter: "2"
source_section: "8. Random Variables: II"
---

# Proof of Density Transformation Formula (Piecewise Monotone Case)

Let $\xi$ be a random variable with density $f_\xi(x)$. Suppose the transformation $\varphi = \varphi(x)$ is not globally monotone, but is defined on a finite union of closed intervals $\bigcup_{k=1}^{n} [a_k, b_k]$ and satisfies the following conditions on each open interval $I_k = (a_k, b_k)$:

1. $\varphi$ is continuously differentiable on $I_k$;
2. $\varphi$ is either strictly increasing or strictly decreasing on $I_k$;
3. $\varphi'(x) \neq 0$ for all $x \in I_k$.

Let $h_k = h_k(y)$ be the inverse function of the restriction $\varphi|_{I_k}$, and let $D_k$ be the domain of $h_k$ (i.e., the image $\varphi(I_k)$).

We wish to find $f_\eta(y)$, the density of $\eta = \varphi(\xi)$.

**Proof.** The event $\{\eta \leq y\}$ can be decomposed according to which interval $I_k$ contains $\xi$:

$$
\{\eta \leq y\} = \bigcup_{k=1}^{n} \{\xi \in I_k,\; \varphi(\xi) \leq y\}.
$$

Since the intervals $I_k$ are disjoint, these events are mutually exclusive. Hence

$$
F_\eta(y) = P(\eta \leq y) = \sum_{k=1}^{n} P(\xi \in I_k,\; \varphi(\xi) \leq y). \tag{1}
$$

For each fixed $k$, the restriction of $\varphi$ to $I_k$ is strictly monotone. Applying the monotone density transformation formula (22) to each branch:

- If $\varphi$ is strictly increasing on $I_k$, then for $y \in D_k$,
  $$
  P(\xi \in I_k,\; \varphi(\xi) \leq y) = P(\xi \in I_k,\; \xi \leq h_k(y)) = \int_{a_k}^{h_k(y)} f_\xi(x)\,dx.
  $$
  Differentiating with respect to $y$ gives $f_\xi(h_k(y))\,h'_k(y)$.

- If $\varphi$ is strictly decreasing on $I_k$, then for $y \in D_k$,
  $$
  P(\xi \in I_k,\; \varphi(\xi) \leq y) = P(\xi \in I_k,\; \xi \geq h_k(y)) = \int_{h_k(y)}^{b_k} f_\xi(x)\,dx.
  $$
  Differentiating gives $-f_\xi(h_k(y))\,h'_k(y) = f_\xi(h_k(y))\,|h'_k(y)|$, since $h'_k(y) < 0$.

In both cases, the contribution of branch $k$ to the density is $f_\xi(h_k(y))\,|h'_k(y)|$, valid for $y \in D_k$, and zero otherwise.

Summing over all $k$ yields the generalized density transformation formula:

$$
\boxed{f_{\eta}(y) = \sum_{k=1}^{n} f_{\xi}(h_k(y))\,|h'_k(y)| \cdot I_{D_k}(y)}, \tag{24}
$$

where $I_{D_k}(y)$ is the indicator function of the domain $D_k = \varphi(I_k)$.

**Example.** For $\eta = \xi^2$, take $I_1 = (-\infty, 0)$ (decreasing branch) and $I_2 = (0, \infty)$ (increasing branch). Then $h_1(y) = -\sqrt{y}$, $h_2(y) = \sqrt{y}$, $|h'_1(y)| = |h'_2(y)| = 1/(2\sqrt{y})$, and $D_1 = D_2 = (0, \infty)$. Hence

$$
f_\eta(y) = \frac{1}{2\sqrt{y}}\bigl[f_\xi(-\sqrt{y}) + f_\xi(\sqrt{y})\bigr], \quad y > 0,
$$

and $f_\eta(y) = 0$ for $y \leq 0$.
