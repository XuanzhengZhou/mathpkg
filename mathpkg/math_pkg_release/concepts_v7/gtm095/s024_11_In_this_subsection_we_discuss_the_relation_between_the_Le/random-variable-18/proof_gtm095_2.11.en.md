---
role: proof
locale: en
of_concept: random-variable-18
source_book: gtm095
source_chapter: "2"
source_section: "11"
---

# Proof of Theorem 12 (Stochastic Exponent as Unique Locally Bounded Solution)

Consider the linear integral equation (the Doleans-Dade equation)

$$Z_t = 1 + \int_0^t Z_{s-}\, dA(s), \tag{74}$$

where $A(t)$, $t \geq 0$, is a function of locally bounded variation with $A(0) = 0$, or equivalently its differential form

$$dZ_t = Z_{t-}\, dA(t), \quad Z_0 = 1. \tag{75}$$

The integration by parts formula (Theorem 11) lets us solve (74) explicitly in the class of functions of locally bounded variation.

**Step 1: Construction of a solution.** We introduce the **stochastic exponent** (see Shiryaev [43])

$$\mathcal{E}_t(A) = e^{A(t)-A(0)} \prod_{0 \leq s \leq t} (1 + \Delta A(s))\, e^{-\Delta A(s)}, \tag{76}$$

where $\Delta A(s) = A(s) - A(s-)$ for $s > 0$, and $\Delta A(0) = 0$.

The function $A(s)$, $0 \leq s \leq t$, has bounded variation and therefore has at most countably many discontinuities, and the series $\sum_{0 \leq s \leq t} |\Delta A(s)|$ converges. It follows that

$$\prod_{0 \leq s \leq t} (1 + \Delta A(s))\, e^{-\Delta A(s)}, \quad t \geq 0,$$

is a function of locally bounded variation.

If $A^c(t) = A(t) - \sum_{0 \leq s \leq t} \Delta A(s)$ is the continuous component of $A(t)$, we can rewrite (76) in the form

$$\mathcal{E}_t(A) = e^{A^c(t)-A^c(0)} \prod_{0 < s \leq t} (1 + \Delta A(s)). \tag{77}$$

Now let us write

$$F(t) = e^{A^c(t)-A^c(0)}, \quad G(t) = \prod_{0 < s \leq t} (1 + \Delta A(s)), \quad G(0) = 1.$$

Then $\mathcal{E}_t(A) = F(t)G(t)$. Applying the integration by parts formula (62) from Theorem 11:

$$\mathcal{E}_t(A) = F(t)G(t) = F(0)G(0) + \int_0^t F(s)\, dG(s) + \int_0^t G(s-)\, dF(s)$$

$$= 1 + \sum_{0 < s \leq t} F(s)G(s-)\Delta A(s) + \int_0^t G(s-)F(s)\, dA^c(s),$$

where we used that $dG(s) = G(s-)\Delta A(s)$ (since $G$ is a pure jump function) and $dF(s) = F(s)\, dA^c(s)$ (since $F$ is the exponential of the continuous part). Simplifying,

$$\mathcal{E}_t(A) = 1 + \int_0^t \mathcal{E}_{s-}(A)\, dA(s),$$

which shows that $\mathcal{E}_t(A)$ satisfies the integral equation (74). Hence $\mathcal{E}_t(A)$ is a locally bounded solution.

**Step 2: Uniqueness.** Suppose $Y(t)$ is another locally bounded solution of (74) and let $Z(t) = \mathcal{E}_t(A) - Y(t)$. Then $Z(t)$ also satisfies the homogeneous equation

$$dZ_t = Z_{t-}\, dA(t), \quad Z_0 = 0,$$

or equivalently

$$Z(t) = \int_0^t Z(s-)\, dA(s).$$

Now put

$$T = \inf\{t \geq 0 : Z(t) \neq 0\},$$

where we take $T = \infty$ if $Z(t) = 0$ for all $t \geq 0$. We must show that $T = \infty$.

Since $A(t)$, $t \geq 0$, is a function of locally bounded variation, there exist two generalized distribution functions $A_1(t)$ and $A_2(t)$ such that $A(t) = A_1(t) - A_2(t)$. If we suppose that $T < \infty$, we can find a finite $T' > T$ such that

$$[A_1(T') + A_2(T')] - [A_1(T) + A_2(T)] \leq \frac{1}{2}.$$

Then, from the equation satisfied by $Z$ for $t \geq T$:

$$Z(t) = \int_T^t Z(s-)\, dA(s), \quad t \geq T,$$

we obtain the estimate

$$\sup_{t \leq T'} |Z(t)| \leq \frac{1}{2} \sup_{t \leq T'} |Z(t)|.$$

Since $Z$ is locally bounded, $\sup_{t \leq T'} |Z(t)| < \infty$. Thus the inequality forces $\sup_{t \leq T'} |Z(t)| = 0$, which means $Z(t) = 0$ for all $t \in [T, T']$, contradicting the definition of $T$ (that $Z \neq 0$ on a set arbitrarily close to $T$ from the right).

Therefore $T = \infty$, i.e., $Z(t) \equiv 0$ for all $t \geq 0$, which proves that $Y(t) \equiv \mathcal{E}_t(A)$. The solution is unique. $\square$
