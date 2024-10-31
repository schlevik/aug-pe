import random

def get_prompt(prompt, ds_name):
    if ds_name == 'psytar':
        return get_psytar_prompt(prompt)
    elif ds_name == 'hallmarks_of_cancer':
        return get_hoc_prompt(prompt)
    raise NotImplementedError()

def get_psytar_prompt(prompt):
    labels = prompt.split("|")
    styles = """Chronic patient
New parent
Senior reviewer
Allergy sufferer
Prescription user
Healthcare professional
Migraine patient
Fitness enthusiast
Mental health patient
Insomnia sufferer""".splitlines()

    label_map = {
        "ADR": "Adverse Drug Reaction",
        "DI": "Drug Indications",
        "EF": "Drug Effectiveness",
        "INF": "Drug Ineffeciveness",
        "Others": "Others",
        "SSI": "Sign/Symptoms/Illness",
        "WD": "Withdrowal Symptoms"
    }
    style = random.choice(styles)
    return f"Suppose you're a {style}. Write a one-sentence medication review that mentions the following adverse drug reactions: {', '.join(label_map.get(l, 'No reactions.') for l in labels)}"



def get_hoc_prompt(prompt):
    labels = prompt.split("|")
    styles = """Cell Biologist
Immunologist
Molecular Geneticist
Metabolic Scientist
Vascular Biologist
Evolutionary Biologist
Systems Biologist
Epigeneticist
Tissue Engineer
Biochemist""".splitlines()

    label_map = [
        "activating invasion and metastasis",
        "avoiding immune destruction",
        "cellular energetics",
        "enabling replicative immortality",
        "evading growth suppressors",
        "genomic instability and mutation",
        "inducing angiogenesis",
        "resisting cell death",
        "sustaining proliferative signaling",
        "tumor promoting inflammation"
    ]
    label_map = {l:l for l in label_map}
    style = random.choice(styles)
    return f"Suppose you're a {style} writing a scientific paper about hallmarks of cancer. Write one sentence from your papers' abstract, that mentions the following hallmark(s): {', '.join(label_map.get(l, 'No hallmark.') for l in labels)}"
