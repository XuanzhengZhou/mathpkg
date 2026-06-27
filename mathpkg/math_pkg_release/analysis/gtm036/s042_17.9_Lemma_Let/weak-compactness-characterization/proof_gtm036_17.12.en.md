---
role: proof
locale: en
of_concept: weak-compactness-characterization
source_book: gtm036
source_chapter: "17"
source_section: "17.12"
---
**Proof that (i) implies (ii).** Let $x_0$ be a cluster point in $E$ of $\{x_m\}$ and let $f_0$ be a weak* cluster point in $E^*$ of $\{f_n\}$. The latter exists because $\{f_n\}$, being equicontinuous, is contained in a weak* compact set (by 17.4). If $\lim_{m \to \infty} f_n(x_m)$ exists, then

$$\lim_{m \to \infty} f_n(x_m) = \lim_{m \to \infty} f_0(x_m) = f_0(x_0).$$

Similarly, if $\lim_{n \to \infty} f_n(x_m)$ exists, it is equal to $f_0(x_0)$. Hence the two iterated limits coincide.

**Proof that (ii) implies (iii).** First observe that it suffices to prove the weak closure $A^-$ of $A$ in the completion $\hat{E}$ is weakly compact. The closure $C^-$ (in $E$) is closed in $\hat{E}$ and hence weakly closed in $\hat{E}$; therefore the weak closures of $A$ in $E$ and $\hat{E}$ are identical. Consequently, without loss of generality suppose $E$ is complete. Let $F = E^*$ and embed $E$ in $F'$ (the algebraic dual of $F$). Condition (ii) implies the iterated limit condition for each $x$ in $A^-$. As before embed $E$ in $F'$, and regard $\{f_n - f_0\}$ as a sequence of $w(F', E^*)$-continuous linear functionals on $F'$ which are uniformly bounded on $A^-$. Since $\{f_n - f_0\}$ converges pointwise to zero on $A^-$, Theorem 17.11 implies that $\lim \langle f_n, \phi \rangle = \langle f_0, \phi \rangle$ for each member $\phi$ of the $w(F', E^*)$-closure $C^-$ of $C$ in $F'$. Since $C^-$ is $w(F', E^*)$-compact, there is a cluster point $\phi_0$ of $\{x_m\}$ in $C^-$. Hence, if the iterated limit $\lim_{n \to \infty} \lim_{m \to \infty} f_n(x_m)$ exists, it equals $\lim_n \langle f_n, \phi_0 \rangle = \langle f_0, \phi_0 \rangle$. On the other hand, $\lim_{m \to \infty} \lim_{n \to \infty} f_n(x_m) = \lim_{m \to \infty} f_0(x_m) = \langle f_0, \phi_0 \rangle$, provided the left-hand iterated limit exists. It follows that the convex extension $C$ of $A$ satisfies the iterated limit condition.

The equivalence of (iii) and (iv) follows from the fact that the weak closure of $C$ contains $A$, and the compactness of the weak closure of $C$ implies the weak compactness of the weak closure of $A$ (as a closed subset of a compact set).
