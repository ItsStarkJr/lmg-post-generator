from tkinter import *
from generator import Generator
import json

import customtkinter
from utils import write_to_json_file, open_json_file


class AddScript:
    def __init__(self) -> None:
        self.widget_background_colour = "#101010"
        self.get_user_settings()
        self.app_setup()
        self.new_script_data = {}

    # User settings

    def get_user_settings(self):
        try:
            with open("user_settings.json", "r") as file:
                file_content = json.load(file)
                self.author = file_content["author"]
                self.profile_link = file_content["profile_link"]
        except:
            print("Something went wrong.")

    def set_author_placeholder(self):
        if self.author != "":
            return self.author
        else:
            return "Author"

    def set_profile_link_placeholder(self):
        if self.profile_link != "":
            return self.profile_link
        else:
            return "LMG profile link"

    def update_user_settings(self):
        user_settings = {}
        user_settings["author"] = self.author_entry.get().strip()
        user_settings["profile_link"] = self.profile_link_entry.get().strip()
        write_to_json_file(user_settings, "user_settings.json")

    # App setup

    def app_setup(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.root = customtkinter.CTk()
        self.root.geometry("1280x1180+300+100")
        self.root.title("Add Script")
        self.root.bind("<Escape>", self.close_app)

        self.frame_1 = customtkinter.CTkFrame(master=self.root)
        self.frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        self.setup_author_frame()
        self.setup_main_puzzle_frame()
        self.setup_example_puzzle_frame()

    def setup_author_frame(self):
        # Author settings
        self.author_frame = customtkinter.CTkFrame(self.frame_1)
        self.author_frame.pack(pady=10)

        self.author_label = customtkinter.CTkLabel(
            master=self.author_frame,
            text="Author settings",
            text_color="grey",
        )

        self.author_entry = customtkinter.CTkEntry(
            master=self.author_frame,
            placeholder_text=self.set_author_placeholder(),
            width=300,
            fg_color=self.widget_background_colour,
            corner_radius=0,
            border_width=0,
            height=40,
        )

        self.profile_link_entry = customtkinter.CTkEntry(
            master=self.author_frame,
            placeholder_text=self.set_profile_link_placeholder(),
            width=300,
            fg_color=self.widget_background_colour,
            corner_radius=0,
            border_width=0,
            height=40,
        )

        self.update_user_settings_button = customtkinter.CTkButton(
            master=self.author_frame,
            command=self.update_user_settings,
            text="Update author settings",
            corner_radius=0,
            fg_color="#252525",
            hover_color="#404040",
            width=300,
            height=40,
        )

        self.author_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.author_entry.grid(row=1, column=0, padx=10, pady=10)
        self.profile_link_entry.grid(row=1, column=1, padx=10, pady=10)
        self.update_user_settings_button.grid(row=1, column=2, padx=10, pady=10)

    def setup_main_puzzle_frame(self):
        # Title frame

        self.main_puzzle_frame = customtkinter.CTkFrame(self.frame_1)
        self.main_puzzle_frame.pack(pady=10)

        self.title_entry = customtkinter.CTkEntry(
            master=self.main_puzzle_frame,
            placeholder_text="Title",
            width=475,
            fg_color=self.widget_background_colour,
            corner_radius=0,
            border_width=0,
            height=40,
        )

        self.main_image_id_entry = customtkinter.CTkEntry(
            master=self.main_puzzle_frame,
            placeholder_text="Image ID",
            width=475,
            fg_color=self.widget_background_colour,
            corner_radius=0,
            height=40,
            border_width=0,
        )

        self.description_label = customtkinter.CTkLabel(
            master=self.main_puzzle_frame,
            text="Intro (case sensitive):",
            text_color="grey",
        )

        self.description_box = customtkinter.CTkTextbox(
            master=self.main_puzzle_frame,
            width=1020,
            height=100,
            fg_color=self.widget_background_colour,
            corner_radius=0,
        )

        self.rules_label = customtkinter.CTkLabel(
            master=self.main_puzzle_frame,
            text="Rules (case sensitive):",
            text_color="grey",
        )

        self.rules_box = customtkinter.CTkTextbox(
            master=self.main_puzzle_frame,
            width=1020,
            height=150,
            fg_color=self.widget_background_colour,
            corner_radius=0,
        )

        self.links_label = customtkinter.CTkLabel(
            master=self.main_puzzle_frame,
            text="Links (case sensitive):",
            text_color="grey",
        )

        self.links_box = customtkinter.CTkTextbox(
            master=self.main_puzzle_frame,
            width=1020,
            height=75,
            fg_color=self.widget_background_colour,
            corner_radius=0,
        )

        self.title_entry.grid(row=0, column=0, padx=10, pady=10)
        self.main_image_id_entry.grid(row=0, column=1, padx=10, pady=10)
        self.description_label.grid(
            row=2, column=0, columnspan=2, padx=10, pady=(10, 0)
        )
        self.description_box.grid(row=3, column=0, columnspan=2, padx=10)
        self.rules_label.grid(row=4, column=0, columnspan=2, padx=10, pady=(10, 0))
        self.rules_box.grid(row=5, column=0, columnspan=2, padx=10)
        self.links_label.grid(row=6, column=0, columnspan=2, padx=10, pady=(10, 0))
        self.links_box.grid(row=7, column=0, columnspan=2, padx=10)

        self.buttons_frame = customtkinter.CTkFrame(self.frame_1)
        self.buttons_frame.pack(pady=10)

        # Buttons

        self.submit_button = customtkinter.CTkButton(
            master=self.buttons_frame,
            command=self.submit,
            text="Submit",
            corner_radius=0,
            fg_color="#252525",
            hover_color="#404040",
        )

        self.update_html_button = customtkinter.CTkButton(
            master=self.buttons_frame,
            command=self.update_html,
            text="Update HTML",
            corner_radius=0,
            fg_color="#252525",
            hover_color="#404040",
        )

        self.submit_button.grid(row=0, column=0, padx=10, pady=10)
        self.update_html_button.grid(row=0, column=1, padx=10, pady=10)

    def setup_example_puzzle_frame(self):
        pass

    def get_title(self):
        self.title = self.title_entry.get().strip()
        self.new_script_data["title"] = self.title

    def get_filename(self):
        self.filename = self.main_image_id_entry.get().strip()

    def get_description(self):
        self.new_script_data["description"] = self.description_box.get(
            0.0, "end"
        ).strip()

    def create_raw_gist_link(self):
        self.gist_link_raw = f"{self.gist_link}/raw/{self.filename}"
        self.new_script_data["link"] = self.gist_link_raw

    def append_new_data(self):
        self.scripts_data.append(self.new_script_data)

    def get_data(self):
        self.get_title()
        self.get_filename()
        self.get_gist_link()
        self.get_website()
        self.get_description()
        self.create_raw_gist_link()
        self.append_new_data()

    def submit(self):
        self.scripts_data = open_json_file("scripts_data.json")
        self.get_data()
        write_to_json_file(self.scripts_data, "scripts_data.json")

    def update_html(self):
        webpage_generator = Generator()
        webpage_generator.run()

    def close_app(self, event=None):
        self.root.destroy()

    def run(self):
        self.root.mainloop()


awesome_script_adder = AddScript()
awesome_script_adder.run()
