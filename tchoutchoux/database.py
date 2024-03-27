from train_track.models import Train


Train(name="RERA", destination="Marne-la-Vallée", date_start="08:00", date_end="08:45", plan="a.png").save()
Train(name="RERB", destination="Saint-Rémy-lès-Chevreuse", date_start="08:15", date_end="09:10", plan="b.pn").save()
Train(name="RERC", destination="Versailles-Chantiers", date_start="08:30", date_end="09:15", plan="c.png").save()
Train(name="RERD", destination="Melun", date_start="08:45", date_end="09:30", plan="d.png").save()
Train(name="RERE", destination="Chelles-Gournay", date_start="09:00", date_end="09:45", plan="e.png").save()
Train(name="TransilienH", destination="Persan-Beaumont", date_start="09:15", date_end="10:15", plan="h.png").save()
Train(name="TransilienJ", destination="Mantes-la-Jolie", date_start="09:30", date_end="10:30", plan="j.png").save()
Train(name="TransilienK", destination="Crépy-en-Valois", date_start="09:45", date_end="10:45", plan="k.png").save()
Train(name="TransilienL", destination="Cergy-le-Haut", date_start="10:00", date_end="10:45", plan="l.png").save()
Train(name="TransilienN", destination="Mantes-la-Jolie", date_start="10:15", date_end="11:30", plan="n.png").save()
Train(name="TransilienP", destination="La Ferté-Milon", date_start="10:30", date_end="11:30", plan="p.png").save()
Train(name="TransilienR", destination="Robinson", date_start="10:45", date_end="11:15", plan="r.png").save()