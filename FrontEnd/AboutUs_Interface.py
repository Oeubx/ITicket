
import customtkinter as ctk
import os
from PIL import Image

def get_aboutUs():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "Assets", "AboutUs_Images", "AboutUs.jpeg")

    aboutUs_Img = ctk.CTkImage(Image.open(icon_path), size=(600, 450))
    return aboutUs_Img

def get_aboutRemo():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "Assets", "AboutUs_Images", "AboutRemo.png")

    aboutRemo_Img = ctk.CTkImage(Image.open(icon_path), size=(252, 450))
    return aboutRemo_Img

def get_imagePlaceholder():
    current_dir = os.path.dirname(__file__)
    icon_path = os.path.join(current_dir, "..", "Assets", "AboutUs_Images", "placeholderImage.jpg")

    placeholder_Img = ctk.CTkImage(Image.open(icon_path), size=(252, 450))
    return placeholder_Img

def load_AboutUs():
    aboutUs_Window = ctk.CTkToplevel()
    aboutUs_Window.title("About Us")
    aboutUs_Window.grab_set()

    aboutUs_Frame = ctk.CTkScrollableFrame(
        aboutUs_Window,
        fg_color = "#87CEEB",
        scrollbar_fg_color="#b8f3fa",
        scrollbar_button_color="#0097b2"
        )
    aboutUs_Frame.pack(fill="both", expand=True)

    header_Frame = ctk.CTkFrame(
        aboutUs_Frame,
        fg_color = "#87CEEB"
    )
    header_Frame.pack(side="top", padx=25, pady=15)

    header_Text = ctk.CTkLabel(
        header_Frame,
        text="About Group 6 of BSIT 2-1",
        text_color="#000000",
        font=("Arial", 50, "bold"),
        bg_color= "#87CEEB",
    )
    header_Text.pack(side="top")

    us_Frame = ctk.CTkFrame(
        aboutUs_Frame,
        fg_color = "#87CEEB"
    )
    us_Frame.pack(side="top", fill="x", padx=25, pady=(0, 25))

    aboutUs_Image = get_aboutUs()

    aboutUs_ImageLabel = ctk.CTkLabel(
        us_Frame,
        image=aboutUs_Image,
        text=""
    )
    aboutUs_ImageLabel.pack(pady=(0, 5))

    # short description text label
    aboutUs_TextLabel = ctk.CTkLabel(
        us_Frame,
        text="Remo | Ulgasan | Piolen | Esquivel",
        justify="center",
        text_color="#000000",
        font=("Arial", 25, "bold"),
        bg_color= "#87CEEB",
    )
    aboutUs_TextLabel.pack()

    #Contents of aboutUs frame

    # --------------------------------------------------------- #
    # remo frame
    # --------------------------------------------------------- #
    remoFrame = ctk.CTkFrame(
        aboutUs_Frame,
        fg_color = "#87CEEB"
        )
    remoFrame.pack(side="top", padx=250, pady=(0,25))

    aboutRemo_Image = get_aboutRemo()
    
    remo_ImageLabel = ctk.CTkLabel(
        remoFrame,
        image=aboutRemo_Image,
        text=""
    )
    remo_ImageLabel.pack(side="left")

    remo_DetailsFrame = ctk.CTkFrame(
        remoFrame,
        fg_color = "#87CEEB"
    )
    remo_DetailsFrame.pack(side="left", padx=25)

    remoContribution = ctk.CTkLabel(
        remo_DetailsFrame,
        text="Leader | Fullstack Developer",
        text_color="#000000"
    )
    remoContribution.pack(side="top", anchor="w")

    remoName = ctk.CTkLabel(
        remo_DetailsFrame,
        text="Prince Amorsolo C. Remo",
        text_color="#000000"
    )
    remoName.pack(side="top", anchor="w")

    remoDivider1 = ctk.CTkFrame(
        remo_DetailsFrame,        
        height=2,
        fg_color="#cfcfcf"
    )
    remoDivider1.pack(side="top", fill="x")

    remoGithubLink = ctk.CTkLabel(
        remo_DetailsFrame,
        text="https://github.com/Oeubx",
        text_color="#000000"
    )
    remoGithubLink.pack(side="top", anchor="w", pady=(0,5))

    remoFacebookLink = ctk.CTkLabel(
        remo_DetailsFrame,
        text="https://www.facebook.com/oeubxwaa",
        text_color="#000000"
    )
    remoFacebookLink.pack(side="top", anchor="w", pady=(0,5))

    remoXLink = ctk.CTkLabel(
        remo_DetailsFrame,
        text="https://x.com/AmorsoloRemo",
        text_color="#000000"
    )
    remoXLink.pack(side="top", anchor="w", pady=(0,5))

    remoDivider2 = ctk.CTkFrame(
        remo_DetailsFrame,        
        height=2,
        fg_color="#cfcfcf"
    )
    remoDivider2.pack(side="top", fill="x")

    remoBio1 = ctk.CTkLabel(
        remo_DetailsFrame,
        text="Im an introverted dude. I love the kpop group NMIXX.",
        text_color="#000000"
    )
    remoBio1.pack(side="top", anchor="w")

    remoDivider3 = ctk.CTkFrame(
        remo_DetailsFrame,        
        height=2,
        fg_color="#cfcfcf"
    )
    remoDivider3.pack(side="top", fill="x")
    # --------------------------------------------------------- #
    # end of remo frame
    # --------------------------------------------------------- #

    # --------------------------------------------------------- #
    # ulgasan frame
    # --------------------------------------------------------- #
    ulgasanFrame = ctk.CTkFrame(
        aboutUs_Frame,
        fg_color = "#87CEEB"
    )
    ulgasanFrame.pack(side="top", padx=250, pady=(0,25))

    aboutUlgasan_Image = get_imagePlaceholder()

    ulgasan_ImageLabel = ctk.CTkLabel(
        ulgasanFrame,
        image=aboutUlgasan_Image,
        text=""
    )
    ulgasan_ImageLabel.pack(side="left")

    ulgasan_DetailsFrame = ctk.CTkFrame(
        ulgasanFrame,
        fg_color = "#87CEEB"
    )
    ulgasan_DetailsFrame.pack(side="left", padx=25)

    ulgasanContribution = ctk.CTkLabel(
        ulgasan_DetailsFrame,
        text="Member | Frontend Designer",
        text_color="#000000"
    )
    ulgasanContribution.pack(side="top", anchor="w")

    ulgasanName = ctk.CTkLabel(
        ulgasan_DetailsFrame,
        text="Baby Claire ?. Ulgasan",
        text_color="#000000"
    )
    ulgasanName.pack(side="top", anchor="w")

    ulgasanDivider1 = ctk.CTkFrame(
        ulgasan_DetailsFrame,
        height=2,
        fg_color="#cfcfcf"
    )
    ulgasanDivider1.pack(side="top", fill="x")

    ulgasanGithubLink = ctk.CTkLabel(
        ulgasan_DetailsFrame,
        text="https://github.com/babyclaire555",
        text_color="#000000"
    )
    ulgasanGithubLink.pack(side="top", anchor="w", pady=(0,5))

    ulgasanFacebookLink = ctk.CTkLabel(
        ulgasan_DetailsFrame,
        text="https://www.facebook.com/claire.pereseo.19",
        text_color="#000000"
    )
    ulgasanFacebookLink.pack(side="top", anchor="w", pady=(0,5))

    ulgasanXLink = ctk.CTkLabel(
        ulgasan_DetailsFrame,
        text="No Twitter/X Account",
        text_color="#000000"
    )
    ulgasanXLink.pack(side="top", anchor="w", pady=(0,5))

    ulgasanDivider2 = ctk.CTkFrame(
        ulgasan_DetailsFrame,
        height=2,
        fg_color="#cfcfcf"
    )
    ulgasanDivider2.pack(side="top", fill="x")

    ulgasanBio1 = ctk.CTkLabel(
        ulgasan_DetailsFrame,
        text="I am a girl.",
        text_color="#000000"
    )
    ulgasanBio1.pack(side="top", anchor="w")

    ulgasanDivider3 = ctk.CTkFrame(
        ulgasan_DetailsFrame,
        height=2,
        fg_color="#cfcfcf"
    )
    ulgasanDivider3.pack(side="top", fill="x")
    # --------------------------------------------------------- #
    # end of ulgasan frame
    # --------------------------------------------------------- #

    # --------------------------------------------------------- #
    # piolen frame
    # --------------------------------------------------------- #
    piolenFrame = ctk.CTkFrame(
        aboutUs_Frame,
        fg_color = "#87CEEB"
    )
    piolenFrame.pack(side="top", padx=250, pady=(0,25))

    aboutPiolen_Image = get_imagePlaceholder()

    piolen_ImageLabel = ctk.CTkLabel(
        piolenFrame,
        image=aboutPiolen_Image,
        text=""
    )
    piolen_ImageLabel.pack(side="left")

    piolen_DetailsFrame = ctk.CTkFrame(
        piolenFrame,
        fg_color = "#87CEEB"
    )
    piolen_DetailsFrame.pack(side="left", padx=25)

    piolenContribution = ctk.CTkLabel(
        piolen_DetailsFrame,
        text="Member | Frontend Designer",
        text_color="#000000"
    )
    piolenContribution.pack(side="top", anchor="w")

    piolenName = ctk.CTkLabel(
        piolen_DetailsFrame,
        text="Angela ?. Piolen",
        text_color="#000000"
    )
    piolenName.pack(side="top", anchor="w")

    piolenDivider1 = ctk.CTkFrame(
        piolen_DetailsFrame,
        height=2,
        fg_color="#cfcfcf"
    )
    piolenDivider1.pack(side="top", fill="x")

    piolenGithubLink = ctk.CTkLabel(
        piolen_DetailsFrame,
        text="I dont know her github link",
        text_color="#000000"
    )
    piolenGithubLink.pack(side="top", anchor="w", pady=(0,5))

    piolenFacebookLink = ctk.CTkLabel(
        piolen_DetailsFrame,
        text="https://www.facebook.com/angelae.piolen",
        text_color="#000000"
    )
    piolenFacebookLink.pack(side="top", anchor="w", pady=(0,5))

    piolenXLink = ctk.CTkLabel(
        piolen_DetailsFrame,
        text="No Twitter/X Account",
        text_color="#000000"
    )
    piolenXLink.pack(side="top", anchor="w", pady=(0,5))

    piolenDivider2 = ctk.CTkFrame(
        piolen_DetailsFrame,
        height=2,
        fg_color="#cfcfcf"
    )
    piolenDivider2.pack(side="top", fill="x")

    piolenBio1 = ctk.CTkLabel(
        piolen_DetailsFrame,
        text="Im a girl too.",
        text_color="#000000"
    )
    piolenBio1.pack(side="top", anchor="w")

    piolenDivider3 = ctk.CTkFrame(
        piolen_DetailsFrame,
        height=2,
        fg_color="#cfcfcf"
    )
    piolenDivider3.pack(side="top", fill="x")
    # --------------------------------------------------------- #
    # end of piolen frame
    # --------------------------------------------------------- #

    # --------------------------------------------------------- #
    # esquivel frame
    # --------------------------------------------------------- #
    esquivelFrame = ctk.CTkFrame(
        aboutUs_Frame,
        fg_color = "#87CEEB"
    )
    esquivelFrame.pack(side="top", padx=250, pady=(0,25))

    aboutEsquivel_Image = get_imagePlaceholder()

    esquivel_ImageLabel = ctk.CTkLabel(
        esquivelFrame,
        image=aboutEsquivel_Image,
        text=""
    )
    esquivel_ImageLabel.pack(side="left")

    esquivel_DetailsFrame = ctk.CTkFrame(
        esquivelFrame,
        fg_color = "#87CEEB"
    )
    esquivel_DetailsFrame.pack(side="left", padx=25)

    esquivelContribution = ctk.CTkLabel(
        esquivel_DetailsFrame,
        text="Member | Backend Assistant/Debugger ",
        text_color="#000000"
    )
    esquivelContribution.pack(side="top", anchor="w")

    esquivelName = ctk.CTkLabel(
        esquivel_DetailsFrame,
        text="Municht ?. Esquivel",
        text_color="#000000"
    )
    esquivelName.pack(side="top", anchor="w")

    esquivelDivider1 = ctk.CTkFrame(
        esquivel_DetailsFrame,
        height=2,
        fg_color="#cfcfcf"
    )
    esquivelDivider1.pack(side="top", fill="x")

    esquivelGithubLink = ctk.CTkLabel(
        esquivel_DetailsFrame,
        text="Put yo github here dawg",
        text_color="#000000"
    )
    esquivelGithubLink.pack(side="top", anchor="w", pady=(0,5))

    esquivelFacebookLink = ctk.CTkLabel(
        esquivel_DetailsFrame,
        text="https://www.facebook.com/esquivel.municht",
        text_color="#000000"
    )
    esquivelFacebookLink.pack(side="top", anchor="w", pady=(0,5))

    esquivelXLink = ctk.CTkLabel(
        esquivel_DetailsFrame,
        text="No X/Twitter Account",
        text_color="#000000"
    )
    esquivelXLink.pack(side="top", anchor="w", pady=(0,5))

    esquivelDivider2 = ctk.CTkFrame(
        esquivel_DetailsFrame,
        height=2,
        fg_color="#cfcfcf"
    )
    esquivelDivider2.pack(side="top", fill="x")

    esquivelBio1 = ctk.CTkLabel(
        esquivel_DetailsFrame,
        text="Im a boi that always mews. I stan Jang Wonyoung in IVE.",
        text_color="#000000"
    )
    esquivelBio1.pack(side="top", anchor="w")

    esquivelDivider3 = ctk.CTkFrame(
        esquivel_DetailsFrame,
        height=2,
        fg_color="#cfcfcf"
    )
    esquivelDivider3.pack(side="top", fill="x")
    # --------------------------------------------------------- #
    # end of esquivel frame
    # --------------------------------------------------------- #