---
role: proof
locale: en
of_concept: homomorphism-representation-via-characteristic-function
source_book: gtm043
source_chapter: "10"
source_section: "10.8"
---

As with any homomorphism, the element $e = \mathfrak{s}\mathbf{1}$ is an idempotent in $C(X)$. Hence it is the characteristic function of the set $E = e^{\leftarrow}(1)$. Since $e$ is continuous, $E$ is open-and-closed in $X$. Furthermore (again as with any homomorphism), $e$ is the unity element of the image ring $\mathfrak{s}[C(Y)]$; it follows that $(\mathfrak{s}g)[X - E] = \{0\}$ for every $g \in C(Y)$.

Consider the homomorphism $t$ from $C(vY)$ into $C(E)$ (assuming $E \neq \emptyset$) defined by: $tg^v = (\mathfrak{s}g)|E$. Evidently, $t$ sends $\mathbf{1}$ to $e|E$, i.e., to the function $\mathbf{1}$ in $C(E)$. By Theorem 10.6, there exists a unique continuous mapping $\tau$ of $E$ into $vY$ such that $\tau' = t$. For $x \in E$, we have

$$(\mathfrak{s}g)(x) = (tg^v)(x) = g^v(\tau x);$$

and for $x \in X - E$, $(\mathfrak{s}g)(x) = 0$.

The proof for $C^*$ is similar.
