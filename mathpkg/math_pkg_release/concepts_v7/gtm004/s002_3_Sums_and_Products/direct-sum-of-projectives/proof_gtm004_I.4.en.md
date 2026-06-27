---
role: proof
locale: en
of_concept: direct-sum-of-projectives
source_book: gtm004
source_chapter: "I. Modules"
source_section: "4. Free and Projective Modules"
---

# Proof that Direct Sum is Projective iff Each Summand is Projective

We prove the statement for $A = P \oplus Q$; the general case is analogous.

**($\Rightarrow$)** Assume $P$ and $Q$ are projective. Let $\varepsilon : B \to C$ be surjective and $\gamma : P \oplus Q \to C$ a homomorphism. Define

$$\gamma_P = \gamma \circ i_P : P \to C, \qquad \gamma_Q = \gamma \circ i_Q : Q \to C,$$

where $i_P : P \to P \oplus Q$ and $i_Q : Q \to P \oplus Q$ are the canonical injections. Since $P$ and $Q$ are projective, there exist homomorphisms $\beta_P : P \to B$ and $\beta_Q : Q \to B$ such that

$$\varepsilon \beta_P = \gamma_P, \qquad \varepsilon \beta_Q = \gamma_Q.$$

By the universal property of the direct sum (Proposition 3.2), there exists a unique homomorphism $\beta : P \oplus Q \to B$ such that $\beta i_P = \beta_P$ and $\beta i_Q = \beta_Q$. Then

$$(\varepsilon \beta) i_P = \varepsilon \beta_P = \gamma_P = \gamma i_P, \qquad (\varepsilon \beta) i_Q = \varepsilon \beta_Q = \gamma_Q = \gamma i_Q.$$

By the uniqueness part of the universal property of the direct sum, $\varepsilon \beta = \gamma$. Hence $P \oplus Q$ is projective.

**($\Leftarrow$)** Assume $P \oplus Q$ is projective. Let $\varepsilon : B \to C$ be a surjection and $\gamma_P : P \to C$ a homomorphism. Choose $\gamma_Q : Q \to C$ to be the zero map. By the universal property of the direct sum, there exists a unique $\gamma : P \oplus Q \to C$ such that $\gamma i_P = \gamma_P$ and $\gamma i_Q = \gamma_Q = 0$.

Since $P \oplus Q$ is projective, there exists $\beta : P \oplus Q \to B$ such that $\varepsilon \beta = \gamma$. Then

$$\varepsilon(\beta i_P) = (\varepsilon \beta) i_P = \gamma i_P = \gamma_P.$$

Thus $\beta i_P : P \to B$ is the desired lift, proving $P$ is projective. By symmetry, $Q$ is projective as well.
