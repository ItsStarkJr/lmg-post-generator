from settings import *
from utils import create_text_file, create_file_name


class Generator:
    def __init__(self) -> None:
        self.title = "Castle Woku (Castle Wall/Sudoku)"
        self.intro = "After my Yajilin sudoku, I thought I'd try another loop hybrid with the same outside clueing. I tried to make the loop building interact with those clues a bit more this time. Let me know what you think:)"
        self.rules = [
            "Normal sudoku rules apply.",
            "Castle wall rules: Draw a non-intersecting loop through the centers of some cells. The loop may not enter outlined cells or cells containing clues. White squares must lie inside the loop, while black squares must lie outside the loop. Grey cells may either be inside or outside the loop. A number represents the sum of the lengths of loop segments in the indicated direction.",
            "Directions and values of all castle wall clues have to be determined, if not given. Clues see their amount of loop segments in at least one direction.",
            "A clue outside a row gives the sum of the digits on the first horizontal segment passing through its row (including the cells which it turns), likewise for columns and vertical segments.",
        ]
        self.image_id = "000GJX"
        self.links = {
            "sudokupad": "https://tinyurl.com/2us8mysw",
            "f-puzzles": "https://f-puzzles.com/?id=2pwhzaqm",
        }

    def create_rules_string(self) -> str:
        rules_string = ""
        for rule in self.rules:
            rules_string += f'<li style="{RESET_WIDTH}">{rule}</li>'
        return rules_string

    def create_links_string(self) -> str:
        links_string = ""
        for index, link in enumerate(self.links.items()):
            if index + 1 < len(self.links):
                links_string += f'<a style="{TEXT_COLOUR};{LINKS_MARGIN}" href="{link[1]}"><b>{link[0].capitalize()}</b></a>'
            else:
                links_string += f'<a style="{TEXT_COLOUR};" href="{link[1]}"><b>{link[0].capitalize()}</b></a>'
        return links_string

    def create_page(self) -> None:
        self.script_string = f"""
<div style="background: {BACKGROUND_COLOUR}; padding: 2rem;{SHADOW};margin: 1rem;">
    <div style="background: {TEXT_CONTAINER_BGC}; padding: 1.5rem; {SHADOW}; margin-bottom: 1rem;">
        <p style="{RESET_WIDTH}; {TITLE_COLOUR}; font-size: 1.5rem; margin: 0;"><b>{self.title}</b></p>
        <p style="{RESET_WIDTH}; {TEXT_COLOUR}; margin-top: 0.25rem;"><i>by Wessel Strijkstra</i></p>
        <p style="{RESET_WIDTH}; {TEXT_COLOUR}; margin-bottom: 0;">{self.intro}</p>
    </div>
    <div style="background: {TEXT_CONTAINER_BGC}; padding: 1.5rem; {SHADOW}; margin-bottom: 1rem;">
        <p style="margin-top: 0; {TITLE_COLOUR}"><b>Rules:</b></p>
        <ul style="{TEXT_COLOUR}; margin-bottom: 0">{self.create_rules_string()}</ul>
    </div>
    <div style="text-align: center; padding: 10px; width: 90%; margin: auto; background: white;{SHADOW};margin-bottom: 1rem;">
        <img:{self.image_id}>
    </div>
    <div style="background: {TEXT_CONTAINER_BGC}; padding: 1.5rem; {SHADOW}; text-align: center;">
        <p style="{RESET_WIDTH}; margin-top: 0;{TEXT_COLOUR};"><b>Solve on:</b></p>
        {self.create_links_string()}
        <p style="{TEXT_COLOUR}; margin-bottom: 0;{RESET_WIDTH}"><b>Enjoy!</b></p>
    </div>
</div>"""

    def run(self) -> None:
        self.create_page()
        create_text_file(self.script_string, create_file_name(self.title))


generator = Generator()
generator.run()
