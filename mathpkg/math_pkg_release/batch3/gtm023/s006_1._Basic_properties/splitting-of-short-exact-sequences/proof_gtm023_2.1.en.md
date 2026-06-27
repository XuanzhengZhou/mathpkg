---
role: proof
locale: en
of_concept: splitting-of-short-exact-sequences
source_book: gtm023
source_chapter: "2"
source_section: "§1. Basic properties, 2.8"
---
Given the short exact sequence $0 \to F \xrightarrow{\varphi} E \xrightarrow{\psi} G \to 0$, let $E_1$ be a complementary subspace of $\ker \psi$ in $E$, so that
$$E = E_1 \oplus \ker \psi.$$

Consider the restriction $\psi_1$ of $\psi$ to $E_1$, mapping into $G$. Since $\ker \psi_1 = E_1 \cap \ker \psi = 0$, the map $\psi_1$ is injective. Moreover, for any $x \in E$, write $x = x_1 + x_0$ with $x_1 \in E_1$, $x_0 \in \ker \psi$. Then $\psi(x) = \psi(x_1) = \psi_1(x_1)$, so $\psi_1$ is also surjective. Hence $\psi_1: E_1 \xrightarrow{\cong} G$ is a linear isomorphism.

Define $\chi: G \to E$ by $\chi = \psi_1^{-1}$. Then for any $z \in G$,
$$\psi(\chi(z)) = \psi(\psi_1^{-1}(z)) = \psi_1(\psi_1^{-1}(z)) = z = \iota_G(z),$$
so $\psi \circ \chi = \iota_G$. Thus the sequence splits.
