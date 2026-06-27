---
role: proof
locale: en
of_concept: universal-property-of-free-algebra
source_book: gtm026
source_chapter: "2"
source_section: ""
---

Consider the commutative diagram

\[
\begin{CD}
A @>{A\eta}>> AT \\
@V{f}VV @. \\
X @= X
\end{CD}
\]

By the universal property of the term algebra (Proposition 1.20), the function $f: A \to X$ extends uniquely to an $\Omega$-homomorphism

$$
f^{\#}: A\Omega \longrightarrow (X, \delta).
$$

Now suppose $p E_A q$ for terms $p, q \in A\Omega$. By definition of $E_A$ (Definition 2.1), this means that for every $(\Omega, E)$-algebra and every variable assignment, $p$ and $q$ evaluate to the same element. In particular, under the assignment $f$ and algebra $(X, \delta)$, we have $p f^{\#} = q f^{\#}$. Hence $f^{\#}: A\Omega \to X$ respects the equivalence relation $E_A$.

Therefore $f^{\#}$ factors uniquely through the quotient map $A\rho: A\Omega \twoheadrightarrow AT = A\Omega/E_A$, yielding a unique function

$$
f^{\#}: AT \longrightarrow X
$$

such that $f^{\#} \circ A\rho = f^{\#}_{\text{term}}$ (the term-algebra extension). Since $A\rho$ is a surjective $\Omega$-homomorphism and $f^{\#}_{\text{term}}$ is an $\Omega$-homomorphism, their composition ensures that the induced map $f^{\#}: AT \to X$ is also an $\Omega$-homomorphism.

By construction, for any $a \in A$,
$$
a \cdot (A\eta \cdot f^{\#}) = [a] \cdot f^{\#} = a \cdot f^{\#}_{\text{term}} = a f,
$$
so $f = A\eta \cdot f^{\#}$, i.e., $f^{\#}$ extends $f$ along $A\eta$.

**Uniqueness:** If $g: AT \to X$ is another $\Omega$-homomorphism satisfying $f = A\eta \cdot g$, then for any equivalence class $[t] \in AT$ (with $t \in A\Omega$), we have $[t] \cdot g = t f^{\#}_{\text{term}} = [t] \cdot f^{\#}$, since $g$ agrees with $f^{\#}$ on the generators $A\eta(A)$ and both are $\Omega$-homomorphisms. Hence $g = f^{\#}$, completing the proof.
