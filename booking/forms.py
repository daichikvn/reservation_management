from django import forms
from .models import Schedule


class ScheduleForm(forms.ModelForm):
    TIME = (
        ("12:00" , "12:00"),
        ("12:30" , "12:30"),
        ("13:00" , "13:00"),
        ("13:30" , "13:30"),
        ("17:30" , "17:30"),
        ("18:00" , "18:00"),
        ("18:30" , "18:30"),
        ("19:00" , "19:00"),
        ("19:30" , "19:30"),
        ("20:00" , "20:00"),
        ("20:30" , "20:30"),
        ("21:00" , "21:00"),
    )

    NUM = (
        (1 , 1),
        (2 , 2),
        (3 , 3),
        (4 , 4),
        (5 , 5),
        (6 , 6),
        (7 , 7),
        (8 , 8),
        (9 , 9),
        (10 , 10),
    )

    time = forms.ChoiceField(label='時間', widget=forms.Select, choices=TIME)
    num_of_people = forms.ChoiceField(label='人数', widget=forms.Select, choices=NUM)

    class Meta:
        model = Schedule
        fields =['date', 'time', 'name', 'num_of_people', 'tel_number', 'memo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
            field.widget.attrs['placeholder'] = field.help_text