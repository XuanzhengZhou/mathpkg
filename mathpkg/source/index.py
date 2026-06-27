"""
Index parser (modeled after apt's tagfile parser).

Parses a topic's index.yaml file to extract the list of concept IDs.
"""

from __future__ import annotations

import os
import logging
from typing import Dict, List, Any

logger = logging.getLogger(__name__)


def parse_index(index_path: str) -> Dict[str, Any]:
    """
    Parse an index.yaml file and return a structured representation.

    Parameters
    ----------
    index_path : str
        Absolute path to the index.yaml file.

    Returns
    -------
    dict with keys:
        source_name : str — name of the source (from the file or derived)
        source_uri  : str — directory containing the index
        topics      : list of topic dicts (original structure preserved)
        concept_ids : list[str] — all concept IDs mentioned in any topic
    """
    if not os.path.isfile(index_path):
        raise FileNotFoundError(f"Index file not found: {index_path}")

    import yaml

    with open(index_path, "r", encoding="utf-8") as fh:
        doc = yaml.safe_load(fh) or {}

    source_name = doc.get("source_name", os.path.basename(os.path.dirname(index_path)))
    source_uri = os.path.dirname(os.path.abspath(index_path))
    topics = doc.get("topics", [])
    if not isinstance(topics, list):
        topics = []

    concept_ids: List[str] = []
    for topic in topics:
        if not isinstance(topic, dict):
            continue
        concepts = topic.get("concepts", [])
        if isinstance(concepts, list):
            for cid in concepts:
                cid = str(cid).strip()
                if cid and cid not in concept_ids:
                    concept_ids.append(cid)

    return {
        "source_name": str(source_name),
        "source_uri": source_uri,
        "topics": topics,
        "concept_ids": concept_ids,
    }
