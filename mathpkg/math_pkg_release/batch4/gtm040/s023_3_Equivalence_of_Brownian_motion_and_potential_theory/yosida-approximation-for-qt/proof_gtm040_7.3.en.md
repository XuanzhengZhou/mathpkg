---
role: proof
locale: en
of_concept: yosida-approximation-for-qt
source_book: gtm040
source_chapter: "7"
source_section: "3. Equivalence of Brownian motion and potential theory"
---

The proof consists in writing down the concrete formula for $Q^t$ in terms of $A$ and $t$ and verifying that it satisfies the required properties. Define the Yosida approximant

$$A_\lambda = \lambda^2 (\lambda I - A)^{-1} - \lambda I.$$

One shows that as $\lambda \to \infty$, the family $\{A_\lambda\}$ approximates $A$ in a suitable sense: for each $f$ in the domain of $A$, $A_\lambda f \to A f$ uniformly. The semigroup is then recovered via the exponential formula

$$Q^t = \lim_{\lambda \to \infty} e^{t A_\lambda} = \lim_{\lambda \to \infty} \sum_{k=0}^{\infty} \frac{t^k}{k!} A_\lambda^k,$$

which is precisely the stated formula. The existence and uniqueness of a semigroup $\{Q^t\}$ satisfying the four listed properties (semigroup property, strong continuity at $0$, uniform decay at $\infty$, and the definition of $A$) follow from the construction. Therefore, if $A$ can be defined within potential theory, so can each $Q^t$, and via the duality relation, so can each $P^t$.
