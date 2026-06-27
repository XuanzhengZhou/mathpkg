---
role: proof
locale: en
of_concept: proposition-15-10
source_book: gtm055
source_chapter: "15"
source_section: "Section 16_Section_16"
---

PROOF. For each vector $x$ in $\mathcal{E}$ set $D_x^- = \{\lambda \in \mathbb{C} : |\lambda| \leq \|x\|\}$, and form the topological product

$$\Pi = \prod_{x \in \mathcal{E}} D_x^-.$$

Each $D_x^-$ is a compact disc in $\mathbb{C}$, and it follows by Tihonov's theorem (Theorem 3.15) that $\Pi$ is compact. Moreover, if we define

$$\Phi(f) = \{f(x)\}_{x \in \mathcal{E}}, \quad f \in (\mathcal{E}^*)_1,$$

then it is clear that $\Phi$ is a continuous one-to-one mapping of $(\mathcal{E}^*)_1$ into $\Pi$. The proof will be completed by showing that the range $R = \Phi((\mathcal{E}^*)_1)$ of $\Phi$ is closed in $\Pi$ (which will show that $R$ is compact; cf. Proposition 3.2) and that the mapping $\Phi^{-1}: R \to (\mathcal{E}^*)_1$ is continuous when $\mathcal{E}^*$ is given the weak* topology (which will show that $\Phi$ is a homeomorphism between $(\mathcal{E}^*)_1$ and $R$). To that end, let $\{f_\lambda\}_{\lambda \in \Lambda}$ be a net in $(\mathcal{E}^*)_1$ with the property that the net $\{\Phi(f_\lambda)\}_{\lambda \in \Lambda}$ is convergent in $\Pi$. We must show that there exists a linear functional $f_0$ in $(\mathcal{E}^*)_1$ such that $\Phi(f_\lambda) \to \Phi(f_0)$ (this will show that $R$ is closed in $\Pi$) and such that $f_\lambda \to f_0$ in the weak* topology (this will show that $\Phi^{-1}$ is continuous on $R$). But to say that the net $\{\Phi(f_\lambda)\}$ converges in $\Pi$ is the same as saying that all of the coordinate nets $\{\Phi(f

infinite sequence $\{x_{k_m(n)}\}$ of sequences, $m = 1, 2, \ldots$, each of which is a subsequence of the foregoing one, and with the property that $\{x_{k_m(n)}\}$ converges along the first $m + 1$ coordinates to the first $m + 1$ terms of a sequence $b = \{\beta_m\}_{m=0}^{\infty}$ belonging to $(\gamma)_1$. But then the diagonal sequence $\{x'_n = x_{k_m(n)}\}_{n=0}^{\infty}$ is eventually a subsequence of every one of the sequences $\{x_{k_m(n)}\}$ and therefore converges coordinatewise to $b$. Hence, by Problem C, $b$ belongs to $(\gamma)_1$ and $\{x'_n\}$ converges weakly to $b$. We have shown that every sequence in $(\gamma)_1$ possesses weakly convergent subsequences, and since $(\gamma)_1$ is weakly metrizable (Prob. M), this implies that $(\gamma)_1$ is weakly compact. Thus, by the device of extracting a whole sequence of successively finer subsequences, and then extracting the diagonal from the resulting infinite tableau—that is, by employing the diagonal process; cf. Problem 4P—we obtain an independent proof of the weak* compactness of the unit ball in the space $(\gamma), 1 < p < +\infty$. Historically it was this construction and others like it that led to the discovery of Alaoglu's theorem.

The topologies induced on a linear space by various families of linear functionals are of interest by virtue of being the coarsest topologies satisfying certain conditions. There are also many situations in which a linear topology is interesting because it is the finest topology satisfying certain specified conditions. To see how this goes we need the following result.
