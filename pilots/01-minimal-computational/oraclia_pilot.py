# Oraclia · Symbolic Self-Insight Engine (Prototype C)
# ----------------------------------------------------
# This prototype shows how Oraclia can operate as a symbolic layer
# that detects internal structural movements inside a user’s input.
# The system is NOT psychological, NOT predictive, NOT emotional.
# It only identifies structural states using a fixed rule-set.

import re

# ------------------------------
# 1. Symbol Mapping (Structural)
# ------------------------------

symbol_map = {
    "uncertainty": {
        "patterns": [r"\bnot sure\b", r"\bdon't know\b", r"\bunsure\b", r"\bconfused\b"],
        "symbol": "?",
        "meaning": "Indeterminacy — the field lacks clear criteria.",
        "suggestion": "Stay with the question. Do not force direction."
    },

    "decision_point": {
        "patterns": [r"\bdecide\b", r"\bchoice\b", r"\bchoose\b"],
        "symbol": "Y",
        "meaning": "Bifurcation — a decision between multiple paths.",
        "suggestion": "Identify the minimum criteria before choosing."
    },

    "tension": {
        "patterns": [r"\bstuck\b", r"\bblocked\b", r"\bpressure\b"],
        "symbol": "⊘",
        "meaning": "Interruption — movement cannot continue as is.",
        "suggestion": "Pause the movement. Let the structure reorganize."
    },

    "focus": {
        "patterns": [r"\bneed to understand\b", r"\btrying to see\b", r"\bclarify\b"],
        "symbol": "◉",
        "meaning": "Focus — attention narrows onto a relevant element.",
        "suggestion": "Observe without acting. Identify the core point."
    },

    "change": {
        "patterns": [r"\bchanging\b", r"\bshift\b", r"\btransform\b"],
        "symbol": "∆",
        "meaning": "Transformation — the configuration is altering.",
        "suggestion": "Let the transition complete before redefining direction."
    },

    "limit": {
        "patterns": [r"\bcan't\b", r"\bimpossible\b", r"\brestriction\b"],
        "symbol": "†",
        "meaning": "Limit — a boundary becomes visible.",
        "suggestion": "Locate the exact point of constraint."
    },

    "movement": {
        "patterns": [r"\bstart\b", r"\bmove forward\b", r"\bprogress\b"],
        "symbol": "→",
        "meaning": "Direction — initial operative movement.",
        "suggestion": "Proceed with minimal steps, not conclusions."
    },

    "integration": {
        "patterns": [r"\bfeels coherent\b", r"\bthings align\b", r"\bcomes together\b"],
        "symbol": "≡",
        "meaning": "Integration — elements begin to fit into structure.",
        "suggestion": "Stabilize the configuration before adding new action."
    }
}

# ---------------------------------------
# 2. Processing Function (Structural Scan)
# ---------------------------------------

def oraclia_read(text):
    text = text.lower()
    
    for key, data in symbol_map.items():
        for pattern in data["patterns"]:
            if re.search(pattern, text):
                return {
                    "symbol": data["symbol"],
                    "meaning": data["meaning"],
                    "suggestion": data["suggestion"]
                }
    
    return {
        "symbol": "◌",
        "meaning": "No structural signal detected.",
        "suggestion": "Provide a more specific internal movement."
    }

# -------------------------
# 3. Simple Console Runner
# -------------------------

if __name__ == "__main__":
    print("Oraclia · Symbolic Self-Insight Prototype")
    print("-----------------------------------------")
    user_input = input("Describe your internal movement or situation:\n> ")

    result = oraclia_read(user_input)

    print("\nSymbol:", result["symbol"])
    print("Meaning:", result["meaning"])
    print("Structural suggestion:", result["suggestion"])
