"""
ORION Advanced Configuration
Customize agent behavior, consensus thresholds, and research parameters
"""

AGENT_CONFIG = {
    "default_model": "gpt-4o",  # Options: gpt-4o, gpt-4o-mini, gpt-4-turbo
    "fast_model": "gpt-4o-mini",  # For less critical tasks
    "explorer_temperature": 0.3,
    "verifier_temperature": 0.1,  # Low for strict fact-checking
    "critic_temperature": 0.5,  # Higher for creative challenges
    "synthesizer_temperature": 0.2,
    "writer_temperature": 0.4,
    "supervisor_temperature": 0.2,
}

RESEARCH_CONFIG = {
    "min_verification_sources": 2,
    "max_verification_sources": 5,
    "consensus_threshold": 0.85,
    "strong_consensus_threshold": 0.95,
    "min_confidence_for_inclusion": 0.3,
    "high_confidence_threshold": 0.8,
    "max_exploration_iterations": 3,
    "max_verification_cycles": 2,
    "min_source_credibility": 0.4,
    "preferred_source_age_days": 365,
    "max_source_age_days": 1825,
}

INTELLIGENCE_CONFIG = {
    "epistemic_humility": True,
    "knowledge_boundary_detection": True,
    "evidence_aging_penalties": True,
    "claim_decomposition": True,
    "assumption_registry": True,
    "counterfactual_testing": True,
    "bias_rotation": True,
    "confidence_volatility_tracking": True,
    "hallucination_risk_assessment": True,
    "truth_abstention": True,
    "assumption_confidence_threshold": 0.6,
    "volatility_tolerance": 0.15,
    "hallucination_risk_threshold": 0.4,
}

OUTPUT_CONFIG = {
    "include_executive_summary": True,
    "include_full_report": True,
    "include_evidence_ledger": True,
    "include_uncertainty_map": True,
    "include_agent_contributions": True,
    "include_knowledge_boundaries": True,
    "include_comparison_analysis": True,
    "include_explainability_appendix": True,
    "include_future_questions": True,
    "executive_summary_length": "medium",
    "citation_style": "inline",
    "uncertainty_notation": "explicit",
    "enable_txt_export": True,
    "enable_json_export": True,
    "enable_pdf_export": False,
    "enable_markdown_export": True,
}

AGENT_ROLES = {
    "web_explorer": {
        "name": "Web Explorer",
        "description": "General web research, news, and trends",
        "tools": ["duckduckgo", "newspaper4k"],
        "specialization": "broad_coverage",
        "priority_sources": ["news", "blogs", "general_web"],
    },
    "technical_explorer": {
        "name": "Technical Literature Explorer",
        "description": "Academic papers, whitepapers, technical documentation",
        "tools": ["duckduckgo", "newspaper4k"],
        "specialization": "technical_depth",
        "priority_sources": ["academic", "technical_blogs", "whitepapers"],
    },
    "news_explorer": {
        "name": "News & Current Events Explorer",
        "description": "Breaking news, recent developments, temporal trends",
        "tools": ["duckduckgo", "newspaper4k"],
        "specialization": "currency",
        "priority_sources": ["news_sites", "press_releases", "announcements"],
    },
    "verifier": {
        "name": "Verification Agent",
        "description": "Fact-checking and source verification",
        "tools": ["duckduckgo", "newspaper4k"],
        "specialization": "accuracy",
        "verification_mode": "strict",
    },
    "critic": {
        "name": "Adversarial Critic",
        "description": "Challenge assumptions and identify biases",
        "tools": ["duckduckgo"],
        "specialization": "critical_thinking",
        "challenge_mode": "aggressive",
    },
    "synthesizer": {
        "name": "Synthesis Agent",
        "description": "Integrate verified information and resolve contradictions",
        "tools": [],
        "specialization": "reasoning",
        "integration_strategy": "confidence_weighted",
    },
    "writer": {
        "name": "Research Writer",
        "description": "Generate professional research reports",
        "tools": [],
        "specialization": "communication",
        "writing_style": "academic",
    },
    "supervisor": {
        "name": "Meta-Supervisor",
        "description": "Quality control and bias detection",
        "tools": [],
        "specialization": "oversight",
        "monitoring_mode": "continuous",
    },
}

