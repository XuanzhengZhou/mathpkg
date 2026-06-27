---
role: proof
locale: en
of_concept: algebra-epimorphism-complex
source_book: gtm015
source_chapter: "10"
source_section: "70"
---

# Proof of Continuity of algebra epimorphisms to the complex numbers

Proof. {It is not assumed that $A$ has a unity element; and if $A$ does have a unity element, it is not assumed to have norm one.}

Let $A_1 = A \oplus \mathbb{C}$ be the unitification of $A$ constructed in (49.5). In particular, every $x \in A_1$ has a unique representation $x = a + \lambda u$ ($a \in A$, $\lambda \in \mathbb{C}$), and $\|x\| = \|a\| + |\lambda|$. Define $\psi: A_1 \to \mathbb{C}$ by the formula

$$\psi(a + \lambda u) = \varphi(a) + \lambda \quad (a \in A, \lambda \in \mathbb{C}).$$

Evidently $\psi$ is an algebra epimorphism that extends $\varphi$. Since $A$ is isometrically embedded in $A_1$, it will suffice to show that $\psi$ is continuous and $\|\psi\| = 1$.

Let $M$ be the kernel of $\psi$. Since the quotient algebra $A/M$ is isomorphic to the field $\mathbb{C}$, $M$ is a maximal ideal; by the proof of (52.3), $M$ is closed in $A_1$. Since $\psi$ is a linear form, we conclude that $\psi$ is continuous (22.2).

If $x \in A_1$ and $\|x\| = 1$, then

$$|\psi(x)|^n = |\psi(x^n)| \leq \|\psi\| \|x^n\| \leq \|\psi\|$$

for every positive integer $n$. Letting $n \to \infty$, we obtain $|\psi(x)| \leq 1$ whenever $\|x\| = 1$, thus $\|\psi\| \leq 1$. Since $\psi(u) = 1$ and $\|u\| = 1$, we have $\|\psi\| = 1$.
