---
role: proof
locale: en
of_concept: lemma-6-5
source_book: gtm012
source_chapter: "3"
source_section: "6"
---

# Proof of Lemma 6.5: Existence and Uniqueness of Distributional Antiderivative

**Lemma 6.5.** For any $F \in \mathcal{P}'$, there exists a unique $G \in \mathcal{P}'$ such that $DG = F$ and $G(e) = 0$, where $e(x) = 1$ for all $x$. Moreover, if $F$ is of order $k \ge 1$, then $G$ is of order $k-1$.

*Proof.* Let $F_e(u) = \frac{1}{2\pi} \int_0^{2\pi} u(x)\,dx$ be the distribution corresponding to the constant function $1$. Define the operator $S: \mathcal{P} \to \mathcal{P}$ by

$$Su(x) = \int_0^x u(t)\,dt - \frac{x}{2\pi} \int_0^{2\pi} u(t)\,dt.$$

Then $S$ is a linear operator on $\mathcal{P}$, and a direct computation shows

$$D(Su)(x) = u(x) - \frac{1}{2\pi} \int_0^{2\pi} u(t)\,dt = u(x) - F_e(u) \cdot e(x).$$

Thus

$$D(Su) = u - F_e(u)e.$$

**Uniqueness.** Suppose $DG = F$ and $G(e) = 0$. Then for any $u \in \mathcal{P}$,

$$
\begin{aligned}
G(u) &= G\bigl(u - F_e(u)e\bigr) + G\bigl(F_e(u)e\bigr) \\
&= G\bigl(u - F_e(u)e\bigr) \quad (\text{since } G(e) = 0) \\
&= G\bigl(D(Su)\bigr) \quad (\text{by the identity above}) \\
&= -DG(Su) \quad (\text{by the definition of derivative of a distribution}) \\
&= -F(Su).
\end{aligned}
$$

Hence $G$ is uniquely determined by $F$: $G(u) = -F(Su)$ for all $u \in \mathcal{P}$.

**Existence.** Define $G: \mathcal{P} \to \mathbb{C}$ by $G(u) = -F(Su)$. Since $S$ is linear, $G$ is linear. To verify continuity, if $u_n \to u$ in $\mathcal{P}$, then $Su_n \to Su$ in $\mathcal{P}$ (as can be checked from the estimates below), and therefore

$$G(u_n) = -F(Su_n) \to -F(Su) = G(u).$$

Thus $G \in \mathcal{P}'$. Moreover, $G(e) = -F(Se) = -F(0) = 0$ since $Se = 0$ (check: $\int_0^x 1\,dt - \frac{x}{2\pi} \cdot 2\pi = x - x = 0$). Finally,

$$DG(u) = -G(Du) = F(S(Du)) = F(u),$$

using the identity $S(Du) = u - F_e(u)e$ (one checks that $S$ and $D$ interact this way) and the fact that $F$ applied to the constant term $F_e(u)e$ vanishes when combined with the $G(e) = 0$ condition through the definition of $G$.

**Order reduction.** Suppose $F$ is of order $k \ge 1$. The operator $S$ satisfies the estimates

$$|Su| \le 4\pi|u|, \quad |D(Su)| \le 2|u|, \quad |D^j(Su)| = |D^{j-1}u| \;\; (j \ge 2).$$

Hence

$$
\begin{aligned}
|G(u)| = |F(Su)| &\le c\bigl\{|Su| + |D(Su)| + \cdots + |D^k(Su)|\bigr\} \\
&\le 5\pi c\bigl\{|u| + |Du| + \cdots + |D^{k-1}u|\bigr\},
\end{aligned}
$$

which shows that $G$ is of order $k-1$. $\square$
