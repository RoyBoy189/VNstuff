init python:
    class NotesButton:
        notes = []
        what = []
        @classmethod
        def create_note(cls):
            if _last_say_who is None:
                note = "detective"
            else:
                note = _last_say_who
            what = _last_say_what
            cls.notes.append(note)
            cls.what.append(what)
            return cls.notes, cls.what
            