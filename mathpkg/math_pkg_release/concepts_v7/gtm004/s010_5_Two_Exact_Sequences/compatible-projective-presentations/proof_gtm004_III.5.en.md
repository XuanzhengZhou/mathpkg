---
role: proof
locale: en
of_concept: compatible-projective-presentations
source_book: gtm004
source_chapter: "III"
source_section: "5"
---

# Proof of Compatible Projective Presentations (Lemma 5.4)

To a short exact sequence $A' \xrightarrow{\varphi} A \xrightarrow{\psi} A''$ and to projective presentations $\varepsilon' : P' \rightarrow A'$ and $\varepsilon'' : P'' \rightarrow A''$, there exists a projective presentation $\varepsilon : P \rightarrow A$ and homomorphisms $\iota : P' \rightarrow P$ and $\pi : P \rightarrow P''$ such that the following diagram is commutative with exact rows:

$$
\begin{array}{ccccccccc}
0 & \rightarrow & R' & \rightarrow & P' & \xrightarrow{\varepsilon'} & A' & \rightarrow & 0 \\
& & \downarrow & & \downarrow \iota & & \downarrow \varphi & & \\
0 & \rightarrow & R & \rightarrow & P & \xrightarrow{\varepsilon} & A & \rightarrow & 0 \\
& & \downarrow & & \downarrow \pi & & \downarrow \psi & & \\
0 & \rightarrow & R'' & \rightarrow & P'' & \xrightarrow{\varepsilon''} & A'' & \rightarrow & 0
\end{array}
$$

**Proof.** Set $P = P' \oplus P''$. Since $P''$ is projective, we can lift $\psi : A \rightarrow A''$ to a map $\chi : P'' \rightarrow A$ such that $\psi \chi = \varepsilon''$. Define $\iota : P' \rightarrow P$ as the inclusion into the first summand, and $\pi : P \rightarrow P''$ as the projection onto the second summand. Define $\varepsilon : P \rightarrow A$ by $\varepsilon(p', p'') = \varphi \varepsilon'(p') + \chi(p'')$. It is plain that with this definition the above diagram commutes. By Lemma I.1.1, $\varepsilon$ is epimorphic.

The maps between the kernels $R', R, R''$ are induced by restriction, yielding the short exact sequence of kernels as shown.
