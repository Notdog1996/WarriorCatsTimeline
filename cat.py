from clan import Clan

class Cat:
    """An individual cat from the Warriors series.
    Args:
        prefix: The cat's prefix. Normally doesn't change.
        suffix: The cat's suffix. The unique one that is given to the cat, not their current one.
        current_name: The cat's name as it appears currently in the timeline.
        other_names: List of all the names the cat has had.
        sex: The cat's sex.
        affiliation: The clan they belong to, or None if they're a loner.
        previous_affiliation: Other affiliations the cat had before.
        rank: Their rank in the clan, if they are in one.
        previous_ranks: The ranks the cat previously had.
        birth: The book in which they were born.
        became_apprentice: The book in which they became an apprentice.
        became_apprentice_medicine: The book in which they became a medicine cat apprentice.
        became_warrior: The book in which they became a warrior.
        became_mentor: The book(s) in which they became a mentor.
        apprentices: The list of apprentices the cat had.
        became_medicine_cat: The book in which they became a medicine cat.
        became_queen: The book(s) in which they became a queen.
        became_elder: The book in which they became an elder.
        became_deputy: The book in which they became a deputy.
        became_leader: The book in which they became a leader.
        death: The book(s) in which they died.
        lifecount: The amount of lives they have left. Only leader have 9 lives.
        double_death: The book in which they died while in the afterlife.
        left_clan: The book in which they left their clan.
        joined_clan: The book in which they joined their clan.
        mentor(s): The cat(s) who had them as an apprentice.
        tree: Their direct family tree, including parents, siblings and children."""

    def __init__(self):
        """Constructing the initial parameters of the Cat class."""
        self.prefix = None
        self.suffix = None
        self.current_name = None
        self.other_names = []
        self.sex = None
        self.affiliation = None
        self.previous_affiliations = []
        self.rank = None
        self.previous_ranks = []
        self.birth = []
        self.became_apprentice = []
        self.became_apprentice_medicine = []
        self.became_warrior = []
        self.became_mentor = []
        self.apprentices = []
        self.became_medicine_cat = []
        self.became_queen = []
        self.became_elder = []
        self.became_deputy = []
        self.became_leader = []
        self.death = []
        self.lifecount = 1
        self.double_death = []
        self.left_clan = []
        self.joined_clan = []
        self.mentors = []
        self.tree = Tree()

class Tree:
    """Family tree for the cats.
    Args:
        mother: The cat's mother
        father: The cat's father
        siblings: The cat's siblings
        children: The cat's children"""

    def __init__(self):
        """Constructing the initial parameters."""
        self.mother = "Unknown"
        self.father = "Unknown"
        self.siblings = []
        self.children = []

    def has_siblings(self):
        return len(self.siblings) > 0

    def is_aunt_uncle(self, cat):
        mother = self.mother
        father = self.father
        if mother.has_siblings():
            if cat in mother.siblings:
                if cat.sex == "Female":
                    return "Aunt"
                else:
                    return "Uncle"
        if father.has_siblings():
            if cat in father.siblings:
                if cat.sex == "Female":
                    return "Aunt"
                else:
                    return "Uncle"
        else:
            return False

    def has_children(self):
        return len(self.children) > 0

    def is_niece_nephew(self, cat):
        siblings = self.siblings
        for sibling in siblings:
            if sibling.has_children():
                if cat in sibling.children:
                    if cat.sex == "Female":
                        return "Niece"
                    else:
                        return "Nephew"
            else:
                return False

    def is_grandparent(self, cat):
        mother = self.mother
        father = self.father
        if mother.mother != "Unknown":
            if mother.mother == cat:
                return "Grandmother"
        if mother.father != "Unknown":
            if mother.father == cat:
                return "Grandfather"
        if father.mother != "Unknown":
            if father.mother == cat:
                return "Grandmother"
        if father.father != "Unknown":
            if father.father == cat:
                return "Grandfather"
        else:
            return False

    def is_cousin(self, cat):
        mother = self.mother
        father = self.father
        if mother.has_siblings():
            for sibling in mother.siblings:
                if sibling.has_children():
                    for child in sibling.children:
                        if child == cat:
                            return "Cousin"
        if father.has_siblings():
            for sibling in father.siblings:
                if sibling.has_children():
                    for child in sibling.children:
                        if child == cat:
                            return "Cousin"
        else:
            return False

    def is_grandchild(self, cat):
        children = self.children
        if self.has_children():
            for child in children:
                if child.has_children():
                    if child.children == cat:
                        if cat.sex == "Female":
                            return "Granddaughter"
                        else:
                            return "Grandson"
        else:
            return False

