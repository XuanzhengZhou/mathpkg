---
role: exercise
locale: en
chapter: "3"
section: "Exercises"
exercise_number: 8
source_book: gtm026
---

([Alagić '74]; cf. [Applegate '65], [Manes '67, 1.7], [Meyer '72])

establishes a bijective correspondence from liftings $\bar{X}$ as above to inverse-state transformations, with inverse passage

$$\lambda \rightarrow \bar{X}, (A \xrightarrow{\alpha} B) \bar{X} = AX \xrightarrow{\alpha X} BSX \xrightarrow{B \lambda} BXT$$

(b) Let $Z: \mathcal{K} \rightarrow \mathcal{K}$ be an input process, let $X$ have a right adjoint $X^\bullet$, and let $\lambda_\bullet: ZX \rightarrow XT$ be a natural transformation. Prove that there exists a unique inverse-state transformation $\lambda: Z^\circ X \rightarrow XT$ such that

[Hint:

$$ZX \xrightarrow{\lambda_\bullet} XT$$

$$Z \rightarrow XTX^\bullet$$

$$Z^\circ X \xrightarrow{\lambda} XT$$

where $Z^\circ \rightarrow XTX^\bullet$ is a theory map.]

(c) When $X = \text{id}_{\mathcal{K}}$, an inverse-state transformation is just a theory map $\lambda: \mathbf{S} \longrightarrow \mathbf{T}$. Study the structure of $\bar{X}$ for various examples of theory maps. Observe that $\bar{X}$ does not commute with the underlying $\mathcal{K}$-object functors in general.

(d) When $\mathbf{S} = \mathbf{T}$, an inverse-state transformation $\lambda$ is just a distributive law of $X$ over $T$. If, also, $X$ is an input process, prove that the corresponding lift $\bar{X}: \mathcal{K}_{\mathbf{T}} \longrightarrow \mathcal{K}_{\mathbf{T}}$ is an input process in $\mathcal{K}_{\mathbf{T}}$ with $A\bar{X}^{(a)} = AX^{(a)}$ on objects. Observe, further, that an $\bar{X}$-automaton is the same thing as a $\lambda$-automaton for which the output algebra $(Y, \theta)$ is a free $\mathbf{T}$-algebra, and that the responses coincide.

(e) The following example illustrates the computer science origins of inverse-state transformations. See the bibliography of [Alagić '74] for more about applications of inverse-state (and also direct-state) natural transformations in computer science. We thank Jim Thatcher for calling our attention to this example. In the context of (d), let $X = - \times X_0$ with $X_0 = \{D, I\}$ (for "derivative" and "identity"), let $Z = X_\Omega$ where $\Omega_1 = \{S\}$ (for "sine") and $\Omega_2 = \{+, m\}$ and let $\mathbf{T}$ be the theory whose algebras are rings equipped with two unary functions labelled "$C$" and "$S$" (e.g. the reals with "cosine" and "sine"). Define $\lambda_0: ZX \longrightarrow XT$ as follows:

$$
\begin{array}{l}
AZ \times X_0 \xrightarrow{A\lambda_0} (A \times X_0)T \\
(ab+, D)
\end{array}
$$
