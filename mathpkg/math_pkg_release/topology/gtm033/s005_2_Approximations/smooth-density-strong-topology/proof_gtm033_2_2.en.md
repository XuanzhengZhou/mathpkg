---
role: proof
locale: en
of_concept: smooth-density-strong-topology
source_book: gtm033
source_chapter: "2"
source_section: "2"
---

# Proof of Theorem 2.4 — Smooth Density in Strong Topology

**Theorem 2.4.** Let $U \subset \mathbb{R}^m$ and $V \subset \mathbb{R}^n$ be open sets. Then $C^\infty(U,V)$ is dense in $C^r_S(U,V)$, $0 \leqslant r < \infty$.

*Proof.* Since $C^r_S(U,V)$ is open in $C^r_S(U,\mathbb{R}^n)$, it suffices to prove the theorem with $V = \mathbb{R}^n$.

Let $f \in C^r(U,\mathbb{R}^n)$. A neighborhood base at $f$ in $C^r_S(U,\mathbb{R}^n)$ consists of sets $\mathcal{N}(f,K,\varepsilon)$ of the following form (see Exercise 12, Section 2.1). Let $K = \{K_i\}_{i \in \Lambda}$ be a locally finite family of compact sets covering $U$; let $\varepsilon = \{\varepsilon_i\}_{i \in \Lambda}$ be a family of positive numbers, and let $\mathcal{N}(f,K,\varepsilon)$ be the set of $C^r$ maps $g: U \to \mathbb{R}^n$ such that for all $i \in \Lambda$

$$\|g - f\|_{r, K_i} < \varepsilon_i. \tag{4}$$

Fixing $f$, $K$ and $\varepsilon$, we must show

$$C^\infty(U,\mathbb{R}^n) \cap \mathcal{N}(f,K,\varepsilon) \neq \varnothing.$$

Let $\{\lambda_i\}_{i \in \Lambda}$ be a $C^\infty$ partition of unity on $U$ such that $\operatorname{Supp} \lambda_i$ is compact and contains $K_i$.

Given positive numbers $\{\alpha_i\}_{i \in \Lambda}$, there are $C^\infty$ maps $g_i: U_i \to \mathbb{R}^n$ such that for $x \in K_i$ and $k = 0, \ldots, r$,

$$\|D^k g_i(x) - D^k f(x)\| < \alpha_i.$$

Put

$$g: U \to \mathbb{R}^n,$$

$$g(x) = \sum_i \lambda_i(x) g_i(x).$$

Then $g$ is $C^\infty$. To estimate $\|D^k g(x) - D^k f(x)\|$ we observe that if $\lambda: U \to \mathbb{R}$ and $\varphi: U \to \mathbb{R}^n$ are $C^k$ and $\psi(x) = \lambda(x)\varphi(x)$, then $D^k \psi(x)$ is a bilinear function of $D^p \lambda(x)$, $D^q \varphi(x)$, $p, q = 0, \ldots, k$; this bilinear function is universal and independent of $x$, $\lambda$ and $\varphi$. Thus there is a universal constant $A_k > 0$ such that

$$\|D^k(\lambda \varphi)(x)\| \leqslant A_k \max_{0 \leqslant p \leqslant k} \|D^p \lambda(x)\| \cdot \max_{0 \leqslant q \leqslant k} \|D^q \varphi(x)\|.$$

Set

$$A = \max\{A_0, \ldots, A_r\}.$$

Fix $i \in \Lambda$ and set

$$\Lambda_i = \{j \in \Lambda : K_i \cap K_j \neq \varnothing\}.$$

This is a finite set; let its cardinality be $m_i$. Put

$$\mu_i = \max\left\{ \|\lambda_j\|_{r, K_i} : j \in \Lambda_i \right\},$$

$$\beta_i = \max\left\{ \alpha_j : j \in \Lambda_i \right\}.$$

In the following sums $j$ varies over $\Lambda_i$. For $x \in K_i$ and $0 \leqslant k \leqslant r$ we have

$$
\begin{aligned}
\|D^k g(x) - D^k f(x)\|
&= \left\| \sum_j D^k\left( \lambda_j g_j - \lambda_j f \right)(x) \right\| \\
&\leqslant \sum_j \left\| D^k\left( \lambda_j (g_j - f) \right)(x) \right\| \\
&\leqslant m_i A \mu_i \beta_i.
\end{aligned}
$$

It is clear that the numbers $\alpha_i$ can be chosen so that

$$m_i A \mu_i \beta_i < \varepsilon_i.$$

With this choice of $\alpha_i$ we have, for all $i \in \Lambda$,

$$\|g - f\|_{r, K_i} < \varepsilon_i.$$

QED
