---
role: proof
locale: en
of_concept: shelah-categoricity-aec
source_book: gtm053
source_chapter: "X"
source_section: "7"
---

# Shelah's Theorems on Abstract Elementary Classes

**Theorem 7.8 (S. Shelah — Categoricity Transfer for AEC).** There exists a Hanf number $\mu$ (depending only on the Löwenheim-Skolem number $\operatorname{LS}(K)$ of the class) such that if an abstract elementary class $K$ has arbitrarily large models and satisfies the amalgamation property and the joint embedding property, then provided that $K$ is categorical in some successor cardinal $\lambda > \mu$, it is categorical in all larger cardinals.

**Theorem 7.9 (S. Shelah).** Assume the mild set-theoretic assumptions $2^{\aleph_n} < 2^{\aleph_{n+1}}$ for all natural $n$. Let $\Sigma$ be an $L_{\omega_1,\omega}$-sentence that is categorical in $\aleph_n$ for every $n$. Then $\Sigma$ has a unique model in every infinite cardinal.

*Note.* The full proofs of these theorems are far beyond the scope of GTM053. The text provides only the statements as concluding results of the theory of abstract elementary classes. We sketch the background and significance.

**Background: Abstract Elementary Classes (Definition 7.1, 7.6).** Shelah introduced the concept of Abstract Elementary Classes (AEC) to shift the focus from syntactic specifications of non-first-order languages to algebraic characteristics of classes of models. An AEC is a class $\mathbf{K}$ of $L$-structures equipped with a notion of "strong submodel" $\preceq_{\mathbf{K}}$ satisfying:

- Closure under isomorphisms,
- Coherence: if $\mathbf{A} \preceq_{\mathbf{K}} \mathbf{B}$ then $\mathbf{A} \subseteq \mathbf{B}$,
- Tarski-Vaught chain axioms: unions of $\preceq_{\mathbf{K}}$-chains belong to $\mathbf{K}$,
- Löwenheim-Skolem: there exists a cardinal $\operatorname{LS}(\mathbf{K})$ such that every structure in $\mathbf{K}$ has a strong submodel of size $\leq \operatorname{LS}(\mathbf{K})$.

Examples include models of $L_{\omega_1,\omega}$-sentences, and the class of fields with pseudoexponentiation (with respect to the strong embedding corresponding to the Schanuel predimension).

**Proof Ideas.** Shelah's proof of Theorem 7.8 develops a deep classification theory for AECs, generalizing stability theory from first-order logic. Key ingredients include:

1. **Galois types**: A notion of type defined via automorphisms of saturated models (replacing syntactic types).
2. **Splitting and non-splitting**: Generalizing the first-order notion to isolate the concept of a stable AEC.
3. **Tameness**: A property that Galois types are determined by their restrictions to small submodels, which Shelah shows follows from categoricity.
4. **Categoricity transfer**: Using these tools, one proves that categoricity in one sufficiently large cardinal propagates to all larger cardinals, analogous to Morley's categoricity theorem for first-order theories.

The Hanf number $\mu$ is roughly $\beth_{(2^{\operatorname{LS}(\mathbf{K})})^+}$, bounding the threshold beyond which categoricity transfers.

Theorem 7.9 refines this for $L_{\omega_1,\omega}$-sentences under mild cardinal arithmetic assumptions, showing that categoricity in all $\aleph_n$ implies categoricity in all infinite cardinals. $\square$
