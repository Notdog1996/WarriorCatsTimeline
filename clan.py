class Clan:
    """A clan from the warrior series
    Args:
        name: The name of the clan.
        current_members: All the cats currently in the clan.
        current_kittens: All the kittens in the clan.
        current_apprentices: All the apprentices in the clan.
        current_medicine_apprentices: All the medicine cat apprentices in the clan.
        current_warriors: All the warriors in the clan.
        current_medicine_cats: All the medicine cats in the clan.
        current_queens: All the queens in the clan.
        current_elders: All the elders in the clan.
        current_deputy: The current deputy of the clan.
        current_leader: The current leader of the clan.
        previous_members: Cats who were previously members of the clan."""

    def __init__(self):
        """Constructing the initial paremeters of the Clan class."""
        self.name = None
        self.current_members = []
        self.current_kittens = []
        self.current_apprentices = []
        self.current_medicine_apprentices = []
        self.current_warriors = []
        self.current_medicine_cats = []
        self.current_queens = []
        self.current_elders = []
        self.current_deputy = []
        self.current_leader = []
        self.previous_members = []