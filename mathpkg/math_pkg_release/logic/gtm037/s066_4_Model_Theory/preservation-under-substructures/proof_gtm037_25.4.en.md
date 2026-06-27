---
role: proof
locale: en
of_concept: preservation-under-substructures
source_book: gtm037
source_chapter: "25"
source_section: "4"
---

It is trivial that $(ii) \Rightarrow (i)$. Now assume that $(i)$ holds. By 25.3, $S\,\mathrm{Mod}(\Gamma \cup \{\varphi\})$ is closed under ultraproducts $Up$, so by 25.2 we may write $S\,\mathrm{Mod}(\Gamma \cup \{\varphi\}) = \mathrm{Mod}\,\Delta$ for some set $\Delta$ of universal sentences. Now by $(i)$ we have $\mathrm{Mod}\,\Gamma \cap S\,\mathrm{Mod}(\Gamma \cup \{\varphi\}) \subseteq \mathrm{Mod}\,\{\varphi\}$, so $\Gamma \cup \Delta \models \varphi$. By compactness, $\Gamma \models \psi \rightarrow \varphi$ for some finite conjunction $\psi$ of members of $\Delta$. Conversely, since $\Delta$ axiomatizes $S\,\mathrm{Mod}(\Gamma \cup \{\varphi\})$, every model of $\Gamma \cup \{\varphi\}$ satisfies every member of $\Delta$, so $\Gamma \models \varphi \rightarrow \psi$. Thus $\Gamma \models \varphi \leftrightarrow \psi$, where $\psi$ is a universal sentence (as a finite conjunction of universal sentences).
