---
role: exercise
locale: en
chapter: "2"
section: "Exercises"
exercise_number: 16
---

(The contravariant representation theorem [Linton '70].) Let $A$ be locally small and let $J$ in $A$ be such that the power $J^n$ exists for every set $n$. Then $A(-, J): A^{\mathrm{op}} \longrightarrow \mathbf{Set}$ has $n \mapsto J^n$ as left adjoint, giving rise to the double dualization theory $J$.

(a) Let $T$ be a theory in $\mathbf{Set}$ such that every monomorphism in $\mathbf{Set}^T$ is an equalizer. Write $|A|$ for $AU^T$ and $[A, B]$ for $\mathbf{Set}^T(A, B)$. Let $J$ be an injective cogenerator (Exercises 2.1.20 and 2.1.59) of $\mathbf{Set}^T$. Prove that the structural reflection of $[-, J] : (\mathbf{Set}^T)^{\mathrm{op}} \longrightarrow \mathbf{Set}$ is obtained, via the semantic comparison functor $\Phi : (\mathbf{Set}^T)^{\mathrm{op}} \longrightarrow \mathbf{Set}^J$, as the full subcategory over $\mathbf{Set}$ of $\mathbf{Set}^J$ of all $A$ for which the evaluation map

$$A \xrightarrow{ev} \bar{J}^{\langle A, \bar{J} \rangle}$$

is injective, where $\bar{J}$ is the $J$-algebra $(|J|, \mathrm{pr}_{\mathrm{id}} : J^{(|J|)} \longrightarrow J)$ and $\langle -, - \rangle$ means $J$-homomorphisms. For each set $A$, show that the $T$-homomorphic extension of

$$A \xrightarrow{ev} J^{(|J|^A)}$$

is injective and establishes a theory isomorphism of $T$ with $\bar{J}$; thus $T$ is a double-dualization theory.

(b) Let $\mathbf{Set}^T$ be Boolean rings with unit and let $J = 2$. Show that $\mathbf{Set}^J$ is compact Hausdorff spaces and that $\Phi$ is the Stone duality functor.

(c) Given $f: A \longrightarrow B$ with $B\eta$ split mono and $fT$ an isomorphism, prove that $f$ is an isomorphism. [Hint: use (b) and exercise 2.1.21.]
