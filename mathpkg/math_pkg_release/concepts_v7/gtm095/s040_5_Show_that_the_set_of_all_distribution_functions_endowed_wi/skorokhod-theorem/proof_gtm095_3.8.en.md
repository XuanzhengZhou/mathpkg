---
role: proof
locale: en
of_concept: skorokhod-theorem
source_book: gtm095
source_chapter: "3"
source_section: "8"
---

# Proof of the Skorokhod Representation Theorem (Case $E = \mathbb{R}$)

**Theorem (Skorokhod).** Let $X_n, X$ be random elements taking values in a metric space $(E, \mathcal{E}, \rho)$ and suppose $X_n \xrightarrow{\mathcal{D}} X$. Then there exist random elements $X_n^*$ and $X^*$ defined on a common probability space $(\Omega^*, \mathcal{F}^*, \mathbb{P}^*)$ such that

$$X_n^* \xrightarrow{\text{a.s.}} X^*$$

and

$$P^* = P, \quad P_n^* = P_n, \quad n \geq 1,$$

where $P^*$ and $P_n^*$ are the probability distributions of $X^*$ and $X_n^*$, respectively.

**Proof.** We note that it suffices to prove only the second conclusion (the existence of $X^*$, $X_n^*$ with the same laws and a.s. convergence), since the first follows from it by taking $P$ and $P_n$ to be the distributions of $X$ and $X_n$ themselves. Conversely, the second follows from the first. The proof in full generality is technically rather complicated; here we give a proof only for the case $E = \mathbb{R}$, which is transparent and provides a simple, clear construction.

---

**Proof for $E = \mathbb{R}$.** Let $F = F(x)$ and $F_n = F_n(x)$ be the distribution functions corresponding to the probability measures $P$ and $P_n$ on $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$.

**Step 1: Quantile functions.** We associate with $F$ its **quantile function** $Q = Q(u)$, defined for $0 < u < 1$ by

$$Q(u) = \inf \{ x \in \mathbb{R} : F(x) \geq u \}, \quad 0 < u < 1.$$

It is easily verified that the following equivalence holds (this is a fundamental property connecting distribution functions and quantile functions):

$$F(x) \geq u \quad\Longleftrightarrow\quad Q(u) \leq x.$$

Indeed, if $F(x) \geq u$, then $x$ belongs to the set $\{y : F(y) \geq u\}$, and so $\inf\{y : F(y) \geq u\} \leq x$, i.e., $Q(u) \leq x$. Conversely, if $Q(u) \leq x$, then by the right-continuity of $F$, we have $F(x) \geq F(Q(u)) \geq u$.

**Step 2: Construction of the common probability space.** Take

$$\Omega^* = (0,1), \quad \mathcal{F}^* = \mathcal{B}(0,1), \quad \mathbb{P}^*(d\omega^*) = d\omega^* \text{ (Lebesgue measure)}.$$

Define the random variables on this space by

$$X^*(\omega^*) = Q(\omega^*), \quad X_n^*(\omega^*) = Q_n(\omega^*), \qquad \omega^* \in (0,1),$$

where $Q_n$ is the quantile function associated with $F_n$.

**Step 3: Verification of equal laws.** For any $x \in \mathbb{R}$, we have

$$
\begin{aligned}
\mathbb{P}^*\{\omega^* : X^*(\omega^*) \leq x\}
&= \mathbb{P}^*\{\omega^* : Q(\omega^*) \leq x\} \\
&= \lambda\{\omega^* \in (0,1) : Q(\omega^*) \leq x\} \\
&= \lambda\{\omega^* \in (0,1) : \omega^* \leq F(x)\} \quad \text{(by the equivalence } F(x) \geq u \Leftrightarrow Q(u) \leq x\text{)} \\
&= \lambda((0, F(x)]) = F(x) = P((-\infty, x]),
\end{aligned}
$$

where $\lambda$ denotes Lebesgue measure. Thus $\operatorname{Law}(X^*) = P$. The same argument shows $\operatorname{Law}(X_n^*) = P_n$ for each $n$, so the distributions are preserved.

**Step 4: Almost sure convergence.** The hypothesis $X_n \xrightarrow{\mathcal{D}} X$ means $P_n \xrightarrow{w} P$, which is equivalent to pointwise convergence of distribution functions at every continuity point $x$ of $F$:

$$F_n(x) \to F(x) \quad \text{for every continuity point } x \text{ of } F.$$

It is a standard fact that $F_n(x) \to F(x)$ at continuity points of $F$ implies the convergence of the corresponding quantile functions:

$$Q_n(u) \to Q(u) \quad \text{for every continuity point } u \text{ of } Q \text{ in } (0,1).$$

Since $Q$ is monotone (non-decreasing), it can have at most countably many discontinuity points. Therefore the set of points where $Q_n(u)$ may fail to converge to $Q(u)$ has Lebesgue measure zero. Consequently,

$$Q_n(\omega^*) \to Q(\omega^*) \quad \text{for } \mathbb{P}^*\text{-almost every } \omega^* \in (0,1).$$

That is, $X_n^*(\omega^*) \to X^*(\omega^*)$ for $\mathbb{P}^*$-almost every $\omega^*$, which means

$$X_n^* \xrightarrow{\text{a.s.}} X^*.$$

This completes the proof for the case $E = \mathbb{R}$. $\square$

**Remark.** The construction above does not directly generalize to $E = \mathbb{R}^2$ or more general spaces, where a different approach is needed. The general case of the Skorokhod representation theorem (for arbitrary complete separable metric spaces) is considerably more involved.
