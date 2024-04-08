from settings import *
from utils import create_text_file, create_file_name, open_json_file
from bs4 import BeautifulSoup



class Generator:
    def __init__(self, json_file) -> None:
        
        self.set_puzzle_data("json_files/test.json")

    def set_puzzle_data(self, file_name):
        self.data_dict = open_json_file(file_name)
        self.title = self.data_dict["title"]
        self.intro = self.data_dict["intro"]
        self.rules = self.data_dict["rules"]
        self.main_image_id = self.data_dict["main_image_id"]
        self.main_links = self.data_dict["main_links"]
        self.example_image_id = self.data_dict["example_image_id"]
        self.example_links = self.data_dict["example_links"]
        self.has_example = self.data_dict["has_example"] 
        if self.has_example:
            self.example_image_id = self.data_dict["example_image_id"]
            self.example_links = self.data_dict["example_links"]


    def create_rules_string(self) -> str:
        rules_string = ""
        for rule in self.rules:
            rules_string += f'<li style="{RESET_WIDTH}">{rule}</li>'
        return rules_string

    def create_links_string(self, links_dict) -> str:
        links_string = ""
        for index, link in enumerate(links_dict.items()):
            if index + 1 < len(links_dict):
                links_string += f'<a style="{TEXT_COLOUR};{LINKS_MARGIN}" href="{link[1]}"><b>{link[0].upper()}</b></a>'
            else:
                links_string += f'<a style="{TEXT_COLOUR};" href="{link[1]}"><b>{link[0].upper()}</b></a>'
        return links_string

    def string_if_has_example(self, text: str):
        if self.has_example:
            return text
        else: return ""

    def clean_up_html(self):
        soup = BeautifulSoup(self.script_string, 'html.parser')
        self.script_string = soup.prettify()

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
    {self.string_if_has_example(f"""
    <div style="text-align:left; background: {TEXT_CONTAINER_BGC}; padding: 1.5rem; {SHADOW}; text-align: center;margin-bottom: 1rem;">
        <p style="max-width: none; margin-top: 0;{TITLE_COLOUR};"><b>Example</b></p>
        <div style="display: inline-block; text-align: center; padding: 10px; background: white;{SHADOW};margin-bottom: 1rem;"><img:{self.example_image_id}></div>
        <p style="{RESET_WIDTH}; margin-top: 0;{TITLE_COLOUR};"><b>Solve example on:</b></p>
        {self.create_links_string(self.example_links)}
    </div>""")}
    <div style="text-align:left; background: {TEXT_CONTAINER_BGC}; padding: 1.5rem; {SHADOW}; text-align: center;">
        {self.string_if_has_example(f"""<p style="max-width: none; margin-top: 0;{TITLE_COLOUR};"><b>Main puzzle</b></p>""")}
        <div style="display: inline-block; text-align: center; padding: 10px; background: white;{SHADOW};margin-bottom: 1rem;"><img:{self.main_image_id}></div>
        <p style="{RESET_WIDTH}; margin-top: 0;{TITLE_COLOUR};"><b>Solve on:</b></p>
        {self.create_links_string(self.main_links)}
        <p style="{TEXT_COLOUR}; margin-bottom: 0;{RESET_WIDTH}"><b>Enjoy!</b></p>
    </div>
</div>"""

    def run(self) -> None:
        self.create_page()
        # self.clean_up_html()
        create_text_file(self.script_string, create_file_name(self.title))


# generator = Generator(True)
# generator.run()
