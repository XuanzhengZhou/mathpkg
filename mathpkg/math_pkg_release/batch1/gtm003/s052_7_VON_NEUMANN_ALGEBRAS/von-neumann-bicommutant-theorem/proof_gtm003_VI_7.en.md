---
role: proof
locale: en
of_concept: von-neumann-bicommutant-theorem
source_book: gtm003
source_chapter: "VI"
source_section: "7"
---

The proof of von Neumann's bicommutant theorem establishes a cycle of implications among the four equivalent conditions. The standard proof proceeds by showing $(d) \Rightarrow (c) \Rightarrow (b) \Rightarrow (a) \Rightarrow (d)$.

For $(d) \Rightarrow (c) \Rightarrow (b)$: These implications follow from the fact that the $\sigma$-weak topology is finer than the strong operator topology, which in turn is finer than the weak operator topology. Hence closure in a coarser topology implies closure in a finer topology.

For $(b) \Rightarrow (a)$: If $M$ is weakly closed and contains $e$, then clearly $M \subset M^{cc}$. For the reverse inclusion, let $x \in M^{cc}$. One shows that $x$ belongs to the weak closure of $M$ using the bicommutant property and the Hahn-Banach theorem applied to the locally convex space $\mathcal{L}_w(H)$. Since $M$ is weakly closed, $x \in M$, establishing $M^{cc} \subset M$.

For $(a) \Rightarrow (d)$: If $M = M^{cc}$, then $M$ is a commutant and therefore automatically $\sigma$-weakly closed, since commutants are closed in the weak operator topology and hence in the finer $\sigma$-weak topology as well.

The equivalence of these conditions characterizes von Neumann algebras as precisely those $C^*$-subalgebras of $\mathcal{L}(H)$ containing the identity that are closed in any of these natural operator topologies.
