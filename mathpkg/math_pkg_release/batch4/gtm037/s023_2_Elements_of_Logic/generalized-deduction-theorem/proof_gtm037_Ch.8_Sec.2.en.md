---
role: proof
locale: en
of_concept: generalized-deduction-theorem
source_book: gtm037
source_chapter: "Chapter 8: Sentential Logic"
source_section: "2. Elements of Logic"
---
By 8.9(ii) we may assume that $\Delta$ is finite. Hence it is enough to prove by induction on $m$ that for all $m \in \omega$ and all $\varphi \in {}^{m+1}\text{Sent}(\mathcal{P})$, if $\Gamma \cup \{\varphi_i : i \leq m\} \vdash \psi$ then $\Gamma \vdash \bigwedge_{i \leq m} \varphi_i \rightarrow \psi$. This statement for $m = 1$ is just the deduction theorem. Now we assume our statement for $m$ (and for all sentences $\psi$), and we assume that $\varphi \in {}^{m+2}\text{Sent}(\mathcal{P})$ and $\Gamma \cup \{\varphi_i : i \leq m+1\} \vdash \psi$. By the deduction theorem, $\Gamma \cup \{\varphi_i : i \leq m\} \vdash \varphi_{m+1} \rightarrow \psi$. Hence by the induction assumption, $\Gamma \vdash \bigwedge_{i \leq m} \varphi_i \rightarrow (\varphi_{m+1} \rightarrow \psi)$. Now using Proposition 8.35 it is easily checked that the following sentence is a tautology, and hence is a $\Gamma$-theorem:

$$\left[ \bigwedge_{i \leq m} \varphi_i \rightarrow (\varphi_{m+1} \rightarrow \psi) \right] \rightarrow \left( \bigwedge_{i \leq m+1} \varphi_i \rightarrow \psi \right).$$

It follows that $\Gamma \vdash \bigwedge_{i \leq m+1} \varphi_i \rightarrow \psi$, as desired.
