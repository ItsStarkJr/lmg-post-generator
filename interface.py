from tkinter import *
from webpage_generator import WebpageGenerator

import customtkinter
from utils import write_to_json_file, open_json_file, sort_scripts_data_by_website


class AddScript:
    def __init__(self) -> None:
        self.widget_background_colour = "#101010"
        self.app_setup()
        self.new_script_data = {}

    def app_setup(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.root = customtkinter.CTk()
        self.root.geometry("1280x1180+300+100")
        self.root.title("Add Script")
        self.root.bind("<Escape>", self.close_app)

        self.frame_1 = customtkinter.CTkFrame(master=self.root)
        self.frame_1.pack(pady=20, padx=60, fill="both", expand=True)

        self.label_1 = customtkinter.CTkLabel(
            master=self.frame_1,
            justify=customtkinter.LEFT,
            text="Enter initial gist link, conversion to raw will be done.",
            text_color="grey",
        )
        self.label_1.pack(pady=10, padx=10)

        # Title frame

        self.title_frame = customtkinter.CTkFrame(self.frame_1)
        self.title_frame.pack(pady=10)

        self.title_entry = customtkinter.CTkEntry(
            master=self.title_frame,
            placeholder_text="Title",
            width=475,
            fg_color=self.widget_background_colour,
            corner_radius=0,
            border_width=0,
            height=40,
        )

        self.filename_entry = customtkinter.CTkEntry(
            master=self.title_frame,
            placeholder_text="File name",
            width=475,
            fg_color=self.widget_background_colour,
            corner_radius=0,
            height=40,
            border_width=0,
        )

        self.gist_link_entry = customtkinter.CTkEntry(
            master=self.title_frame,
            placeholder_text="Gist link",
            width=475,
            fg_color=self.widget_background_colour,
            corner_radius=0,
            height=40,
            border_width=0,
        )

        self.website_entry = customtkinter.CTkEntry(
            master=self.title_frame,
            placeholder_text="Website it works on",
            width=475,
            fg_color=self.widget_background_colour,
            corner_radius=0,
            height=40,
            border_width=0,
        )

        self.description_label = customtkinter.CTkLabel(
            master=self.title_frame,
            text="Description (case sensitive):",
            text_color="grey",
        )

        self.description_box = customtkinter.CTkTextbox(
            master=self.title_frame,
            width=1020,
            height=150,
            fg_color=self.widget_background_colour,
            corner_radius=0,
        )

        self.title_entry.grid(row=0, column=0, padx=10, pady=10)
        self.filename_entry.grid(row=0, column=1, padx=10, pady=10)
        self.gist_link_entry.grid(row=1, column=0, padx=10, pady=10)
        self.website_entry.grid(row=1, column=1, padx=10, pady=10)
        self.description_label.grid(row=2, column=0, padx=10)
        self.description_box.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

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

    def get_title(self):
        self.title = self.title_entry.get().strip()
        self.new_script_data["title"] = self.title

    def get_filename(self):
        self.filename = self.filename_entry.get().strip()

    def get_gist_link(self):
        self.gist_link = self.gist_link_entry.get().strip()

    def get_website(self):
        self.new_script_data["website"] = self.website_entry.get().strip()

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
        sort_scripts_data_by_website()
        webpage_generator = WebpageGenerator()
        webpage_generator.run()

    def close_app(self, event=None):
        self.root.destroy()

    def run(self):
        self.root.mainloop()


awesome_script_adder = AddScript()
awesome_script_adder.run()
