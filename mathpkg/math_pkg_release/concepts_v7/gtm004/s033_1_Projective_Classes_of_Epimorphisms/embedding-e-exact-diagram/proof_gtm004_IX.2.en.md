---
role: proof
locale: en
of_concept: embedding-e-exact-diagram
source_book: gtm004
source_chapter: "IX. Relative Homological Algebra"
source_section: "2. E-Derived Functors"
---

# Proof of Embedding of Short E-Exact Sequence in E-Projective Diagram

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

**Proof.** Take $\mathcal{E}$-projective presentations

$$0 \to K' \to P' \xrightarrow{\varepsilon'} A' \to 0, \qquad 0 \to K'' \to P'' \xrightarrow{\varepsilon''} A'' \to 0.$$

Set $P = P' \oplus P''$ with $\lambda'$ the injection and $\lambda''$ the projection. Define $\varepsilon = \langle \alpha' \varepsilon', \theta \rangle : P \to A$, where $\theta : P'' \to A$ lifts $\varepsilon''$ through $\alpha''$ (possible since $P''$ is $\mathcal{E}$-projective and $\alpha'' \in \mathcal{E}$). Let $\mu$ be the kernel of $\varepsilon$. The additional verifications that $\varepsilon \in \mathcal{E}$ and $\kappa'' \in \mathcal{E}$ use the fact that $\mathcal{E}$ is a closed class: to show $\varepsilon \in \mathcal{E}$, take an $\mathcal{E}$-projective $Q$ and $\varphi : Q \to A$. Since $\alpha'' \in \mathcal{E}$, lift $\alpha'' \varphi$ to $\psi'' : Q \to P''$. Then $\varphi - \theta \psi''$ maps to $0$ in $A''$, hence factors through $\alpha'$. Using $\mathcal{E}$-projectivity of $P'$, lift to $\psi' : Q \to P'$. Then $(\psi', \psi'')$ gives the required lift, proving $\varepsilon \in \mathcal{E}$ (by closure of $\mathcal{E}$). The verification for $\kappa''$ is similar.
