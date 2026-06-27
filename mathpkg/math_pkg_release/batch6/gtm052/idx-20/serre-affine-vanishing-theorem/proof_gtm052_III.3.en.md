---
role: proof
locale: en
of_concept: serre-affine-vanishing-theorem
source_book: gtm052
source_chapter: "III"
source_section: "§3 Cohomology of a Noetherian Affine Scheme"
---

Given $\mathcal{F}$, let $M = \Gamma(X, \mathcal{F})$, and take an injective resolution $0 \to M \to I^\bullet$ in the category of $A$-modules. Applying the associated sheaf functor $\tilde{\cdot}$ yields a resolution

$$0 \to \tilde{M} \to \tilde{I}^0 \to \tilde{I}^1 \to \cdots.$$

Since $\mathcal{F}$ is quasi-coherent, $\mathcal{F} \cong \tilde{M}$. The key step is to show that each $\tilde{I}^i$ is flasque. This is proved by induction on the dimension of the support of the sheaf.

Let $I$ be an injective $A$-module. To show $\tilde{I}$ is flasque, take an open subset $U \subseteq X$ and a section $s \in \Gamma(U, \tilde{I})$. Let $Y = X \setminus U$ and let $Z$ be the complement of a distinguished open $X_f$ contained in $U$. Then $\Gamma(X_f, \tilde{I}) = I_f$, and by Lemma 3.3 the map $I \to I_f$ is surjective, so there exists $t \in I = \Gamma(X, \tilde{I})$ restricting to the image of $s$ in $\Gamma(X_f, \tilde{I})$. The difference $s - t|_U$ has support in $Z$, and by an induction on the dimension of the support (using Lemma 3.2 and the fact that sections with support form an injective module), one shows that the restriction map $\Gamma_Z(X, \tilde{I}) \to \Gamma_Z(U, \tilde{I})$ is surjective. Hence $\tilde{I}$ is flasque.

Therefore $\tilde{I}^\bullet$ is a flasque resolution of $\mathcal{F}$. Taking global sections, we recover the original injective resolution $0 \to M \to I^\bullet$, so the complex $\Gamma(X, \tilde{I}^\bullet)$ is exact in positive degrees. Since flasque sheaves are acyclic by Proposition 2.5, the cohomology of $\mathcal{F}$ is computed by this complex, giving $H^i(X, \mathcal{F}) = 0$ for all $i > 0$.
