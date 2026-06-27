---
role: proof
locale: en
of_concept: pietsch-nuclear-characterization
source_book: gtm003
source_chapter: "III"
source_section: "10.7"
---
In view of (10.2) through (10.6), we have the following chain of implications:

$E$ is nuclear $\Rightarrow$ every equicontinuous subset of $E'$ is pre-nuclear (by (10.2)) $\Rightarrow$ every equicontinuous subset of $l^1[\mathbb{N}, E]'$ is contained in and equicontinuous in $l^1(\mathbb{N}, E)'$ (by the identification of duals in (10.4)) $\Rightarrow$ $l^1[\mathbb{N}, E]$ is a dense topological vector subspace of $l^1(\mathbb{N}, E)$ (by the bipolar theorem and the fact that equicontinuous sets determine the topology) $\Rightarrow$ $l^1[\mathbb{N}, E] = l^1(\mathbb{N}, E)$ as topological vector spaces (cf. the proof of (10.5), which shows that the density together with the completeness argument forces equality) $\Rightarrow$ $l^1[\mathbf{A}, E] = l^1(\mathbf{A}, E)$ for any $\mathbf{A} \neq \emptyset$ (by (10.5), which reduces the arbitrary index set case to $\mathbb{N}$) $\Rightarrow$ every summable family in $E$ is absolutely summable $\Rightarrow$ every equicontinuous family in $E'$ is pre-nuclear (by the dual characterization in (10.4) applied to arbitrary $\mathbf{A}$) $\Rightarrow$ every equicontinuous subset of $E'$ is prenuclear $\Rightarrow$ $E$ is nuclear (by (10.2), which states that prenuclearity of all equicontinuous sets characterizes nuclear spaces).

More explicitly:

*($E$ nuclear $\Rightarrow$ isomorphism):* If $E$ is nuclear, then by (10.2) every equicontinuous subset of $E'$ is prenuclear. Theorem 10.4 then implies that the dual of $l^1[\mathbb{N}, E]$ is contained in the dual of $l^1(\mathbb{N}, E)$, and the Mackey-Arens theorem yields that the topology of $l^1[\mathbb{N}, E]$ is finer than that induced by $l^1(\mathbb{N}, E)$. Since the reverse inclusion of topologies always holds, the two topologies coincide on the subspace where both are defined. By (10.6), $l^1(\mathbb{N}) \otimes E$ is dense in both spaces, so the completions coincide, forcing $l^1[\mathbb{N}, E] = l^1(\mathbb{N}, E)$ topologically.

*($E$ not nuclear $\Rightarrow$ not isomorphic):* If $E$ is not nuclear, there exists an equicontinuous subset of $E'$ that is not prenuclear. By the dual characterization in (10.4), this produces a continuous linear functional on $l^1[\mathbb{N}, E]$ that does not extend continuously to $l^1(\mathbb{N}, E)$, showing the imbedding cannot be onto, hence not an isomorphism.

The chain of equivalences closes, establishing the theorem.
