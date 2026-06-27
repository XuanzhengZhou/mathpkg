---
role: proof
locale: en
of_concept: distinguished-conjunctive-normal-form
source_book: gtm037
source_chapter: "8. Sentential Logic"
source_section: "8.2 Elements of Logic"
---

By duality from the distinguished disjunctive normal form. Let $M$ be the set of all models of $\varphi$; $M \neq \emptyset$ by the assumption that $\varphi$ is not a tautology (so there exists a model in which $\varphi$ is false). Let $g$ be a one-one function mapping some integer $p + 1$ onto $M$. For each $i \leq p$ and $j \leq m$ let

$$\psi_{ij} = \begin{cases} \langle s_j \rangle & \text{if } g_i s_j = 1, \\ \neg \langle s_j \rangle & \text{if } g_i s_j = 0. \end{cases}$$

Thus $g_i^+ \bigwedge_{j \leq m} \psi_{ij} = 1$, while $f^+ \bigwedge_{j \leq m} \psi_{ij} = 0$ if $f \neq g_i$, for each $i \leq p$. From this it follows easily that $f^+ \varphi = f^+ \bigvee_{i \leq p} \bigwedge_{j \leq m} \psi_{ij}$ for every model $f$, as desired. The conjunctive normal form is then obtained by duality.
