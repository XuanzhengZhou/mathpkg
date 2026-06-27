---
role: proof
locale: en
of_concept: proposition-2-5-proj-structure-sheaf
source_book: gtm052
source_chapter: "II"
source_section: "2"
---

Part (a) says $\text{Proj } S$ is a locally ringed space, and (b) tells us it is covered by open affine schemes, so (c) is a consequence of (a) and (b).

The proof of (a) is practically identical to the proof of Proposition 2.2(a), so is left to the reader.

To prove (b), first note that $D_+(f) = \text{Proj } S - V((f))$, so it is open. Since the elements of $\text{Proj } S$ are those homogeneous prime ideals $\mathfrak{p}$ of $S$ which do not contain all of $S_+$, it follows that the open sets $D_+(f)$ for homogeneous $f \in S_+$ cover $\text{Proj } S$.

Now fix a homogeneous $f \in S_+$. We define an isomorphism $(\varphi, \varphi^\#)$ of locally ringed spaces from $D_+(f)$ to $\text{Spec } S_{(f)}$.

There is a natural homomorphism of rings $S \to S_f$, and $S_{(f)}$ is a subring of $S_f$. For any homogeneous ideal $\mathfrak{a} \subseteq S$, let $\varphi(\mathfrak{a}) = (\mathfrak{a} S_f) \cap S_{(f)}$. In particular, if $\mathfrak{p} \in D_+(f)$, then $\varphi(\mathfrak{p}) \in \text{Spec } S_{(f)}$, giving the map $\varphi$ on sets. The properties of localization show that $\varphi$ is bijective as a map from $D_+(f)$ to $\text{Spec } S_{(f)}$, and it can be shown that $\varphi$ is a homeomorphism.

The sheaf map $\varphi^\#$ is defined using the same localization properties. For an open set $U \subseteq \text{Spec } S_{(f)}$, a section in $\mathcal{O}_{\text{Spec } S_{(f)}}(U)$ is represented locally by fractions whose numerator and denominator are elements of the same degree in $S$, ensuring compatibility with the grading. This yields an isomorphism of sheaves, completing the proof that $(D_+(f), \mathcal{O}|_{D_+(f)}) \cong \text{Spec } S_{(f)}$.
