---
role: proof
locale: en
of_concept: lemma-2-3-ez-approximation
source_book: gtm012
source_chapter: "7"
source_section: "§2. The space $\mathcal{L}$"
---

# Proof of Approximation of Exponentials by $\mathcal{L}$ Functions

**Lemma 2.3.** Suppose $\operatorname{Re} z > a$. There is a sequence $(u_n)_{1}^{\infty}$ in $\mathcal{L}$ such that for each integer $k \geq 0$ and each $M \in \mathbb{R}$,

$$|u_n - e_z|_{k,a,M} \to 0 \quad \text{as} \quad n \to \infty,$$

where $e_z(t) = e^{-zt}$, $t \in \mathbb{R}$.

**Proof.** Choose a smooth function $\varphi: \mathbb{R} \to \mathbb{R}$ such that

$$\varphi(t) = 1 \quad \text{for} \quad t \leq 1,$$
$$\varphi(t) = 0 \quad \text{for} \quad t \geq 2,$$
$$0 \leq \varphi(t) \leq 1 \quad \text{for all } t.$$

Let $\varphi_n(t) = \varphi(t/n)$. Then $\varphi_n$ is smooth, $\varphi_n(t) = 1$ for $t \leq n$, $\varphi_n(t) = 0$ for $t \geq 2n$, and $0 \leq \varphi_n(t) \leq 1$ for all $t, n$.

Define $u_n(t) = \varphi_n(t) e_z(t)$. Since $\varphi_n$ has bounded support on the right, $u_n \in \mathcal{L}$.

Now both $1 - \varphi_n(t)$ and $D\varphi_n(t)$ are bounded independent of $t$ and $n$, and vanish except on the interval $[n, 2n]$. Therefore

$$|e^{at}(Du_n(t) - De_z(t))| \leq c \exp(na - n \operatorname{Re} z),$$

with $c$ independent of $n$ and $t$. Since $\operatorname{Re} z > a$, the right-hand side tends to zero as $n \to \infty$. Thus

$$|u_n - e_z|_{1,a,M} \to 0 \quad \text{as} \quad n \to \infty,$$

for all $M$. The argument for other values of $k$ is similar: each derivative $D^k(u_n - e_z)$ is a linear combination of terms $D^j \varphi_n \cdot D^{k-j} e_z$ with $j \geq 1$ (when $j = 0$, the term is $(\varphi_n - 1)D^k e_z$). All such terms are supported in $[n, 2n]$ and are bounded by $c \exp((a - \operatorname{Re} z)n)$, which tends to zero since $\operatorname{Re} z > a$. $\square$

**Explanation.** The functions $e_z(t) = e^{-zt}$ are not themselves in $\mathcal{L}$ because for $\operatorname{Re} z > 0$, they decay to the left but blow up to the right; for $\operatorname{Re} z < 0$, they decay to the right but blow up to the left; and for $\operatorname{Re} z = 0$, they oscillate without decay. However, they can be approximated in the seminorm topology by multiplying by a smooth cutoff $\varphi_n$ that truncates the function to the right. The approximation works precisely when $\operatorname{Re} z > a$, ensuring that the error on the cutoff interval $[n, 2n]$ is exponentially small as $n \to \infty$.
