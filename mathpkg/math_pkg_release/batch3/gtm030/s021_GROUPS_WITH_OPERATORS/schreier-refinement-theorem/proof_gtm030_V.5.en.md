---
role: proof
locale: en
of_concept: schreier-refinement-theorem
source_book: gtm030
source_chapter: "V: Groups with Operators"
source_section: "5: Normal series and composition series"
---

Let

$$\mathfrak{G} = \mathfrak{G}_1 \supseteq \mathfrak{G}_2 \supseteq \cdots \supseteq \mathfrak{G}_{s+1} = 1$$

and

$$\mathfrak{G} = \mathfrak{H}_1 \supseteq \mathfrak{H}_2 \supseteq \cdots \supseteq \mathfrak{H}_{t+1} = 1$$

be two normal series for $\mathfrak{G}$. Define

$$\mathfrak{G}_{ik} = (\mathfrak{G}_i \cap \mathfrak{H}_k)\mathfrak{G}_{i+1}$$

for $i = 1, \ldots, s$ and $k = 1, \ldots, t+1$. Note that $\mathfrak{G}_{i1} = \mathfrak{G}_i$ and $\mathfrak{G}_{i,t+1} = \mathfrak{G}_{i+1}$.

Then $\mathfrak{G} = \mathfrak{G}_{11} \supseteq \mathfrak{G}_{12} \supseteq \cdots \supseteq \mathfrak{G}_{1t} \supseteq \mathfrak{G}_{21} \supseteq \cdots \supseteq \mathfrak{G}_{s,t} \supseteq \mathfrak{G}_{s+1,1} = 1$ is a refinement of the first series. Similarly, defining $\mathfrak{H}_{ki} = (\mathfrak{G}_i \cap \mathfrak{H}_k)\mathfrak{H}_{k+1}$ gives a refinement of the second series.

Now apply the third isomorphism theorem to the groups $\mathfrak{G}_i, \mathfrak{H}_k, \mathfrak{G}_{i+1}, \mathfrak{H}_{k+1}$ to conclude that $\mathfrak{G}_{i,k+1} = (\mathfrak{G}_i \cap \mathfrak{H}_{k+1})\mathfrak{G}_{i+1}$ is invariant in $\mathfrak{G}_{ik} = (\mathfrak{G}_i \cap \mathfrak{H}_k)\mathfrak{G}_{i+1}$, that $\mathfrak{H}_{k,i+1} = (\mathfrak{G}_{i+1} \cap \mathfrak{H}_k)\mathfrak{H}_{k+1}$ is invariant in $\mathfrak{H}_{ki} = (\mathfrak{G}_i \cap \mathfrak{H}_k)\mathfrak{H}_{k+1}$, and that

$$\mathfrak{G}_{ik}/\mathfrak{G}_{i,k+1} \cong \mathfrak{H}_{ki}/\mathfrak{H}_{k,i+1}.$$

Hence the two refined series are normal and equivalent.
