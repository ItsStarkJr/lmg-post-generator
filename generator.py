from settings import *
from utils import create_text_file, create_file_name, open_json_file


class Generator:
    def __init__(self) -> None:
        self.set_puzzle_data("json_files/test.json")

    def set_puzzle_data(self, file_name):
        data_dict = open_json_file(file_name)
        self.title = data_dict["title"]
        self.intro = data_dict["intro"]
        self.rules = data_dict["rules"]
        self.image_id = data_dict["image_id"]
        self.links = data_dict["links"]

    def create_rules_string(self) -> str:
        rules_string = ""
        for rule in self.rules:
            rules_string += f'<li style="{RESET_WIDTH}">{rule}</li>'
        return rules_string

    def create_links_string(self) -> str:
        links_string = ""
        for index, link in enumerate(self.links.items()):
            if index + 1 < len(self.links):
                links_string += f'<a style="{TEXT_COLOUR};{LINKS_MARGIN}" href="{link[1]}"><b>{link[0].upper()}</b></a>'
            else:
                links_string += f'<a style="{TEXT_COLOUR};" href="{link[1]}"><b>{link[0].upper()}</b></a>'
        return links_string

    def create_page(self) -> None:
        self.script_string = f"""
<div style="text-align:center; background: {BACKGROUND_COLOUR}; padding: 2rem;{SHADOW};margin: 1rem;">
    <div style="text-align:left; background: {TEXT_CONTAINER_BGC}; padding: 1.5rem; {SHADOW}; margin-bottom: 1rem;">
        <p style="{RESET_WIDTH}; {TITLE_COLOUR}; font-size: 1.5rem; margin: 0;"><b>{self.title}</b></p>
        <p style="{RESET_WIDTH}; {TEXT_COLOUR}; margin-top: 0.25rem;"><i>by Wessel Strijkstra</i></p>
        <p style="{RESET_WIDTH}; {TEXT_COLOUR}; margin-bottom: 0;">{self.intro}</p>
    </div>
    <div style="text-align:left; background: {TEXT_CONTAINER_BGC}; padding: 1.5rem; {SHADOW}; margin-bottom: 1rem;">
        <p style="margin-top: 0; {TITLE_COLOUR}"><b>Rules:</b></p>
        <ul style="{TEXT_COLOUR}; margin-bottom: 0">{self.create_rules_string()}</ul>
    </div>
    <div style="display: inline-block; text-align: center; padding: 10px; background: white;{SHADOW};margin-bottom: 1rem;">
        <img:{self.image_id}>
    </div>
    <div style="text-align:left; background: {TEXT_CONTAINER_BGC}; padding: 1.5rem; {SHADOW}; text-align: center;">
        <p style="{RESET_WIDTH}; margin-top: 0;{TITLE_COLOUR};"><b>Solve on:</b></p>
        {self.create_links_string()}
        <p style="{TEXT_COLOUR}; margin-bottom: 0;{RESET_WIDTH}"><b>Enjoy!</b></p>
    </div>
</div>"""

    def run(self) -> None:
        self.create_page()
        create_text_file(self.script_string, create_file_name(self.title))


generator = Generator()
generator.run()
