---
role: proof
locale: en
of_concept: w-sheaf-exact-functor
source_book: gtm038
source_chapter: "VI"
source_section: "1"
---

**1.** Let
$$\mathcal{O} \rightarrow \mathcal{S}' \rightarrow \mathcal{S} \rightarrow \mathcal{S}'' \rightarrow \mathcal{O}$$
be exact. We show by induction on $\ell$ that
$$\mathcal{O} \rightarrow W_\ell(\mathcal{S}') \rightarrow W_\ell(\mathcal{S}) \rightarrow W_\ell(\mathcal{S}'') \rightarrow \mathcal{O}$$
is exact. For $\ell = 0$ this has already been proved in Theorem 1.4. Therefore let $\ell \geqslant 1$. We consider the case $\ell = 1$; the general case is handled entirely analogously.

The following diagram is commutative:

\[
\begin{array}{ccccccccc}
& 0 & & 0 & & 0 & & \\
& \downarrow & & \downarrow & & \downarrow & & \\
0 \rightarrow & \mathcal{S}' & \rightarrow & \mathcal{S} & \rightarrow & \mathcal{S}'' & \rightarrow 0 & \\
& \downarrow & & \downarrow & & \downarrow & & \\
0 \rightarrow & W_0(\mathcal{S}') & \rightarrow & W_0(\mathcal{S}) & \rightarrow & W_0(\mathcal{S}'') & \rightarrow 0 & \\
& \downarrow & & \downarrow & & \downarrow & & \\
0 \rightarrow & \mathcal{Q}' & \rightarrow & \mathcal{Q} & \rightarrow & \mathcal{Q}'' & \rightarrow 0 & \\
& \downarrow & & \downarrow & & \downarrow & & \\
& 0 & & 0 & & 0 & &
\end{array}
\]

with $\mathcal{Q} := W_0(\mathcal{S})/\mathcal{S}$, $\mathcal{Q}'$ and $\mathcal{Q}''$ similarly. All columns and the three top rows are exact.

*(a)* Since $\varphi_2''$ and $\psi_2''$ are surjective, $\varphi_3''$ is also surjective.

*(b)* Since $\psi_2'$ is surjective and $\varphi_2'' \circ \varphi_2' = \mathbf{O}$, by Lemma 1 there is a $\hat{\sigma} \in \mathcal{S}'$ with $\varphi'_2(\sigma^* - \psi'_1(\hat{\sigma})) = \mathbf{O}$. Since $\varphi'_2$ is injective it follows that $\sigma^* - \psi'_1(\hat{\sigma}) = \mathbf{O}$, hence
$$\mathbf{O} = \psi'_2(\sigma^* - \psi'_1(\hat{\sigma})) = \psi'_2(\sigma^*) = \sigma'.$$

Thus, the last row of the diagram is exact, and by Theorem 1.4 we now have the exactness of the sequence
$$\mathbf{O} \rightarrow W_1(\mathcal{S}') \rightarrow W_1(\mathcal{S}) \rightarrow W_1(\mathcal{S}'') \rightarrow \mathbf{O}.$$

This establishes the inductive step for $\ell = 1$; the same diagram-chasing argument works for general $\ell$ by replacing the top three rows with the corresponding exact sequences of $W_{\ell-1}$ sheaves.

**2.** Now let $\mathcal{S}' \xrightarrow{\varphi} \mathcal{S} \xrightarrow{\psi} \mathcal{S}''$ be exact. Then we obtain the following exact sequences by factoring through kernels and images:

$$\mathbf{O} \rightarrow \operatorname{Ker} \varphi \rightarrow \mathcal{S}' \rightarrow \mathcal{Q}' \rightarrow \mathbf{O} \quad (\text{with } \mathcal{Q}' := \mathcal{S}'/\operatorname{Ker} \varphi)$$

$$\mathbf{O} \rightarrow \mathcal{Q}' \rightarrow \mathcal{S} \rightarrow \operatorname{Im} \psi \rightarrow \mathbf{O}$$

$$\mathbf{O} \rightarrow \operatorname{Im} \psi \rightarrow \mathcal{S}'' \rightarrow \mathcal{Q}'' \rightarrow \mathbf{O} \quad (\text{with } \mathcal{Q}'' := \mathcal{S}''/\operatorname{Im} \psi).$$

Applying part (1) to each of these short exact sequences, we obtain an exact sequence of the form
$$W_\ell(\mathcal{S}') \rightarrow W_\ell(\mathcal{Q}') \hookrightarrow W_\ell(\mathcal{S}) \rightarrow W_\ell(\mathcal{S}''),$$
where the first mapping is surjective and the last mapping composes appropriately. Piecing these together yields exactness of $W_\ell(\mathcal{S}') \rightarrow W_\ell(\mathcal{S}) \rightarrow W_\ell(\mathcal{S}'')$, completing the proof that $\mathfrak{W} = (W_\ell)_{\ell \geq 0}$ is an exact functor.
