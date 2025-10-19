from rich import box
from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console(record=True, width=110)

tree = Tree(":call_me_hand: [link=https://vaibhavs10.github.io]Vaibhav (VB) Srivastav", guide_style="bold cyan")
python_tree = tree.add(":computer: Computational Linguist | ML Engineer", guide_style="green")
python_tree.add("⭐ [link=https://github.com/Vaibhavs10/insanely-fast-whisper]Insanely Fast Whisper")
python_tree.add("⭐ [link=https://github.com/Vaibhavs10/how-to-asr]How to ASR")
python_tree.add("⭐ [link=https://github.com/Vaibhavs10/anli-performance-prediction]Performance Prediction")
interests_tree = tree.add(":speaking_head: Interests")
interests_tree.add("On-device and LLM Inference")
interests_tree.add("Evaluations")
interests_tree.add("Product/ Growth Hacking")
tree.add(":runner: Runner")

about = """\
I am the Head of Developer Experience and Community at Hugging Face focusing on open source, audio & on-device ML.
Been a freelancer, tax analyst and a consultant for the past ~10 years.

I’ve invested significant time in past 6 years volunteering for open source and science organisations like Hugging Face, EuroPython, PyCons across APAC.

Delhi native, I now live in Paris, France!

Follow me on Twitter! [link=https://twitter.com/reach_vb]@reach_vb
"""

panel = Panel.fit(
    about, box=box.DOUBLE, border_style="blue", title="[b]Hey Hey! :wave:", width =60
)

console.print(Columns([panel, tree]))

CONSOLE_HTML_FORMAT = """\
<pre style="font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace">{code}</pre>
"""

console.save_html("README.md", inline_styles=True, code_format=CONSOLE_HTML_FORMAT)
