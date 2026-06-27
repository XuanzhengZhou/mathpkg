---
role: proof
locale: en
of_concept: gns-construction
source_book: gtm015
source_chapter: "Chapter 7: C*-Algebras"
source_section: "58. Preliminaries"
---

# Proof of GNS Construction

Proof. In particular, we seek a Hilbert space $H$. Where is the inner product to come from? Answer: from the function $(x, y) \mapsto f(y^*x)$. The details are as follows. The formula

(1) $\langle x, y \rangle = f(y^*x)$ $(x, y \in A)$

defines a positive sesquilinear form on $A$ (41.9). {The choice of $f(y^*x)$ instead of $f(xy^*)$ reflects a preference for using the left regular representation of $A$ rather than the right regular antirepresentation.} Applying (41.14), we have the Cauchy-Schwarz inequality

(2) $|\langle x, y \rangle|^2 \leq \langle x, x \rangle \langle y, y \rangle$,

as well as the Hermitian property

(3) $\langle x, y \rangle^* = \langle y, x \rangle$.

The form $\langle x, y \rangle$ is in general not strictly positive; to get strict positivity, we must pass to quotients modulo a suitable linear subspace $N$ of $A$. Namely, let

$$N = \{x \in A : \langle x, x \rangle = 0\};$$

it is clear from (2) that

(4) $$N = \{x \in A : \langle x, y \rangle = 0 \quad \text{for all } y \in A\}$$

$$= \{y \in A : \langle x, y \rangle = 0 \quad \text{for all } x \in A\},$$

therefore $N$ is obviously a linear subspace of $A$. Write $E

for all $a, x, y$ in $A$. It follows at once from (4) and (6) that $N$ is a left ideal of $A$. Each $a \in A$ defines a linear mapping $\varphi(a) : E \rightarrow E$ by the formula

(7) $$\varphi(a)\tilde{x} = (ax)^{\sim} \quad (x \in A).$$

{The mapping is well-defined because if $\tilde{x} = \tilde{y}$, i.e., if $x - y \in N$, then $a(x - y) \in N$, $(ax)^{\sim} = (ay)^{\sim}$.} Routine calculations show that $a \mapsto \varphi(a)$ is an algebra homomorphism of $A$ into the algebra of all linear mappings on $E$:

(8) $$\varphi(a + b) = \varphi(a) + \varphi(b),$$

(9) $$\varphi(\lambda a) = \lambda \varphi(a),$$

(10) $$\varphi(ab) = \varphi(a)\varphi(b),$$

for all $a, b \in A$ and $\lambda \in \mathbb{C}$. Moreover,

(11) $(\varphi(a)\tilde{x}|\tilde{y}) = (\tilde{x}|\varphi(a^*)\tilde{y})$$

for all $a, x, y \in A$. {Proof: Citing (6) at the appropriate step, we have $(\varphi(a)\tilde{x}|\tilde{y}) = ((ax)^{\sim}|\tilde{y}) = \langle ax, y \rangle = \langle x, a^*y \rangle = (\tilde{x}|\varphi(a^*)\tilde{y}).$}

We have constructed, so to speak, a ‘*-representation’ $\varphi : A \rightarrow \mathcal{V}(E)$, where $\mathcal{V}(E)$ is the algebra of all linear mappings on $E$ (cf. the proof of (40.4)). {We remark that the construction of $\varphi$ satisfying (8)–(10) can be performed for any positive sesquilinear form on any *-algebra; and (11) holds iff (6) does.}

To produce a *-representation

The rest of the section is devoted to complementary material that gives additional perspective on what has gone before and opens several new themes of general importance.
