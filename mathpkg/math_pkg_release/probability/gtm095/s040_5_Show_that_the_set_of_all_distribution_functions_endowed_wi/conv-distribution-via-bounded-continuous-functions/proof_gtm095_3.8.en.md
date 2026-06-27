---
role: proof
locale: en
of_concept: conv-distribution-via-bounded-continuous-functions
source_book: gtm095
source_chapter: "3"
source_section: "8"
---

# Proof of Characterization of Convergence in Distribution via Bounded Continuous Functions

**Statement.** Let $X_n, X$ be random elements taking values in a metric space $(E, \mathcal{E}, \rho)$, with distributions $P_n$ and $P$ respectively. Then

$$X_n \xrightarrow{\mathcal{D}} X \quad\Longleftrightarrow\quad \mathbb{E}f(X_n) \to \mathbb{E}f(X)$$

for every bounded continuous function $f: E \to \mathbb{R}$.

**Proof.** By Definition 1, $X_n \xrightarrow{\mathcal{D}} X$ means precisely that $P_n \xrightarrow{w} P$, i.e., the sequence of probability measures $P_n$ converges weakly to $P$.

By the definition of weak convergence of probability measures (see the Portmanteau theorem, or equivalently the definition in terms of integrals of bounded continuous functions), we have

$$P_n \xrightarrow{w} P \quad\Longleftrightarrow\quad \int_E f(x) \, dP_n(x) \to \int_E f(x) \, dP(x)$$

for every bounded continuous function $f: E \to \mathbb{R}$.

Now apply the theorem on change of variables under the Lebesgue integral sign (Theorem 7, Sect. 6, Chap. 2). For the random element $X$ with distribution $P = P_X$, we have

$$\int_E f(x) \, dP(x) = \int_\Omega f(X(\omega)) \, d\mathbb{P}(\omega) = \mathbb{E}f(X).$$

Similarly, for each $X_n$ with distribution $P_n$, we have

$$\int_E f(x) \, dP_n(x) = \mathbb{E}f(X_n).$$

Combining these equalities with the characterization of weak convergence yields

$$X_n \xrightarrow{\mathcal{D}} X \;\Longleftrightarrow\; P_n \xrightarrow{w} P \;\Longleftrightarrow\; \int_E f \, dP_n \to \int_E f \, dP \;\Longleftrightarrow\; \mathbb{E}f(X_n) \to \mathbb{E}f(X)$$

for every bounded continuous $f$. $\square$

**Remark.** From this characterization, together with Lebesgue's dominated convergence theorem, it follows that almost sure convergence $X_n \xrightarrow{\text{a.s.}} X$ implies convergence in distribution $X_n \xrightarrow{\mathcal{D}} X$ (since for any bounded continuous $f$, the sequence $f(X_n)$ converges almost surely to $f(X)$ and is bounded, hence $\mathbb{E}f(X_n) \to \mathbb{E}f(X)$ by dominated convergence).