EPISTEMIC_STATUS = {
    "confirmed": {
        "min_sources": 3,
        "min_confidence": 0.9,
        "language": ["established", "confirmed", "demonstrated"],
    },
    "probable": {
        "min_sources": 2,
        "min_confidence": 0.7,
        "language": ["likely", "suggests", "indicates"],
    },
    "disputed": {
        "min_sources": 2,
        "contradictory_evidence": True,
        "language": ["contested", "debated", "unclear"],
    },
    "unknown": {
        "max_sources": 1,
        "max_confidence": 0.5,
        "language": ["uncertain", "unclear", "not established"],
    },
    "abstain": {
        "insufficient_evidence": True,
        "language": ["cannot determine", "insufficient evidence"],
    },
}

SOURCE_CREDIBILITY = {
    "high": [
        "peer_reviewed_journals",
        "government_agencies",
        "established_research_institutions",
        "expert_consensus",
    ],
    "medium": [
        "mainstream_news",
        "technical_blogs",
        "industry_reports",
        "professional_organizations",
    ],
    "low": [
        "personal_blogs",
        "social_media",
        "anonymous_sources",
        "promotional_content",
    ],
    "very_low": [
        "known_misinformation_sources",
        "conspiracy_sites",
        "fabricated_content",
    ],
}

HALLUCINATION_INDICATORS = {
    "high_risk": [
        "single_source_only",
        "no_verifiable_citations",
        "contradicts_known_facts",
        "implausible_claims",
        "lack_of_detail",
    ],
    "medium_risk": [
        "limited_sources",
        "indirect_evidence",
        "generalized_claims",
        "temporal_vagueness",
    ],
    "low_risk": [
        "multiple_independent_sources",
        "specific_verifiable_details",
        "consistent_across_sources",
        "expert_attribution",
    ],
}

BIAS_PATTERNS = {
    "confirmation_bias": {
        "indicators": [
            "selective_source_citation",
            "ignoring_contradictory_evidence",
            "overweighting_supporting_evidence",
        ],
        "mitigation": "adversarial_review",
    },
    "recency_bias": {
        "indicators": [
            "overweighting_recent_sources",
            "ignoring_historical_context",
        ],
        "mitigation": "temporal_balance_check",
    },
    "authority_bias": {
        "indicators": [
            "overreliance_on_expert_opinion",
            "insufficient_verification",
        ],
        "mitigation": "independent_verification",
    },
    "framing_bias": {
        "indicators": [
            "loaded_language",
            "selective_presentation",
        ],
        "mitigation": "perspective_rotation",
    },
}

LANGUAGE_STRENGTH = {
    "high": {
        "verbs": ["demonstrates", "proves", "establishes", "confirms"],
        "qualifiers": [],
    },
    "strong": {
        "verbs": ["indicates", "shows", "suggests strongly"],
        "qualifiers": ["substantial evidence", "well-documented"],
    },
    "moderate": {
        "verbs": ["suggests", "implies", "may indicate"],
        "qualifiers": ["some evidence", "preliminary findings"],
    },
    "weak": {
        "verbs": ["might suggest", "could indicate", "appears to"],
        "qualifiers": ["limited evidence", "uncertain"],
    },
    "very_weak": {
        "verbs": ["is unclear", "remains uncertain"],
        "qualifiers": ["insufficient evidence", "highly uncertain"],
    },
}

def get_config():
    """Return complete configuration dictionary"""
    return {
        "agents": AGENT_CONFIG,
        "research": RESEARCH_CONFIG,
        "intelligence": INTELLIGENCE_CONFIG,
        "output": OUTPUT_CONFIG,
        "roles": AGENT_ROLES,
        "epistemic": EPISTEMIC_STATUS,
        "credibility": SOURCE_CREDIBILITY,
        "hallucination": HALLUCINATION_INDICATORS,
        "bias": BIAS_PATTERNS,
        "language": LANGUAGE_STRENGTH,
    }
