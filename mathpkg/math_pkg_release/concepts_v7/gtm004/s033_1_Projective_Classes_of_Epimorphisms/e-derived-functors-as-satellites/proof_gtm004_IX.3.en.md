---
role: proof
locale: en
of_concept: e-derived-functors-as-satellites
source_book: gtm004
source_chapter: "IX. Relative Homological Algebra"
source_section: "3. E-Satellites"
---

# Proof of E-Derived Functors as E-Satellites

**Theorem 3.2.** If $H : \mathfrak{A} \to \mathfrak{B}$ is a right $\mathfrak{E}$-exact functor, where $\mathfrak{E}$ is a projective class of epimorphisms in $\mathfrak{A}$, then the $\mathfrak{E}$-connected sequence of functors $\{L_j^{\mathfrak{E}} H\}$ is the left $\mathfrak{E}$-satellite of $H$, i.e., $L_j^{\mathfrak{E}} H = S_j^{\mathfrak{E}} H$ (with $L_j^{\mathfrak{E}} H = 0$ for $j < 0$).

**Proof.** Since $H$ is right $\mathfrak{E}$-exact, we have $H = L_0 H$. Suppose given an $\mathfrak{E}$-connected sequence of functors $T = \{T_j, \omega_j\}$ and a natural transformation $\varphi : T_0 \to L_0 H$. We must show there exist unique natural transformations $\varphi_j : T_j \to L_j H$ with $\varphi_0 = \varphi$, such that for every short $\mathfrak{E}$-exact sequence $0 \to A' \to A \to A'' \to 0$, the diagram

$$
\begin{array}{ccc}
T_j(A'') & \xrightarrow{\omega_j} & T_{j-1}(A') \\
\downarrow_{\varphi_j} & & \downarrow_{\varphi_{j-1}} \\
L_j H(A'') & \xrightarrow{\omega_j} & L_{j-1} H(A')
\end{array}
$$

commutes for all $j$.

We proceed by induction on $j$, assuming $\varphi_{j-1}$ constructed and natural. To define $\varphi_j$, take any $A$ in $\mathfrak{A}$ and an $\mathfrak{E}$-projective presentation

$$0 \to K \to P \xrightarrow{\varepsilon} A \to 0.$$

Since $P$ is $\mathfrak{E}$-projective, $L_j H(P) = 0$ for $j \geq 1$, so the connecting homomorphism $\omega_j : L_j H(A) \to L_{j-1} H(K)$ is monomorphic (by the exactness of the long exact sequence for $L_* H$). We define $\varphi_j(A)$ to be the unique morphism making the diagram

$$
\begin{array}{ccc}
T_j(A) & \xrightarrow{\omega_j} & T_{j-1}(K) \\
\downarrow_{\varphi_j} & & \downarrow_{\varphi_{j-1}} \\
L_j H(A) & \xrightarrow{\omega_j} & L_{j-1} H(K)
\end{array}
$$

commute. The fact that this definition is independent of the choice of $\mathfrak{E}$-projective presentation and yields a natural transformation follows from the Lemma below.

**Lemma.** The definition of $\varphi_{j+1}$ is natural with respect to all morphisms $\alpha : A \to A'$ in $\mathfrak{A}$. That is, given a morphism of $\mathfrak{E}$-projective presentations induced by $\alpha$, the diagram

$$
\begin{array}{ccc}
T_{j+1}(A) & \xrightarrow{T_{j+1}\alpha} & T_{j+1}(A') \\
\downarrow_{\varphi_{j+1}} & & \downarrow_{\varphi_{j+1}} \\
L_{j+1} H(A) & \xrightarrow{L_{j+1} H\alpha} & L_{j+1} H(A')
\end{array}
$$

commutes.

**Proof of Lemma.** Embed the diagram of $\mathfrak{E}$-projective presentations into a cube. All faces of the cube commute by the induction hypothesis and the naturality of the connecting homomorphisms, and the morphism $\omega_{j+1} : L_{j+1} H(A') \to L_j H(K')$ is monomorphic. Hence the remaining face commutes as well.

To complete the proof, we verify commutativity of the square

$$
\begin{array}{ccc}
T_{j+1}(A'') & \xrightarrow{\omega_{j+1}} & T_j(A') \\
\downarrow_{\varphi_{j+1}} & & \downarrow_{\varphi_j} \\
L_{j+1} H(A'') & \xrightarrow{\omega_{j+1}} & L_j H(A')
\end{array}
$$

for a short $\mathfrak{E}$-exact sequence $0 \to A' \to A \to A'' \to 0$. Take a morphism from an $\mathfrak{E}$-projective presentation

$$0 \to K'' \to P'' \to A'' \to 0$$

to the given $\mathfrak{E}$-exact sequence. Consider the two squares:

$$T_{j+1} A'' \to T_j K'' \qquad T_j K'' \to T_j A'$$
$$L_{j+1} H A'' \to L_j H K'' \qquad L_j H K'' \to L_j H A'$$

The first commutes by definition of $\varphi_{j+1}$, the second by naturality of $\varphi_j$. Naturality of $\omega_{j+1}$ applied to the morphism of $\mathfrak{E}$-exact sequences ensures their composite is the desired square.

This establishes the universal property, proving that $L_j^{\mathfrak{E}} H = S_j^{\mathfrak{E}} H$.
