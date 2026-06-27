---
role: proof
locale: en
of_concept: lemma-embedding-short-e-exact
source_book: gtm004
source_chapter: "IX"
source_section: "2. $\mathcal{E}$-Derived Functors"
---

# Proof of Embedding of a Short $\mathcal{E}$-Exact Sequence

**Lemma 2.2.** The short $\mathcal{E}$-exact sequence $0 \to A' \xrightarrow{\alpha'} A \xrightarrow{\alpha''} A'' \to 0$ may be embedded in a diagram

$$
\begin{array}{cccccc}
K' & \xrightarrow{\kappa'} & K & \xrightarrow{\kappa''} & K'' \\
\downarrow & & \downarrow & & \downarrow \\
P' & \xrightarrow{\lambda'} & P & \xrightarrow{\lambda''} & P'' \\
\downarrow_{\varepsilon'} & & \downarrow_{\varepsilon} & & \downarrow_{\varepsilon''} \\
A' & \xrightarrow{\alpha'} & A & \xrightarrow{\alpha''} & A''
\end{array}
$$

with all rows and columns $\mathcal{E}$-exact and $P', P, P''$ $\mathcal{E}$-projective.

**Proof.** The construction of the diagram is exactly as in the absolute case (Chapter IV). We proceed as follows:

1. Take $\mathcal{E}$-projective presentations of $A'$ and $A''$:

$$0 \to K' \to P' \xrightarrow{\varepsilon'} A' \to 0, \qquad 0 \to K'' \to P'' \xrightarrow{\varepsilon''} A'' \to 0.$$

2. Set $P = P' \oplus P''$, with $\lambda' : P' \to P$ the canonical injection and $\lambda'' : P \to P''$ the canonical projection.

3. Define $\varepsilon : P \to A$ as $\varepsilon = \langle \alpha' \varepsilon' \pi', \theta \rangle$, where $\pi' : P \to P'$ is the projection, and $\theta : P'' \to A$ is a lift of $\varepsilon''$ through $\alpha''$, i.e., $\alpha'' \circ \theta = \varepsilon''$. Such a lift exists because $P''$ is $\mathcal{E}$-projective and $\alpha'' \in \mathcal{E}$.

4. Let $\mu : K \to P$ be the kernel of $\varepsilon$, so $K = \ker \varepsilon$.

The extra points requiring verification are (i) $\varepsilon \in \mathcal{E}$, (ii) $\kappa'' \in \mathcal{E}$; it is trivial (by Proposition 1.2) that $\lambda'' \in \mathcal{E}$ since $\lambda''$ is the projection of a direct sum.

**Verification of (i):** We must show that $\varepsilon \in \mathcal{E}$. Since $\mathcal{E}$ is closed, it suffices to prove that every $\mathcal{E}$-projective object $Q$ is projective rel $\varepsilon$. Given $\varphi : Q \to A$, we seek $\psi : Q \to P$ such that $\varepsilon \circ \psi = \varphi$. Decompose $\psi = (\psi', \psi'')$ with $\psi' : Q \to P'$, $\psi'' : Q \to P''$. The equation $\varepsilon \circ \psi = \varphi$ becomes $\alpha' \varepsilon' \psi' + \theta \psi'' = \varphi$. Since $P''$ is $\mathcal{E}$-projective and $\alpha'' \in \mathcal{E}$, we may lift $\alpha'' \varphi : Q \to A''$ to obtain $\psi'' : Q \to P''$ with $\varepsilon'' \psi'' = \alpha'' \varphi$. Then $\alpha''(\varphi - \theta \psi'') = \alpha'' \varphi - \varepsilon'' \psi'' = 0$, so $\varphi - \theta \psi''$ factors through $\ker \alpha'' = \operatorname{im} \alpha'$. Since $\varepsilon'$ is in $\mathcal{E}$ and $P'$ is $\mathcal{E}$-projective, we obtain $\psi' : Q \to P'$ with $\varepsilon' \psi'$ mapping to the appropriate element. This yields the required lift.

**Verification of (ii):** By a similar argument using the fact that $\mathcal{E}$ is closed and the construction of $K$ as the kernel, one shows that $\kappa'' : K \to K''$ is in $\mathcal{E}$.

The exactness of all rows and columns then follows from the construction and the properties of kernels and cokernels in an abelian category, exactly as in the absolute case.
