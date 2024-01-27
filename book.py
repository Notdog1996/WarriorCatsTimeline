from cat import Cat
from clan import Clan


class Book:
    """A book in the Warriors series.
    Args:
        title: The title of the book.
        series: The series the book belongs to.
        series_order: Its order in the series.
        previous_in_series: The book before it in the series.
        next_in_series: The book after it in the series.
        publishing_order: Its order in publishing.
        previous_publishing_order: The book before it in publishing order.
        next_publishing_order: The book after it in publishing order.
        chronological_order: Its order in the chronology.
        previous_chronological_order: The book before it in chronological order.
        next_chronological_order: The book after it in chronological order.
        appearances: List of cats who appear in the book.
        births: Kittens born in the book.
        new_apprentices: Cats who became apprentices in the book.
        new_medicine_apprentices: Cats who became medicine cat apprentices.
        new_mentors: Cats who became
        new_warriors: Cats who became warriors in the book.
        new_medicine_cats: Cats who became medicine cats in the book.
        new_queens: Cats who became queens in the book.
        new_elders: Cats who became elders in the book.
        new_deputies: Cats who became deputies in the book.
        new_leaders: Cats who became leaders in the book.
        deaths: Cats who died in the book.
        double_deaths: Cats who died in the afterlife in the book.
        left_clan: Cats who left their clans in the book.
        joined_clan: Cats who joined their clans in the book.
        """

    def __init__(self):
        self.title = None
        self.series = None
        self.series_order = 0
        self.previous_in_series = None
        self.next_in_series = None
        self.publishing_order = 0
        self.previous_publishing_order = None
        self.next_publishing_order = None
        self.chronological_order = 0
        self.previous_chronological_order = None
        self.next_chronological_order = None
        self.appearances = []
        self.births = []
        self.new_apprentices = []
        self.new_medicine_apprentices = []
        self.new_mentors = []
        self.new_warriors = []
        self.new_medicine_cats = []
        self.new_queens = []
        self.new_elders = []
        self.new_deputies = []
        self.new_leaders = []
        self.deaths = []
        self.double_deaths = []
        self.left_clan = []
        self.joined_clan = []

    def is_born(self, cat):
        mother = cat.mother
        father = cat.father
        clan = cat.affiliation
        cat.rank = "Kitten"
        self.births.append(cat)
        cat.birth = self.title
        if mother != "Unknown":
            mother.children.append(cat)
        if father != "Unknown":
            father.children.append(cat)
        if isinstance(clan, Clan):
            clan.current_members.append(cat)
            clan.current_kittens.append(cat)
            if clan == Wind_Clan:
                cat.current_name = cat.prefix + "kit"
            if clan == Thunder_Clan:
                cat.current_name = cat.prefix + "kit"
            if clan == River_Clan:
                cat.current_name = cat.prefix + "kit"
            if clan == Shadow_Clan:
                cat.current_name = cat.prefix + "kit"


    def becomes_apprentice(self, cat1, cat2):
        """Function to become an apprentice. The arguments are cat1 (the apprentice) and cat2 (the mentor)"""
        clan = cat1.affiliation
        if isinstance(clan, Clan):
            if cat1 in clan.current_kittens:
                clan.current_kittens.remove(cat1)
            if cat1 in clan.current_medicine_apprentices:
                clan.current_medicine_apprentices.remove(cat1)
        cat1.other_names.append(cat1.current_name)
        cat1.current_name = cat1.prefix + "paw"
        self.new_apprentices.append(cat1)
        cat1.mentors.append(cat2)
        cat1.previous_ranks.append(cat1.rank)
        cat1.rank = "Apprentice"
        cat1.became_apprentice.append(self.title)
        if isinstance(clan, Clan):
            clan.current_apprentices.append(cat1)

    def becomes_med_apprentice(self, cat1, cat2):
        """Function to become an apprentice. The arguments are cat1 (the apprentice) and cat2 (the mentor)"""
        clan = cat1.affiliation
        if isinstance(clan, Clan):
            if cat1 in clan.current_kittens:
                clan.current_kittens.remove(cat1)
            if cat1 in clan.current_apprentices:
                clan.current_apprentices.remove(cat1)
        cat1.other_names.append(cat1.current_name)
        cat1.current_name = cat1.prefix + "paw"
        self.new_medicine_apprentices.append(cat1)
        cat1.mentors.append(cat2)
        cat1.previous_ranks.append(cat1.rank)
        cat1.rank = "Medicine Apprentice"
        cat1.became_apprentice_medicine.append(self.title)
        if isinstance(clan, Clan):
            clan.current_medicine_apprentices.append(cat1)

    def becomes_mentor(self, cat1, cat2):
        """Function to become a mentor. The arguments are cat1 (the mentor) and cat2 (the apprentice)."""
        self.new_mentors.append(cat1)
        cat1.apprentices.append(cat2)
        cat1.became_mentor.append(self.title)

    def becomes_warrior(self, cat):
        clan = cat.affiliation
        if isinstance(clan, Clan):
            if cat.current_name in clan.current_apprentices:
                clan.current_apprentices.remove(cat)
            if cat.current_name in clan.current_medicine_cats:
                clan.current_medicine_cats.remove(cat)
        cat.other_names.append(cat.current_name)
        cat.current_name = cat.prefix + cat.suffix
        self.new_warriors.append(cat)
        cat.previous_ranks.append(cat.rank)
        cat.rank = "Warrior"
        cat.became_warrior.append(self.title)
        if isinstance(clan, Clan):
            clan.current_warriors.append(cat)

    def becomes_medicine_cat(self, cat):
        """When a cat becomes the clan's medicine cat."""
        clan = cat.affiliation
        if isinstance(clan, Clan):
            if cat in clan.current_medicine_apprentices:
                clan.current_medicine_apprentices.remove(cat)
            if cat in clan.current_warriors:
                clan.current_warriors.remove(cat)
        cat.other_names.append(cat.current_name)
        cat.current_name = cat.prefix + cat.suffix
        self.new_medicine_cats.append(cat)
        cat.previous_ranks.append(cat.rank)
        cat.rank = "Medicine Cat"
        cat.became_medicine_cat.append(self.title)
        if isinstance(cat.affiliation, Clan):
            clan.current_medicine_cats.append(cat)

    def becomes_queen(self, cat):
        """When a pregnant cat moves into the nursery."""
        clan = cat.affiliation
        if isinstance(clan, Clan):
            if cat in clan.current_warriors:
                clan.current_warriors.remove(cat)
            clan.current_queens.append(cat)
        cat.previous_ranks.append(cat.rank)
        cat.rank = "Queen"
        self.new_queens.append(cat)
        cat.became_queen.append(self.title)

    def becomes_elder(self, cat):
        """When an old cat retires."""
        clan = cat.affiliation
        if isinstance(clan, Clan):
            if cat in clan.current_warriors:
                clan.current_warriors.remove(cat)
            if cat in clan.current_medicine_cats:
                clan.current_medicine_cats.remove(cat)
            if cat in clan.current_queens:
                clan.current_queens.remove(cat)
            clan.current_elders.append(cat)
        cat.previous_ranks.append(cat.rank)
        cat.rank = "Elder"
        self.new_elders.append(cat)
        cat.became_elder.append(self.title)


    def becomes_deputy(self, cat):
        """When a cat becomes the clan deputy."""
        clan = cat.affiliation
        if isinstance(clan, Clan):
            if cat in clan.current_warriors:
                clan.current_warriors.remove(cat)
            if cat in clan.current_queens:
                clan.current_queens.remove(cat)
            clan.current_deputy = cat
        cat.previous_ranks.append(cat.rank)
        cat.rank = "Deputy"
        self.new_deputies.append(cat)
        cat.became_deputy.append(self.title)

    def becomes_leader(self, cat):
        """When a cat becomes the clan leader. They also get nine lives and their star suffix."""
        clan = cat.affiliation
        if isinstance(cat.affiliation, Clan):
            if cat in clan.current_deputy:
                clan.current_deputy.remove(cat)
            if cat in clan.current_queens:
                clan.current_queens.remove(cat)
            cat.other_names.append(cat.current_name)
            cat.current_name = cat.prefix + "star"
            cat.lifecount = 9
        cat.previous_ranks.append(cat.rank)
        cat.rank = "Leader"
        clan.current_leader = cat
        self.new_leaders.append(cat)
        cat.became_leader.append(self.title)

    def dies(self, cat):
        """When a cat dies in the book. If this was their final life, their rank is reset and they are removed from their clan's member list."""
        cat.lifecount = cat.lifecount - 1
        if cat.lifecount == 0:
            cat.previous_affiliations.append(cat.affiliation)
            if isinstance(cat.affiliation, Clan):
                clan = cat.affiliation
                clan.current_members.remove(cat)
                clan.previous_members.append(cat)
                if cat in clan.current_kittens:
                    clan.current_kittens.remove(cat)
                if cat in clan.current_apprentices:
                    clan.current_apprentices.remove(cat)
                if cat in clan.current_medicine_apprentices:
                    clan.current_apprentices.remove(cat)
                if cat in clan.current_warriors:
                    clan.current_warriors.remove(cat)
                if cat in clan.current_medicine_cats:
                    clan.current_medicine_cats.remove(cat)
                if cat in clan.current_queens:
                    clan.current_queens.remove(cat)
                if cat in clan.current_elders:
                    clan.current_elders.remove(cat)
                if cat in clan.current_deputy:
                    clan.current_deputy.remove(cat)
                if cat in clan.current_leader:
                    clan.current_leader.remove(cat)
                cat.affiliation = None
            else:
                cat.affiliation = None
            cat.previous_ranks.append(cat.rank)
            cat.rank = None
        self.deaths.append(cat.current_name)
        cat.death.append(self.title)

    def double_dies(self, cat):
        """When a cat dies in the afterlife."""
        cat.previous_affiliations.append(cat.affiliation)
        clan = cat.affiliation
        if isinstance(clan, Clan):
            clan.current_members.remove(cat)
            clan.previous_members.append(cat)
            clan = None
        cat.double_death = self.title
        self.double_deaths.append(cat)

    def leaves_clan(self, cat):
        """When a cat leaves the clan in the book. They lose their rank and affiliation."""
        cat.previous_affiliations.append(cat.affiliation)
        clan = cat.affiliation
        if isinstance(clan, Clan):
            clan.current_members.remove(cat)
            clan.previous_members.append(cat)
            clan = None
        cat.left_clan.append(self.title)
        self.left_clan.append(cat)

    def joins_clan(self, cat, clan, rank):
        """When a cat joins a clan. Takes the cat and the rank they join into as arguments."""
        cat.previous_affiliations.append(cat.affiliation)
        clan.current_members.append(cat)
        cat.joined_clan.append(self.title)
        self.joined_clan.append(cat)
        if rank == "Kitten":
            clan.current_kittens.append(cat)
        if rank == "Apprentice":
            clan.current_apprentices.append(cat)
        if rank == "Medicine Apprentice":
            clan.current_medicine_apprentices.append(cat)
        if rank == "Warrior":
            clan.current_warriors.append(cat)
        if rank == "Medicine Cat":
            clan.current_medicine_cats.append(cat)
        if rank == "Queen":
            clan.current_queens.append(cat)
        if rank == "Elder":
            clan.current_elders.append(cat)
        if rank == "Deputy":
            clan.current_deputy = cat
        if rank == "Leader":
            clan.current_leader = cat

    def changes_name(self, cat, old_name, new_name):
        """When a cat changes names outside of a main ceremony, like becoming a leader an getting nine lives from StarClan.
        args:
        cat: the cat.
        old_name: the name they currently had up to that point.
        new_name: the new name they'll have."""
        cat.other_names.append(old_name)
        cat.current_name = new_name

    def kills(self, cat1, cat2):
        """When a cat kills another cat.
        args:
        cat1: The cat who killed the other.
        cat2: The cat who has been killed."""
        self.dies(cat2)
        cat1.killcount = cat1.killcount + 1
        cat1.kills.append(cat2)

    def double_kills(self, cat1, cat2):
        """When a cat kills a spirit-cat.
        args:
        cat1: The cat who killed the other.
        cat2: The cat who has been killed."""
        self.double_dies(cat2)
        cat1.killcount = cat1.killcount + 1
        cat1.kills.append(cat2)


