---
role: proof
locale: en
of_concept: properties-of-deducibility
source_book: gtm037
source_chapter: "1"
source_section: "1.2"
---

The proof of each part follows directly from the definition of formal proof.

(i) Any formal proof of $\varphi$ from $\Delta$ is also a formal proof of $\varphi$ from $\Gamma$, since every $\psi_i \in \Delta$ is also in $\Gamma$ (by $\Delta \subseteq \Gamma$).

(ii) Let $\langle \psi_0, \ldots, \psi_{m-1} \rangle$ be a formal proof of $\varphi$ from $\Gamma$. Let $\Theta = \Gamma \cap \{\psi_0, \ldots, \psi_{m-1}\}$, i.e., the set of hypotheses from $\Gamma$ that actually appear in the proof. Then $\Theta$ is a finite subset of $\Gamma$, and the same sequence is a formal proof of $\varphi$ from $\Theta$.

(iii) For each $\chi \in \Delta$, let $P_\chi$ be a formal proof of $\chi$ from $\Gamma$. Let $Q$ be a formal proof of $\varphi$ from $\Delta$. Concatenate all the $P_\chi$ proofs (for the finitely or infinitely many $\chi$ actually appearing in $Q$) followed by $Q$, and replace each occurrence of a $\chi \in \Delta$ in $Q$ with the corresponding proof $P_\chi$, to obtain a formal proof of $\varphi$ from $\Gamma$.

(iv) Let $P$ be a formal proof of $\varphi$ from $\Gamma$ and $Q$ a formal proof of $\varphi \to \psi$ from $\Gamma$. Concatenate $P$ and $Q$ and append $\psi$, which follows by detachment from $\varphi$ and $\varphi \to \psi$.
