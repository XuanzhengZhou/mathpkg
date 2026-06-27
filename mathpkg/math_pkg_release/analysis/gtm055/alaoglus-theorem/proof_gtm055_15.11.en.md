---
role: proof
locale: en
of_concept: alaoglus-theorem
source_book: gtm055
source_chapter: "15"
source_section: "11"
---

For each $x \in \mathcal{E}$, set $D_x^- = \{\lambda \in \mathbb{C} : |\lambda| \leq \|x\|\}$, and form the topological product $\Pi = \prod_{x \in \mathcal{E}} D_x^-$. Each $D_x^-$ is a compact disc in $\mathbb{C}$, and by Tychonoff's theorem (Theorem 3.15), $\Pi$ is compact. Define $\Phi(f) = \{f(x)\}_{x \in \mathcal{E}}$ for $f \in (\mathcal{E}^*)_1$. Then $\Phi$ is a continuous one-to-one mapping of $(\mathcal{E}^*)_1$ into $\Pi$. To complete the proof we show the range $R = \Phi((\mathcal{E}^*)_1)$ is closed in $\Pi$ (so $R$ is compact; cf. Proposition 3.2) and $\Phi^{-1}: R \to (\mathcal{E}^*)_1$ is continuous when $\mathcal{E}^*$ has the weak* topology (so $\Phi$ is a homeomorphism). Let $\{f_\lambda\}$ be a net in $(\mathcal{E}^*)_1$ with $\{\Phi(f_\lambda)\}$ convergent in $\Pi$. This means all coordinate nets $\{\Phi(f_\lambda)_x\} = \{f_\lambda(x)\}$ converge. Define $f_0(x) = \lim_\lambda f_\lambda(x)$. By linearity of the limit, $f_0$ is linear, and $|f_0(x)| \leq \|x\|$ implies $\|f_0\| \leq 1$, so $f_0 \in (\mathcal{E}^*)_1$. Then $\Phi(f_\lambda) \to \Phi(f_0)$, showing $R$ is closed, and $f_\lambda \to f_0$ in the weak* topology, showing continuity of $\Phi^{-1}$.
