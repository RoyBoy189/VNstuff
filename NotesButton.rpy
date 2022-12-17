init python:
    class NotesButton:
        notes = []
        what = []
        @classmethod
        def create_note(cls):
            note = _last_say_who
            what = _last_say_what
            cls.notes.append(note)
            cls.what.append(what)
            return cls.notes, cls.what
            