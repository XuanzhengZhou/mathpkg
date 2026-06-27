---
role: proof
locale: en
of_concept: direct-sum-projective-rel-e
source_book: gtm004
source_chapter: "IX"
source_section: "1. Projective Classes of Epimorphisms"
---

# Proof of Direct Sum of Projective-Rel Objects

**Statement.** $P_1 \oplus P_2$ is projective rel $\mathcal{E}$ if, and only if, both $P_1$ and $P_2$ are projective rel $\mathcal{E}$, where $\mathcal{E}: B \to C$ is an epimorphism in the abelian category $\mathfrak{U}$.

**Proof.** Recall that an object $P$ is projective rel $\mathcal{E}$ if $\mathcal{E}_* : \mathfrak{U}(P, B) \to \mathfrak{U}(P, C)$ is surjective.

$(\Rightarrow)$ Suppose $P_1 \oplus P_2$ is projective rel $\mathcal{E}$. Let $\iota_1 : P_1 \to P_1 \oplus P_2$ be the canonical injection. For any morphism $f : P_1 \to C$, precompose with the projection $\pi_1 : P_1 \oplus P_2 \to P_1$ to obtain $f \circ \pi_1 : P_1 \oplus P_2 \to C$. By the projective property of $P_1 \oplus P_2$, there exists $g : P_1 \oplus P_2 \to B$ such that $\mathcal{E} \circ g = f \circ \pi_1$. Then $g \circ \iota_1 : P_1 \to B$ satisfies $\mathcal{E} \circ (g \circ \iota_1) = f \circ \pi_1 \circ \iota_1 = f$. Hence $P_1$ is projective rel $\mathcal{E}$. The proof for $P_2$ is symmetric using $\iota_2$.

$(\Leftarrow)$ Suppose both $P_1$ and $P_2$ are projective rel $\mathcal{E}$. Let $f : P_1 \oplus P_2 \to C$ be arbitrary. Consider the restrictions $f_1 = f \circ \iota_1 : P_1 \to C$ and $f_2 = f \circ \iota_2 : P_2 \to C$. Since $P_1$ is projective rel $\mathcal{E}$, there exists $g_1 : P_1 \to B$ with $\mathcal{E} \circ g_1 = f_1$. Similarly, there exists $g_2 : P_2 \to B$ with $\mathcal{E} \circ g_2 = f_2$. By the universal property of the biproduct, there exists a unique $g = g_1 \oplus g_2 : P_1 \oplus P_2 \to B$ such that $g \circ \iota_1 = g_1$ and $g \circ \iota_2 = g_2$. Then $\mathcal{E} \circ g \circ \iota_1 = \mathcal{E} \circ g_1 = f_1 = f \circ \iota_1$ and similarly for $\iota_2$, so $\mathcal{E} \circ g = f$. Thus $P_1 \oplus P_2$ is projective rel $\mathcal{E}$.
