---
role: proof
locale: en
of_concept: principal-unit-module-structure
source_book: gtm059
source_chapter: "13"
source_section: "Iwasawa Theory of Local Units"
---

% WARNING: OCR is heavily corrupted. Proof text recovered from partial source.

We work under the assumption that $K = \mathbb{Q}_p$, so that the residue field is $\mathbb{F}_p$. Let
$$e_k = \frac{1}{p-1} \sum_{i=0}^{p-1} \chi^{-k}(\sigma) \sigma$$
be the idempotent in the group ring $\mathbb{Z}_p[G]$ for the character $\chi^k$. For a unit $u \in U_1$, we define the projection onto the $\chi^k$-eigenspace.

Let
$$u_k = (1 - \tau) e_k(u^*)$$
for $k = 1, \dots, p-1$, where $\tau$ is a topological generator and $u^*$ is a limit of coherent units.

Then:
\begin{itemize}
    \item[(i)] $u_1 \equiv 1 - \tau \pmod{u^*}$;
    \item[(ii)] The elements $u_1, u_2, u_3, u_4$ form a basis of a submodule of $U_1$, where $U_i(k)$ is the $\chi^k$-eigenspace of $U_{i+1}$.
\end{itemize}

Statement (i) follows by expanding the product:
\begin{align*}
u_0 &= \prod_{i=1}^{p-1} (1 - \tau) \chi^i \sigma(u^*) \pmod{u^*} \\
    &= \prod_{i=1}^{p-1} (1 - \tau) \chi^i \sigma(u^*) \pmod{u^*} \\
    &\equiv 1 - \tau u^*.
\end{align*}

Statement (ii) follows from standard properties of the idempotent $e_k$.

\noindent\textit{[The remainder of the proof is lost due to OCR truncation.]}
