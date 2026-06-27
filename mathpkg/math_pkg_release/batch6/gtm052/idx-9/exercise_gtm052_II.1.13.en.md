---
role: exercise
locale: en
chapter: "II"
section: "1"
exercise_number: "1.13"
---
Given a presheaf $\mathcal{F}$ on $X$, define a topological space $\text{Spé}(\mathcal{F})$, called the **espace étalé** of $\mathcal{F}$, as follows. As a set, $\text{Spé}(\mathcal{F}) = \bigcup_{P \in X} \mathcal{F}_P$. Define a projection map $\pi: \text{Spé}(\mathcal{F}) \to X$ by sending $s \in \mathcal{F}_P$ to $P$. For each open set $U \subseteq X$ and each section $s \in \mathcal{F}(U)$, define a map $\bar{s}: U \to \text{Spé}(\mathcal{F})$ by sending $P \in U$ to the germ $s_P \in \mathcal{F}_P$. Give $\text{Spé}(\mathcal{F})$ the strongest topology such that all the maps $\bar{s}: U \to \text{Spé}(\mathcal{F})$ for all open $U \subseteq X$ and all $s \in \mathcal{F}(U)$ are continuous. Show that the sheaf of continuous sections of $\pi$ is isomorphic to the sheafification $\mathcal{F}^+$ of $\mathcal{F}$.

(This exercise is included to establish the connection between the sheaf definition used here and another definition often found in the literature. See for example Godement [1, Ch. II, §1.2].)
