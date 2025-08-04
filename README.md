# 🇩🇪 germancode
**germancode** ist eine neue deutschsprachige Programmiersprache, die moderne Programmierkonzepte in einer klar lesbaren deutschen Syntax abbildet. Sie lässt sich nahtlos in bestehende Codestrukturen integrieren, da sie in etablierte Zielsprache (z. B. Python) transpiliert wird.
## 🔧 Ziel
Ziel ist die Entwicklung einer benutzerfreundlichen, vollständig deutschsprachigen Programmiersprache mit folgenden Eigenschaften:
- Deutsch als Programmiersyntax (Schlüsselwörter, Datentypen, Funktionen etc.)
- Transpilation in Python (weitere Zielsprachen möglich)
- Kommandozeilentool zum Ausführen von `.de`-Dateien
- Standardbibliothek in deutscher Sprache
- Modularer, erweiterbarer Aufbau
## 🛠️ Beispielcode
```de
funktion begruessung(zeichenkette name) {
    zeige("Hallo, " + name);
}
begruessung("Emma");

Transpiliert zu:

def begruessung(name):
    print("Hallo, " + name)
begruessung("Emma")

📦 Projektstruktur

germancode/
├── deutschcode/         # Hauptmodul
│   ├── parser/          # Lexer & Parser (Lark)
│   ├── transpiler/      # Übersetzer in Python
│   ├── runtime/         # Standardfunktionen (z. B. zeige)
│   ├── cli/             # Kommandozeilentool
│   └── utils/           # Fehlerbehandlung
├── examples/            # Beispielprogramme
├── tests/               # Testfälle
├── docs/                # Dokumentation
├── requirements.txt
├── README.md
└── setup.py

🚀 Schnellstart

# Repository klonen:
git clone https://github.com/dein-name/germancode.git
cd germancode
# Abhängigkeiten installieren:
pip install -r requirements.txt
# Beispiel ausführen:
python -m deutschcode.cli.deutsch examples/hallo_welt.de

📚 Dokumentation

Detaillierte Dokumentation befindet sich im Ordner /docs, darunter:
	•	Sprachsyntax
	•	Transpilerstruktur
	•	Fehlerbehandlung
	•	Interoperabilität mit existierendem Code

🤝 Mitwirken

Pull Requests und Vorschläge sind willkommen. Wenn du mitmachen möchtest, beachte bitte den Beitragenden-Leitfaden.

🧾 Lizenz

Dieses Projekt steht unter der MIT-Lizenz – siehe LICENSE für Details.

