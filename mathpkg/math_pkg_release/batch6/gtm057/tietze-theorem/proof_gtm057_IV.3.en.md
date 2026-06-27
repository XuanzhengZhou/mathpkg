---
role: proof
locale: en
of_concept: tietze-theorem
source_book: gtm057
source_chapter: "IV"
source_section: "3"
---

The Tietze theorem asserts that any two finite presentations of isomorphic groups are related by a finite sequence of Tietze operations I, I', II, II'. We prove that an arbitrary presentation equivalence

$$f: (\mathbf{x} : \mathbf{r}) \to (\mathbf{y} : \mathbf{s}), \quad g: (\mathbf{y} : \mathbf{s}) \to (\mathbf{x} : \mathbf{r})$$

can be factored into these elementary operations.

Let $(\mathbf{x} : \mathbf{r})_\phi$ and $(\mathbf{y} : \mathbf{s})_\psi$ be presentations of the same group $G$. The mapping $f$ is a homomorphism $F(\mathbf{x}) \to F(\mathbf{y})$ such that $\gamma f(r) = 1$ for all $r \in \mathbf{r}$, where $\gamma$ is the canonical homomorphism onto $|\mathbf{y} : \mathbf{s}|$. Similarly $g$ satisfies the dual condition, and $gf \simeq 1$, $fg \simeq 1$.

First, introduce the union presentation $(\mathbf{x} \cup \mathbf{y} : \mathbf{r} \cup \mathbf{s} \cup \mathbf{a} \cup \mathbf{b})$ where

$$\mathbf{a} = \{y \cdot f(y)^{-1} : y \in \mathbf{y}\}, \quad \mathbf{b} = \{x \cdot g(x)^{-1} : x \in \mathbf{x}\}.$$

The identity mapping on $F(\mathbf{x})$ together with the mapping $x \mapsto f(x)$ on generators gives a presentation mapping from $(\mathbf{x} : \mathbf{r})$ to this union. By Theorem (3.1), the kernel of the natural homomorphism from $F(\mathbf{x} \cup \mathbf{y})$ to $G$ equals the consequence of $\mathbf{r} \cup \mathbf{a}$, and by symmetry also of $\mathbf{s} \cup \mathbf{b}$. Hence the added relators in $\mathbf{a}$ and $\mathbf{b}$ are all consequences of the existing ones, which means the passage from $(\mathbf{x} : \mathbf{r})$ to the union presentation and back factors through Tietze I and I' operations.

The passage from $(\mathbf{x} : \mathbf{r})$ to $(\mathbf{x} \cup \mathbf{y} : \mathbf{r} \cup \mathbf{a})$ is a composition of Tietze II equivalences (adding one generator $y \in \mathbf{y}$ at a time, each with the corresponding relator $y \cdot f(y)^{-1}$). Similarly, the return passage via Tietze II' removes the extra generators. The intermediate steps through the full union presentation involve Tietze I/I' operations to add and remove redundant relators. Thus every presentation equivalence factors through the four Tietze operations.
