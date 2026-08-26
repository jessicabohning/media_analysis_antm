# tag_definitions is a python dictionary that tracks all of the tags
# and their general description

# Multiple tags can be applied to a single statement.
# For example, if the statement is "Jane's eyes are gorgeous" then the character tags
# would include both <jane> and <face>

# Other Definitions:
# Character: this refers to one of the human speakers or a general topic like "facial beauty"
# Speaker: the person that made the statement
# Scene or Chapter: the section of the episode

tag_definitions = {
    "strength": "the sentence referenced a strength of the character. Example: Jane has great hair",
    "weakness": "the sentence referenced a weakness of the character. Example: Jane's nose is too big",
    "self": "the speaker is talking about themselves. Example: I am so nervous",
    "face": "the sentence referenced something about the character's face: Example: Jane has brown eyes",
    "physique": "the sentence referenced a something about the character's body/physique. Example: Jane is really tall",
    "modeling": "the sentence references something about a character's modeling ability or the modeling industry in general. Example: Jane takes great photos",
    "personality": "the sentence referenced a character's personality. Example: Jane makes everyone laugh.",
    "prize": "the sentence referenced the show's prize package. Example: I want to win that Covergirl Contract.",
    # "walk": "the sentence referenced a character's walk. Example: Jane walks like a duck on the runway",
    "runway": "the sentence referenced a character's walk. Example: Jane walks like a duck on the runway",
    "personal beliefs": "the sentence referenced a character's personal beliefs. Example: God drives every decision I make",
    "hopes": "the sentence referenced a character's hopes. Example: I just want to be able to provide for my family",
    "photo": "the sentence referenced a character's photo (not necessarily the photo shot). Example: She looks stunning in this photo",
    "the show": "the sentence references the TV Show itself. Example: I have always wanted to be on the show",
    "ethnicity": "the sentence references a character's ethnicity. Example: Jane is Asian.",
    "athleticism": "the sentence references a character's athleticism. Example: Jane was the slowest runner in the challenge.",
    "drama": "the sentence refers to drama between contestants. Example: Jane flipped me off.",
    "sex appeal": "the sentence refers to the character's sex appeal. Example: She looked really sexy on the runway",
    "femininity": "the sentence refers to the character's femininity or womanhood. Example: she is someone little girls can look up to",
    "tyra mail": "the spoken text of the Tyra Mail",
    "style": "the sentence referces to the character's personal style. Example: Jane has a bohemian look.",
    "house": "the sentence is about the model house. Example: the bedroom is so pink and pretty",
    "speech": "the sentence refers to the character's dialect, how they speak, their voice etc. Example: Jane talks with a southern twang",


}

scene_definitions = {
    "recap": "this section summarizes what happened previously. These sections typically start with 'previously on'",
    "judging_panel": "the section of the show where the contestants interact with the judges",
    "judging_deliberation": "the section of the show where the judges privately decide who stays and who goes home",
    "challenge": "the section of the show where the contestants compete in a challege",
    "photo shot": "the section of the show where the contestants do a photo shoot",
    "house": "any part of the show that takes place at the model house"
}