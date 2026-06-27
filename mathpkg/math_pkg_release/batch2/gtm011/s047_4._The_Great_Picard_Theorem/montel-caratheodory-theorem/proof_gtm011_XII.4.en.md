---
role: proof
locale: en
of_concept: montel-caratheodory-theorem
source_book: gtm011
source_chapter: "XII"
source_section: "§4. The Great Picard Theorem"
---

Fix a point $z_0$ in $G$ and define the families $\mathcal{G}$ and $\mathcal{H}$ by

$$\mathcal{G} = \{ f \in F : |f(z_0)| \leq 1 \},$$
$$\mathcal{H} = \{ f \in F : |f(z_0)| \geq 1 \};$$

so $F = \mathcal{G} \cup \mathcal{H}$. It will be shown that $\mathcal{G}$ is normal in $H(G)$ and that $\mathcal{H}$ is normal in $C(G, \mathbb{C}_\infty)$ (that $\infty$ is a limit of a sequence in $\mathcal{H}$ is easily seen by considering constant functions). To show that $\mathcal{G}$ is normal in $H(G)$, Montel's Theorem is invoked; that is, it is sufficient to show that $\mathcal{G}$ is locally bounded.

If $a$ is any point in $G$, let $\gamma$ be a curve in $G$ from $z_0$ to $a$. Let $D_0, D_1, \ldots, D_n$ be disks in $G$ with centers $z_0, z_1, \ldots, z_n = a$ on $\{\gamma\}$ and such that $z_{k-1}$ and $z_k$ are in $D_{k-1} \cap D_k$ for $1 \leq k \leq n$. Also assume that $D_k^- \subset G$ for $0 \leq k \leq n$. Apply Schottky's Theorem to $D_0$. It follows that there is a constant $C_0$ such that $|f(z)| \leq C_0$ for $z$ in $D_0$ and $f$ in $\mathcal{G}$. (If $D_0 = B(z_0; r)$ and $R > r$ is such that $\bar{B}(z_0; R) \subset G$, then Schottky's Theorem gives a bound on the smaller disk.)

By induction, applying Schottky's Theorem successively to each disk $D_k$, we obtain constants $C_k$ such that $|f(z)| \leq C_k$ for all $z \in D_k$ and all $f \in \mathcal{G}$. In particular, on a neighborhood of $a$, $\mathcal{G}$ is uniformly bounded by $C_n$. Since $a$ was arbitrary, $\mathcal{G}$ is locally bounded, hence normal in $H(G)$ by Montel's Theorem.

For $\mathcal{H}$, consider the family $\tilde{\mathcal{H}} = \{ 1/f : f \in \mathcal{H} \}$. Each $1/f$ is analytic on $G$, omits $0$ and $1$, and satisfies $|(1/f)(z_0)| \leq 1$. Thus $\tilde{\mathcal{H}} \subset \mathcal{G}$, so $\tilde{\mathcal{H}}$ is normal in $H(G)$. It follows that $\mathcal{H}$ is normal in $C(G, \mathbb{C}_\infty)$, where convergence to $\infty$ corresponds to convergence of the reciprocals to $0$.

Therefore $F = \mathcal{G} \cup \mathcal{H}$ is normal in $C(G, \mathbb{C}_\infty)$.
