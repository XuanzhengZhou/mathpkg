---
role: proof
locale: en
of_concept: duality-isomorphism-for-finite-cw-complexes
source_book: gtm020
source_chapter: "16"
source_section: "3"
---

The proof proceeds by induction on the number of cells of $Z$. For the base case, when $Z$ has zero cells (i.e., $Z$ is a finite discrete space), the statement reduces to the definition of $n$-duality on spheres.

For the inductive step, suppose $Z$ is obtained from a subcomplex $Z_0$ by attaching a single cell $D^m$ via an attaching map $\alpha: S^{m-1} \to Z_0$. This gives a cofibration sequence

$$S^{m-1} \xrightarrow{\alpha} Z_0 \to Z \to S^m \xrightarrow{S\alpha} SZ_0 \to \cdots$$

which induces a Puppe exact sequence of $S$-maps. Applying the functors $\{-, X'\}$ and $\{X \wedge -, S^n\}$ yields two long exact sequences, and the natural transformation $u_{(-)}$ gives a map between them:

$$\begin{CD}
\{S^m, X'\} @>>> \{Z, X'\} @>>> \{Z_0, X'\} @>>> \{S^{m-1}, X'\} \\
@V{u_m}VV @V{u_Z}VV @V{u_{Z_0}}VV @V{u_{m-1}}VV \\
\{X \wedge S^m, S^n\} @>>> \{X \wedge Z, S^n\} @>>> \{X \wedge Z_0, S^n\} @>>> \{X \wedge S^{m-1}, S^n\}
\end{CD}$$

By the induction hypothesis, $u_{Z_0}$ is an isomorphism. By the definition of $n$-duality, $u_m$ and $u_{m-1}$ are isomorphisms. By the five lemma applied to the exact sequences, $u_Z$ is an isomorphism. The proof for $u_Z'$ is symmetric.