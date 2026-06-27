---
role: proof
locale: en
of_concept: independence-of-pi-star
source_book: gtm004
source_chapter: "III"
source_section: "2. The Functor Ext"
---

# Proof of Independence of the Induced Map on Ext from the Choice of Lifting

Let $\pi_i : P' \to P$, $i = 1, 2$, be two homomorphisms lifting $\alpha : A' \to A$ and inducing $\sigma_i : R' \to R$, so that the following diagram is commutative for $i = 1, 2$:

$$
\begin{CD}
R' @>{\mu'}>> P' @>{\varepsilon'}>> A' \\
@V{\sigma_i}VV @V{\pi_i}VV @VV{\alpha}V \\
R @>{\mu}>> P @>{\varepsilon}>> A
\end{CD}
$$

Consider $\pi_1 - \pi_2$. Since $\pi_1, \pi_2$ induce the same map $\alpha : A' \to A$, we have $\varepsilon(\pi_1 - \pi_2) = \varepsilon\pi_1 - \varepsilon\pi_2 = \alpha\varepsilon' - \alpha\varepsilon' = 0$. Hence $\pi_1 - \pi_2$ factors through a map $\tau : P' \to R$, such that $\pi_1 - \pi_2 = \mu\tau$.

It follows that $\sigma_1 - \sigma_2 = \tau\mu'$. Indeed, from the commutativity of the diagram we have $\mu\sigma_i = \pi_i\mu'$ for $i=1,2$, so

$$
\mu(\sigma_1 - \sigma_2) = (\pi_1 - \pi_2)\mu' = \mu\tau\mu',
$$

and since $\mu$ is monic (being the first map in a short exact sequence), we obtain $\sigma_1 - \sigma_2 = \tau\mu'$.

Now, if $\varphi : R \to B$ is a representative of the element $[\varphi] \in \operatorname{Ext}_A^\varepsilon(A, B)$, we have

$$
\pi_1^*[\varphi] = [\varphi\sigma_1] = [\varphi\sigma_2 + \varphi\tau\mu'] = [\varphi\sigma_2] = \pi_2^*[\varphi].
$$

The middle equality holds because $\varphi\tau\mu'$ factors through $\mu'$, and $\operatorname{im}\mu' \subseteq \ker\varepsilon'$. More precisely, any map of the form $\psi\mu'$ with $\psi : P' \to B$ represents the zero element in $\operatorname{Ext}_A^\varepsilon(A, B)$, since it lies in the image of $\mu'^* : \operatorname{Hom}_\Lambda(P', B) \to \operatorname{Hom}_\Lambda(R', B)$. Thus $[\varphi\tau\mu'] = 0$ in the cokernel, and $[\varphi\sigma_2 + \varphi\tau\mu'] = [\varphi\sigma_2]$.

Hence $\pi^*$ does not depend on the chosen $\pi : P' \to P$ but only on $\alpha : A' \to A$.
